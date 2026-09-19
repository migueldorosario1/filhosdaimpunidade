const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  console.log('Navigating to PesqEle...');
  await page.goto('https://pesqele-divulgacao.tse.jus.br/');

  await page.waitForTimeout(2000); 
  await page.click('text=Consultar Pesquisas');
  await page.waitForTimeout(2000);

  await page.click('#formPesquisa\\:eleicoes .ui-selectonemenu-trigger');
  await page.waitForTimeout(500);
  await page.click('li[data-label="Eleições Gerais 2026"]');
  await page.waitForTimeout(1000);

  await page.click('#formPesquisa\\:filtroUF .ui-selectonemenu-trigger');
  await page.waitForTimeout(500);
  await page.click('li[data-label="BRASIL"]');
  await page.waitForTimeout(1000);

  await page.click('#formPesquisa\\:idBtnPesquisar');
  await page.waitForTimeout(4000);

  const rawData = fs.readFileSync('pesquisas_tse_2026_detalhes.json');
  const pesquisas = JSON.parse(rawData);
  
  for (let i = 0; i < pesquisas.length; i++) {
     const p = pesquisas[i];
     console.log(`Extracting details for ${p.registro} (ID: ${p.detalharId})...`);
     
     try {
         // Invoke the AJAX request directly
         await page.evaluate((id) => {
             PrimeFaces.ab({s: id, f: "formPesquisa"});
         }, p.detalharId);
         
         await page.waitForSelector('.ui-dialog-content', { state: 'visible', timeout: 8000 });
         await page.waitForTimeout(500);
         
         const modalText = await page.innerText('.ui-dialog-content');
         p.modalText = modalText;
         
         await page.click('.ui-dialog-titlebar-close');
         await page.waitForSelector('.ui-dialog-content', { state: 'hidden', timeout: 5000 });
         await page.waitForTimeout(500);
         
     } catch(e) {
         console.error(`Failed on ${p.registro}:`, e.message);
         try {
             await page.click('.ui-dialog-titlebar-close', { timeout: 1000 });
         } catch(err){}
     }
  }

  fs.writeFileSync('pesquisas_tse_2026_full.json', JSON.stringify(pesquisas, null, 2));
  console.log(`Done!`);
  
  await browser.close();
})();

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

  const results = [];
  
  console.log('Extracting all pages...');
  let p = 1;
  while (true) {
      console.log(`Processing page ${p}...`);
      const rowCount = await page.$$eval('tbody.ui-datatable-data tr', trs => trs.length);
      
      for (let r = 0; r < rowCount; r++) {
          const currentRow = (await page.$$('tbody.ui-datatable-data tr'))[r];
          const text = await currentRow.innerText();
          if(!text.includes('BR-')) continue;
          
          const columns = await currentRow.$$('td');
          const registro = await columns[0].innerText();
          const contratante = await columns[1].innerText();
          const instituto = await columns[2].innerText();
          const dataRegistro = await columns[3].innerText();
          
          results.push({
              registro,
              instituto,
              contratante,
              dataRegistro
          });
      }
      
      const nextBtn = await page.$('.ui-paginator-next');
      if (!nextBtn) break;
      const isDisabled = await nextBtn.evaluate(node => node.classList.contains('ui-state-disabled'));
      if (isDisabled) break; 
      
      await nextBtn.click();
      await page.waitForTimeout(2000);
      p++;
  }

  fs.writeFileSync('pesquisas_tse_2026_todas_br.json', JSON.stringify(results, null, 2));
  console.log(`Done! Found ${results.length} basic records.`);
  
  // Let's print out if Quaest, Ipec or Ipsos exist
  console.log('Quaest:', results.filter(r => r.instituto.toUpperCase().includes('QUAEST')).length);
  console.log('Ipec:', results.filter(r => r.instituto.toUpperCase().includes('IPEC')).length);
  console.log('Ipsos:', results.filter(r => r.instituto.toUpperCase().includes('IPSOS')).length);
  
  await browser.close();
})();

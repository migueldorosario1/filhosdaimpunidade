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
  
  // Try to find how many pages there are
  let maxPages = 1;
  const paginators = await page.$$('.ui-paginator-page');
  if (paginators.length > 0) {
      maxPages = paginators.length;
  }
  
  console.log(`Found ${maxPages} pages.`);

  for (let p = 1; p <= maxPages; p++) {
      console.log(`Processing page ${p}`);
      
      const rowCount = await page.$$eval('tbody.ui-datatable-data tr', trs => trs.length);
      
      for (let r = 0; r < rowCount; r++) {
          // Check if we need to navigate to page 'p'
          let activePageStr = '1';
          try {
              activePageStr = await page.$eval('.ui-paginator-page.ui-state-active', el => el.innerText);
          } catch(e) {}
          
          if (parseInt(activePageStr) !== p) {
              await page.click(`[aria-label="Page ${p}"]`);
              await page.waitForTimeout(3000);
          }
          
          const currentRow = (await page.$$('tbody.ui-datatable-data tr'))[r];
          const text = await currentRow.innerText();
          if(!text.includes('BR-')) continue;
          
          const columns = await currentRow.$$('td');
          const registro = await columns[0].innerText();
          const institutoFull = await columns[2].innerText();
          const dataRegistro = await columns[3].innerText();
          
          console.log(`Extracting details for ${registro}...`);
          
          const detailBtn = await currentRow.$('a[title="Visualizar dados da pesquisa"]');
          if (detailBtn) {
             await Promise.all([
                 page.waitForNavigation(),
                 detailBtn.click()
             ]);
             
             const bodyText = await page.innerText('body');
             
             results.push({
                 registro,
                 institutoFull,
                 dataRegistro,
                 bodyText
             });
             
             // Click Voltar
             await Promise.all([
                 page.waitForNavigation(),
                 page.click('text=Voltar')
             ]);
             await page.waitForTimeout(1000);
          }
      }
  }

  fs.writeFileSync('pesquisas_tse_2026_scraped.json', JSON.stringify(results, null, 2));
  console.log(`Done! Extracted ${results.length} records.`);
  await browser.close();
})();

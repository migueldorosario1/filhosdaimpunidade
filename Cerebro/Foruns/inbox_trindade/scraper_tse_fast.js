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
  const pageButtons = await page.$$('.ui-paginator-page');
  if (pageButtons.length > 0) {
      // Find the last page number
      maxPages = await pageButtons[pageButtons.length - 1].innerText();
      maxPages = parseInt(maxPages) || 5;
  }
  
  // actually, let's just loop until the 'Next' button is disabled
  console.log('Extracting all pages...');
  
  let p = 1;
  while (true) {
      console.log(`Processing page ${p}`);
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
      const isDisabled = await nextBtn.evaluate(node => node.classList.contains('ui-state-disabled'));
      if (isDisabled || p >= 20) break; // Limit to 20 pages max for now to prevent infinite
      
      await nextBtn.click();
      await page.waitForTimeout(2000);
      p++;
  }

  fs.writeFileSync('pesquisas_tse_2026_todas.json', JSON.stringify(results, null, 2));
  console.log(`Done! Found ${results.length} basic records.`);
  await browser.close();
})();

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
  await page.waitForTimeout(3000);

  const resultsWithDetails = [];
  
  let pageCount = 1;
  while(true) {
      console.log(`Processing page ${pageCount}`);
      
      const rows = await page.$$('tbody.ui-datatable-data tr');
      const rowCount = rows.length;
      
      for (let i = 0; i < rowCount; i++) {
          // In primefaces, the ID of the detail button usually follows this pattern:
          const detailBtnId = `formPesquisa:tabelaPesquisas:${i}:detalhar`;
          
          try {
             // Extract row basic text just to have the registration number
             const rowText = await page.$eval(`tr[data-ri="${i}"]`, tr => tr.innerText);
             const cols = rowText.split('\t').map(t => t.trim());
             const registro = cols[0];
             const institutoFull = cols[2];
             
             if (!registro.startsWith('BR-')) {
                 continue; // empty row or something
             }
             
             console.log(`Extracting details for ${registro}...`);
             
             await page.click(`[id="${detailBtnId}"]`);
             
             // Wait for modal content to load
             await page.waitForSelector('.ui-dialog-content', { state: 'visible', timeout: 5000 });
             await page.waitForTimeout(1000);
             
             const modalText = await page.innerText('.ui-dialog-content');
             
             // Close modal
             await page.click('.ui-dialog-titlebar-close');
             await page.waitForSelector('.ui-dialog-content', { state: 'hidden', timeout: 5000 });
             await page.waitForTimeout(500);
             
             resultsWithDetails.push({
                 registro,
                 institutoFull,
                 modalText
             });
          } catch(e) {
             console.log(`Error on index ${i}: ${e}`);
             // try to close modal just in case
             try {
                await page.click('.ui-dialog-titlebar-close', { timeout: 1000 });
             } catch(err){}
          }
      }
      
      const nextButton = await page.$('.ui-paginator-next:not(.ui-state-disabled)');
      if (nextButton) {
         await nextButton.click();
         await page.waitForTimeout(3000); // wait for ajax table refresh
         pageCount++;
      } else {
         break;
      }
  }

  fs.writeFileSync('pesquisas_tse_2026_raw_modals.json', JSON.stringify(resultsWithDetails, null, 2));
  console.log(`Extracted details for ${resultsWithDetails.length} records.`);
  
  await browser.close();
})();

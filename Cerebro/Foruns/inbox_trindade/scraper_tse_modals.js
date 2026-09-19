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
          const row = rows[i];
          const text = await row.innerText();
          if(!text.includes('BR-')) continue;
          
          const columns = await row.$$('td');
          const registro = await columns[0].innerText();
          const institutoFull = await columns[2].innerText();
          
          console.log(`Extracting details for ${registro}...`);
          
          const detailBtn = await row.$('a[title="Visualizar dados da pesquisa"]');
          if (detailBtn) {
             await detailBtn.click();
             await page.waitForTimeout(1000); // Wait for modal
             
             try {
                // Get all text content from the modal to easily parse it later
                const modalText = await page.innerText('.ui-dialog-content');
                
                // Close modal using Escape
                await page.keyboard.press('Escape');
                await page.waitForTimeout(500);
                
                resultsWithDetails.push({
                   registro,
                   institutoFull,
                   modalText
                });
             } catch (e) {
                 console.error(`Error extracting details for ${registro}: ${e}`);
                 await page.keyboard.press('Escape');
             }
          }
      }
      
      const nextButton = await page.$('.ui-paginator-next:not(.ui-state-disabled)');
      if (nextButton) {
         await nextButton.click();
         await page.waitForTimeout(2000);
         pageCount++;
      } else {
         break;
      }
  }

  fs.writeFileSync('pesquisas_tse_2026_raw_modals.json', JSON.stringify(resultsWithDetails, null, 2));
  console.log(`Extracted details for ${resultsWithDetails.length} records.`);
  
  await browser.close();
})();

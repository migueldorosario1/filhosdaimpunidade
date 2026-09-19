const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  console.log('Navigating to PesqEle...');
  await page.goto('https://pesqele-divulgacao.tse.jus.br/');

  await page.waitForTimeout(3000); 

  console.log('Clicking on Consultar Pesquisas...');
  await page.click('text=Consultar Pesquisas');

  await page.waitForTimeout(3000);

  console.log('Selecting Eleições Gerais 2026...');
  
  await page.click('#formPesquisa\\:eleicoes .ui-selectonemenu-trigger');
  await page.waitForTimeout(1000);
  await page.click('li[data-label="Eleições Gerais 2026"]');
  await page.waitForTimeout(2000);

  console.log('Selecting BRASIL as UF...');
  await page.click('#formPesquisa\\:filtroUF .ui-selectonemenu-trigger');
  await page.waitForTimeout(1000);
  await page.click('li[data-label="BRASIL"]');
  await page.waitForTimeout(2000);

  console.log('Clicking Pesquisar...');
  // Find the button and click it
  await page.click('#formPesquisa\\:idBtnPesquisar');
  
  // Wait for the results table to load
  await page.waitForTimeout(5000);

  console.log('Extracting data...');

  const results = [];
  
  let hasNextPage = true;
  let pageCount = 1;

  while (hasNextPage) {
     console.log(`Extracting page ${pageCount}...`);
     
     // Extract rows for the current page
     const rows = await page.$$eval('tbody.ui-datatable-data tr', trs => {
        return trs.map((tr, index) => {
          const tds = Array.from(tr.querySelectorAll('td'));
          const data = tds.map(td => td.innerText.trim());
          
          // Also check for the detailed view button id to extract its href/onclick
          const btn = tr.querySelector('a[title="Visualizar dados da pesquisa"]');
          const detalharId = btn ? btn.id : null;
          
          return [...data, detalharId, index];
        });
      });
      
     results.push(...rows);
     
     // Check if there's a next page
     const nextButton = await page.$('.ui-paginator-next:not(.ui-state-disabled)');
     if (nextButton) {
        console.log('Going to next page...');
        await nextButton.click();
        await page.waitForTimeout(3000); // Wait for the table to update
        pageCount++;
     } else {
        hasNextPage = false;
     }
  }

  // Filter out any empty rows or rows that don't match the expected format
  const validResults = results.filter(row => row.length >= 7 && row[0].startsWith('BR-'));
  
  // Deduplicate results based on the first column (registration number)
  const uniqueResults = [];
  const seen = new Set();
  
  for (const row of validResults) {
     if (!seen.has(row[0])) {
         seen.add(row[0]);
         uniqueResults.push(row);
     }
  }

  // Formatting for output
  const formattedResults = uniqueResults.map(row => {
      // Split the company / institute string
      let empresaContratada = row[2];
      let instituto = row[2];
      if (row[2].includes(' / ')) {
          const parts = row[2].split(' / ');
          empresaContratada = parts[0].trim();
          instituto = parts[1].trim();
      }
      
      return {
          registro: row[0],
          eleicao: row[1],
          contratante: empresaContratada,
          instituto: instituto,
          dataRegistro: row[3],
          abrangencia: row[4],
          detalharId: row[6],
          rowIndex: row[7]
      };
  });

  fs.writeFileSync('pesquisas_tse_2026_detalhes.json', JSON.stringify(formattedResults, null, 2));

  console.log(`Done. Extracted ${formattedResults.length} unique records.`);
  await browser.close();
})();

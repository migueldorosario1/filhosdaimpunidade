const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true });
  
  const rawData = fs.readFileSync('pesquisas_tse_2026.json');
  const pesquisas = JSON.parse(rawData);

  const results = [];
  
  async function processRecord(p, index) {
      const context = await browser.newContext();
      const page = await context.newPage();
      try {
          await page.goto('https://pesqele-divulgacao.tse.jus.br/');
          await page.waitForTimeout(2000); 

          await page.click('text=Consultar Pesquisas');
          await page.waitForTimeout(1000);

          await page.click('#formPesquisa\\:eleicoes .ui-selectonemenu-trigger');
          await page.waitForTimeout(500);
          await page.click('li[data-label="Eleições Gerais 2026"]');
          await page.waitForTimeout(500);

          await page.click('#formPesquisa\\:filtroUF .ui-selectonemenu-trigger');
          await page.waitForTimeout(500);
          await page.click('li[data-label="BRASIL"]');
          await page.waitForTimeout(500);

          await page.click('#formPesquisa\\:idBtnPesquisar');
          await page.waitForTimeout(2500);
          
          const targetPageNum = Math.floor(index / 10) + 1;
          const targetRowIndex = index % 10;
          
          if (targetPageNum > 1) {
              await page.click(`[aria-label="Page ${targetPageNum}"]`);
              await page.waitForTimeout(2500);
          }
          
          const detailBtnId = `formPesquisa:tabelaPesquisas:${index}:detalhar`;
          
          await Promise.all([
              page.waitForNavigation(),
              page.click(`[id="${detailBtnId}"]`)
          ]);
          
          const bodyText = await page.innerText('body');
          p.bodyText = bodyText;
          
          results.push(p);
          console.log(`Successfully extracted ${p.registro}`);
      } catch(e) {
          console.error(`Error on ${p.registro}: ${e.message}`);
      } finally {
          await context.close();
      }
  }

  // We have 50 records. Let's do batches of 2 to speed it up (2 browsers at a time)
  // That takes around 25 * 8s = 200 seconds.
  const batchSize = 2;
  for (let i = 0; i < pesquisas.length; i += batchSize) {
      const batch = pesquisas.slice(i, i + batchSize);
      console.log(`Processing batch ${i} to ${i + batch.length - 1}...`);
      await Promise.all(batch.map((p, idx) => processRecord(p, i + idx)));
  }

  fs.writeFileSync('pesquisas_tse_2026_full.json', JSON.stringify(results, null, 2));
  console.log(`Done! Extracted ${results.length} records.`);
  await browser.close();
})();

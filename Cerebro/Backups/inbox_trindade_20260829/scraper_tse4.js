const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  console.log('Navigating to PesqEle...');
  await page.goto('https://pesqele-divulgacao.tse.jus.br/app/pesquisa/pesquisas.xhtml');

  await page.waitForTimeout(3000); 

  console.log('Selecting Eleições Gerais 2026...');
  
  // Click on the Eleição dropdown
  await page.click('label:has-text("Eleição:") + div .ui-selectonemenu-trigger');
  await page.waitForTimeout(1000);
  // Click on the option
  await page.click('li[data-label="Eleições Gerais 2026"]');
  await page.waitForTimeout(2000);

  // Click on the UF dropdown
  console.log('Selecting BRASIL as UF...');
  await page.click('label:has-text("UF:") + div .ui-selectonemenu-trigger');
  await page.waitForTimeout(1000);
  await page.click('li[data-label="BRASIL"]');
  await page.waitForTimeout(2000);

  console.log('Clicking Pesquisar...');
  // Find the button and click it
  await page.click('button span:has-text("Pesquisar")');
  
  // Wait for the results table to load
  await page.waitForTimeout(5000);

  console.log('Extracting data...');
  const html = await page.content();
  fs.writeFileSync('pesqele_results_html.txt', html);
  
  // Let's try to extract table rows
  const rows = await page.$$eval('tbody.ui-datatable-data tr', trs => {
    return trs.map(tr => {
      const tds = Array.from(tr.querySelectorAll('td'));
      return tds.map(td => td.innerText.trim());
    });
  });

  fs.writeFileSync('pesqele_data.json', JSON.stringify(rows, null, 2));

  console.log('Taking screenshot...');
  await page.screenshot({ path: 'pesqele_results.png', fullPage: true });

  console.log('Done.');
  await browser.close();
})();

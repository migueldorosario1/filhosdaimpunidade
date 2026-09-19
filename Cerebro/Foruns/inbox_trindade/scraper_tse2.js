const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: false }); // headless: false for debugging
  const context = await browser.newContext();
  const page = await context.newPage();

  console.log('Navigating to PesqEle...');
  await page.goto('https://pesqele-divulgacao.tse.jus.br/');

  await page.waitForTimeout(3000); 

  console.log('Clicking on Consultar Pesquisas...');
  // Click on the link that contains the text 'Consultar Pesquisas'
  await page.click('text=Consultar Pesquisas');

  // Wait for the next view to load
  await page.waitForTimeout(3000);

  console.log('Taking screenshot of search page...');
  await page.screenshot({ path: 'pesqele_search.png' });

  const bodyText = await page.innerText('body');
  fs.writeFileSync('pesqele_search_body.txt', bodyText);
  
  const html = await page.content();
  fs.writeFileSync('pesqele_search_html.txt', html);
  
  console.log('Done.');

  await browser.close();
})();

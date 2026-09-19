const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: false }); // headless: false for debugging
  const context = await browser.newContext();
  const page = await context.newPage();

  console.log('Navigating to PesqEle...');
  await page.goto('https://pesqele-divulgacao.tse.jus.br/');

  // Wait for the app to load. Let's see what the main selector is.
  // We'll pause for a moment to let the angular app load and then dump some HTML.
  await page.waitForTimeout(5000); 

  console.log('Taking screenshot for debugging...');
  await page.screenshot({ path: 'pesqele_home.png' });

  // Let's try to find elements related to "Eleições Gerais 2026" or similar.
  // First, we need to select the election year.
  // This is highly dependent on the layout. Let's just dump the body text first to understand the structure.
  const bodyText = await page.innerText('body');
  fs.writeFileSync('pesqele_body.txt', bodyText);
  
  const html = await page.content();
  fs.writeFileSync('pesqele_html.txt', html);
  
  console.log('Done initial extraction.');

  await browser.close();
})();

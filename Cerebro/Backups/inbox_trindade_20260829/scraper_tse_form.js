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

  const bodyHtml = await page.innerHTML('body');
  fs.writeFileSync('pesqele_form_html.txt', bodyHtml);

  await browser.close();
})();

const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: false }); // headless: false for debugging
  const context = await browser.newContext();
  const page = await context.newPage();

  console.log('Navigating to PesqEle...');
  await page.goto('https://pesqele-divulgacao.tse.jus.br/app/pesquisa/pesquisas.xhtml');

  await page.waitForTimeout(3000); 

  console.log('Selecting Eleições Gerais 2026...');
  
  // The select element ID is likely formPesquisa:eleicoes
  // It's a JSF/Primefaces component. Let's try to select it.
  // Actually, Primefaces uses a div structure. Let's click the dropdown and then the item.
  
  // Try finding the label "Eleição:" and the associated dropdown
  await page.click('label:has-text("Eleição:") + div .ui-selectonemenu-trigger');
  await page.waitForTimeout(1000);
  
  await page.click('li[data-label="Eleições Gerais 2026"]');
  await page.waitForTimeout(2000);

  // We want national polls: "BRASIL"
  console.log('Selecting BRASIL as UF...');
  await page.click('label:has-text("UF:") + div .ui-selectonemenu-trigger');
  await page.waitForTimeout(1000);
  await page.click('li[data-label="BRASIL"]');
  await page.waitForTimeout(2000);

  console.log('Clicking Pesquisar...');
  await page.click('span:has-text("Pesquisar")');
  await page.waitForTimeout(5000);

  console.log('Taking screenshot of results page...');
  await page.screenshot({ path: 'pesqele_results.png' });

  const bodyText = await page.innerText('body');
  fs.writeFileSync('pesqele_results_body.txt', bodyText);
  
  const html = await page.content();
  fs.writeFileSync('pesqele_results_html.txt', html);
  
  console.log('Done.');

  await browser.close();
})();

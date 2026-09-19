const { chromium } = require('playwright');

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

  console.log('Clicking the first detail link...');
  
  // Wait for navigation
  await Promise.all([
      page.waitForNavigation(),
      page.click('[id="formPesquisa:tabelaPesquisas:0:detalhar"]')
  ]);
  
  console.log('Navigated to:', page.url());
  const bodyText = await page.innerText('body');
  
  require('fs').writeFileSync('detalhar_page.txt', bodyText);
  
  // Also get the HTML to see the buttons
  const bodyHtml = await page.innerHTML('body');
  require('fs').writeFileSync('detalhar_page_html.txt', bodyHtml);
  
  console.log('Done!');
  await browser.close();
})();

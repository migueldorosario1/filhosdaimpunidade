const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();
  
  await page.goto('https://pesqele-divulgacao.tse.jus.br/');
  await page.waitForTimeout(2000); 
  
  await page.click('text=Consultar Pesquisas');
  await page.waitForTimeout(2000);
  
  await page.click('#formPesquisa\\:eleicoes .ui-selectonemenu-trigger');
  await page.waitForTimeout(500);
  await page.click('li[data-label="Eleições Gerais 2026"]');
  await page.waitForTimeout(1000);
  
  await page.click('#formPesquisa\\:idBtnPesquisar');
  await page.waitForTimeout(4000);
  
  const results = [];
  let maxPages = 1;
  const pageButtons = await page.$$('.ui-paginator-page');
  if (pageButtons.length > 0) {
      maxPages = parseInt(await pageButtons[pageButtons.length - 1].innerText()) || 5;
  }
  
  console.log('Scanning...');
  let p = 1;
  while (true) {
      const trs = await page.$$('tbody.ui-datatable-data tr');
      for (const tr of trs) {
          const text = await tr.innerText();
          if (text.toUpperCase().includes('QUAEST') || text.toUpperCase().includes('IPEC') || text.toUpperCase().includes('IPSOS')) {
              console.log('FOUND MATCH ON PAGE', p);
              console.log(text);
          }
      }
      
      const nextBtn = await page.$('.ui-paginator-next');
      if (!nextBtn) break;
      const isDisabled = await nextBtn.evaluate(node => node.classList.contains('ui-state-disabled'));
      if (isDisabled) break;
      
      await nextBtn.click();
      await page.waitForTimeout(1500);
      p++;
  }
  
  await browser.close();
})();

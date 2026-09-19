const { chromium } = require('playwright');
const fs = require('fs');

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
  
  // DON'T filter by BRASIL. We want ALL states!
  await page.click('#formPesquisa\\:idBtnPesquisar');
  await page.waitForTimeout(4000);
  
  const results = [];
  
  let p = 1;
  while (true) {
      console.log(`Processing page ${p}`);
      const rowCount = await page.$$eval('tbody.ui-datatable-data tr', trs => trs.length);
      
      for (let r = 0; r < rowCount; r++) {
          const currentRow = (await page.$$('tbody.ui-datatable-data tr'))[r];
          const text = await currentRow.innerText();
          if(!text.includes('BR-') && !text.includes('SP-') && !text.includes('RJ-') && !text.includes('MG-')) continue;
          
          const columns = await currentRow.$$('td');
          if (columns.length > 5) {
              const registro = await columns[0].innerText();
              const contratante = await columns[1].innerText();
              const instituto = await columns[2].innerText();
              const uf = await columns[5].innerText();
              
              if (instituto.toUpperCase().includes('QUAEST') || instituto.toUpperCase().includes('IPEC') || instituto.toUpperCase().includes('IPSOS')) {
                  results.push({registro, instituto, contratante, uf});
              }
          }
      }
      
      const nextBtn = await page.$('.ui-paginator-next');
      const isDisabled = await nextBtn.evaluate(node => node.classList.contains('ui-state-disabled'));
      if (isDisabled || p >= 5) break; // Look at first 5 pages for now
      
      await nextBtn.click();
      await page.waitForTimeout(2000);
      p++;
  }
  
  console.log('Found:', results);
  fs.writeFileSync('quaest_ipec.json', JSON.stringify(results, null, 2));
  await browser.close();
})();

const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();
  
  const rawData = fs.readFileSync('pesquisas_tse_2026_detalhes.json');
  const pesquisas = JSON.parse(rawData);

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
  await page.click('#formPesquisa\\:idBtnPesquisar');
  await page.waitForTimeout(5000);

  const resultsWithCost = [];

  // We only need to iterate over the items that match our criteria (cost > 20000, maybe filter later)
  // But for now let's just get the cost for the top ones as a demonstration, or we can get all if it doesn't take too long.
  // There are 50 records. Let's iterate through pages to click 'detalhar'.
  
  let pageCount = 1;
  while(true) {
      console.log(`Processing page ${pageCount}`);
      
      const rows = await page.$$('tbody.ui-datatable-data tr');
      for (let i = 0; i < rows.length; i++) {
          const row = rows[i];
          const text = await row.innerText();
          if(!text.includes('BR-')) continue;
          
          const columns = await row.$$('td');
          const registro = await columns[0].innerText();
          const institutoFull = await columns[2].innerText();
          const dataRegistro = await columns[3].innerText();
          
          let empresaContratada = institutoFull;
          let instituto = institutoFull;
          if (institutoFull.includes(' / ')) {
              const parts = institutoFull.split(' / ');
              empresaContratada = parts[0].trim();
              instituto = parts[1].trim();
          }

          console.log(`Extracting details for ${registro}...`);
          
          // Click the details button
          const detailBtn = await row.$('a[title="Visualizar dados da pesquisa"]');
          if (detailBtn) {
             await detailBtn.click();
             await page.waitForTimeout(2000); // Wait for modal to load
             
             try {
                // Extract cost, interviews, etc.
                // The modal has a table or definition list. Let's look for "Valor:" and "Entrevistados:"
                
                // Usually it is a panel grid
                const content = await page.innerText('.ui-dialog-content');
                
                let valor = "Não informado";
                let entrevistados = "Não informado";
                let divulgacao = "Não informado";
                let estatistico = "Não informado";
                let metodologia = "Não informado"; // "Presencial", "Telefônica", etc
                
                const lines = content.split('\\n');
                for (let j = 0; j < lines.length; j++) {
                    const line = lines[j].trim();
                    if (line.startsWith('Valor:')) {
                       valor = lines[j+1] ? lines[j+1].trim() : "Não informado";
                    } else if (line.startsWith('Entrevistados:')) {
                       entrevistados = lines[j+1] ? lines[j+1].trim() : "Não informado";
                    } else if (line.startsWith('Data de divulgação:')) {
                       divulgacao = lines[j+1] ? lines[j+1].trim() : "Não informado";
                    } else if (line.startsWith('Estatístico responsável:')) {
                       estatistico = lines[j+1] ? lines[j+1].trim() : "Não informado";
                    } else if (line.startsWith('Metodologia de pesquisa:')) {
                       metodologia = lines[j+1] ? lines[j+1].trim() : "Não informado";
                    }
                }
                
                resultsWithCost.push({
                   registro,
                   instituto,
                   contratante: empresaContratada,
                   dataRegistro,
                   divulgacao,
                   entrevistados,
                   valor,
                   estatistico,
                   metodologia
                });

                // Close modal
                await page.click('.ui-dialog-titlebar-close');
                await page.waitForTimeout(1000);

             } catch (e) {
                 console.error(`Error extracting details for ${registro}: ${e}`);
                 // Try to close modal just in case
                 try { await page.click('.ui-dialog-titlebar-close'); } catch(e2){}
             }
          }
      }
      
      const nextButton = await page.$('.ui-paginator-next:not(.ui-state-disabled)');
      if (nextButton) {
         console.log('Going to next page...');
         await nextButton.click();
         await page.waitForTimeout(3000);
         pageCount++;
      } else {
         break;
      }
  }

  fs.writeFileSync('pesquisas_tse_2026_com_custo.json', JSON.stringify(resultsWithCost, null, 2));
  console.log(`Extracted details for ${resultsWithCost.length} records.`);
  
  await browser.close();
})();

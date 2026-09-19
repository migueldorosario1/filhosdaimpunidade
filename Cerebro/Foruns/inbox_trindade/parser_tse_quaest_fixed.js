const fs = require('fs');
const raw = fs.readFileSync('pesquisas_tse_2026_full.json');
const pesquisas = JSON.parse(raw);

const parsed = pesquisas.map(p => {
    let valor = 'Não informado';
    let entrevistados = 'Não informado';
    let divulgacao = 'Não informado';
    let estatistico = 'Não informado';
    let metodologia = 'Não informado';
    let dataInicio = '';
    let dataFim = '';
    
    if (p.bodyText) {
        const text = p.bodyText; 
        const lines = text.split('\n').map(l => l.trim());
        
        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            
            const valorMatch = line.match(/Valor:\s*(R\$\s*[\d\.,]+)/);
            if (valorMatch) valor = valorMatch[1];
            else if (line.startsWith('Valor:')) valor = lines[i+1] ? lines[i+1].split('\t')[0] : 'Não informado';
            
            const entMatch = line.match(/Entrevistados:\s*(\d+)/);
            if (entMatch) entrevistados = entMatch[1];
            else if (line.startsWith('Entrevistados:')) entrevistados = lines[i+1] ? lines[i+1].split('\t')[0] : 'Não informado';
            
            const divMatch = line.match(/Data de divulgação:\s*([\d\/]+)/);
            if (divMatch) divulgacao = divMatch[1];
            else if (line.startsWith('Data de divulgação:')) divulgacao = lines[i+1] ? lines[i+1].split('\t')[0] : 'Não informado';
            
            const inMatch = line.match(/Data de início da pesquisa:\s*([\d\/]+)/);
            if (inMatch) dataInicio = inMatch[1];
            else if (line.startsWith('Data de início da pesquisa:')) dataInicio = lines[i+1] ? lines[i+1].split('\t')[0] : '';
            
            const fimMatch = line.match(/Data de término da pesquisa:\s*([\d\/]+)/);
            if (fimMatch) dataFim = fimMatch[1];
            else if (line.startsWith('Data de término da pesquisa:')) dataFim = lines[i+1] ? lines[i+1].split('\t')[0] : '';
            
            if (line.includes('Estatístico responsável:')) {
                const parts = line.split('Estatístico responsável:');
                if (parts[1].trim()) estatistico = parts[1].trim().split('\t')[0];
                else estatistico = lines[i+1] ? lines[i+1].split('\t')[0] : 'Não informado';
            }
            if (line.includes('Metodologia de pesquisa:')) metodologia = lines[i+1] ? lines[i+1] : 'Não informado';
        }
        
        if (valor.includes('\t')) valor = valor.split('\t')[0];
        if (entrevistados.includes('\t')) entrevistados = entrevistados.split('\t')[0];
        if (divulgacao.includes('\t')) divulgacao = divulgacao.split('\t')[0];
        if (dataInicio.includes('\t')) dataInicio = dataInicio.split('\t')[0];
        if (dataFim.includes('\t')) dataFim = dataFim.split('\t')[0];
    }
    
    let valorNum = 0;
    if (valor !== 'Não informado') valorNum = parseFloat(valor.replace('R$', '').replace(/\./g, '').replace(',', '.').trim()) || 0;
    
    let metodoClean = 'Não informado';
    if (metodologia.toLowerCase().includes('presencial') || metodologia.toLowerCase().includes('face a face')) metodoClean = 'Presencial';
    else if (metodologia.toLowerCase().includes('telefônica') || metodologia.toLowerCase().includes('telefone')) metodoClean = 'Telefônica';
    else if (metodologia.toLowerCase().includes('internet') || metodologia.toLowerCase().includes('online')) metodoClean = 'Internet';
    else metodoClean = 'Mista / Outra';
    
    let periodoEntrevistas = 'Não informado';
    if (dataInicio && dataFim) periodoEntrevistas = dataInicio === dataFim ? dataInicio : dataInicio.substring(0, 5) + ' a ' + dataFim;
    
    return {
        registro: p.registro,
        instituto: p.instituto,
        contratante: p.contratante,
        dataRegistro: p.dataRegistro,
        dataDivulgacao: divulgacao,
        dataEntrevistas: periodoEntrevistas,
        entrevistados: entrevistados,
        estatistico: estatistico,
        metodo: metodoClean,
        valor: valor,
        valorNum: valorNum
    };
});

// Adicionando manualmente as pesquisas enviadas pelo usuário
parsed.push({
    registro: 'BR-07661/2026',
    instituto: 'QUAEST PESQUISAS, CONSULTORIA E PROJETOS LTDA.',
    contratante: 'BANCO GENIAL S.A.',
    dataRegistro: '04/06/2026',
    dataDivulgacao: '10/06/2026',
    dataEntrevistas: '05/06 a 08/06/2026',
    entrevistados: '2004',
    estatistico: 'Margarida Maria de Mendonça',
    metodo: 'Presencial',
    valor: 'R$ 433.255,92',
    valorNum: 433255.92
});

// Institutos grandes
const grandes = ['DATAFOLHA', 'ATLASINTEL', 'REAL TIME BIG DATA', 'IPEC', 'QUAEST', 'CNT', 'MDA', 'PARANA', 'FUTURA', 'IDEIA'];

let veritaCount = 0;

const filtradas = parsed
    .sort((a, b) => b.dataRegistro.split('/').reverse().join('-').localeCompare(a.dataRegistro.split('/').reverse().join('-')))
    .filter(p => {
        // SEMPRE INCLUIR QUAEST e IDEIA
        if (p.registro === 'BR-05628/2026') return true; // IDEIA
        if (p.registro === 'BR-07661/2026') return true; // QUAEST
        
        // Limitar Verita
        if (p.instituto.toUpperCase().includes('VERITA')) {
            if (veritaCount >= 1) return false;
            veritaCount++;
            return true;
        }
        
        const isGrande = grandes.some(i => p.instituto.toUpperCase().includes(i));
        const isCaro = p.valorNum > 35000;
        return isGrande || isCaro;
    });

// Pega as 10 mais caras do array filtrado
const top10Caras = [...filtradas].sort((a, b) => b.valorNum - a.valorNum).slice(0, 10);

// Pega as mais recentes até completar 20 (evitando duplicação)
const finalSelection = [...top10Caras];
for (const p of filtradas) {
    if (finalSelection.length >= 20) break;
    if (!finalSelection.some(x => x.registro === p.registro)) {
        finalSelection.push(p);
    }
}

// Re-ordena por data de registro decrescente para a tabela
finalSelection.sort((a, b) => b.dataRegistro.split('/').reverse().join('-').localeCompare(a.dataRegistro.split('/').reverse().join('-')));

// Generate CSV
let csv = 'Data da Divulgação;Data das Entrevistas;Registro;Instituto / Contratante;Valor;Entrevistas;Metodologia\n';
finalSelection.forEach(p => {
    let instContr = (p.instituto + ' / ' + p.contratante).replace(/;/g, ',');
    if (p.registro === 'BR-05628/2026') instContr = 'IDEIA / MEIO E MENSAGEM (' + instContr + ')';
    if (p.registro === 'BR-07661/2026') instContr = 'QUAEST / GENIAL (' + instContr + ')';
    
    const valor = p.valor.replace(/;/g, ',');
    const met = p.metodo.replace(/;/g, ',');
    csv += `${p.dataDivulgacao};${p.dataEntrevistas};${p.registro};${instContr};${valor};${p.entrevistados};${met}\n`;
});
fs.writeFileSync('pesquisas_tse_2026_tabela.csv', csv);

// Create Markdown
let md = '# Últimas Pesquisas Eleitorais 2026 (Nacionais)\n\n';
md += '> [!NOTE]\n> **Filtros aplicados**: 20 registros com foco nos maiores institutos (Quaest, Ipec, Datafolha, Atlas, IDEIA, Paraná, Real Time). Veritá limitada a 1 registro.\n\n';
md += '| Data da Divulgação | Data das Entrevistas | Registro | Instituto / Contratante | Valor | Entrevistas | Metodologia |\n';
md += '|---|---|---|---|---|---|---|\n';
finalSelection.forEach(p => {
    let destaque = '**' + p.instituto + '**';
    if (p.registro === 'BR-05628/2026') destaque = '⭐ **MEIO / IDEIA**';
    if (p.registro === 'BR-07661/2026') destaque = '⭐ **QUAEST / GENIAL**';

    
    md += '| ' + p.dataDivulgacao + ' | ' + p.dataEntrevistas + ' | ' + p.registro + ' | ' + destaque + ' <br/> ' + p.contratante + ' | ' + p.valor + ' | ' + p.entrevistados + ' | ' + p.metodo + ' |\n';
});
fs.writeFileSync('relatorio_pesquisas_2026.md', md);
console.log('Done!');

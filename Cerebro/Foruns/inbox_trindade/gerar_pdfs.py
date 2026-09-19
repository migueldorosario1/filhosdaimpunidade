import os
import shutil
import subprocess

# Define paths
base_dir = "/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/Foruns/inbox_trindade"
assets_dir = os.path.join(base_dir, "eidas_assets")

# Source image paths
src_images = {
    "key.png": "/home/migueldorosario/.gemini/antigravity/brain/72dcc03b-9ca8-4afd-bcb4-6e2b9442de03/digital_trust_eidas_1782842778055.png",
    "wallet.png": "/home/migueldorosario/.gemini/antigravity/brain/72dcc03b-9ca8-4afd-bcb4-6e2b9442de03/eudi_wallet_presentation_1782842786266.png",
    "global.png": "/home/migueldorosario/.gemini/antigravity/brain/72dcc03b-9ca8-4afd-bcb4-6e2b9442de03/global_trust_connectivity_1782842794016.png"
}

# Create assets directory
os.makedirs(assets_dir, exist_ok=True)

# Copy images
for dest_name, src_path in src_images.items():
    dest_path = os.path.join(assets_dir, dest_name)
    try:
        shutil.copy(src_path, dest_path)
        print(f"Copied {src_path} to {dest_path}")
    except Exception as e:
        print(f"Error copying {src_path}: {e}")

# HTML for the article (materia_eidas_diagramada.html)
materia_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Especial Confiança Digital - eIDAS</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
        
        @page {
            size: A4;
            margin: 2.5cm 2cm 2.5cm 2cm;
            @top-center {
                content: "ESPECIAL O CAFEZINHO • CONFIANÇA E RASTREABILIDADE DIGITAL";
                font-family: 'Outfit', sans-serif;
                font-size: 8pt;
                color: #8c9ba5;
                font-weight: 600;
                letter-spacing: 0.1em;
                border-bottom: 0.5px solid #e2e8f0;
                width: 100%;
                padding-bottom: 8px;
            }
            @bottom-right {
                content: counter(page);
                font-family: 'Outfit', sans-serif;
                font-size: 9pt;
                color: #718096;
                font-weight: 600;
            }
            @bottom-left {
                content: "ocafezinho.com";
                font-family: 'Outfit', sans-serif;
                font-size: 8pt;
                color: #a0aec0;
                font-weight: 400;
            }
        }

        body {
            font-family: 'Outfit', sans-serif;
            color: #2d3748;
            line-height: 1.6;
            font-size: 10.5pt;
            background-color: #ffffff;
        }

        .cover {
            page-break-after: always;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            padding-top: 2cm;
        }

        .cover-tag {
            background-color: #1a365d;
            color: #f7fafc;
            padding: 6px 12px;
            font-size: 8.5pt;
            font-weight: 600;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            border-radius: 2px;
            margin-bottom: 24px;
        }

        h1.cover-title {
            font-family: 'Playfair Display', serif;
            font-size: 32pt;
            line-height: 1.15;
            color: #1a202c;
            font-weight: 700;
            margin: 0 0 16px 0;
        }

        .cover-subtitle {
            font-size: 14pt;
            color: #4a5568;
            font-weight: 300;
            margin-bottom: 40px;
            line-height: 1.4;
        }

        .cover-meta {
            border-top: 1px solid #e2e8f0;
            padding-top: 20px;
            width: 100%;
            font-size: 9.5pt;
            color: #718096;
        }

        .cover-meta strong {
            color: #2d3748;
        }

        .cover-image-container {
            width: 100%;
            margin-top: 1.5cm;
            text-align: center;
        }

        .cover-image-container img {
            width: 80%;
            max-height: 10cm;
            border-radius: 6px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            border: 1px solid #e2e8f0;
        }

        h2 {
            font-family: 'Playfair Display', serif;
            font-size: 18pt;
            color: #1a365d;
            margin-top: 40px;
            margin-bottom: 16px;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 6px;
            page-break-inside: avoid;
        }

        p {
            margin-bottom: 16px;
            text-align: justify;
        }

        .intro-lead {
            font-size: 11.5pt;
            color: #4a5568;
            font-weight: 400;
            line-height: 1.7;
            margin-bottom: 24px;
        }

        .highlight-box {
            background-color: #f7fafc;
            border-left: 4px solid #c5a059;
            padding: 16px 20px;
            margin: 24px 0;
            border-radius: 0 4px 4px 0;
            page-break-inside: avoid;
        }

        .highlight-box p {
            margin: 0;
            font-style: italic;
            color: #2d3748;
        }

        .article-image {
            width: 100%;
            margin: 30px 0;
            text-align: center;
            page-break-inside: avoid;
        }

        .article-image img {
            width: 90%;
            max-height: 8.5cm;
            border-radius: 4px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            border: 1px solid #e2e8f0;
        }

        .image-caption {
            font-size: 8pt;
            color: #718096;
            margin-top: 8px;
            font-style: italic;
            text-align: center;
        }

        .recommendations {
            margin-top: 24px;
        }

        .recommendation-item {
            margin-bottom: 20px;
            page-break-inside: avoid;
        }

        .recommendation-title {
            font-weight: 600;
            color: #1a365d;
            font-size: 11pt;
            margin-bottom: 4px;
        }

        .two-column {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            margin-top: 20px;
            page-break-inside: avoid;
        }

        .column {
            flex: 1;
            background-color: #f8fafc;
            padding: 15px;
            border-radius: 4px;
            border: 1px solid #e2e8f0;
        }

        .column h3 {
            margin-top: 0;
            font-family: 'Outfit', sans-serif;
            font-size: 11pt;
            color: #1a365d;
            border-bottom: 2px solid #c5a059;
            padding-bottom: 4px;
        }

        .column ul {
            padding-left: 18px;
            margin-bottom: 0;
            font-size: 9.5pt;
        }

        .column li {
            margin-bottom: 6px;
        }

        .market-metrics {
            display: flex;
            justify-content: space-between;
            gap: 15px;
            margin: 25px 0;
            page-break-inside: avoid;
        }

        .metric-card {
            flex: 1;
            background-color: #1a365d;
            color: #ffffff;
            padding: 15px;
            text-align: center;
            border-radius: 4px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }

        .metric-value {
            font-size: 20pt;
            font-weight: 800;
            color: #c5a059;
            margin-bottom: 4px;
        }

        .metric-label {
            font-size: 8pt;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #e2e8f0;
        }
    </style>
</head>
<body>

    <!-- Capa -->
    <div class="cover">
        <div class="cover-tag">Relatório Especial</div>
        <h1 class="cover-title">Rastreabilidade e<br>Confiança Digital</h1>
        <div class="cover-subtitle">O impacto global do regulamento eIDAS europeu e as diretrizes estratégicas para o avanço da infraestrutura brasileira.</div>
        
        <div class="cover-image-container">
            <img src="eidas_assets/key.png" alt="Chave Digital de Confiança">
        </div>
        
        <div style="flex-grow: 1;"></div>
        
        <div class="cover-meta">
            Veículo: <strong>O Cafezinho</strong> &nbsp;|&nbsp; 
            Autor: <strong>Equipe de Jornalismo e Tecnologia</strong> &nbsp;|&nbsp; 
            Data: <strong>30 de Junho de 2026</strong>
        </div>
    </div>

    <!-- Introdução -->
    <h2>1. O que é o eIDAS e a Revolução da Identidade</h2>
    
    <p class="intro-lead">No cenário global de transformação digital, a segurança nas transações eletrônicas deixou de ser apenas um diferencial técnico para se tornar uma infraestrutura crítica de soberania e governança. O principal referencial regulatório dessa mudança é o <strong>eIDAS</strong> (<em>electronic Identification, Authentication and trust Services</em>), instituído pela União Europeia por meio do <strong>Regulamento (UE) nº 910/2014</strong> e recentemente atualizado pela versão <strong>eIDAS 2.0 (Regulamento UE 2024/1183)</strong>.</p>
    
    <p>Ao contrário do que muitos pensam, o eIDAS não é uma empresa privada espanhola ou europeia, mas sim a norma jurídica comunitária que padroniza os serviços de identificação eletrônica e serviços de confiança no Mercado Único Europeu. Ele provê a base legal para garantir a rastreabilidade, o não-repúdio, a autenticidade e a integridade de documentos e transações transfronteiriças, dividindo os serviços de confiança em assinaturas eletrônicas, selos eletrônicos (para pessoas jurídicas), carimbos do tempo, serviços de entrega eletrônica registrada e autenticação de sites.</p>

    <div class="highlight-box">
        <p>"O eIDAS 2.0 redefine a cidadania europeia ao introduzir a EUDI Wallet, uma carteira digital que descentraliza a identidade e devolve ao cidadão o controle estrito sobre seus atributos e credenciais verificáveis."</p>
    </div>

    <h2>2. O Ecossistema e os Certificadores (QTSPs)</h2>
    
    <p>A robustez do eIDAS reside no papel dos <strong>Prestadores de Serviços de Confiança Qualificados</strong> (<em>Qualified Trust Service Providers</em> - QTSPs). Essas entidades privadas e públicas são rigorosamente auditadas por órgãos nacionais de supervisão para emitir certificados qualificados que garantem o valor jurídico máximo das transações eletrônicas, equivalente ao de uma assinatura física feita de próprio punho.</p>
    
    <p>A Espanha é um dos países com o ecossistema mais ativo e diversificado sob o regulamento eIDAS. O país possui diversos certificadores qualificados, que operam sob a supervisão do <em>Ministerio para la Transformación Digital y de la Función Pública</em>. Entre os principais nomes espanhóis e europeus destacam-se:</p>

    <div class="two-column">
        <div class="column">
            <h3>Destaques na Espanha</h3>
            <ul>
                <li><strong>FNMT-RCM:</strong> Fábrica Nacional de Moneda y Timbre, principal emissora pública estatal de chaves públicas.</li>
                <li><strong>Camerfirma:</strong> Criada pelas Câmaras de Comércio espanholas para o ecossistema corporativo.</li>
                <li><strong>Firmaprofesional:</strong> Focada em certificados profissionais e de corporações reguladas.</li>
                <li><strong>Tecalis, Víntegris, Lleida.net:</strong> Players de tecnologia qualificados com forte presença em nuvem.</li>
                <li><strong>Signaturit:</strong> Solução integrada de assinaturas eletrônicas e carimbo do tempo.</li>
            </ul>
        </div>
        <div class="column">
            <h3>Destaques na Europa</h3>
            <ul>
                <li><strong>D-Trust (Alemanha):</strong> Subsidiária da Bundesdruckerei, focada na segurança do cidadão e do Estado.</li>
                <li><strong>LuxTrust (Luxemburgo):</strong> Prestador de serviços integrados e chaves para o setor bancário europeu.</li>
                <li><strong>InfoCert (Itália):</strong> O maior prestador qualificado europeu, com atuação globalizada.</li>
                <li><strong>Swisscom (Suíça):</strong> Opera em conformidade e interoperabilidade de forma equivalente via ZertES.</li>
            </ul>
        </div>
    </div>

    <!-- Nova Página -->
    <h2 style="page-break-before: always;">3. Dados de Mercado: Valores da Confiança Digital</h2>
    
    <p>O mercado global de assinaturas eletrônicas e confiança digital vive uma expansão acelerada, catalisada pela necessidade de transações digitais sem papel, pela redução de custos operacionais e, mais recentemente, pela introdução do eIDAS 2.0.</p>

    <div class="market-metrics">
        <div class="metric-card">
            <div class="metric-value">US$ 2.05 B</div>
            <div class="metric-label">Valor do Mercado Europeu (2024)</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">US$ 39.74 B</div>
            <div class="metric-label">Projeção de Mercado (2033)</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">~39%</div>
            <div class="metric-label">Taxa de Crescimento Anual (CAGR)</div>
        </div>
    </div>

    <p>Apenas na França, o mercado específico de serviços de confiança digital já movimenta cerca de <strong>€ 950 milhões</strong> anuais. Analistas apontam que a transição de processos físicos para eletrônicos na União Europeia tem o potencial de multiplicar o volume de transações certificadas por sete até 2030, superando os <strong>US$ 10 bilhões</strong> líquidos em receitas diretas para prestadores qualificados. O motor principal deste crescimento na segunda metade desta década é a implementação da <strong>EUDI Wallet (European Digital Identity Wallet)</strong>, que deve ser adotada por todos os Estados-membros até 2026.</p>

    <div class="article-image">
        <img src="eidas_assets/wallet.png" alt="EUDI Wallet e Identidades Digitais">
        <div class="image-caption">Figura 1: A representação visual das credenciais digitais descentralizadas no ecossistema eIDAS.</div>
    </div>

    <h2>4. Cenário Mundial: Sistemas de Certificação Fora da Europa</h2>
    
    <p>Diversos países criaram suas próprias estruturas jurídicas e tecnológicas para legitimar assinaturas digitais e estabelecer a rastreabilidade nas comunicações, variando em rigor técnico e centralização institucional:</p>
    
    <p><strong>Estados Unidos:</strong> Operam sob uma filosofia focada no mercado livre e na facilidade de uso, regidos pelo <strong>ESIGN Act</strong> federal (2000) e pela lei estadual <strong>UETA</strong> (<em>Uniform Electronic Transactions Act</em>). Diferente do eIDAS, que impõe requisitos técnicos centralizados e certificações estatais estritas para a validade máxima (QES), a lei norte-americana adota uma abordagem minimalista de "intencionalidade". A assinatura eletrônica é válida se as partes concordarem, o que permitiu o domínio de grandes corporações de software (como Adobe Sign e DocuSign).</p>
    
    <p><strong>China:</strong> A <strong>Lei de Assinatura Eletrônica da República Popular da China</strong> distingue assinaturas comuns de assinaturas eletrônicas "confiáveis" (tecnicamente equivalentes às qualificadas do eIDAS). Os certificadores operam sob autorização do Ministério da Indústria e Tecnologia da Informação (MIIT), sendo amplamente utilizados em grandes ecossistemas digitais locais.</p>
    
    <p><strong>Brasil:</strong> O país conta com a <strong>ICP-Brasil (Infraestrutura de Chaves Públicas Brasileira)</strong>, criada em 2001 e gerida pelo <strong>ITI (Instituto Nacional de Tecnologia da Informação)</strong>. Adicionalmente, a <strong>Lei nº 14.063 de 2020</strong> dividiu as assinaturas eletrônicas brasileiras em três níveis (Simples, Avançada e Qualificada), replicando de forma muito próxima a lógica conceitual de gradação de segurança do eIDAS europeu.</p>

    <!-- Nova Página -->
    <h2 style="page-break-before: always;">5. O Caminho para o Brasil: Diretrizes para Integração</h2>
    
    <p>O Brasil possui um dos sistemas de identidade digital mais sofisticados do mundo, com o portal <strong>Gov.br</strong> atendendo a mais de 150 milhões de cidadãos e a ICP-Brasil garantindo a validade jurídica de transações críticas. Contudo, para se padronizar e se integrar plenamente ao eIDAS europeu, o Brasil deve priorizar as seguintes ações estratégicas:</p>

    <div class="article-image">
        <img src="eidas_assets/global.png" alt="Conectividade Digital Brasil e Europa">
        <div class="image-caption">Figura 2: A unificação e conformidade entre os modelos de chaves públicas do Sul Global e o eIDAS.</div>
    </div>

    <div class="recommendations">
        <div class="recommendation-item">
            <div class="recommendation-title">1. Acordos de Reconhecimento Mútuo (eIDAS Artigo 14)</div>
            <p>O ITI brasileiro deve estabelecer negociações com a Comissão Europeia sob o amparo do Artigo 14 do eIDAS. Isso garante que as assinaturas eletrônicas qualificadas da ICP-Brasil tenham equivalência na Europa como Qualified Electronic Signatures (QES), permitindo que empresas nacionais assinem contratos transfronteiriços com validade instantânea.</p>
        </div>

        <div class="recommendation-item">
            <div class="recommendation-title">2. Alinhamento Técnico da Carteira Digital Gov.br com a EUDI Wallet</div>
            <p>A carteira do Gov.br deve adotar os padrões técnicos do Architecture and Reference Framework (ARF) europeu, como chaves de Credenciais Verificáveis (Verifiable Credentials - W3C) e protocolos OpenID Connect. Isso possibilitará que identidades brasileiras sejam validadas em wallets europeias em tempo real.</p>
        </div>

        <div class="recommendation-item">
            <div class="recommendation-title">3. Regulamentação de Novos Serviços de Confiança</div>
            <p>O Brasil deve formalizar padrões específicos para Serviços de Entrega Eletrônica Registrada Qualificada (e-Delivery) e certificados de autenticação de servidores web equivalentes aos QWACs (Qualified Website Authentication Certificates) europeus, blindando as transações do e-commerce.</p>
        </div>

        <div class="recommendation-item">
            <div class="recommendation-title">4. Desburocratização e Redução de Custos na ICP-Brasil</div>
            <p>Diferente do eIDAS, que caminha para chaves em nuvem baratas integradas ao mobile, a ICP-Brasil ainda impõe custos significativos. É essencial democratizar o acesso e baratear a certificação qualificada para expandir a maturidade digital nacional.</p>
        </div>
    </div>

</body>
</html>
"""

# Write HTML for the article
with open(os.path.join(base_dir, "materia_eidas_diagramada.html"), "w", encoding="utf-8") as f:
    f.write(materia_html)
print("Saved materia_eidas_diagramada.html")

# HTML for the presentation slides (apresentacao_eidas.html)
presentation_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Apresentação eIDAS & Confiança Digital</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Playfair+Display:wght@700&display=swap');
        
        @page {
            size: 297mm 167mm; /* 16:9 Landscape */
            margin: 0;
        }

        body {
            font-family: 'Outfit', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #050c18;
            color: #ffffff;
            -webkit-print-color-adjust: exact;
        }

        .slide {
            width: 297mm;
            height: 167mm;
            page-break-after: always;
            box-sizing: border-box;
            position: relative;
            padding: 20mm 25mm;
            background: linear-gradient(135deg, #050c18 0%, #0d1e3d 100%);
            overflow: hidden;
        }

        /* Slide elements */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 10px;
            margin-bottom: 15px;
        }

        .header .logo {
            font-weight: 800;
            font-size: 11pt;
            letter-spacing: 0.15em;
            color: #c5a059;
            text-transform: uppercase;
        }

        .header .slide-number {
            font-size: 10pt;
            color: #8c9ba5;
            font-weight: 600;
        }

        h2.slide-title {
            font-family: 'Playfair Display', serif;
            font-size: 28pt;
            color: #ffffff;
            margin-top: 0;
            margin-bottom: 20px;
            font-weight: 700;
        }

        h2.slide-title span {
            color: #c5a059;
        }

        /* Title Slide Layout */
        .cover-slide {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            padding: 25mm 25mm;
            background: radial-gradient(circle at 80% 20%, #1e3a6a 0%, #050c18 70%);
        }

        .cover-tag {
            color: #00d2ff;
            font-size: 10pt;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.25em;
            margin-bottom: 15px;
        }

        .cover-title {
            font-family: 'Playfair Display', serif;
            font-size: 42pt;
            line-height: 1.15;
            margin: 0 0 15px 0;
            font-weight: 700;
        }

        .cover-title span {
            color: #c5a059;
        }

        .cover-subtitle {
            font-size: 16pt;
            color: #cbd5e0;
            font-weight: 300;
            max-width: 75%;
            line-height: 1.4;
            margin-bottom: 30px;
        }

        .cover-footer {
            margin-top: auto;
            font-size: 10pt;
            color: #718096;
            border-top: 1px solid rgba(255,255,255,0.1);
            width: 100%;
            padding-top: 15px;
        }

        /* Two Column Layout */
        .columns {
            display: flex;
            justify-content: space-between;
            gap: 40px;
            height: 105mm;
        }

        .col-left {
            flex: 1.2;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .col-right {
            flex: 0.8;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .col-right img {
            width: 100%;
            max-height: 90mm;
            border-radius: 6px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.5);
            border: 1px solid rgba(197, 160, 89, 0.3);
        }

        /* Lists */
        ul.slide-list {
            padding-left: 20px;
            margin: 0;
        }

        ul.slide-list li {
            font-size: 13pt;
            margin-bottom: 15px;
            line-height: 1.4;
            color: #e2e8f0;
        }

        ul.slide-list li strong {
            color: #c5a059;
        }

        /* Stat cards */
        .stats-grid {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            margin-top: 20px;
        }

        .stat-card {
            flex: 1;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 6px;
            padding: 25px 15px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            border-color: #c5a059;
            background: rgba(255, 255, 255, 0.08);
        }

        .stat-num {
            font-size: 32pt;
            font-weight: 800;
            color: #00d2ff;
            margin-bottom: 8px;
        }

        .stat-num.gold {
            color: #c5a059;
        }

        .stat-desc {
            font-size: 10.5pt;
            color: #cbd5e0;
            line-height: 1.3;
        }

        /* Comparison Table */
        table.compare-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            font-size: 11pt;
        }

        table.compare-table th {
            background-color: rgba(197, 160, 89, 0.15);
            color: #c5a059;
            text-align: left;
            padding: 10px 15px;
            font-weight: 600;
            border-bottom: 2px solid #c5a059;
        }

        table.compare-table td {
            padding: 12px 15px;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            color: #cbd5e0;
        }

        table.compare-table tr:hover td {
            color: #ffffff;
            background-color: rgba(255,255,255,0.02);
        }

        .badge {
            background-color: #1c3d5a;
            color: #00d2ff;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 8.5pt;
            font-weight: 600;
        }

        .badge.gold {
            background-color: #5c4819;
            color: #c5a059;
        }
    </style>
</head>
<body>

    <!-- Slide 1: Cover -->
    <div class="slide cover-slide">
        <div class="cover-tag">Apresentação Estratégica</div>
        <h1 class="cover-title">eIDAS & <span>Confiança Digital</span></h1>
        <div class="cover-subtitle">Rastreabilidade Eletrônica, Roteiro Global e a Padronização Transfronteiriça para o Brasil.</div>
        <div class="cover-footer">
            Veículo: <strong>O Cafezinho</strong> &nbsp;|&nbsp; Data: <strong>Junho de 2026</strong>
        </div>
    </div>

    <!-- Slide 2: O que é eIDAS -->
    <div class="slide">
        <div class="header">
            <div class="logo">O Cafezinho</div>
            <div class="slide-number">02</div>
        </div>
        <h2 class="slide-title">O que é o <span>eIDAS</span>?</h2>
        <div class="columns">
            <div class="col-left">
                <ul class="slide-list">
                    <li><strong>Regulamento Comunitário:</strong> Norma da UE (Regulamento 910/2014) que unifica chaves de identidade e segurança digital.</li>
                    <li><strong>eIDAS 2.0 (Regulamento UE 2024/1183):</strong> Atualização que traz a <strong>EUDI Wallet</strong> (Carteira de Identidade Digital da UE).</li>
                    <li><strong>Foco em Segurança:</strong> Estabelece validade legal qualificada para assinaturas, selos, carimbos do tempo e entrega de documentos.</li>
                    <li><strong>Não é uma Empresa:</strong> É um padrão regulatório continental que serve de referência mundial de governança.</li>
                </ul>
            </div>
            <div class="col-right">
                <img src="eidas_assets/key.png" alt="Chave de Confiança">
            </div>
        </div>
    </div>

    <!-- Slide 3: O Ecossistema e Certificadoras -->
    <div class="slide">
        <div class="header">
            <div class="logo">O Cafezinho</div>
            <div class="slide-number">03</div>
        </div>
        <h2 class="slide-title">Certificadores Qualificados <span>(QTSPs)</span></h2>
        <div class="columns" style="height: 110mm;">
            <div class="col-left" style="flex: 1; justify-content: flex-start; padding-top: 10px;">
                <h3 style="color: #c5a059; margin-bottom: 12px; font-family: 'Outfit'; font-size: 15pt;">O Mercado Espanhol (Destaques)</h3>
                <ul class="slide-list" style="font-size: 11pt;">
                    <li><strong>FNMT-RCM:</strong> Emissora pública estatal espanhola de alta confiabilidade.</li>
                    <li><strong>Camerfirma:</strong> Criada pelas Câmaras de Comércio espanholas para o setor empresarial.</li>
                    <li><strong>Tecalis, Víntegris e Lleida.net:</strong> Players dinâmicos privados que oferecem software de assinatura e identidades descentralizadas na nuvem.</li>
                </ul>
            </div>
            <div class="col-left" style="flex: 1; justify-content: flex-start; padding-top: 10px;">
                <h3 style="color: #00d2ff; margin-bottom: 12px; font-family: 'Outfit'; font-size: 15pt;">O Mercado Europeu (Destaques)</h3>
                <ul class="slide-list" style="font-size: 11pt;">
                    <li><strong>InfoCert (Itália):</strong> A maior QTSP do bloco europeu, com presença em diversos continentes.</li>
                    <li><strong>D-Trust (Alemanha):</strong> Braço de segurança do grupo federal alemão Bundesdruckerei.</li>
                    <li><strong>LuxTrust (Luxemburgo):</strong> Forte integração de certificados de confiança ao mercado de investimentos e financeiro.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Slide 4: Dados de Mercado -->
    <div class="slide">
        <div class="header">
            <div class="logo">O Cafezinho</div>
            <div class="slide-number">04</div>
        </div>
        <h2 class="slide-title">Valores de Mercado &amp; <span>Projeções</span></h2>
        <div class="columns">
            <div class="col-left" style="flex: 1.1;">
                <ul class="slide-list">
                    <li><strong>Crescimento Acelerado:</strong> Transição paperless e exigências regulatórias impulsionam a confiança digital.</li>
                    <li><strong>Mercado Europeu 2024:</strong> Avaliado em <strong>US$ 2,05 bilhões</strong>.</li>
                    <li><strong>Foco 2033:</strong> Projeções estimam que alcançará a marca de <strong>US$ 39,74 bilhões</strong>.</li>
                    <li><strong>Efeito EUDI Wallet:</strong> A massificação da carteira móvel até 2026 abrirá novas frentes comerciais de atributos qualificados.</li>
                </ul>
            </div>
            <div class="col-right" style="flex: 0.9; display: block; padding-top: 15px;">
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-num">US$ 2.05B</div>
                        <div class="stat-desc">Mercado Europeu em 2024</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-num gold">US$ 39.74B</div>
                        <div class="stat-desc">Projeção de Fechamento (2033)</div>
                    </div>
                </div>
                <div class="stats-grid" style="margin-top: 15px;">
                    <div class="stat-card" style="padding: 15px;">
                        <div class="stat-num" style="font-size: 24pt; color: #00d2ff;">39%</div>
                        <div class="stat-desc" style="font-size: 9pt;">Taxa de Crescimento Anual (CAGR)</div>
                    </div>
                    <div class="stat-card" style="padding: 15px;">
                        <div class="stat-num gold" style="font-size: 24pt;">€ 950M</div>
                        <div class="stat-desc" style="font-size: 9pt;">Valor do Mercado na França</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Slide 5: Cenário Mundial -->
    <div class="slide">
        <div class="header">
            <div class="logo">O Cafezinho</div>
            <div class="slide-number">05</div>
        </div>
        <h2 class="slide-title">Mundo: <span>Modelos Comparados</span></h2>
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Região / País</th>
                    <th>Estrutura Legal</th>
                    <th>Filosofia / Rigor Técnico</th>
                    <th>Destaques</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>União Europeia</strong></td>
                    <td>Regulamento eIDAS 1.0 &amp; 2.0</td>
                    <td>Rígido, centralizado com certificados qualificados estatais (QES)</td>
                    <td><span class="badge">EUDI Wallet (2026)</span></td>
                </tr>
                <tr>
                    <td><strong>Estados Unidos</strong></td>
                    <td>ESIGN Act &amp; UETA</td>
                    <td>Flexível, focado em mercado livre e intencionalidade de partes</td>
                    <td><span class="badge gold">Adobe Sign / DocuSign</span></td>
                </tr>
                <tr>
                    <td><strong>China</strong></td>
                    <td>Lei de Assinatura Eletrônica</td>
                    <td>Assinaturas "Confiáveis" validadas sob permissões do governo (MIIT)</td>
                    <td><span class="badge">Criptografia Local</span></td>
                </tr>
                <tr>
                    <td><strong>Brasil</strong></td>
                    <td>ICP-Brasil &amp; Lei 14.063/2020</td>
                    <td>Misto: ICP-Brasil (qualificada) + Gov.br (avançada e simples)</td>
                    <td><span class="badge gold">150M de Contas Gov.br</span></td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- Slide 6: O Caminho do Brasil -->
    <div class="slide">
        <div class="header">
            <div class="logo">O Cafezinho</div>
            <div class="slide-number">06</div>
        </div>
        <h2 class="slide-title">Brasil: <span>4 Diretrizes Estratégicas</span></h2>
        <div class="columns">
            <div class="col-left">
                <ul class="slide-list" style="font-size: 11pt;">
                    <li><strong>Reconhecimento Mútuo:</strong> Iniciar tratativas de acordo sob o <strong>eIDAS Artigo 14</strong>, validando assinaturas ICP-Brasil diretamente na Europa.</li>
                    <li><strong>Evolução Tecnológica:</strong> Adequar a carteira do <strong>Gov.br</strong> aos padrões europeus da EUDI Wallet (W3C Verifiable Credentials).</li>
                    <li><strong>Novas Certificações:</strong> Implementar regulação local de serviços qualificados de e-Delivery e chaves qualificadas de servidores (QWACs).</li>
                    <li><strong>Desburocratização:</strong> Baratear e incentivar o acesso à certificação qualificada para expandir a inclusão digital corporativa.</li>
                </ul>
            </div>
            <div class="col-right">
                <img src="eidas_assets/global.png" alt="Conectividade Digital">
            </div>
        </div>
    </div>

    <!-- Slide 7: Conclusão -->
    <div class="slide" style="background: radial-gradient(circle at 10% 80%, #0d1e3d 0%, #050c18 70%);">
        <div class="header">
            <div class="logo">O Cafezinho</div>
            <div class="slide-number">07</div>
        </div>
        <h2 class="slide-title"><span>Conclusão:</span> O Futuro da Soberania Digital</h2>
        <div class="columns" style="height: 110mm; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
            <p style="font-size: 18pt; max-width: 85%; font-weight: 300; line-height: 1.5; color: #cbd5e0; margin-bottom: 25px;">
                A padronização transfronteiriça com o eIDAS não é apenas uma facilitação burocrática, mas uma <strong>estratégia de soberania digital</strong> para o Sul Global competir em igualdade técnica e jurídica nas transações comerciais internacionais.
            </p>
            <div style="font-size: 14pt; font-weight: 600; color: #c5a059;">
                O Cafezinho • Especial Confiança Digital 2026
            </div>
        </div>
    </div>

</body>
</html>
"""

# Write HTML for the presentation
with open(os.path.join(base_dir, "apresentacao_eidas.html"), "w", encoding="utf-8") as f:
    f.write(presentation_html)
print("Saved apresentacao_eidas.html")

# Render PDFs using WeasyPrint
try:
    print("Compiling materia_eidas_diagramada.pdf using WeasyPrint...")
    subprocess.run([
        "/home/migueldorosario/.local/bin/weasyprint", 
        os.path.join(base_dir, "materia_eidas_diagramada.html"),
        os.path.join(base_dir, "materia_eidas_diagramada.pdf")
    ], check=True)
    print("Successfully compiled materia_eidas_diagramada.pdf")
    
    print("Compiling apresentacao_eidas.pdf using WeasyPrint...")
    subprocess.run([
        "/home/migueldorosario/.local/bin/weasyprint", 
        os.path.join(base_dir, "apresentacao_eidas.html"),
        os.path.join(base_dir, "apresentacao_eidas.pdf")
    ], check=True)
    print("Successfully compiled apresentacao_eidas.pdf")
    
except Exception as e:
    print(f"Error compiling PDFs: {e}")

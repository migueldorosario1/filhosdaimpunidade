import os
import requests
from requests.auth import HTTPBasicAuth
import json

wp_site = "https://controle.ocafezinho.com"
wp_user = "Redator"
wp_pass = "Ziod RKRI SESl vGwF UfGW KJWG"

# 1. Upload the image
image_path = "/home/migueldorosario/.gemini/antigravity/brain/a250bd43-11c8-4b7e-bc0d-2f718495271e/abstract_copyright_1783023442020.png"
media_url = f"{wp_site}/wp-json/wp/v2/media"

with open(image_path, "rb") as img_file:
    headers = {
        "Content-Type": "image/png",
        "Content-Disposition": f"attachment; filename={os.path.basename(image_path)}"
    }
    print("Uploading image...")
    res = requests.post(media_url, headers=headers, auth=HTTPBasicAuth(wp_user, wp_pass), data=img_file)
    if res.status_code != 201:
        print(f"Failed to upload image: {res.status_code} {res.text}")
        exit(1)
    
    media_data = res.json()
    image_id = media_data["id"]
    print(f"Image uploaded successfully. ID: {image_id}")

# 2. Create the page
page_url = f"{wp_site}/wp-json/wp/v2/pages"

title = "Como verificar o status de direitos autorais de uma imagem"
slug = "como-verificar-o-status-de-direitos-autorais-de-uma-imagem"

content = """
<p>Não tem certeza se uma imagem é de uso livre? Explore métodos práticos para verificar o status dos direitos autorais, identificar os criadores e evitar o uso não autorizado da imagem.</p>
<hr />
<p>Usar uma imagem protegida por direitos autorais pode lhe causar problemas legais. Muitos proprietários de sites copiam imagens de mecanismos de busca e presumem que o acesso gratuito abrange o uso público. Essa presunção frequentemente leva a reclamações de direitos autorais, cobranças ou remoção de conteúdo.</p>

<p>Algumas fotos pertencem a agências, enquanto outras são de propriedade pessoal. A ausência de marca d'água também não confirma o uso gratuito. Uma verificação cuidadosa protege sites, blogs e páginas de redes sociais de disputas desnecessárias.</p>

<p>Aqui estão alguns métodos comprovados que podem ajudar a identificar o status de direitos autorais de uma imagem com mais confiança.</p>

<h2>Verificar metadados da imagem</h2>
<p>Muitas fotos digitais contêm metadados, que armazenam informações ocultas sobre o arquivo. Isso inclui informações sobre câmeras, softwares de edição, autoria, datas de criação e histórico de licenciamento. Uma rápida análise dos metadados pode revelar pistas úteis sobre a propriedade da imagem antes que alguém a utilize publicamente.</p>

<p>Tanto o Windows quanto o macOS incluem ferramentas integradas para visualização de metadados. Clique com o botão direito do mouse no arquivo, abra as propriedades e examine a guia de detalhes com atenção. Alguns programas de edição também exibem nomes de criadores, avisos de direitos autorais e informações da agência dentro da estrutura do arquivo.</p>

<p>Ainda assim, os metadados por si só não resolvem completamente as questões de propriedade. Alguns sites removem esses dados durante o upload para reduzir o tamanho do arquivo. Outros os alteram durante a compressão. Mesmo assim, a ausência de metadados ainda gera cautela, pois criadores legítimos geralmente deixam informações sobre a propriedade intelectual associadas a seus trabalhos profissionais.</p>

<h2>Examine o site de origem</h2>
<p>O site que hospeda uma imagem geralmente revela detalhes importantes sobre o licenciamento. Editores confiáveis costumam colocar os créditos da imagem perto da imagem ou em uma página dedicada às políticas de uso. Esses detalhes podem explicar os direitos de uso, restrições ou requisitos de pagamento relacionados ao arquivo.</p>

<p>Sites de notícias, museus e plataformas de fotografia geralmente exibem avisos de direitos autorais abaixo das seções de mídia. Algumas páginas também incluem os nomes dos colaboradores, vinculados a contratos de licenciamento. Ler esses avisos com atenção ajuda os usuários a evitar o uso indevido acidental e suposições incorretas sobre o acesso público.</p>

<h2>Procure por marcas d'água</h2>
<p>As marcas d'água geralmente indicam propriedade ativa e direitos de distribuição controlados. Os criadores costumam colocar marcas visíveis sobre as imagens. Isso desencoraja o uso não autorizado por terceiros. Uma marca d'água geralmente inclui um logotipo, o nome do criador ou o endereço do site. Ela indica a quem pertence a obra.</p>

<p>Algumas marcas d'água aparecem tênues perto dos cantos, enquanto outras se estendem por toda a imagem. Uma inspeção cuidadosa ajuda a identificar edições recortadas que tentam ocultar sinais de propriedade. Ampliar a imagem às vezes revela marcas parciais removidas durante tentativas de republicação não autorizada.</p>

<p>Ainda assim, alguns criadores evitam completamente as marcas d'água porque elas reduzem o apelo visual. Essa escolha não coloca a imagem automaticamente em domínio público.</p>

<h2>Encontre o criador original</h2>
<p>Você já tentou todos os métodos e ainda não conseguiu descobrir os direitos de uso? Então, encontre o criador original. Plataformas online frequentemente distribuem imagens sem a devida atribuição. Portanto, você precisa rastrear o primeiro upload conhecido. Isso ajuda a descobrir detalhes de licenciamento, restrições de uso e informações de contato do criador com mais precisão.</p>

<p>Nesse caso, use uma ferramenta avançada de busca por imagem para rastrear versões antigas de uma foto online. Os resultados da busca podem revelar páginas de portfólio, sites de fotografia ou artigos arquivados relacionados ao criador. Uploads mais antigos geralmente contêm registros de propriedade mais confiáveis do que versões republicadas recentemente em sites aleatórios.</p>

<p>E os perfis dos criadores geralmente contêm políticas de licenciamento diretas. Alguns fotógrafos permitem o uso editorial, mas restringem projetos comerciais. Outros exigem pagamento antes do início da redistribuição. Entrar em contato por meio das páginas de contato oficiais também ajuda a resolver dúvidas sobre a propriedade antes que surjam riscos legais posteriormente.</p>

<h2>Pesquisar registros de domínio público</h2>
<p>As imagens em bancos de dados de domínio público geralmente contêm notas de uso explicando os direitos de reprodução e as expectativas de atribuição para acesso público. Diversos arquivos confiáveis mantêm coleções pesquisáveis com orientações legais claras. Algumas fotografias entraram em domínio público porque os prazos de direitos autorais expiraram há muito tempo.</p>

<p>Outras obras se qualificaram por meio de normas de produção governamentais, que excluem certas obras oficiais dos requisitos padrão de proteção de propriedade. Ainda assim, cada registro segue regras diferentes em relação à reutilização e modificação. Algumas coleções permitem o uso educacional, mas restringem projetos de publicidade comercial. Ler as notas de licenciamento ao lado de cada imagem evita confusões posteriores. Uma análise cuidadosa continua sendo necessária, pois o acesso público nem sempre significa permissão comercial irrestrita.</p>

<h2>Consulte os registros do Escritório de Direitos Autorais</h2>
<p>Os escritórios de direitos autorais mantêm bancos de dados de registro contendo informações sobre a titularidade de obras criativas protegidas. Esses bancos de dados ajudam a confirmar os direitos autorais relativos a fotografias, ilustrações e obras de arte digitais. O registro fortalece a proteção legal, por isso muitos profissionais registram imagens valiosas por meio de sistemas governamentais oficiais.</p>

<p>As ferramentas de busca nos sites dos escritórios de direitos autorais geralmente incluem nomes de criadores, títulos e números de registro. A comparação desses registros com a fonte da imagem pode revelar rapidamente as relações de propriedade.</p>

<p>No entanto, obras não registradas ainda recebem proteção de direitos autorais em muitos países. O registro simplesmente aprimora as opções de aplicação da lei em caso de disputas. Esse detalhe confunde muitos usuários, pois eles esperam que toda imagem protegida esteja presente em bancos de dados públicos. A ausência de registros deve incentivar mais pesquisas, e não a reutilização imediata.</p>

<h2>Leia os termos do site de ações</h2>
<p>As plataformas de banco de imagens operam sob contratos de licenciamento detalhados. A compra de acesso a uma imagem raramente transfere os direitos de propriedade integralmente. Em vez disso, os usuários recebem permissão para uso limitado, sob as condições descritas nos termos de licenciamento e nas políticas de distribuição da plataforma.</p>

<p>Algumas licenças permitem campanhas publicitárias, banners de sites e produtos impressos. Outras restringem a revenda, a produção de mercadorias ou a criação de logotipos. Ler essas restrições atentamente evita o uso indevido após a compra. As agências costumam cobrar taxas adicionais quando os usuários excedem o escopo de distribuição permitido posteriormente.</p>

<h2>Conclusão</h2>
<p>A verificação de direitos autorais de imagens exige paciência, atenção e uma análise cuidadosa de múltiplas fontes. Metadados, perfis de criadores, avisos de licenciamento e registros de direitos autorais fornecem diferentes informações sobre a propriedade intelectual. Depender de apenas um método aumenta a probabilidade de conclusões incorretas e uso indevido da imagem posteriormente.</p>

<p>A verificação confiável também protege a credibilidade profissional. Empresas, blogueiros e criadores de conteúdo se beneficiam de práticas de publicação mais robustas quando confirmam os direitos de imagem antes do início da distribuição. Alguns minutos extras dedicados à verificação dos detalhes de propriedade podem evitar reclamações, notificações judiciais e danos à confiança após a publicação do conteúdo online.</p>
"""

data = {
    "title": title,
    "slug": slug,
    "content": content,
    "status": "publish",
    "featured_media": image_id
}

print("Creating page...")
res_page = requests.post(page_url, auth=HTTPBasicAuth(wp_user, wp_pass), json=data)

if res_page.status_code == 201:
    page_data = res_page.json()
    print("Page published successfully!")
    print(f"Link: {page_data['link']}")
else:
    print(f"Failed to create page: {res_page.status_code} {res_page.text}")

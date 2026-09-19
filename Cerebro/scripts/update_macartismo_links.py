import requests
from requests.auth import HTTPBasicAuth
import json
import os
from pathlib import Path
from dotenv import load_dotenv

ENV_FILE = Path("/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/.env.unificado")
load_dotenv(ENV_FILE)
wp_user = os.getenv("WP_USER_CAFEZINHO") or os.getenv("WP_USER")
wp_password = (
    os.getenv("WP_APP_PASSWORD_CAFEZINHO")
    or os.getenv("WP_PASS_CAFEZINHO")
    or os.getenv("WP_APP_PASSWORD")
    or os.getenv("WP_PASS")
)
if not wp_user or not wp_password:
    raise RuntimeError(f"Credenciais WordPress Cafezinho ausentes em {ENV_FILE}")

title = "A ressurreição do macartismo americano"

html_content = """<!-- wp:paragraph -->
<p>O Departamento de Estado dos Estados Unidos publicou recentemente um relatório intitulado <em>"<a href="https://unpopularfront.news" target="_blank" rel="noopener">Cuba: A Capital do Comunismo do Século XXI</a>"</em>. No anúncio oficial feito na rede social X, o Secretário de Estado Marco Rubio declarou que, por mais de seis décadas, o regime cubano teria sido o principal patrocinador do esquerdismo radical e do terceiromundismo dentro do território norte-americano, prometendo expor o que chamou de história de espionagem e subversão para a população dos Estados Unidos.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>O movimento seguiu-se à realização da chamada "Ministerial sobre o Ressurgimento do Terrorismo Político", evento organizado por Rubio que contou com discursos de nomes proeminentes da nova administração, como Scott Bessent, Kash Patel e Stephen Miller. Com sua retórica agressiva, Miller chegou a classificar os movimentos progressistas como um "câncer fatal para a civilização", afirmando que as instituições ocidentais se tornaram "covardes" e exortando a defesa da nação com a mesma força empregada contra um invasor que entra em uma residência familiar.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>O relatório governamental mira explicitamente organizadores da esquerda democrática interna, como os Socialistas Democráticos da América (DSA). Embora o próprio documento seja forçado a admitir que a organização possui compromissos ideológicos orgânicos e não foi moldada por controle direto de Havana, insiste em enquadrá-la em supostas redes de influência por conta de delegações enviadas à ilha. A combinação entre desqualificação das garantias constitucionais, ameaças formais de designação de grupos de esquerda como organizações terroristas e menções explícitas a investigações nos moldes das listas negras da Guerra Fria acendeu o alerta sobre a preparação de um clima sufocante de repressão política interna.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Em análise detalhada sobre a ofensiva promovida em Washington, o ensaísta e historiador americano <a href="https://johnganz.substack.com" target="_blank" rel="noopener">John Ganz</a> assinala que a tentativa da Casa Branca de atribuir a fermentação política interna a fantasmagóricas operações estrangeiras não é uma novidade, mas a reciclagem de um velho manual partidário. Ganz lembra que a tática remete diretamente ao "Pequeno Pânico Vermelho" da era Reagan, deflagrado em 1981 quando o Subcomitê do Senado sobre Segurança e Terrorismo, chefiado pelo senador Jeremiah Denton e abastecido por ideólogos ultraconservadores como Samuel Francis, tentou ressuscitar os mecanismos de caça às bruxas das décadas de 1950.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Como recorda Ganz em seu texto, analistas e conspiradores daquela época — como Arnaud de Borchgrave, autor do romance de desinformação <em>The Spike</em> — acusavam jornais independentes e movimentos sociais de atuarem como fantoches de Havana ou de Moscou para promover tumultos urbanos nos Estados Unidos. Contudo, o próprio ex-diretor da CIA, William Colby, ao depor na comissão da época, descartou tais teses conspiratórias ao certificar que os protestos e o ativismo político americano eram fenômenos estritamente autóctones, nascidos das próprias contradições sociais do país. Naquele momento, o hysteria mccarthista acabou naufragando em sua própria inconsistência fática.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Como era de se esperar, o bolsonarismo e a extrema-direita latino-americana já tentam se apropriar dessa cruzada norte-americana para alimentar seus próprios expedientes políticos. Na América Latina, marcada por gritantes desigualdades sociais e concentrada estrutura de renda, as elites conservadoras historicamente recorreram ao espantalho do anticomunismo como ferramenta de desinformação. O objetivo sempre foi criminalizar a luta por direitos sociais, proteger lucros e privilégios corporativos e desviar a atenção pública das reformas estruturais urgentes.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A narrativa reacionária, no entanto, falseia a realidade histórica ao pregar o fim da esquerda. O pensamento socialista e as forças progressistas nunca morreram nas Américas nem nos próprios Estados Unidos. Pelo contrário, permanecem dinâmicos e vivos. Exemplo recente e expressivo é a <a href="https://zohranmamdani.com" target="_blank" rel="noopener">vitória eleitoral expressiva de Zohran Mamdani</a> em Nova York, somada ao fortalecimento contínuo de candidaturas abertamente socialistas nas grandes metrópoles norte-americanas. Além disso, os Estados Unidos ostentam um sólido e vibrante ecossistema cultural e acadêmico onde o pensamento de esquerda desempenha papel central. Vale lembrar também que, antes da sufocante onda macartista de meados do século passado, o país serviu de refúgio e lar acolhedor para numerosos intelectuais e socialistas europeus que moldaram o debate público global.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A fixação da extrema-direita em reviver fantasmas da Guerra Fria escancara o desejo de ocultar os dramas sociais do modelo americano. Enquanto a retórica de segurança nacional avança, os Estados Unidos enfrentam uma desigualdade de renda crescente e visível precarização de seus serviços básicos. No setor de transportes, o país jamais desenvolveu uma rede moderna de trens de alta velocidade para integração territorial e mobilidade urbana, mantendo sua população dependente do transporte individual corporativo. Além disso, a ausência de um sistema público universal de saúde impõe um modelo financeiramente punitivo aos mais pobres, arrastando milhões de famílias trabalhadoras a dramas pessoais desumanos e falências por dívidas médicas.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>O contraste com a dinâmica geopolítica global fica ainda mais evidente quando se observa a estratégia da China. No centro da corrida tecnológica contemporânea, Pequim adota uma postura voltada ao desenvolvimento de plataformas de Inteligência Artificial de código aberto, como os recentes modelos globais disponibilizados abertamente pela comunidade chinesa. A diplomacia e a política tecnológica chinesas promovem um discurso prático de combate à desigualdade, incentivando o compartilhamento de códigos e ferramentas avançadas. Essa abordagem atua diretamente para evitar um futuro distópico no qual a inteligência artificial fique confinada ao monopólio exclusivo de poucas corporações transnacionais que controlam o acesso ao conhecimento do planeta.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A tentativa da atual Casa Branca de ressuscitar o macartismo anticomunista não passa de um sintoma de exaustão intelectual e impotência diante dos problemas reais da sociedade contemporânea. Fantasiar ameaças cubanas não criará redes de transporte rápido nos Estados Unidos, não garantirá médicos aos desassistidos e tampouco deterá a busca dos povos latino-americanos por justiça social e soberania tecnológica.</p>
<!-- /wp:paragraph -->"""

url_post = "https://controle.ocafezinho.com/wp-json/wp/v2/posts/262434"
auth = HTTPBasicAuth(wp_user, wp_password)

payload = {
    "title": title,
    "content": html_content,
    "status": "draft"
}

res = requests.post(url_post, auth=auth, json=payload)
print("Update Post status:", res.status_code)
if res.status_code in (200, 201):
    data = res.json()
    print("SUCCESSFULLY UPDATED DRAFT WITH LINKS!")
    print("Draft ID:", data.get("id"))
    print("Draft Link:", data.get("link"))
else:
    print("Error updating draft:", res.text)

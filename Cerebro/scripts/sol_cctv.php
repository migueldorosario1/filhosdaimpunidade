<?php
/**
 * SOL ☀️ — Contador do Cafezinho (WP Statistics) — página privada do CCTV.
 * Ordem do Miguel 01/09/2026: NADA visível no site; página só no controle, com histórico.
 * Batismo: 4º contador = SOL (GA4 · FAROL · LUMINA · SOL).
 * Regras: só responde em Host controle.* (404 no domínio público) + token ?k= (cofre: SOL_CCTV_TOKEN).
 * Mantenedor: DSM (Cerebro). Dados: plugin wp-statistics (instalado 01/09/2026 por esta ordem).
 */
if ( strpos( strtolower( $_SERVER['HTTP_HOST'] ?? '' ), 'controle.' ) !== 0 ) {
	http_response_code( 404 );
	exit( '404' );
}
if ( ! hash_equals( '__SOL_TOKEN__', (string) ( $_GET['k'] ?? '' ) ) ) {
	http_response_code( 403 );
	exit( '🔒' );
}
require __DIR__ . '/wp-load.php';

$online = do_shortcode( '[wpstatistics stat=usersonline]' );
$hoje   = do_shortcode( '[wpstatistics stat=visits time=today]' );
$total  = do_shortcode( '[wpstatistics stat=visitors time=total]' );

global $wpdb;
$dias30 = $wpdb->get_results(
	"SELECT last_counter d, COUNT(*) v FROM {$wpdb->prefix}statistics_visitor
	 WHERE last_counter >= DATE_SUB(CURDATE(), INTERVAL 29 DAY)
	 GROUP BY last_counter ORDER BY d", ARRAY_A );
$meses12 = $wpdb->get_results(
	"SELECT DATE_FORMAT(last_counter,'%Y-%m') m, COUNT(*) v FROM {$wpdb->prefix}statistics_visitor
	 WHERE last_counter >= DATE_SUB(CURDATE(), INTERVAL 11 MONTH)
	 GROUP BY m ORDER BY m", ARRAY_A );
$tabela = array_slice( array_reverse( $dias30 ), 0, 14 );

$fmt = function ( $rows, $k, $v ) {
	return [ wp_json_encode( array_column( $rows, $k ) ), wp_json_encode( array_map( 'intval', array_column( $rows, $v ) ) ) ];
};
[ $l30, $v30 ]   = $fmt( $dias30, 'd', 'v' );
[ $l12, $v12 ]   = $fmt( $meses12, 'm', 'v' );
$pico30          = $dias30 ? max( array_column( $dias30, 'v' ) ) : 0;
$media30         = $dias30 ? round( array_sum( array_column( $dias30, 'v' ) ) / max( count( $dias30 ), 1 ), 1 ) : 0;

/* Modo máquina: alimenta a página ☀️ SOL do painel CCTV V6 (Tencent) — mesmo token. */
if ( ( $_GET['fmt'] ?? '' ) === 'json' ) {
	$map = fn( $rows ) => array_map( fn( $r ) => [ 'data' => (string) $r['d'] ?: (string) $r['m'], 'views' => (int) $r['v'] ], $rows );
	header( 'Content-Type: application/json; charset=utf-8' );
	header( 'X-Robots-Tag: noindex, nofollow' );
	echo wp_json_encode( [
		'online'  => (int) $online,
		'hoje'    => (int) $hoje,
		'total'   => (int) $total,
		'pico30'  => (int) $pico30,
		'media30' => $media30,
		'dias30'  => $map( $dias30 ),
		'meses12' => array_map( fn( $r ) => [ 'data' => (string) $r['m'], 'views' => (int) $r['v'] ], $meses12 ),
	] );
	exit;
}
header( 'Content-Type: text/html; charset=utf-8' );
header( 'X-Robots-Tag: noindex, nofollow' );
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="120">
<meta name="robots" content="noindex,nofollow">
<title>SOL ☀️ — Contador do Cafezinho (CCTV)</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<style>
	:root { --bg:#101418; --card:#1a2129; --amber:#f5b942; --orange:#e8833a; --txt:#e8e6e1; --mut:#8b949e; }
	* { box-sizing:border-box; margin:0 }
	body { background:var(--bg); color:var(--txt); font:15px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif; padding:22px; max-width:1080px; margin:auto }
	h1 { font-size:26px; letter-spacing:.5px } h1 span { color:var(--amber) }
	.sub { color:var(--mut); margin:4px 0 18px; font-size:13px }
	.grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:12px; margin-bottom:18px }
	.card { background:var(--card); border:1px solid #2a333d; border-radius:12px; padding:16px }
	.card .n { font-size:34px; font-weight:700; color:var(--amber) } .card .t { color:var(--mut); font-size:12.5px; text-transform:uppercase; letter-spacing:.6px }
	.painel { background:var(--card); border:1px solid #2a333d; border-radius:12px; padding:16px; margin-bottom:18px }
	.painel h2 { font-size:15px; color:var(--orange); margin-bottom:10px; font-weight:600 }
	table { width:100%; border-collapse:collapse; font-size:14px }
	td,th { padding:7px 10px; border-bottom:1px solid #2a333d; text-align:left } th { color:var(--mut); font-weight:600; font-size:12px; text-transform:uppercase }
	td.num, th.num { text-align:right }
	footer { color:var(--mut); font-size:12px; margin-top:14px; text-align:center }
</style>
</head>
<body>
<h1><span>☀️ SOL</span> — Contador do Cafezinho</h1>
<p class="sub">CCTV privado · fonte: WP Statistics (contando desde 01/09/2026) · constelação: GA4 · FAROL · LUMINA · <b>SOL</b> · atualiza a cada 2 min</p>

<div class="grid">
	<div class="card"><div class="n"><?= esc_html( $online ) ?></div><div class="t">Online agora</div></div>
	<div class="card"><div class="n"><?= esc_html( $hoje ) ?></div><div class="t">Visitas hoje</div></div>
	<div class="card"><div class="n"><?= esc_html( $total ) ?></div><div class="t">Visitantes total</div></div>
	<div class="card"><div class="n"><?= esc_html( $pico30 ) ?></div><div class="t">Pico diário (30d)</div></div>
	<div class="card"><div class="n"><?= esc_html( $media30 ) ?></div><div class="t">Média diária (30d)</div></div>
</div>

<div class="painel">
	<h2>Visitas por dia — últimos 30 dias</h2>
	<canvas id="c30" height="110"></canvas>
</div>
<div class="painel">
	<h2>Visitas por mês — últimos 12 meses</h2>
	<canvas id="c12" height="90"></canvas>
</div>
<div class="painel">
	<h2>Histórico recente — últimos 14 dias</h2>
	<table>
		<tr><th>Dia</th><th class="num">Visitas</th></tr>
		<?php foreach ( $tabela as $r ) : ?>
			<tr><td><?= esc_html( $r['d'] ) ?></td><td class="num"><?= (int) $r['v'] ?></td></tr>
		<?php endforeach; ?>
	</table>
</div>
<footer>SOL ☀️ — privado (Host controle + token) · nada aparece no site público · DSM/Cerebro · 01/09/2026</footer>

<script>
const est = (c)=>({ borderColor:'#f5b942', backgroundColor:'rgba(245,185,66,.15)', pointBackgroundColor:'#e8833a', fill:true, tension:.35, borderWidth:2, color:c });
new Chart(c30, { type:'line', data:{ labels:<?= $l30 ?>, datasets:[{ label:'Visitas/dia', data:<?= $v30 ?>, ...est('#f5b942') }] },
	options:{ plugins:{legend:{display:false}}, scales:{ x:{ticks:{color:'#8b949e',maxTicksLimit:10}}, y:{beginAtZero:true,ticks:{color:'#8b949e'}} } } });
new Chart(c12, { type:'bar', data:{ labels:<?= $l12 ?>, datasets:[{ label:'Visitas/mês', data:<?= $v12 ?>, backgroundColor:'rgba(232,131,58,.75)', borderRadius:6 }] },
	options:{ plugins:{legend:{display:false}}, scales:{ x:{ticks:{color:'#8b949e'}}, y:{beginAtZero:true,ticks:{color:'#8b949e'}} } } });
</script>
</body>
</html>

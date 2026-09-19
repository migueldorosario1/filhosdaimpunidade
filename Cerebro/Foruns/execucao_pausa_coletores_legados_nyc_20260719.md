# Execução — pausa emergencial dos coletores legados em NYC

**Autorização:** Miguel, no chat, em 2026-07-19 09:07 BRT  
**Execução:** Codex (OpenAI)  
**Janela:** 2026-07-19 09:08–09:09 BRT / 12:08–12:09 UTC  
**Servidor:** `Cafezinho-failover-vigia`, NYC, `198.199.121.136`  
**Motivo:** coletores legados ativos sem consumidores, tempestade de chamadas LLM e crescimento de filas abandonadas.

## Backup anterior à mudança

- Arquivo remoto: `/root/crontab_backup_pre_pausa_coletores_legados_20260719_120826.txt`
- Tamanho: 10.814 bytes
- SHA-256: `aa44d1fc8b92e05b91c5404f0e87250f5cf991c33bce26e406648ad9dda99541`
- O backup contém o cron integral imediatamente anterior à pausa.
- Recuperação é possível, mas a restauração não deve ser feita integralmente: somente mediante autorização explícita e revisão da lista permitida.

## Onze agendamentos pausados

As linhas foram preservadas como comentários com a marca `PAUSADO_CODEX_MIGUEL_20260719_LEGADO_SEM_CONSUMIDOR`:

1. `robo_coleta_soberania.py` — minutos 8, 23, 38 e 53;
2. `robo_coleta_militar.py` — minutos 12, 27, 42 e 57;
3. `robo_coleta_latam.py` — minutos 2, 17, 32 e 47;
4. `robo_coleta_sheinbaum.py` — minutos 6, 21, 36 e 51;
5. `robo_coleta_ia.py` — minutos 0 e 30;
6. `robo_coleta_matriz_energetica.py` — minutos 5 e 35;
7. `robo_coleta_flavio_bolsonaro.py` — minutos 10 e 40;
8. `robo_coleta_fantastico.py` — minutos 8, 23, 38 e 53;
9. `robo_coleta_turismo.py` — minutos 4, 19, 34 e 49;
10. `robo_coleta_sobrenatural.py` — minutos 12, 27, 42 e 57;
11. `coletor_eleicoes.py` — minutos 0 e 30.

**SHA-256 do cron após a pausa:** `3e720c5d1be9759fcf055d5c6e572546b4b92d7dcc5478d695c4546faa527f48`.

## Processos encerrados

Antes da intervenção havia oito processos/wrappers visíveis:

- dois pares `bash + python` de `robo_coleta_militar.py`, iniciados em 13/07 e 18/07;
- um par `bash + python` de `robo_coleta_soberania.py`;
- um par `bash + python` de `robo_coleta_fantastico.py`.

Foi enviado `SIGTERM` apenas aos executáveis identificados. A primeira sessão de inspeção encerrou a si própria porque o padrão de busca aparecia no comando, mas a mudança do cron já estava concluída. Uma verificação independente posterior mostrou:

- processos-alvo restantes: **0**;
- agendamentos-alvo ativos: **0**;
- linhas-alvo preservadas e pausadas: **11**.

## Auditoria de portas laterais

Foram examinados:

- cron de todos os usuários;
- `/etc/cron.d`, rotinas diárias, horárias e semanais;
- `/var/spool/cron`;
- unidades e temporizadores systemd em `/etc/systemd/system` e `/lib/systemd/system`;
- lista de temporizadores ativos.

Resultado: nenhuma referência ativa lateral. As únicas 11 referências encontradas são as próprias linhas comentadas no cron de `root`. Tencent já estava silencioso e sem esses processos.

## Evidência de cessação

- Última chamada registrada como `motor_coletor:curadoria`: **2026-07-19 12:06:07 UTC**, `deepseek-v4-flash`.
- Momento do backup e pausa: **12:08:26 UTC**.
- Chamadas do motor posteriores a 12:08:26: **0**, verificadas às 12:09:22 UTC.

## Dimensão do gasto de hoje antes da pausa

Até a interrupção, o motor legado havia produzido 3.263 chamadas, 12.582.948 tokens de entrada, 1.169.047 tokens de saída e custo interno estimado de US$ 12,275416:

| Modelo | Chamadas | Custo interno US$ |
|---|---:|---:|
| `gpt-5-mini` | 910 | 8,881169 |
| `deepseek-v4-flash` | 1.585 | 2,465029 |
| `gemini-2.5-flash` | 768 | 0,929218 |

Esses valores são estimativas internas e ainda exigem conciliação com as cobranças reais dos provedores.

## Proteções estruturais pendentes

1. manifesto de produção com lista positiva de agentes autorizados;
2. failover incapaz de habilitar processos fora do manifesto;
3. validação produtor–consumidor antes de qualquer ativação;
4. trava contra sobreposição e tempo máximo obrigatório;
5. identidade real de cada chamador na telemetria;
6. rastreio de `pipeline_version`, host, `run_id`, `call_id`, tema, feed, item e destino;
7. alerta para fila crescendo sem consumo e explosão de chamadas;
8. conciliação diária com faturamento real por provedor, projeto e SKU;
9. separação rígida entre legado/V3, V4, Repetidor Estatal e sites temáticos;
10. teste de failover em modo simulação antes de aplicar cron em produção.

## Estado final

**DESATIVADO E VERIFICADO.** Nenhum arquivo de conteúdo ou fila foi apagado. O backup do cron permite auditoria e recuperação seletiva.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO — 2026-07-19 09:09 BRT

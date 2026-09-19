from pathlib import Path
import subprocess, json, hashlib, datetime, difflib

out = Path('/tmp/xm_20260910_0247')
root = Path('/home/migueldorosario/cerebro-miguel')
path = 'cerebro/Foruns/ponte_laura_completa/de_dell.md'
commit = 'eaf82844a59bec3347c745f53a07ca27aeed2a9d'
parent = subprocess.check_output(['git','rev-parse',commit+'^'],cwd=root).decode().strip()
before = subprocess.check_output(['git','show',parent+':'+path],cwd=root)
after = subprocess.check_output(['git','show',commit+':'+path],cwd=root)
removed = b''.join(line[1:] for line in subprocess.check_output(['git','diff','--unified=0',parent,commit,'--',path],cwd=root).splitlines(keepends=True) if line.startswith(b'-') and not line.startswith(b'---'))
(out/'removed_original.txt').write_bytes(removed)
adendo = removed.decode().split('[10/09/2026 02:36 BRT]',1)[1]
hook = adendo.split('```bash\n',1)[1].split('```',1)[0]
(out/'proposed_final_hook.sh').write_text(hook)
records=[]
def run(args,cwd,check=True):
    p=subprocess.run(args,cwd=cwd,capture_output=True,text=True)
    records.append({'args':args,'cwd':str(cwd),'rc':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    if check: assert p.returncode==0,records[-1]
    return p

cases=[]
base='BASE\nBloco alheio com ação e acentuação\n'
for name in ['valid_append','committed_removal','dirty_worktree_masks_removal','whole_file_deleted','removed_then_restored','lines_reordered']:
    repo=out/('fixture_'+name);repo.mkdir();remote=out/(name+'.git')
    run(['git','init','-q','--template='],repo)
    run(['git','config','user.name','XM Fixture'],repo)
    run(['git','config','user.email','fixture@example.invalid'],repo)
    hooks=repo/'.githooks';hooks.mkdir()
    run(['git','config','core.hooksPath',str(hooks)],repo)
    f=repo/path;f.parent.mkdir(parents=True);f.write_text(base)
    run(['git','add','--',path],repo);run(['git','commit','-qm','fixture base'],repo)
    run(['git','branch','-M','main'],repo)
    run(['git','init','--bare','-q','--template=',str(remote)],repo)
    run(['git','remote','add','origin',str(remote)],repo);run(['git','push','-q','origin','main'],repo)
    h=hooks/'pre-push';h.write_text(hook);h.chmod(0o755)
    if name=='valid_append':f.write_text(base+'NOVA LINHA\n')
    elif name=='whole_file_deleted':f.unlink()
    elif name=='lines_reordered':f.write_text('Bloco alheio com ação e acentuação\nBASE\n')
    else:f.write_text('BASE\n')
    run(['git','add','--',path],repo);run(['git','commit','-qm','fixture candidate'],repo)
    bad=run(['git','rev-parse','HEAD'],repo).stdout.strip()
    if name=='dirty_worktree_masks_removal':f.write_text(base)
    if name=='removed_then_restored':
        f.write_text(base+'NOVA LINHA\n');run(['git','add','--',path],repo);run(['git','commit','-qm','fixture restore'],repo)
    p=run(['git','push','origin','main'],repo,False)
    obj=run(['git','show','refs/heads/main:'+path],remote,False)
    cases.append({'name':name,'push_rc':p.returncode,'push_stderr':p.stderr,'remote_blob_exists':obj.returncode==0,'remote_blob':obj.stdout,'bad_commit':bad})
expected={'valid_append':0,'committed_removal':1,'dirty_worktree_masks_removal':0,'whole_file_deleted':0,'removed_then_restored':0,'lines_reordered':0}
for case in cases: assert (case['push_rc']==0)==(expected[case['name']]==0),case
res={'timestamp_brt':datetime.datetime.now().astimezone().isoformat(),'synthetic_only':True,'external_remotes_used':False,'hook_source_commit':parent,'hook_source_ref':'DS-Dell-20260910-006-ADENDO','hook_sha256':hashlib.sha256(hook.encode()).hexdigest(),'removal':{'commit':commit,'parent':parent,'path':path,'bytes':len(removed),'lines':len(removed.splitlines()),'sha256':hashlib.sha256(removed).hexdigest(),'refs':['DS-N-20260910-007','DS-Dell-20260910-006','DS-Dell-20260910-006-ADENDO'],'attribution_limit':'O commit comprova remoção; processo escritor não identificado pelo diff.'},'cases':cases,'commands':records}
(out/'probe_results.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'removal':res['removal'],'hook_sha256':res['hook_sha256'],'cases':cases},ensure_ascii=False,indent=2))

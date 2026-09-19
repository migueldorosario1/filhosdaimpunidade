"""Auditoria local dos commits da janela; nao usa rede nem executa runtime."""
import hashlib,json,subprocess,sys

def git(*args):
 return subprocess.check_output(['git']+list(args))

def audit(base,head):
 git('merge-base','--is-ancestor',base,head)
 commits=git('rev-list','--reverse','--first-parent',base+'..'+head).decode().splitlines()
 checks=[]
 for commit in commits:
  parent=git('rev-parse',commit+'^1').decode().strip()
  for path in git('diff','--name-only',parent,commit).decode().splitlines():
   if not path.startswith('cerebro/Foruns/ponte_laura_completa/'):continue
   if not ('/ledger/' in path or '/de_' in path or path.endswith('/telegram_dsc/RESPOSTAS.md')):continue
   old=git('show',parent+':'+path);new=git('show',commit+':'+path)
   d=git('diff','--unified=0',parent,commit,'--',path).decode().splitlines()
   minus=[x[1:] for x in d if x.startswith('-') and not x.startswith('---')]
   plus=[x[1:] for x in d if x.startswith('+') and not x.startswith('+++')]
   checks.append(dict(commit=commit,path=path,before_sha256=hashlib.sha256(old).hexdigest(),after_sha256=hashlib.sha256(new).hexdigest(),exact_prefix=new.startswith(old),prefix_ignoring_final_lf=new.startswith(old.rstrip(b'\n')),added=len(plus),removed=len(minus),nonblank_removed=sum(bool(x.strip()) for x in minus)))
 return dict(base=base,head=head,commits=len(commits),checks=checks,total_added=sum(c['added'] for c in checks),total_removed=sum(c['removed'] for c in checks),nonblank_removed=sum(c['nonblank_removed'] for c in checks))

if __name__=='__main__':
 result=audit(sys.argv[1],sys.argv[2]);print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(int(bool(result['nonblank_removed'])))

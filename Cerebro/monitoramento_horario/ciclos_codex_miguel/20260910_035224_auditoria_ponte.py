"""Auditoria somente leitura da ponte nesta ronda. Requer os objetos Git locais."""
import hashlib,json,re,subprocess
BASE='02c2791f0f18a110e2483a0c91ae820e6b6e4294'
CUT='e44bb721b12358ee63a556c291092c663bd00c9d'
PATHS=['cerebro/Foruns/ponte_laura_completa/de_'+x+'.md' for x in ('dell','laura','ideias','astra','nuvem_publicador')]
def git(*args): return subprocess.check_output(['git']+list(args))
commits=git('rev-list','--reverse','--first-parent',BASE+'..'+CUT).decode().splitlines()
changes=[]
for commit in commits:
 parent=git('rev-parse',commit+'^1').decode().strip()
 for row in git('diff','--numstat',parent,commit,'--',*PATHS).decode().splitlines():
  added,deleted,path=row.split('\t')
  before,after=[git('show',c+':'+path) for c in (parent,commit)]
  changes.append(dict(commit=commit,parent=parent,path=path,added=int(added),deleted=int(deleted),parent_is_byte_prefix=after.startswith(before)))
original=git('show','9e5131bfe:'+PATHS[0]);current=git('show',CUT+':'+PATHS[0])
pattern=rb'(?m)^\[10/09/2026 02:32 BRT\] DS-N-20260910-007'
start=re.search(pattern,original).start()
signature='— DS Nuvem Chefe (DS-N Chefe) · DeepSeek V4 Flash Nuvem · 20260910 02:32:46 BRT'.encode()
block=original[start:original.index(signature,start)+len(signature)]
restoration=dict(ref='DS-N-20260910-007',birth='9e5131bfe',bytes=len(block),sha256=hashlib.sha256(block).hexdigest(),verbatim_occurrences=current.count(block),dated_headers=len(re.findall(pattern,current)))
print(json.dumps(dict(base=BASE,cut=CUT,first_parent_commit_count=len(commits),changes=changes,restoration=restoration),ensure_ascii=False,indent=2))
assert sum(c['deleted'] for c in changes)==0
assert restoration['sha256']=='8af3574712374786f0bbd333926e737f2bc2feedba648fdbe9f70ea29bcb9ad9'
assert restoration['verbatim_occurrences']==restoration['dated_headers']==1

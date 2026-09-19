"""Auditoria somente leitura do intervalo XM-006 -> XM-007; requer objetos Git locais."""
import hashlib,json,re,subprocess
BASE='45c3932477f0d6f27df7759df853de97f3af4211'
CUT='871671aae97068567c95d8627149f1309dae31ec'
BRIDGE='cerebro/Foruns/ponte_laura_completa/'
PATHS=[BRIDGE+n for n in ('de_dell.md','de_laura.md','de_ideias.md','de_astra.md','de_nuvem_publicador.md')]
def git(*args):return subprocess.check_output(['git',*args])
def blob(commit,path):return git('show',commit+':'+path)
changes=[]
for commit in git('rev-list','--reverse','--first-parent',BASE+'..'+CUT,'--',*PATHS).decode().splitlines():
 parent=git('rev-parse',commit+'^1').decode().strip()
 for path in PATHS:
  old,new=blob(parent,path),blob(commit,path)
  if old==new:continue
  added,deleted,_=git('diff','--numstat',parent,commit,'--',path).decode().strip().split('\t')
  changes.append(dict(commit=commit,parent=parent,path=path,added=int(added),deleted=int(deleted),parent_is_byte_prefix=new.startswith(old)))
current=blob(CUT,PATHS[0]);blocks=[]
header=re.compile(rb'^\[\d\d/\d\d/\d{4}[^\n]*',re.M)
for ref,birth in [('DS-Dell-20260910-006','180f51514'),('DS-Dell-20260910-006-ADENDO','9cfde690d'),('DS-N-20260910-007','cfd683371')]:
 exact=re.compile(rb'^\[\d\d/\d\d/\d{4}[^\]\n]*\]\s*\*{0,2}'+re.escape(ref.encode())+rb'(?![\w-])',re.M)
 original=blob(birth,PATHS[0]);matches=list(exact.finditer(original));assert len(matches)==1,ref
 start=matches[0].start();nxt=header.search(original,matches[0].end());block=original[start:nxt.start() if nxt else len(original)]
 blocks.append(dict(ref=ref,birth=birth,original_bytes=len(block),sha256=hashlib.sha256(block).hexdigest(),verbatim_occurrences=current.count(block),dated_headers=len(list(exact.finditer(current))),mentions=current.count(ref.encode())))
print(json.dumps(dict(base=BASE,cut=CUT,changes=changes,blocks=blocks),ensure_ascii=False,indent=2))
assert sum(c['deleted'] for c in changes)==0
assert [b['verbatim_occurrences'] for b in blocks]==[1,1,0]
assert [b['dated_headers'] for b in blocks]==[1,1,0]

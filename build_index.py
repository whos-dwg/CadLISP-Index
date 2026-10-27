from pathlib import Path
import argparse, json, re

root=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description='Link already published tool repositories in this local catalog')
parser.add_argument('--owner',required=True)
parser.add_argument('--published',nargs='+',required=True)
args=parser.parse_args()
if not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',args.owner):
    parser.error('Invalid GitHub owner')
records=json.loads((root/'metadata/tools.json').read_text('utf-8'))
known={r['repository'] for r in records}
if set(args.published)-known:
    parser.error('Unknown repository: '+', '.join(sorted(set(args.published)-known)))
text=(root/'README.md').read_text('utf-8')
for r in records:
    name=r['repository']
    text=re.sub(r'\[`'+re.escape(name)+r'`\]\(https://github\.com/[^/]+/'+re.escape(name)+r'\)', '`'+name+'`',text)
    if name in args.published:
        text=text.replace('`'+name+'`','[`'+name+'`](https://github.com/'+args.owner+'/'+name+')')
(root/'README.md').write_text(text,encoding='utf-8',newline='\n')
print('Updated local catalog links for',len(args.published),'published repositories')

"""Static release checks: broken links, assets, metadata and reciprocal translations."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,xml.etree.ElementTree as ET,subprocess
ROOT=Path(__file__).resolve().parents[1]
BASE='https://evakim-website.pages.dev'
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.tags=[];self.ids=set();self.schemas=[];self.schema=None;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);self.tags.append((tag,a))
  if 'id' in a:self.ids.add(a['id'])
  if tag=='script' and a.get('type')=='application/ld+json':self.schema=''
 def handle_data(self,data):
  if self.schema is not None:self.schema+=data
 def handle_endtag(self,tag):
  if tag=='script' and self.schema is not None:self.schemas.append(json.loads(self.schema));self.schema=None
 def canonical(self):return [a['href'] for t,a in self.tags if t=='link' and a.get('rel')=='canonical']
 def alts(self):return {a['hreflang']:a['href'] for t,a in self.tags if t=='link' and 'hreflang' in a}
pages={p:Page(p.read_text()) for p in ROOT.rglob('*.html') if '.git' not in p.parts and not p.name.startswith('google')}
errors=[];nlinks=0
for p,page in pages.items():
 if len(page.canonical())!=1:errors.append(f'{p}: canonical count')
 for tag,a in page.tags:
  if tag=='img' and not a.get('alt'):errors.append(f'{p}: image alt missing')
  url=a.get('href') if tag in ('a','link') else a.get('src') if tag in ('img','script') else None
  if not url:continue
  u=urlsplit(url)
  if u.netloc and u.netloc!='evakim-website.pages.dev':continue
  if u.scheme and u.scheme not in ('http','https'):continue
  nlinks+=1
  target=ROOT/unquote(u.path).lstrip('/') if u.path.startswith('/') else p.parent/unquote(u.path)
  if not u.path:target=p
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{p.relative_to(ROOT)}: missing {url}')
  if u.fragment and target in pages and u.fragment not in pages[target].ids:errors.append(f'{p}: missing anchor {url}')
  if tag=='link' and a.get('hreflang') and target in pages:
   if page.canonical()[0] not in pages[target].alts().values():errors.append(f'{p}: nonreciprocal {url}')
 urls=[a for t,a in page.tags if t=='a' and a.get('href','').startswith('https://www.youtube.com/')]
 if not urls:errors.append(f'{p}: no YouTube path')
for loc in ET.parse(ROOT/'sitemap.xml').getroot().iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
 p=ROOT/urlsplit(loc.text).path.lstrip('/')/'index.html'
 if not p.exists():errors.append(f'sitemap missing {loc.text}')
assert '697aa533d25c820f5c7a7bd5d9d5987590f553c6' in (ROOT/'index.html').read_text()
assert (ROOT/'google095b64c31caff778.html').read_text().strip()=='google-site-verification: google095b64c31caff778.html'
assert (ROOT/'robots.txt').read_text().find('Disallow: /\n')==-1
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} HTML pages, {nlinks} internal references, JSON-LD, sitemap, reciprocal hreflang, YouTube paths, verification tokens.')

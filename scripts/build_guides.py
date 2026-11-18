"""Build static guides from reviewed content; never rewrites legacy articles."""
import json
from pathlib import Path
from html import escape as e
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://evakim-website.pages.dev'
CHANNEL = 'https://www.youtube.com/@eva7kim'
DATA = json.loads((ROOT / 'content/guides.json').read_text())
LABELS = {
 'ko': ['베트남 생활 가이드', '시장부터 식탁까지, 처음 만나는 베트남을 이해하는 실용 안내.', '핵심 먼저 보기', '이 글의 순서', '바로 쓰는 베트남어', '한국어', 'Tiếng Việt', '함께 읽기', '에바의 시선으로 영상도 만나세요', '채널에서 관련 주제 검색', 'EvaKim 채널 방문', '아래 링크는 특정 영상이 아닌 채널 내 검색입니다. 검색 결과에 따라 관련 영상이 없을 수 있습니다.', '근거와 확인 범위', '작성·검토: EvaKim 생각공장', '본문 바로가기', '글 읽기', '기존 문화 이야기', '업데이트'],
 'vi': ['Cẩm nang đời sống Việt Nam', 'Từ chợ đến bàn ăn: hướng dẫn thực tế để hiểu cuộc sống Việt Nam.', 'Điểm chính', 'Trong bài này', 'Câu tiếng Việt dùng ngay', '한국어', 'Tiếng Việt', 'Đọc tiếp', 'Khám phá thêm qua góc nhìn của Eva', 'Tìm chủ đề liên quan trong kênh', 'Ghé kênh EvaKim', 'Liên kết mở tìm kiếm trong kênh, không phải video cụ thể. Có thể chưa có video phù hợp.', 'Nguồn và phạm vi', 'Biên soạn: EvaKim Think Factory', 'Đến nội dung', 'Đọc bài', 'Câu chuyện văn hóa bằng tiếng Hàn', 'Cập nhật'],
 'en': ['Vietnam everyday guides', 'From market to table: practical guides to everyday Vietnam.', 'At a glance', 'In this guide', 'Vietnamese phrases to use', 'English', 'Tiếng Việt', 'Read next', 'See more through Eva’s eyes', 'Search this topic in the channel', 'Visit EvaKim', 'This opens a channel search, not a specific video. A matching video may not yet be available.', 'Sources and scope', 'Prepared by EvaKim Think Factory', 'Skip to content', 'Read guide', 'Earlier stories in Korean', 'Updated']
}

def path(lang, slug=''):
 return ('/blog/' if lang=='ko' else f'/{lang}/blog/') + (slug+'/' if slug else '')

def links(lang, slug=''):
 return ''.join(f'<a href="{path(l,slug)}" hreflang="{l}" lang="{l}"'+(' aria-current="page"' if l==lang else '')+f'>{label}</a>' for l,label in [('ko','한국어'),('vi','Tiếng Việt'),('en','English')])

def head(lang,title,desc,slug='',kind='article'):
 url=BASE+path(lang,slug)
 alts=''.join(f'<link rel="alternate" hreflang="{l}" href="{BASE+path(l,slug)}">' for l in LABELS)
 return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} | EvaKim 생각공장</title><meta name="description" content="{e(desc)}"><meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="{url}">{alts}<link rel="alternate" hreflang="x-default" href="{BASE+path('ko',slug)}"><link rel="stylesheet" href="/assets/editorial.css"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><meta property="og:type" content="{kind}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/assets/eva-profile.webp"><meta property="og:image:alt" content="EvaKim creator Eva"><meta name="twitter:card" content="summary"></head><body><a class="skip" href="#content">{LABELS[lang][14]}</a><header><div class="site-nav"><a href="/{lang}/"><img src="/assets/thinkfactory-logo.svg" width="180" height="49" alt="Eva &amp; Kim 생각공장"></a><nav class="languages" aria-label="Language">{links(lang,slug)}</nav></div></header>'''

def footer(lang):
 return f'<footer><div class="site-nav"><span>© EvaKim 생각공장 · Korea × Vietnam</span><a href="{path(lang)}">{LABELS[lang][0]}</a><a href="{CHANNEL}">YouTube @eva7kim</a></div></footer></body></html>'

def watch(lang,topic):
 t=LABELS[lang]
 return f'<aside class="watch"><h2>{t[8]}</h2><a class="button" data-youtube-topic="{e(topic)}" href="{CHANNEL}/search?query={quote(topic)}">{t[9]} →</a><a href="{CHANNEL}">{t[10]} ↗</a><p class="meta" style="color:#d8d4c8">{t[11]}</p></aside>'

def card(a,lang):
 c=a[lang];return f'<article class="story-card"><div class="eyebrow">{e(c["category"])}</div><h2><a href="{path(lang,a["slug"])}">{e(c["title"])}</a></h2><p>{e(c["description"])}</p><a href="{path(lang,a["slug"])}">{LABELS[lang][15]} →</a></article>'

def write(url,html):
 p=ROOT/url.lstrip('/')/'index.html';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(html+'\n')

for lang,t in LABELS.items():
 for a in DATA:
  c=a[lang];slug=a['slug'];url=BASE+path(lang,slug)
  schema={'@context':'https://schema.org','@type':'BlogPosting','headline':c['title'],'description':c['description'],'inLanguage':lang,'mainEntityOfPage':url,'datePublished':'2026-11-18','dateModified':'2026-11-18','author':{'@type':'Organization','name':'EvaKim 생각공장','url':BASE},'publisher':{'@type':'Organization','name':'EvaKim 생각공장'},'image':BASE+'/assets/eva-profile.webp'}
  crumb={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':t[0],'item':BASE+path(lang)},{'@type':'ListItem','position':2,'name':c['title'],'item':url}]}
  h=head(lang,c['title'],c['description'],slug)
  h=h.replace('</head>',f'<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(crumb,ensure_ascii=False)}</script></head>')
  h+=f'<main class="reading" id="content"><nav class="crumbs"><a href="{path(lang)}">{t[0]}</a> / {e(c["category"])}</nav><article><div class="eyebrow">{e(c["category"])}</div><h1>{e(c["title"])}</h1><p class="intro">{e(c["intro"])}</p><div class="author"><img src="/assets/eva-profile.webp" width="56" height="56" alt="Eva" loading="lazy"><div><p>{t[13]}</p><p class="meta">{t[17]} <time datetime="2026-11-18">2026-11-18</time></p></div></div><aside class="summary"><strong>{t[2]}</strong>{e(c["summary"])}</aside><nav class="toc" aria-label="{t[3]}"><strong>{t[3]}</strong>'
  h+=''.join(f'<a href="#section-{i}">{i}. {e(s[0])}</a>' for i,s in enumerate(c['sections'],1))+f'<a href="#phrases">{t[4]}</a></nav>'
  h+=''.join(f'<section id="section-{i}"><h2>{e(s[0])}</h2><p>{e(s[1])}</p></section>' for i,s in enumerate(c['sections'],1))
  h+=f'<section id="phrases"><h2>{t[4]}</h2><div class="table-scroll"><table><thead><tr><th scope="col">{t[5]}</th><th scope="col">{t[6]}</th></tr></thead><tbody>'
  h+=''.join(f'<tr><td lang="{"en" if lang=="en" else "ko"}">{e(x)}</td><td lang="vi">{e(y)}</td></tr>' for x,y in c['phrases'])+'</tbody></table></div></section>'
  h+=watch(lang,a['topic'])+f'<aside class="related"><h2>{t[7]}</h2><ul>'
  h+=''.join(f'<li><a href="{path(lang,b["slug"])}">{e(b[lang]["title"])}</a></li>' for b in DATA if b!=a)+'</ul></aside>'
  h+=f'<section class="sources"><h2>{t[12]}</h2><p>{e(c["note"])}</p><ul>'
  h+=''.join(f'<li><a href="{e(u)}">{e(n)}</a></li>' for n,u in a['sources'])+'</ul></section></article></main>'+footer(lang)
  write(path(lang,slug),h)
 h=head(lang,t[0],t[1],kind='website')+f'<main class="reading collection" id="content"><div class="eyebrow">EVA KIM JOURNAL</div><h1>{t[0]}</h1><p class="intro">{t[1]}</p><div class="story-grid">'+''.join(card(a,lang) for a in DATA)+'</div>'
 h+=f'<section><h2>{t[16]}</h2><div class="story-grid"><article class="story-card"><h3><a href="/blog/vietnam-motorbike-market/" lang="ko">베트남 시장에서는 왜 오토바이에서 내리지 않을까?</a></h3></article><article class="story-card"><h3><a href="/blog/vietnam-food-breakdown/" lang="ko">베트남 음식 한 상을 분해하면 무엇이 보일까?</a></h3></article></div></section>'+watch(lang,'베트남')+'</main>'+footer(lang)
 write(path(lang),h)
print('Built 9 guides and 3 language indexes.')

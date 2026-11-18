# EvaKim growth project / 성장 운영 기준 / Kế hoạch phát triển

Primary outcome: Korean organic-search visitors → useful Vietnam reading → EvaKim YouTube viewers.
최우선: 한국인 검색 방문자가 글에서 도움을 얻고 유튜브로 이동한다.
Mục tiêu: người Hàn đến từ tìm kiếm, nhận thông tin hữu ích rồi xem EvaKim trên YouTube.

## Protected behavior
- Keep the four existing daily automations unchanged (08:00, 11:00, 15:00, 21:00 Asia/Ho_Chi_Minh).
- Preserve existing URLs, articles, language switching, Google verification file and Naver verification token.
- No invented prices, weights, quotations, restaurant visits or performance results.
- Keep observations explicitly scoped; cite external factual sources in the relevant guide.
- Use user-supplied photos only for creator identity, never as evidence of an unverified location.
- Do not replace the channel with an old handle: https://www.youtube.com/@eva7kim is the supplied target.

## Initial release — 2026-11-18
- Preserve the two existing Korean culture articles.
- Add three practical guides in Korean, Vietnamese and English (9 article URLs).
- Add localized blog indexes, language alternates, article metadata, breadcrumbs and sitemap entries.
- Add topic-specific channel search links, clearly labelled as searches, and related reading on every article.
- Select 24950.webp as homepage creator image and 24955.webp as portrait. Other supplied photos and screenshots are deliberately not published. No gallery.
- Keep original image files unchanged; use explicit dimensions, CSS layout and lazy loading for secondary images.
- Editorial data: content/guides.json. Build: python3 scripts/build_guides.py. Validate: python3 scripts/check_site.py.
- The generator only owns the 9 new guides and 3 blog indexes; legacy articles and home pages remain separately editable.

## Next 30 days / 다음 30일 / 30 ngày tới
1. Verify the specific published video URL that matches each topic. Replace a search link only after title, content and channel ownership match; never present an unpublished food-breakdown project as a completed video.
2. Check new canonical URLs in Google Search Console and Naver Search Advisor when authorized access is available. Technical validity is not evidence of indexing.
3. Use existing daily content work to deepen one useful reader question at a time: market units, café menus, meal ingredients. Prefer firsthand photos or receipts for price-based articles.
4. Establish a baseline from actual analytics: Korean organic sessions, impressions, clicks, query, landing page and YouTube outbound clicks. Missing data is unknown, not zero.

## Days 31–60 / 31–60일 / Ngày 31–60
- Update titles and introductions from actual search queries, not speculative keyword volume.
- Expand guides that receive relevant impressions; add a next article and a verified matching video.
- Review mobile reading and language navigation after each template change.
- Keep a record of source, checked date and regional scope for changing claims.

## Days 61–90 / 61–90일 / Ngày 61–90
- Compare four-week periods only when enough data exists; report sample size and actual dates.
- Improve weak reader-to-video paths using measured outbound clicks. Do not equate a click with a view, subscription or revenue.
- Merge overlapping drafts before publishing; preserve published URLs or provide appropriate redirects if consolidation is necessary.
- Decide which content clusters deserve expansion from observed search demand and channel relevance.

## Measurement access still needed
Search Console / Naver indexing, search traffic and YouTube conversion have not been measured in this release. No analytics account or tracker is invented. A future privacy-aware measurement change should be documented separately.

## Verification sources
- https://developers.google.com/search/docs/specialty/international/localized-versions
- https://vietnam.travel/things-to-do/5-fantastic-vietnamese-coffees/
- https://www.vietnamairlines.com/go/en/plan-book/travel/travel-guide/bun-dau-mam-tom

## Deployment
Existing GitHub main is connected to Cloudflare Pages. Verify the new commit's Cloudflare check and compare public response bytes to the release files. A successful push alone is not a completed deployment. Do not force-push over another daily task's edits.

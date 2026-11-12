import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _en_shared import shared

LANG = 'en'; CC = 'AU'
TAGS = ['#AusBiz', '#SmallBusinessAustralia', '#PRtips', '#MediaRelations', '#AussieStartups']
def times(pillar):
    return {'linkedin': '08:00 AEDT', 'instagram_facebook': '12:00 AEDT' if pillar in ('EDU', 'PROMO') else '19:30 AEDT'}

loc = dict(cc='AU', uk=True, li_market='Australian',
  ex_head='Brisbane Logistics Start-up Opens 4 Regional Queensland Hubs, Cuts Delivery to One Day',
  ex_quote='"Next-day delivery shouldn\'t stop at the city limits. Regional Queensland is where we start."',
  subj_good=['"Data: 3 in 5 Melbourne cafés lifted prices this quarter"', '"Spokesperson: CFO on 2027 freight costs"', '"Embargo 24 Nov, 6am AEDT: launch of …"'],
  anchor_bad='cheap SEO services Sydney', pov_sub='…along with a few hundred other emails today',
  bf_hook='Black Friday can discount plenty. Credibility isn\'t one of them.')
S = shared(loc)
SRC_PRICE = 'vritimes.com/au/service/pricing'

POSTS = [S['W1Mon'], S['W1Wed'], S['W1Fri'], S['W2Mon'],
# 5 ── W2 Wed FUN single
dict(slot='W2Wed', pillar='FUN', format='single', slug='2-7-million-small-businesses',
 title='Australia has 2.74 million small businesses', cta='Tag a small business owner whose story deserves coverage', src=['AU1'], tags=['#SmallBusinessAustralia', '#FunFact'],
 slides=[dict(t='single_stat', tag='fun fact', pre='australia has', big='2.74M', label='actively trading *small businesses*',
   body='That\'s **97%** of all businesses (30 June 2026). Plenty of stories. Not much airtime.', sub='got news? write the release', src='ASBFEO (2026)')],
 cap=dict(
  hook='Australia has 2,741,087 small businesses. Most of their news never gets a run. 🤔',
  lines=['From the Australian Small Business and Family Enterprise Ombudsman:', '• 2,741,087 actively trading small businesses (30 June 2026)', '• Up 3.2% on a year earlier', '• 97% of all actively trading businesses', '', 'A new site, a first export deal, 20 new hires: genuinely newsworthy.', 'Usually just not written up in a way a newsroom can use.'],
  li_hook='There were 2,741,087 actively trading small businesses in Australia at 30 June 2026, 97% of all businesses.\nTheir share of business coverage is a fraction of that.',
  li_body=['ASBFEO\'s figures are mostly used in policy debates. We see a communications gap: millions of businesses with milestones that never reach a journalist.', 'Not because they lack news value, but because they aren\'t packaged as news. A second location, a first export contract or a hiring round is a solid local story when it comes with clear numbers and a spokesperson who will take a call.'],
  li_close='If you run a small business: what from this year deserved a story?',
  fb='Fun fact: Australia has more than 2.7 million small businesses. If yours is one of them, your news deserves a run too.')),
S['W2Fri'], S['W3Mon'],
# 8 ── W3 Wed VIRAL reel: bye bye "hope a journalist sees it"
dict(slot='W3Wed', pillar='VIRAL', format='reel', slug='bye-bye-hope-a-journalist-sees-it',
 title='Say bye bye to "hope a journalist sees it"', cta='Comment which "hope" you\'re retiring', src=['MR'], tags=['#PRlife', '#MarketingAustralia'],
 slides=[dict(t='cover', tag='we\'ve all done it', title='say bye bye to *"hope a journalist sees it"*')],
 reel=dict(frames=[
   dict(top='bye bye 👋', text='*"hope a journalist sees it"*', dur=2.5, theme='navy'),
   dict(text='"hope they find our *LinkedIn post*"', sub='→ send them the news directly', dur=3.0, theme='pale'),
   dict(text='"hope they open the *attachment*"', sub='→ text in the email body', dur=3.0, theme='blue'),
   dict(text='"hope a *600-word* pitch shows we\'re serious"', sub='→ 69% prefer under 200 words', src='Muck Rack, State of Journalism 2025', dur=3.5, theme='navy'),
   dict(text='"hope they reply if I *chase daily*"', sub='→ one follow-up, 3–7 days later', src='Muck Rack, State of Journalism 2025', dur=3.5, theme='pale'),
   dict(text='swap hope for *a process*', sub='Raise It With Press Release', dur=3.0, theme='blue'),
  ],
  vo=['Say bye bye to hope a journalist sees it.', 'Hope they find our LinkedIn post? Send the news directly.', 'Hope they open the attachment? Put the text in the email.', 'Hope a long pitch looks serious? Sixty-nine percent prefer under two hundred words.', 'Hope they reply if you chase daily? One follow-up, three to seven days later.', 'Swap hope for a process.'],
  broll=['Team member waving goodbye to sticky notes labelled "hope" (props)', 'Mock inbox with a long unread pitch', 'Calendar reminder "follow up in 5 days" (mock)'],
  audio='Trending "bye bye" sound or upbeat beat from the platform\'s licensed library'),
 cap=dict(
  hook='Say bye bye to "hope a journalist sees it" 👋',
  lines=['"Hope they find our LinkedIn post" → send the news directly', '"Hope they open the attachment" → text in the email body', '"Hope a long pitch looks serious" → 69% prefer under 200 words', '"Hope they reply if I chase daily" → one follow-up, 3–7 days later', '', 'Hope isn\'t a media strategy. A process is.'],
  ig_cta='Send this to your marketing team. Link in bio.',
  li_hook='Most small-business media strategies quietly rely on hope.\nFour hopes worth replacing with a process.',
  li_body=['Muck Rack\'s State of Journalism 2025 gives a useful baseline: 69% of journalists prefer pitches under 200 words, 50% say one follow-up is ideal, and 51% want it 3–7 days after the pitch.'],
  li_points=['Instead of hoping a journalist finds your social post, send the news to the right person.', 'Instead of hoping they open the attachment, put the release text in the email body.', 'Instead of hoping length signals seriousness, keep the pitch under 200 words.', 'Instead of chasing daily, follow up once, 3–7 days later.'],
  li_close='Which "hope" is still in your team\'s media plan?',
  fb='Hope isn\'t a media strategy 👋 Here are four swaps that actually work.')),
# 9 ── W3 Fri EDU carousel: embargoes
dict(slot='W3Fri', pillar='EDU', format='carousel', slug='press-release-embargoes-explained',
 title='Press release embargoes, explained', cta='Save before your next launch', src=['MR'], tags=['#MediaRelations', '#PRtips'],
 slides=[
  dict(t='cover', tag='media relations', title='embargoes: *how to use them* without burning bridges', icons=['clock', 'mail', 'shield']),
  dict(t='point', n='01', title='what an embargo *is*', body='A request that journalists don\'t publish before a set date and time. It gives them time to prepare a better story. It is an **agreement**, not a legal contract.'),
  dict(t='point', n='02', title='when it\'s *worth it*', body='Complex news that needs time: research findings, funding rounds, product launches with demos. If the news fits in one sentence, you probably don\'t need one.'),
  dict(t='point', n='03', title='ask *before* you send', body='Offer the news under embargo and wait for a yes. Sending embargoed material unasked and hoping it\'s honoured is how leaks happen.'),
  dict(t='point', n='04', title='timezone-proof *timing*', body='Write the full time and zone, and check it against the journalist\'s timezone.', ex='"EMBARGOED UNTIL 6:00am AEDT, Tuesday 24 November 2026"'),
  dict(t='point', n='05', title='respect their *workload*', body='Journalists are stretched: 62% took on more responsibilities this year. Give enough lead time (two to five working days for most news) and everything they need in one go.', src='Muck Rack, State of Journalism 2025'),
  dict(t='list', title='embargo checklist', items=['News complex enough to need prep time', 'Journalist agreed before receiving details', 'Date, time AND timezone in the subject line', 'Assets, data and spokesperson ready on day one', 'A plan if it breaks early']),
  dict(t='cta', title='embargo = *trust*. treat it that way.', items=['Save this checklist', 'Send it to whoever runs your launches'], sources=['Muck Rack, State of Journalism 2025']),
 ],
 cap=dict(
  hook='Embargoes can make your launch, or burn a media relationship. Here\'s how to use them properly. ⏰',
  lines=['01 It\'s an agreement, not a contract', '02 Use it for complex news that needs prep time', '03 Ask before you send the details', '04 Full date, time and timezone (AEDT!)', '05 Respect their workload: 62% of journalists took on more this year', '', 'Checklist on slide 7.'],
  li_hook='An embargo is one of the few tools that gives journalists more time to do a better story.\nUsed badly, it is also the fastest way to lose their trust.',
  li_body=['Newsrooms are stretched. Muck Rack\'s State of Journalism 2025 found 62% of journalists took on more responsibilities this year. An embargo helps when it gives them time to prepare; it hurts when it adds admin or confusion.', 'How we recommend using one:'],
  li_points=['Reserve it for news that needs preparation: research, funding, launches with demos.', 'Ask first. Share details only after the journalist agrees to the embargo.', 'State the date, time and timezone in full, e.g. 6:00am AEDT, Tuesday 24 November 2026.', 'Give reasonable lead time and send every asset in one package.', 'Have a plan if it breaks early: publish your own version immediately.'],
  li_close='Have you had an embargo broken? What did you change afterwards?',
  fb='Planning a launch? Here\'s how to use a press release embargo without upsetting journalists 👇')),
# 10 ── W4 Mon EDU carousel: PR calendar 2027 AU
dict(slot='W4Mon', pillar='EDU', format='carousel', slug='pr-calendar-2027-australia',
 title='PR calendar 2027 for Australian businesses', cta='Save for your 2027 planning', src=['AU1'], tags=['#PRcalendar', '#Planning2027'],
 src_note='Federal Budget date for 2027 is set by Treasury; check the official announcement. Other dates are fixed or follow standard rules.',
 slides=[
  dict(t='cover', tag='planning 2027', title='your 2027 PR calendar, *sorted early*', sub='save it for the planning meeting', icons=['cal', 'chart', 'mega']),
  dict(t='point', icon='cal', title='why a calendar beats *reacting*', body='Reactive releases almost always arrive late. A calendar means data, photos and spokespeople are ready **before** journalists go looking.'),
  dict(t='list', title='Q1 · jan–mar', items=['Mid-Jan return to work: newsrooms hungry for fresh news', 'Back-to-school & new-year consumer angles', 'Half-year results (Feb): publish your milestones']),
  dict(t='list', title='Q2 · apr–jun', items=['Federal Budget (usually May): react with small-business commentary', 'EOFY on 30 June: tax-time and planning angles', 'Mid-year customer data']),
  dict(t='list', title='Q3 · jul–sep', items=['New financial year from 1 July: plans, hires, pricing', 'Partnership & funding announcements', 'Prep for spring events']),
  dict(t='list', title='Q4 · oct–dec', items=['Black Friday (26 Nov 2027) & Cyber Monday', 'Christmas shutdown from mid-Dec: publish before', 'Year in review & 2028 outlook']),
  dict(t='point', title='the *T-14 to T+3* rule', body='A working timeline for every moment:', exlab='timeline', ex='T-14 research & data · T-7 final release + photos · T-3 pitch journalists · Day 0 publish & share · T+3 coverage recap'),
  dict(t='stat', big='97%', label='of actively trading businesses are small businesses', body='They all compete for the same news days around Budget, EOFY and Christmas. Preparation decides who gets a run.', src='ASBFEO (2026)'),
  dict(t='cta', title='plan 2027 PR *now*', items=['Save this calendar', 'Mark 3 moments for your business', 'Send it to your marketing team'], sources=['ASBFEO (2026)']),
 ],
 cap=dict(
  hook='Your 2027 PR calendar can be built today. 🗓️',
  lines=['Q1: back-to-work news appetite, half-year results', 'Q2: Federal Budget, EOFY (30 June)', 'Q3: new financial year, partnerships & funding', 'Q4: Black Friday, Cyber Monday, Christmas shutdown', '', 'Workflow: T-14 research → T-7 final release → T-3 pitch → Day 0 → T+3 recap.'],
  li_hook='The businesses that get coverage around big moments prepared their releases weeks earlier.\nA 2027 PR calendar framework for Australia.',
  li_body=['Small businesses make up 97% of actively trading businesses in Australia (ASBFEO, 2026), and they all compete for the same news days. Preparation, not volume, decides who gets covered.', 'A quarterly framework to adapt:'],
  li_points=['Q1: the mid-January return to work, when newsrooms are hungry for news, plus half-year results.', 'Q2: Federal Budget commentary (usually May) and EOFY angles.', 'Q3: new financial year plans, hires and pricing, plus partnership and funding news.', 'Q4: Black Friday and Cyber Monday, then publish before the Christmas shutdown.', 'For every moment: T-14 research, T-7 final release, T-3 pitch, Day 0 publish, T+3 recap.'],
  li_close='Which moment matters most for your business next year?',
  fb='Started on 2027 yet? Here\'s a quarter-by-quarter PR calendar for Australian businesses 👇')),
# 11 ── W4 Wed FUN reel: news avoidance
dict(slot='W4Wed', pillar='FUN', format='reel', slug='australians-avoiding-the-news',
 title='69% of Australians avoid the news sometimes or often', cta='Share with your comms team', src=['DNRAU', 'DNR'], tags=['#MediaAustralia', '#FunFact'],
 slides=[dict(t='cover', tag='fun fact', title='*69%* of australians avoid the news')],
 reel=dict(frames=[
   dict(top='fun fact', text='*69%* of australians avoid the news', sub='sometimes or often', src='University of Canberra, Digital News Report: Australia 2025', dur=3.5, theme='blue'),
   dict(text='trust in news: *43%*', sub='up 3 points on last year', src='Reuters Institute, Digital News Report 2025', dur=3.0, theme='pale'),
   dict(text='social media has overtaken going *direct* to news sites', src='University of Canberra, Digital News Report: Australia 2025', dur=3.5, theme='navy'),
   dict(text='so: make your news *easy to understand* and *easy to share*', dur=4.0, theme='blue'),
   dict(text='plain words. real numbers. *one clear point*.', dur=3.0, theme='pale'),
   dict(text='news people *don\'t* skip', sub='Raise It With Press Release', dur=3.0, theme='navy'),
  ],
  vo=['Sixty-nine percent of Australians avoid the news, sometimes or often.', 'Trust in news sits at forty-three percent.', 'Social media has overtaken going direct to news sites.', 'So make your news easy to understand and easy to share.', 'Plain words, real numbers, one clear point.', 'News people don\'t skip.'],
  broll=['Thumb scrolling past headlines (mock UI)', 'Animated 69% / 43% counters (from text cards)', 'Team member reading a one-paragraph release aloud (internal talent)'],
  audio='Calm, understated beat from the platform\'s licensed library'),
 cap=dict(
  hook='69% of Australians avoid the news sometimes or often. Here\'s what that means for your announcement.',
  lines=['Digital News Report: Australia 2025:', '• News avoidance: 69%', '• Trust in news: 43% (+3)', '• Social media has overtaken going direct to news sites', '', 'If people skim or skip, your news has to be clear, specific and easy to share.'],
  li_hook='News avoidance in Australia is 69%, according to the Digital News Report: Australia 2025.\nIf your audience is skimming, your announcement needs to work harder.',
  li_body=['The same research found social media has overtaken going directly to news websites, while the Reuters Institute puts trust in news at 43%, up three points.', 'For business announcements, that suggests a few practical rules:'],
  li_points=['Lead with one clear point in plain language.', 'Use real numbers instead of adjectives.', 'Make it easy to share: a clean web page, a strong image, a short summary.', 'Reuse earned coverage on your own social channels, where people now find their news.'],
  li_close='How are you adapting announcements for audiences who skim?',
  fb='Fun fact: 69% of Australians avoid the news at least sometimes. Here\'s how to make your announcement worth stopping for.')),
# 12 ── W4 Fri PROMO offer-led
dict(slot='W4Fri', pillar='PROMO', format='single', slug='publish-before-christmas-shutdown',
 title='Get your news out before the Christmas shutdown', cta='Check current pricing via the link', src=['PRICE'], tags=['#AusBiz', '#SmallBusinessAustralia'],
 slides=[dict(t='promo', tag='before the shutdown', title='year-end news? *get it out* before the shutdown',
   items=['Published before newsrooms wind down for Christmas', 'Backlink to your launch or product page', 'Distribution report to review the campaign'],
   price='starts from — see link', src=SRC_PRICE, ribbon=True)],
 cap=dict(
  hook='The Christmas shutdown is a week away. Is your news out yet?',
  lines=['Get in before newsrooms wind down:', '✓ Published before the shutdown', '✓ Backlink to your launch/product page', '✓ Distribution report to review results', '', 'Current plans & pricing: link in bio.'],
  ig_cta='Check current plans & pricing via the link in bio.',
  li_hook='Announcements that land during the Christmas shutdown tend to disappear.\nIf it matters, publish before it.',
  li_body=['From mid-December, many Australian newsrooms run skeleton crews until mid-January. Releases that land before the wind-down have a better chance of being picked up and shared.', 'What you can do this week with VRITIMES:'],
  li_points=['Distribute your year-end results, holiday trading news or a January announcement with guaranteed media placement (count depends on plan).', 'Point the backlink to your launch or product page.', 'Use the distribution report to review results and plan Q1.'],
  li_close='Current plans and pricing are on our official page.',
  fb='Don\'t let your news land after everyone\'s gone to the beach. See VRITIMES plans here.')),
]

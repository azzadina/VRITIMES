import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _en_shared import shared

LANG = 'en'; CC = 'MY'
TAGS = ['#PressReleaseMalaysia', '#MalaysiaSME', '#PRtips', '#MSMEMalaysia', '#KLbusiness']
def times(pillar):
    return {'linkedin': '08:30 MYT', 'instagram_facebook': '12:30 MYT' if pillar in ('EDU', 'PROMO') else '20:30 MYT'}

loc = dict(cc='MY', uk=True, li_market='Malaysian',
  ex_head='Penang Logistics Start-up Opens 5 Northern Hubs, Cuts Delivery Times to One Day',
  ex_quote='"Next-day delivery shouldn\'t be a Klang Valley privilege. The northern region is just the start."',
  subj_good=['"Data: 3 in 5 Klang Valley F&B SMEs raised prices in Q4"', '"Spokesperson: CFO on 2027 logistics costs"', '"Embargo 24/11, 9am: launch of …"'],
  anchor_bad='cheap SEO services KL', pov_sub='…along with hundreds of other emails today',
  bf_hook='Black Friday can discount anything. Your credibility isn\'t one of them. 😉')
S = shared(loc)
SRC_PRICE = 'vritimes.com/my/service/pricing'

POSTS = [S['W1Mon'], S['W1Wed'], S['W1Fri'], S['W2Mon'],
# 5 ── W2 Wed FUN single
dict(slot='W2Wed', pillar='FUN', format='single', slug='msmes-39-7-percent-of-gdp',
 title='MSMEs made up 39.7% of Malaysia\'s GDP in 2025', cta='Tag an SME owner whose story deserves coverage', src=['MY1', 'MY2'], tags=['#MalaysiaSME', '#FunFact'],
 slides=[dict(t='single_stat', tag='fun fact', pre='in 2025, MSMEs made up', big='39.7%', label='of malaysia\'s *GDP*',
   body='They are **96.1%** of all business establishments. The stories are everywhere. The coverage isn\'t.', sub='got a story? write the release', src='DOSM, MSMEs Performance 2025; OECD (2026)')],
 cap=dict(
  hook='MSMEs made up 39.7% of Malaysia\'s GDP in 2025. How many made the news? 🤔',
  lines=['From DOSM\'s MSMEs Performance 2025:', '• MSME GDP grew 5.7%', '• MSMEs = 39.7% of national GDP', '• And 96.1% of all establishments (OECD, citing DOSM 2024)', '', 'New outlets, first exports, 50 new hires: these are local news stories.', 'They just rarely get written in a format newsrooms can use.'],
  li_hook='Malaysian MSMEs contributed 39.7% of GDP in 2025 and account for 96.1% of business establishments.\nTheir share of business headlines is far smaller.',
  li_body=['DOSM\'s latest MSME release usually gets read as an economic indicator. We read it as a communications gap: hundreds of thousands of businesses with stories that never reach a journalist.', 'Not because they aren\'t newsworthy, but because they aren\'t packaged as news. A third outlet, a first export contract or 50 new hires is a strong local story when it comes with clear numbers and a quotable spokesperson.'],
  li_close='If you run an SME: which story from this year should the public know about?',
  fb='Fun fact: MSMEs made up 39.7% of Malaysia\'s GDP in 2025. If your business is one of them, your story deserves coverage too 💙')),
S['W2Fri'], S['W3Mon'],
# 8 ── W3 Wed VIRAL reel
dict(slot='W3Wed', pillar='VIRAL', format='reel', slug='things-your-brand-should-ghost-before-2027',
 title='Things your brand should ghost before 2027', cta='Comment the one you\'re ghosting first', src=['BP4', 'MR'], tags=['#PRlife', '#MarketingMalaysia'],
 slides=[dict(t='cover', tag='we give you permission', title='things your brand should *ghost* before 2027')],
 reel=dict(frames=[
   dict(top='hot take', text='things your brand should *ghost* before 2027', dur=2.5, theme='navy'),
   dict(text='"leading", "revolutionary", "world-class" in the *headline*', sub='show the number instead', dur=3.5, theme='pale'),
   dict(text='quotes that say *nothing*', sub='"we are thrilled…" — ghosted', dur=3.0, theme='blue'),
   dict(text='following up *every day*', sub='50% of journalists say once is ideal', src='Muck Rack, State of Journalism 2025', dur=3.5, theme='navy'),
   dict(text='reporting PR in *AVE*', sub='Barcelona Principles 4.0 says don\'t', src='AMEC, Barcelona Principles 4.0 (2025)', dur=3.5, theme='pale'),
   dict(text='"hope a journalist *sees our post*"', sub='send a real release instead', dur=3.0, theme='blue'),
  ],
  vo=['Things your brand should ghost before 2027.', 'Leading, revolutionary, world-class in the headline. Show the number.', 'Quotes that say nothing.', 'Following up every day. Half of journalists say once is ideal.', 'Reporting PR in ad value equivalents. The Barcelona Principles say don\'t.', 'Hoping a journalist sees your post. Send a real release.'],
  broll=['Team member swiping "left" on printed buzzwords (props)', 'Phone notification spam close-up (mock)', 'Spreadsheet labelled "AVE" being deleted (mock screen)', 'Laptop sending a release from the VRITIMES dashboard (demo account)'],
  audio='Trending "ghosting"/"bye" sound or playful beat from the platform\'s licensed library'),
 cap=dict(
  hook='Things your brand should ghost before 2027 👻 (we give you permission)',
  lines=['👻 "Leading", "revolutionary", "world-class" headlines', '👻 Quotes that say nothing', '👻 Following up every day (50% of journalists say once is ideal)', '👻 Reporting PR in AVE (Barcelona Principles 4.0 says no)', '👻 Hoping a journalist sees your post', '', 'Which one are you ghosting first?'],
  ig_cta='Send this to your team before the 2027 planning meeting. Link in bio.',
  li_hook='Five PR habits worth retiring before 2027.\nA light video, a serious point.',
  li_body=['Most of these survive because nobody questions them in the planning meeting. A quick audit:'],
  li_points=['Superlatives in headlines. Editors look for a number, a place or an impact, not "leading".', 'Empty quotes. If it couldn\'t appear in an article, cut it.', 'Daily follow-ups. Muck Rack (2025) found 50% of journalists say one follow-up is ideal, and 51% want it 3–7 days later.', 'AVE reports. AMEC\'s Barcelona Principles 4.0 (2025) say invalid measures such as AVEs should not be used. Report outcomes and business impact instead.', 'Waiting for a journalist to stumble on your social post instead of sending news to the right desk.'],
  li_close='Which one is hardest to drop in your organisation?',
  fb='Bye bye to these five PR habits before 2027 👋 Which one are you ditching first?')),
# 9 ── W3 Fri EDU carousel: crisis first 24h
dict(slot='W3Fri', pillar='EDU', format='carousel', slug='crisis-communication-first-24-hours',
 title='Crisis communication: the first 24 hours', cta='Save this for the day you need it', src=['IL', 'DNR'], tags=['#CrisisComms', '#PRtips'],
 slides=[
  dict(t='cover', tag='crisis comms', title='the *first 24 hours* of a crisis', sub='a playbook for SMEs', icons=['clock', 'shield', 'mega']),
  dict(t='point', n='0–1h', title='confirm, don\'t *speculate*', body='Get the facts from the people closest to the issue. Name **one spokesperson** and one approver. Everyone else stays off the record.'),
  dict(t='point', n='1–3h', title='a *holding statement*', body='Short beats perfect. Say what you know, what you\'re doing and when the next update comes.', ex='"We are aware of (issue). Our priority is (people/customers). We are (action). We will share an update by (time) today."'),
  dict(t='point', n='3–6h', title='*bahasa* and english, same message', body='In Malaysia your audience reads in more than one language. Publish the statement in BM and English at the same time, with identical facts, so no version looks like it is hiding something.'),
  dict(t='stat', big='37%', label='of malaysians trust *most news most of the time*', body='Low trust means rumours move fast. A clear, sourced statement from you gives journalists something solid to quote.', src='Reuters Institute, Digital News Report 2025'),
  dict(t='point', n='6–24h', title='update on *the clock you promised*', body='Miss your own deadline and the story becomes about silence. Update even if the update is "investigation ongoing, next update at 10am".'),
  dict(t='list', title='don\'t, *ever*', items=['~"No comment"', '~Deleting critical comments', '~Blaming a junior staffer in public', '~Guessing numbers before they are confirmed']),
  dict(t='cta', title='speak first, *with facts*. it\'s worked since 1906.', items=['Save this playbook', 'Share it with your management team', 'Prepare a holding statement template today'], sources=['Reuters Institute, Digital News Report 2025', 'Billy Penn (2023) on Ivy Lee, 1906']),
 ],
 cap=dict(
  hook='The first 24 hours of a crisis decide the headline. Here\'s the playbook. ⏱️',
  lines=['0–1h: confirm facts, name one spokesperson', '1–3h: holding statement (know / doing / next update)', '3–6h: BM + English, identical facts', '6–24h: update exactly when you promised', '', 'Never: "no comment", deleting comments, public blame, guessed numbers.', '', 'Only 37% of Malaysians trust most news most of the time (Reuters Institute, 2025). Rumours fill silence.'],
  li_hook='In a crisis, the story is written in the first 24 hours, with or without you.\nA practical playbook for Malaysian SMEs.',
  li_body=['Reuters Institute\'s Digital News Report 2025 puts trust in news in Malaysia at 37%. In a low-trust environment rumours spread faster, and a clear, sourced statement becomes the thing journalists can rely on.', 'The timeline we recommend:'],
  li_points=['0–1 hour: confirm facts with the people closest to the issue. One spokesperson, one approver.', '1–3 hours: a holding statement covering what you know, what you\'re doing and when the next update will come.', '3–6 hours: publish in Bahasa Malaysia and English simultaneously with identical facts.', '6–24 hours: update on the schedule you promised, even if the update is "investigation ongoing".', 'Avoid: "no comment", deleting criticism, blaming individuals publicly, or guessing numbers.'],
  li_close='Does your company have a holding statement template ready? If not, slide 3 is a start.',
  fb='Hopefully you\'ll never need it, but save this: a 24-hour crisis communication playbook for SMEs 👇')),
# 10 ── W4 Mon EDU carousel: PR calendar 2027
dict(slot='W4Mon', pillar='EDU', format='carousel', slug='pr-calendar-2027-malaysia',
 title='PR calendar 2027 for Malaysian brands', cta='Save for your 2027 planning', src=['MY1'], tags=['#PRcalendar', '#Planning2027'],
 src_note='Islamic and lunar holiday dates for 2027 are estimates; confirm against the official federal gazette.',
 slides=[
  dict(t='cover', tag='planning 2027', title='your 2027 PR calendar, *sorted early*', sub='save for the planning meeting', icons=['cal', 'chart', 'mega']),
  dict(t='point', icon='cal', title='why a calendar beats *reacting*', body='Reactive releases almost always arrive late. A calendar means data, photos and spokespeople are ready **before** journalists start looking.'),
  dict(t='list', title='Q1 · jan–mar', items=['Chinese New Year (6–7 Feb 2027): stories on SME festive demand', 'Ramadan & Hari Raya (est. Feb–Mar 2027): prepare releases well ahead', 'Annual results & 2027 targets: release your 2026 milestones']),
  dict(t='list', title='Q2 · apr–jun', items=['Mid-year: customer data or internal research', 'Hiring and expansion announcements', 'Launch new product lines ahead of mid-year sales']),
  dict(t='list', title='Q3 · jul–sep', items=['DOSM\'s MSME release (late July): comment with your own data', '31 Aug Merdeka & 16 Sep Malaysia Day: community programmes, not just discounts', 'Partnership & funding announcements']),
  dict(t='list', title='Q4 · oct–dec', items=['Budget 2028 tabling (Oct): react with SME-relevant commentary', 'Deepavali, 11.11 & 12.12: release promos before peak days', 'Year in review & 2028 outlook']),
  dict(t='point', title='the *T-14 to T+3* rule', body='A working timeline for every moment:', exlab='timeline', ex='T-14 research & data · T-7 final release + photos · T-3 pitch journalists · Day 0 publish & share · T+3 coverage recap'),
  dict(t='stat', big='39.7%', label='MSME share of GDP in 2025', body='DOSM\'s MSME data lands every year. Plan a reaction release with your own numbers and you have a ready news hook.', src='DOSM, MSMEs Performance 2025'),
  dict(t='cta', title='plan 2027 PR *now*', items=['Save this calendar', 'Mark 3 moments for your brand', 'Send it to your marketing team'], sources=['DOSM, MSMEs Performance 2025']),
 ],
 cap=dict(
  hook='Your 2027 PR calendar can be built today. 🗓️',
  lines=['Q1: Chinese New Year, Ramadan & Hari Raya (dates est.)', 'Q2: mid-year data, hiring, product launches', 'Q3: DOSM MSME release (late July), Merdeka (31 Aug), Malaysia Day (16 Sep)', 'Q4: Budget 2028, Deepavali, 11.11 & 12.12', '', 'Workflow: T-14 research → T-7 final release → T-3 pitch → Day 0 → T+3 recap.'],
  li_hook='The brands that appear in the news around big moments usually prepared their releases weeks before.\nHere is a 2027 PR calendar framework for Malaysia.',
  li_body=['Recurring data releases are underrated news hooks. DOSM\'s MSME report, which put MSMEs at 39.7% of GDP in 2025, lands every year. A reaction release with your own numbers on publication day is an easy win.', 'A quarterly framework to adapt:'],
  li_points=['Q1: Chinese New Year, Ramadan and Hari Raya (2027 dates are estimates), plus your annual milestones.', 'Q2: mid-year data, hiring and expansion, and product launches ahead of mid-year sales.', 'Q3: DOSM\'s MSME release in late July, then Merdeka and Malaysia Day with community programmes.', 'Q4: Budget 2028 commentary, Deepavali, 11.11 and 12.12. Send promo releases before peak days.', 'For every moment: T-14 research, T-7 final release, T-3 pitch, Day 0 publish, T+3 recap.'],
  li_close='Which moment matters most for your brand next year?',
  fb='Started on 2027 yet? Here\'s a quarter-by-quarter PR calendar for Malaysian brands 👇')),
# 11 ── W4 Wed FUN reel
dict(slot='W4Wed', pillar='FUN', format='reel', slug='how-malaysians-get-their-news',
 title='How Malaysians get their news', cta='Share with your social media team', src=['DNR'], tags=['#MediaMalaysia', '#FunFact'],
 slides=[dict(t='cover', tag='fun fact', title='where do malaysians *get their news*?')],
 reel=dict(frames=[
   dict(top='fun fact', text='where do malaysians *get their news*?', icon='news', dur=3.0, theme='blue'),
   dict(text='*40%* now use TikTok for news', sub='the fastest-growing network', src='Reuters Institute, Digital News Report 2025', dur=3.5, theme='pale'),
   dict(text='but only *37%* trust most news most of the time', src='Reuters Institute, Digital News Report 2025', dur=3.5, theme='navy'),
   dict(text='discovery happens in *the feed*. trust is checked at *the source*.', dur=4.0, theme='blue'),
   dict(text='so your news needs to be *published* AND *shared*', dur=3.5, theme='pale'),
   dict(text='credible in the media, *visible* in the feed', sub='Raise It With Press Release', dur=3.0, theme='navy'),
  ],
  vo=['Where do Malaysians get their news?', 'Forty percent now use TikTok for news.', 'But only thirty-seven percent trust most news most of the time.', 'Discovery happens in the feed. Trust is checked at the source.', 'So your news needs to be published and shared.', 'Credible in the media, visible in the feed.'],
  broll=['Phone scrolling a short-video feed (mock UI, no real accounts)', 'Animated bars 40% / 37% (from text cards)', 'Hands holding a newspaper and a phone (internal talent)'],
  audio='Upbeat "fact reveal" or ticking beat from the platform\'s licensed library'),
 cap=dict(
  hook='40% of Malaysians now use TikTok for news. But trust is another story. 📱',
  lines=['Reuters Institute Digital News Report 2025:', '• TikTok is the fastest-growing network for news: 40%', '• Only 37% trust most news most of the time', '', 'Discovery happens in the feed. Trust is checked at the source.', 'You need both: published in the media, shared on social.'],
  li_hook='Reuters Institute\'s 2025 data shows 40% of Malaysians use TikTok for news, while only 37% trust most news most of the time.\nWhat does that mean for brand communications?',
  li_body=['The two numbers look contradictory but work together. Audiences discover stories in the feed, then judge credibility by the source.', 'For brands, the implications are practical:'],
  li_points=['Coverage in established media gives people a source they can check.', 'That coverage should be reshared on your social channels, including short video.', 'The message must match across media and social, or doubt creeps in.'],
  li_close='How does your team reuse media coverage on social today?',
  fb='Fun fact: 40% of Malaysians now get news on TikTok. But how much do they trust it? Watch to the end 👀')),
# 12 ── W4 Fri PROMO offer-led
dict(slot='W4Fri', pillar='PROMO', format='single', slug='announce-before-12-12-and-year-end',
 title='Get your year-end news out before 12.12', cta='Check current pricing via the link', src=['PRICE'], tags=['#12dot12', '#MalaysiaSME'],
 slides=[dict(t='promo', tag='before 12.12', title='year-end news? *publish it* before the rush',
   items=['Published before peak shopping & holiday days', 'Backlink to your promo or product page', 'Distribution report to review the campaign'],
   price='starts from — see link', src=SRC_PRICE, ribbon=True)],
 cap=dict(
  hook='12.12 is tomorrow. Next year\'s announcements can start today. 🛒',
  lines=['Year-end newsrooms fill up fast. Get in early:', '✓ Published before peak shopping & holiday days', '✓ Backlink to your promo/product page', '✓ Distribution report to review results', '', 'Latest plans & pricing: link in bio.'],
  ig_cta='Check current plans & pricing via the link in bio.',
  li_hook='A year-end release published after the peak has almost no news value.\nThe window is now, and it closes with the holidays.',
  li_body=['Between 12.12, Christmas and New Year, newsrooms run lean and inboxes run full. Releases that land before the slowdown have a far better chance of being picked up and shared.', 'What you can do this week with VRITIMES:'],
  li_points=['Distribute your year-end promo, results or January announcement with guaranteed media placement (count depends on plan).', 'Point the backlink to your promo or product page.', 'Use the distribution report to review the campaign and plan Q1.'],
  li_close='Current plans and pricing are on our official page.',
  fb='Don\'t let your year-end news land after everyone\'s gone on leave 😅 See VRITIMES plans here 👇')),
]

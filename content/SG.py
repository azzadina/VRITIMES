import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _en_shared import shared

LANG = 'en'; CC = 'SG'
TAGS = ['#SingaporeSME', '#PressReleaseSG', '#PRtips', '#SGbusiness', '#SGstartups']
def times(pillar):
    return {'linkedin': '08:30 SGT', 'instagram_facebook': '12:30 SGT' if pillar in ('EDU', 'PROMO') else '20:00 SGT'}

loc = dict(cc='SG', uk=True, li_market='Singapore',
  ex_head='Singapore Logistics Start-up Opens 3 Johor Hubs, Cuts Cross-Border Delivery to One Day',
  ex_quote='"Cross-border next-day delivery used to be a big-company advantage. We are making it the default for SMEs."',
  subj_good=['"Data: 3 in 5 SG F&B SMEs plan price changes in Q1"', '"Spokesperson: CFO on 2027 shipping costs"', '"Embargo 24 Nov, 9am: launch of …"'],
  anchor_bad='best SEO agency Singapore', pov_sub='…along with hundreds of other emails today',
  bf_hook='Black Friday can discount anything. Your credibility isn\'t on sale. 😉')
S = shared(loc)
SRC_PRICE = 'vritimes.com/sg/service/pricing'

POSTS = [S['W1Mon'], S['W1Wed'], S['W1Fri'], S['W2Mon'],
# 5 ── W2 Wed FUN single
dict(slot='W2Wed', pillar='FUN', format='single', slug='smes-employ-71-percent-of-workforce',
 title='SMEs employ 71% of Singapore\'s workforce', cta='Tag an SME founder whose story deserves coverage', src=['SG1'], tags=['#SingaporeSME', '#FunFact'],
 slides=[dict(t='single_stat', tag='fun fact', pre='singapore SMEs employ', big='71%', label='of the *workforce*',
   body='They make up **99%** of businesses. Most of their milestones never make the news.', sub='got a milestone? write the release', src='MTI Singapore (Nov 2024)')],
 cap=dict(
  hook='SMEs employ 71% of Singapore\'s workforce. Yet most of their news never gets published. 🤔',
  lines=['From MTI (Minister Grace Fu, Nov 2024):', '• SMEs = 99% of Singapore\'s businesses', '• They employ 71% of the total workforce', '', 'A regional expansion, a new grant-funded product, 30 new hires: all newsworthy.', 'They just rarely reach a newsroom in a usable format.'],
  li_hook='SMEs make up 99% of Singapore\'s businesses and employ 71% of its workforce.\nThey account for a much smaller share of business coverage.',
  li_body=['The figure, cited by MTI in November 2024, usually frames policy discussions. We read it as a communications gap: tens of thousands of firms whose milestones never reach a journalist.', 'Not because they lack news value, but because they are not packaged as news. A first overseas office, a new product or a sizeable hiring round is a strong story when it comes with clear numbers and a quotable spokesperson.'],
  li_close='If you run an SME: which milestone from this year should the market know about?',
  fb='Fun fact: SMEs employ 71% of Singapore\'s workforce. If you run one, your news deserves coverage too 💙')),
S['W2Fri'], S['W3Mon'],
# 8 ── W3 Wed VIRAL reel: red flags
dict(slot='W3Wed', pillar='VIRAL', format='reel', slug='red-flags-in-a-press-release',
 title='Red flags in a press release', cta='Comment the red flag you see most', src=['MR'], tags=['#PRlife', '#MarketingSG'],
 slides=[dict(t='cover', tag='editors notice', title='red flags in a *press release* 🚩')],
 reel=dict(frames=[
   dict(top='🚩', text='red flags in a *press release*', sub='editors notice. trust us.', dur=2.5, theme='navy'),
   dict(text='a headline with *no verb*', sub='"Excellence. Innovation. Tomorrow."', dur=3.0, theme='pale'),
   dict(text='the news is in *paragraph four*', sub='nobody reads paragraph four', dur=3.0, theme='blue'),
   dict(text='"world\'s first" with *no proof*', sub='journalists will check', dur=3.0, theme='navy'),
   dict(text='a 600-word *pitch email*', sub='69% prefer under 200 words', src='Muck Rack, State of Journalism 2025', dur=3.5, theme='pale'),
   dict(text='media contact: *"info@"*', sub='nobody answers info@', dur=3.0, theme='blue'),
   dict(text='green flag: news first, *proof* attached, a real person to call', dur=3.5, theme='navy'),
  ],
  vo=['Red flags in a press release. Editors notice.', 'A headline with no verb.', 'The news buried in paragraph four.', 'World\'s first, with no proof.', 'A six-hundred-word pitch. Sixty-nine percent of journalists prefer under two hundred.', 'Media contact: info at.', 'Green flag: news first, proof attached, a real person to call.'],
  broll=['Red flag props waved on each point (internal talent)', 'Mock release on screen with paragraph four highlighted', 'Phone dialling a number that rings out (mock)'],
  audio='Trending "red flag" sound or playful beat from the platform\'s licensed library'),
 cap=dict(
  hook='Red flags in a press release 🚩 (editors notice, trust us)',
  lines=['🚩 A headline with no verb', '🚩 The news buried in paragraph four', '🚩 "World\'s first" with no proof', '🚩 A 600-word pitch (69% of journalists prefer under 200 words)', '🚩 Media contact: info@', '', '✅ Green flag: news first, proof attached, a real person to call.'],
  ig_cta='Send this to whoever writes your releases. Link in bio.',
  li_hook='Five red flags that make editors stop reading a press release.\nAll of them are easy to fix before you send.',
  li_body=['None of these are about writing talent. They are process gaps that a two-minute review would catch.'],
  li_points=['A headline with no verb: if nothing happens, there is no news.', 'The news buried below the fold: lead with it.', 'Unverified superlatives such as "world\'s first": journalists check, and credibility drops when they can\'t.', 'Long pitches: Muck Rack (2025) found 69% of journalists prefer pitches under 200 words.', 'A generic contact: name a person who will answer the phone today.'],
  li_close='Which red flag do you see most often?',
  fb='🚩 Five red flags editors spot in a press release. Which one have you seen lately?')),
# 9 ── W3 Fri EDU carousel: measuring PR
dict(slot='W3Fri', pillar='EDU', format='carousel', slug='measuring-pr-ave-is-dead',
 title='Measuring PR: AVE is dead, here is what to report instead', cta='Save for your next PR report', src=['BP3', 'BP4'], tags=['#PRmeasurement', '#PRtips'],
 slides=[
  dict(t='cover', tag='pr measurement', title='AVE is dead. *report this* instead.', sub='your boss will thank you', icons=['chart', 'eye', 'shield']),
  dict(t='point', n='AVE?', title='advertising value *equivalency*', body='"This article would have cost $X as an ad." Easy to calculate, easy to inflate, and it says nothing about whether anyone changed their mind or bought anything.'),
  dict(t='quote', text='"AVEs are not the value of *communication*."', size=96, by='— AMEC, Barcelona Principles 3.0 (2020)', src='AMEC, Barcelona Principles 3.0 (2020)'),
  dict(t='point', n='4.0', title='the 2025 update is *blunter*', body='AMEC\'s Barcelona Principles 4.0 say invalid measures such as AVEs **should not be used**. Measure outcomes and impact, not just outputs.', src='AMEC, Barcelona Principles 4.0 (2025)'),
  dict(t='compare', title='outputs vs *outcomes*', left=dict(h='outputs', items=['Number of articles', 'Potential reach', 'AVE (don\'t)']), right=dict(h='outcomes', items=['Tier-1 & target-audience coverage', 'Key message pick-up rate', 'Referral visits, sign-ups, enquiries'])),
  dict(t='list', title='a *one-page* PR report', items=['Objective set before the release', 'Coverage by quality, not just count', 'Did our key message appear?', 'What audiences did next (traffic, leads)', 'What we will change next time']),
  dict(t='cta', title='measure what *matters*', items=['Save this report template', 'Share with whoever signs off your PR budget'], sources=['AMEC, Barcelona Principles 3.0 (2020)', 'AMEC, Barcelona Principles 4.0 (2025)']),
 ],
 cap=dict(
  hook='Still reporting PR in AVE? The industry standard says stop. 📉',
  lines=['AMEC\'s Barcelona Principles 3.0: "AVEs are not the value of communication."', '4.0 (2025): invalid measures such as AVEs should not be used.', '', 'Report this instead:', '✓ Coverage quality, not just count', '✓ Key message pick-up', '✓ What audiences did next: visits, sign-ups, enquiries', '✓ What you\'ll change next time'],
  li_hook='If your PR report leads with advertising value equivalency, it is measuring the wrong thing.\nThe industry framework has said so for years, and more bluntly in 2025.',
  li_body=['AMEC\'s Barcelona Principles 3.0 (2020) state that "AVEs are not the value of communication". The 2025 update, Barcelona Principles 4.0, goes further: invalid measures such as AVEs should not be used.', 'A one-page report we recommend for SME and start-up teams:'],
  li_points=['The objective, agreed before the release went out.', 'Coverage by quality: target audience and tier, not just article count.', 'Key message pick-up: did the point you wanted actually appear?', 'Outcomes: referral visits, sign-ups, enquiries.', 'One thing you will change next time.'],
  li_close='What does your management actually ask for in a PR report?',
  fb='Your PR report probably doesn\'t need AVE. Here\'s a simpler one-page version that shows real value 👇')),
# 10 ── W4 Mon EDU carousel: PR calendar 2027 SG
dict(slot='W4Mon', pillar='EDU', format='carousel', slug='pr-calendar-2027-singapore',
 title='PR calendar 2027 for Singapore brands', cta='Save for your 2027 planning', src=['SG1'], tags=['#PRcalendar', '#Planning2027'],
 src_note='2027 public holiday dates are indicative; confirm against MOM\'s official 2027 list.',
 slides=[
  dict(t='cover', tag='planning 2027', title='your 2027 PR calendar, *sorted early*', sub='save for the planning meeting', icons=['cal', 'chart', 'mega']),
  dict(t='point', icon='cal', title='why a calendar beats *reacting*', body='Reactive releases almost always arrive late. A calendar means data, photos and spokespeople are ready **before** journalists start looking.'),
  dict(t='list', title='Q1 · jan–mar', items=['Chinese New Year (early Feb 2027): newsrooms slow, publish before', 'Budget 2027 (Feb): react with SME-relevant commentary', 'Annual results & 2027 targets']),
  dict(t='list', title='Q2 · apr–jun', items=['Mid-year data from your own customers', 'Hiring and regional expansion announcements', 'Industry events & trade shows: pre-announce, don\'t wait']),
  dict(t='list', title='Q3 · jul–sep', items=['9 Aug National Day: community programmes, local pride stories', 'Partnership & funding announcements', 'Prep for year-end events']),
  dict(t='list', title='Q4 · oct–dec', items=['11.11, Black Friday & 12.12: release promos before peak days', 'Year-end slowdown from mid-Dec: plan January news now', 'Year in review & 2028 outlook']),
  dict(t='point', title='the *T-14 to T+3* rule', body='A working timeline for every moment:', exlab='timeline', ex='T-14 research & data · T-7 final release + photos · T-3 pitch journalists · Day 0 publish & share · T+3 coverage recap'),
  dict(t='stat', big='99%', label='of singapore businesses are SMEs', body='Every one of them is competing for the same news days. Preparation decides who gets covered.', src='MTI Singapore (Nov 2024)'),
  dict(t='cta', title='plan 2027 PR *now*', items=['Save this calendar', 'Mark 3 moments for your brand', 'Send it to your marketing team'], sources=['MTI Singapore (Nov 2024)']),
 ],
 cap=dict(
  hook='Your 2027 PR calendar can be built today. 🗓️',
  lines=['Q1: Chinese New Year, Budget 2027, annual results', 'Q2: mid-year data, hiring, trade shows', 'Q3: National Day (9 Aug), partnerships & funding', 'Q4: 11.11, Black Friday, 12.12, year-end slowdown', '', 'Workflow: T-14 research → T-7 final release → T-3 pitch → Day 0 → T+3 recap.'],
  li_hook='The brands that appear in the news around big moments prepared their releases weeks earlier.\nHere is a 2027 PR calendar framework for Singapore.',
  li_body=['With SMEs making up 99% of Singapore\'s businesses (MTI, 2024), news days around Budget, National Day and year-end are crowded. Preparation, not volume, decides who gets covered.', 'A quarterly framework to adapt:'],
  li_points=['Q1: Chinese New Year (publish before the slowdown), Budget 2027 commentary and annual results.', 'Q2: mid-year customer data, hiring and regional expansion, and pre-announcements for trade shows.', 'Q3: National Day community stories, plus partnership and funding news.', 'Q4: 11.11, Black Friday and 12.12, then plan January announcements before the mid-December slowdown.', 'For every moment: T-14 research, T-7 final release, T-3 pitch, Day 0 publish, T+3 recap.'],
  li_close='Which moment matters most for your brand next year?',
  fb='Started on 2027 yet? Here\'s a quarter-by-quarter PR calendar for Singapore brands 👇')),
# 11 ── W4 Wed FUN reel
dict(slot='W4Wed', pillar='FUN', format='reel', slug='singapore-trust-in-news',
 title='How much does Singapore trust the news?', cta='Share with your comms team', src=['DNR'], tags=['#MediaSG', '#FunFact'],
 slides=[dict(t='cover', tag='fun fact', title='how much does singapore *trust the news*?')],
 reel=dict(frames=[
   dict(top='fun fact', text='how much does singapore *trust the news*?', icon='eye', dur=3.0, theme='blue'),
   dict(text='*45%* trust most news most of the time', src='Reuters Institute, Digital News Report 2025', dur=3.5, theme='pale'),
   dict(text='only thailand ranks higher among our markets: *55%*', src='Reuters Institute, Digital News Report 2025', dur=3.5, theme='navy'),
   dict(text='australia *43%* · philippines *38%* · malaysia *37%* · indonesia *36%*', src='Reuters Institute, Digital News Report 2025', dur=4.0, theme='blue'),
   dict(text='higher trust = *earned coverage* carries real weight here', dur=3.5, theme='pale'),
   dict(text='be the story *worth publishing*', sub='Raise It With Press Release', dur=3.0, theme='navy'),
  ],
  vo=['How much does Singapore trust the news?', 'Forty-five percent trust most news most of the time.', 'Among our markets, only Thailand ranks higher, at fifty-five.', 'Australia forty-three, the Philippines thirty-eight, Malaysia thirty-seven, Indonesia thirty-six.', 'Higher trust means earned coverage carries real weight here.', 'Be the story worth publishing.'],
  broll=['Animated bar chart of six markets (from text cards)', 'Commuter reading news on phone (internal talent, no identifiable public)', 'Close-up of a newspaper business section (own photo)'],
  audio='Upbeat "fact reveal" beat from the platform\'s licensed library'),
 cap=dict(
  hook='45% of Singaporeans trust most news most of the time. That\'s high for the region. 📰',
  lines=['Reuters Institute Digital News Report 2025, trust in news:', '🇹🇭 55% · 🇸🇬 45% · 🇦🇺 43%', '🇵🇭 38% · 🇲🇾 37% · 🇮🇩 36%', '', 'Higher trust means earned media coverage carries real weight.', 'Worth getting right.'],
  li_hook='Trust in news in Singapore is 45%, the second highest of the six Asia-Pacific markets we work in, according to the Reuters Institute Digital News Report 2025.\nThat makes earned coverage especially valuable.',
  li_body=['For comparison: Thailand 55%, Australia 43%, the Philippines 38%, Malaysia 37% and Indonesia 36%.', 'When audiences trust established media, being covered by it lends credibility that paid placements rarely match. Practical implications:'],
  li_points=['Invest in news value: data, clear impact, a named spokesperson.', 'Target the outlets your customers actually read.', 'Reuse coverage in sales decks, newsletters and social, with links to the source.'],
  li_close='How does your team put earned coverage to work after it is published?',
  fb='Fun fact: 45% of Singaporeans trust most news most of the time. See how that compares with the region 👀')),
# 12 ── W4 Fri PROMO offer-led
dict(slot='W4Fri', pillar='PROMO', format='single', slug='plan-january-news-before-slowdown',
 title='Line up January news before the year-end slowdown', cta='Check current pricing via the link', src=['PRICE'], tags=['#SGbusiness', '#SingaporeSME'],
 slides=[dict(t='promo', tag='before the slowdown', title='january news? *line it up* before december ends',
   items=['Schedule your release before the year-end slowdown', 'Backlink to your launch or product page', 'Distribution report to review the campaign'],
   price='starts from — see link', src=SRC_PRICE, ribbon=True)],
 cap=dict(
  hook='Mid-December, Singapore newsrooms slow down. Your January news shouldn\'t. 📅',
  lines=['Get ahead before the break:', '✓ Plan & prep your release before year-end', '✓ Backlink to your launch/product page', '✓ Distribution report to review results', '', 'Latest plans & pricing: link in bio.'],
  ig_cta='Check current plans & pricing via the link in bio.',
  li_hook='The first two weeks of January are crowded with announcements that were all prepared in December.\nIf yours isn\'t ready yet, now is the time.',
  li_body=['From mid-December, many newsrooms and comms teams run lean. Teams that finalise January releases before the break go into the new year with momentum instead of a backlog.', 'What you can do this week with VRITIMES:'],
  li_points=['Prepare and distribute your year-end results or January announcement with guaranteed media placement (count depends on plan).', 'Point the backlink to your launch or product page.', 'Use the distribution report to review results and plan Q1.'],
  li_close='Current plans and pricing are on our official page.',
  fb='Finish 2026 with your January news ready to go. See VRITIMES plans here 👇')),
]

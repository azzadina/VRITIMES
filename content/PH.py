import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _en_shared import shared

LANG = 'en'; CC = 'PH'
TAGS = ['#PressReleasePH', '#MSMEPH', '#PRtipsPH', '#NegosyoTips', '#PhilippineBusiness']
def times(pillar):
    return {'linkedin': '08:30 PHT', 'instagram_facebook': '12:00 PHT' if pillar in ('EDU', 'PROMO') else '20:00 PHT'}

loc = dict(cc='PH', uk=False, li_market='Philippine',
  ex_head='Cebu Logistics Startup Opens 5 Visayas Hubs, Cuts Delivery Time to One Day',
  ex_quote='"Next-day delivery shouldn\'t only be for Metro Manila. The Visayas is just the start."',
  subj_good=['"Data: 3 in 5 Metro Manila food MSMEs raised prices in Q4"', '"Spokesperson: CFO on 2027 shipping costs"', '"Embargo Nov 24, 9AM: launch of …"'],
  anchor_bad='cheap SEO services Manila', pov_sub='…kasama ng daan-daang ibang email today',
  bf_hook='Black Friday can discount anything. Just not your credibility. 😉')
S = shared(loc)
SRC_PRICE = 'vritimes.com/ph/service/pricing'

POSTS = [S['W1Mon'], S['W1Wed'], S['W1Fri'], S['W2Mon'],
# 5 ── W2 Wed FUN single
dict(slot='W2Wed', pillar='FUN', format='single', slug='msmes-99-6-percent-of-businesses',
 title='MSMEs are 99.6% of Philippine businesses', cta='Tag a negosyante whose story deserves coverage', src=['PH1'], tags=['#MSMEPH', '#FunFact'],
 slides=[dict(t='single_stat', tag='fun fact', pre='MSMEs are', big='99.6%', label='of philippine *businesses*',
   body='And they generate **66.97%** of all jobs. That\'s a lot of untold business stories.', sub='may kwento ka? write the release', src='DTI, 2023 MSME Statistics')],
 cap=dict(
  hook='99.6% of Philippine businesses are MSMEs. How many have been in the news? 🤔',
  lines=['DTI 2023 MSME Statistics:', '• 1,246,373 business enterprises', '• 99.6% are MSMEs', '• MSMEs generated 6,351,466 jobs = 66.97% of employment', '', 'New branches, first exports, 50 new hires: these are real news stories.', 'They just rarely get written in a format newsrooms can use.'],
  li_hook='MSMEs make up 99.6% of Philippine businesses and generate 66.97% of jobs.\nTheir share of business headlines is a fraction of that.',
  li_body=['DTI\'s 2023 figures (1,246,373 enterprises, 6,351,466 MSME jobs) are usually quoted in policy discussions. We read them as a communications gap: more than a million businesses with stories that never reach a reporter.', 'Not because they lack news value, but because they aren\'t packaged as news. A third branch in Davao, a first export order or 50 new hires is a strong local story when it comes with clear numbers and a quotable spokesperson.'],
  li_close='If you run an MSME: which story from this year should the public hear?',
  fb='Fun fact: 99.6% of businesses in the Philippines are MSMEs. If yours is one of them, your story deserves coverage too 💙')),
S['W2Fri'], S['W3Mon'],
# 8 ── W3 Wed VIRAL reel: myth vs fact
dict(slot='W3Wed', pillar='VIRAL', format='reel', slug='press-release-myth-vs-fact',
 title='Press release myth vs fact', cta='Comment the myth you used to believe', src=['CI', 'MR', 'GG1'], tags=['#PRlife', '#MarketingPH'],
 slides=[dict(t='cover', tag='myth vs fact', title='"press releases are *dead* na daw"')],
 reel=dict(frames=[
   dict(top='myth vs fact', text='"press releases are *dead* na daw"', dur=2.5, theme='navy'),
   dict(top='fact', text='*72%* of journalists call them the most useful thing PR sends', src='Cision, State of the Media 2025', dur=3.5, theme='pale'),
   dict(top='myth', text='"longer pitch = more *serious*"', dur=2.5, theme='blue'),
   dict(top='fact', text='*69%* prefer pitches under 200 words', src='Muck Rack, State of Journalism 2025', dur=3.5, theme='navy'),
   dict(top='myth', text='"follow up *araw-araw* para sure"', dur=2.5, theme='pale'),
   dict(top='fact', text='*50%* say one follow-up is ideal', src='Muck Rack, State of Journalism 2025', dur=3.5, theme='blue'),
   dict(top='myth', text='"releases = easy SEO *backlinks*"', dur=2.5, theme='navy'),
   dict(top='fact', text='google calls optimized anchors in releases *link spam*', src='Google Search Central, Spam policies', dur=3.5, theme='pale'),
  ],
  vo=['Press releases are dead daw?', 'Fact: seventy-two percent of journalists call them the most useful thing PR sends.', 'Longer pitch means more serious?', 'Fact: sixty-nine percent prefer pitches under two hundred words.', 'Follow up every day para sure?', 'Fact: half of journalists say one follow-up is ideal.', 'Releases are easy SEO backlinks?', 'Fact: Google calls optimized anchor text in releases link spam.'],
  broll=['Team member holding "MYTH" / "FACT" paddles (blue & lime props)', 'Phone calendar with daily reminders being deleted (mock)', 'Laptop showing a short pitch email (internal template)'],
  audio='Trending "myth vs fact" buzzer/ding sound from the platform\'s licensed library'),
 cap=dict(
  hook='"Press releases are dead na daw." Let\'s fact-check that. 🔍',
  lines=['❌ Myth: press releases are dead', '✅ Fact: 72% of journalists call them the most useful thing PR sends (Cision, 2025)', '', '❌ Myth: longer pitch = more serious', '✅ Fact: 69% prefer under 200 words (Muck Rack, 2025)', '', '❌ Myth: follow up araw-araw', '✅ Fact: 50% say one follow-up is ideal', '', '❌ Myth: releases = easy SEO backlinks', '✅ Fact: Google calls optimized anchor text in releases link spam'],
  ig_cta='Send this to the tita who says press releases are old school 😄 Link in bio.',
  li_hook='Four press release myths we still hear every week, and what the data actually says.',
  li_body=['Most PR habits are inherited, not tested. Here are the four we see most often, checked against current sources:'],
  li_points=['"Press releases are dead." Cision\'s 2025 State of the Media found 72% of journalists call them the most useful resource PR teams provide.', '"A longer pitch looks more serious." Muck Rack (2025): 69% of journalists prefer pitches under 200 words.', '"Follow up daily to be sure." Same study: 50% say one follow-up is ideal, and 51% want it 3–7 days later.', '"Releases are an SEO shortcut." Google\'s spam policies list optimized anchor text in distributed press releases as link spam.'],
  li_close='Which myth was hardest to unlearn on your team?',
  fb='Myth vs fact: press release edition 😄 Which one did you believe before?')),
# 9 ── W3 Fri EDU carousel: spokesperson quotes
dict(slot='W3Fri', pillar='EDU', format='carousel', slug='writing-quotes-journalists-use',
 title='How to write spokesperson quotes journalists actually use', cta='Save before your next release', src=['CI'], tags=['#PRwriting', '#PRtipsPH'],
 slides=[
  dict(t='cover', tag='pr writing', title='quotes journalists *actually use*', sub='and the ones they cut', icons=['quote', 'mega', 'news']),
  dict(t='point', n='01', title='the "thrilled" test', body='If the quote would fit any company\'s release, it fits none. Delete "thrilled", "proud", "excited" and see what\'s left.', ex='✕ "We are thrilled to launch our new app."\n✓ "Half our orders come after 9PM. The app is built for people who shop after their shift."'),
  dict(t='point', n='02', title='give an *opinion*, not a summary', body='The body of the release covers the facts. The quote is where a human explains **why it matters** or **what happens next**.'),
  dict(t='point', n='03', title='one number, *said like a person*', body='Numbers make quotes quotable, but read them out loud first. If it sounds like a spreadsheet, rewrite it.', ex='✕ "Revenue increased by 37.42% YoY."\n✓ "We grew by more than a third this year, mostly outside Metro Manila."'),
  dict(t='point', n='04', title='keep it *under 40 words*', body='Reporters trim long quotes or skip them. Two sentences: the point, then the reason.'),
  dict(t='stat', big='72%', label='of journalists call press releases the *most useful* PR resource', body='A quote that can be lifted word for word is part of what makes a release usable.', src='Cision, State of the Media 2025'),
  dict(t='list', title='quote checklist', items=['No "thrilled / proud / excited"', 'States a view or what happens next', 'At most one number, said naturally', 'Under 40 words, two sentences', 'Approved by the person named']),
  dict(t='cta', title='write it like they\'ll *quote it*', items=['Save this checklist', 'Send it to whoever drafts your CEO quotes'], sources=['Cision, State of the Media 2025']),
 ],
 cap=dict(
  hook='"We are thrilled to announce…" is the most deleted sentence in PR. 😅',
  lines=['Quotes journalists actually use:', '01 Pass the "thrilled" test', '02 Give an opinion, not a summary', '03 One number, said like a person', '04 Under 40 words', '', 'Before/after examples in the carousel.'],
  li_hook='The quote is the only part of a press release where a person speaks. Most companies waste it.\nHow to write one a journalist will actually use.',
  li_body=['Cision\'s 2025 State of the Media found 72% of journalists call press releases the most useful resource from PR teams. What makes a release usable is that parts of it can be lifted as is, and the quote is the most common candidate.', 'Four rules we apply:'],
  li_points=['The "thrilled" test: if the quote fits any company\'s release, rewrite it.', 'Opinion over summary: explain why it matters or what happens next.', 'One number, phrased the way a person would say it.', 'Under 40 words, two sentences: the point, then the reason.'],
  li_close='What\'s the worst quote you\'ve been asked to approve? (No names, please.)',
  fb='Quotes that journalists actually use, with before & after examples. Save this before your next release 👇')),
# 10 ── W4 Mon EDU carousel: PR calendar 2027 PH
dict(slot='W4Mon', pillar='EDU', format='carousel', slug='pr-calendar-2027-philippines',
 title='PR calendar 2027 for Philippine brands', cta='Save for your 2027 planning', src=['PH1'], tags=['#PRcalendar', '#Planning2027'],
 src_note='2027 holiday dates follow the usual rules (e.g. National Heroes Day = last Monday of August); confirm against the 2027 Presidential Proclamation once issued.',
 slides=[
  dict(t='cover', tag='planning 2027', title='your 2027 PR calendar, *sorted early*', sub='save for the planning meeting', icons=['cal', 'chart', 'mega']),
  dict(t='point', icon='cal', title='why a calendar beats *reacting*', body='Reactive releases almost always arrive late. A calendar means data, photos and spokespeople are ready **before** reporters start looking.'),
  dict(t='list', title='Q1 · jan–mar', items=['Annual results & 2027 targets: release your 2026 milestones', 'Holy Week (25–26 Mar 2027): newsrooms slow, publish before', 'Summer travel & graduation season stories']),
  dict(t='list', title='Q2 · apr–jun', items=['Back-to-school & rainy season preparedness angles', '12 Jun Independence Day: community and local-pride stories', 'Mid-year data from your own customers']),
  dict(t='list', title='Q3 · jul–sep', items=['MSME Development Month (July): MSME stories have a news peg', 'National Heroes Day (30 Aug 2027): frontliners & employee stories', '"Ber" months start: plan Christmas campaigns now']),
  dict(t='list', title='Q4 · oct–dec', items=['11.11 & 12.12: release promos before peak days', 'Bonifacio Day (30 Nov) & Christmas slowdown: publish early', 'Year in review & 2028 outlook']),
  dict(t='point', title='the *T-14 to T+3* rule', body='A working timeline for every moment:', exlab='timeline', ex='T-14 research & data · T-7 final release + photos · T-3 pitch reporters · Day 0 publish & share · T+3 coverage recap'),
  dict(t='stat', big='1.25M', bsize=220, label='business enterprises in the philippines (2023)', body='99.6% are MSMEs. Every one has at least one moment a year worth announcing.', src='DTI, 2023 MSME Statistics'),
  dict(t='cta', title='plan 2027 PR *now*', items=['Save this calendar', 'Mark 3 moments for your brand', 'Send it to your marketing team'], sources=['DTI, 2023 MSME Statistics']),
 ],
 cap=dict(
  hook='Your 2027 PR calendar can be built today. 🗓️',
  lines=['Q1: annual results, Holy Week (publish before), summer stories', 'Q2: Independence Day (12 Jun), back-to-school', 'Q3: MSME Development Month (July), National Heroes Day, "ber" months', 'Q4: 11.11, 12.12, Bonifacio Day, Christmas slowdown', '', 'Workflow: T-14 research → T-7 final release → T-3 pitch → Day 0 → T+3 recap.'],
  li_hook='The brands that show up in the news around big moments prepared their releases weeks before.\nHere is a 2027 PR calendar framework for the Philippines.',
  li_body=['With 1,246,373 enterprises in the country (DTI, 2023), competition for attention around peak moments is real. Preparation, not volume, decides who gets covered.', 'A quarterly framework to adapt:'],
  li_points=['Q1: annual milestones, Holy Week (newsrooms slow, so publish before), summer and graduation angles.', 'Q2: Independence Day on 12 June, back-to-school and mid-year customer data.', 'Q3: MSME Development Month in July, National Heroes Day, and the start of the "ber" months for Christmas planning.', 'Q4: 11.11 and 12.12, Bonifacio Day and the Christmas slowdown. Publish early.', 'For every moment: T-14 research, T-7 final release, T-3 pitch, Day 0 publish, T+3 recap.'],
  li_close='Which moment matters most for your brand next year?',
  fb='Started planning 2027? Here\'s a quarter-by-quarter PR calendar for Philippine brands 👇')),
# 11 ── W4 Wed FUN reel: trust ranking
dict(slot='W4Wed', pillar='FUN', format='reel', slug='trust-in-news-philippines-vs-region',
 title='How much do Filipinos trust the news?', cta='Share with your comms team', src=['DNR'], tags=['#MediaPH', '#FunFact'],
 slides=[dict(t='cover', tag='fun fact', title='how much do filipinos *trust the news*?')],
 reel=dict(frames=[
   dict(top='fun fact', text='how much do filipinos *trust the news*?', icon='eye', dur=3.0, theme='blue'),
   dict(text='*38%* trust most news most of the time', src='Reuters Institute, Digital News Report 2025', dur=3.5, theme='pale'),
   dict(text='thailand *55%* · singapore *45%* · australia *43%*', sub='same survey, 2025', src='Reuters Institute, Digital News Report 2025', dur=4.0, theme='navy'),
   dict(text='malaysia *37%* · indonesia *36%*', src='Reuters Institute, Digital News Report 2025', dur=3.0, theme='blue'),
   dict(text='low trust = your news needs *proof*: data, names, sources', dur=4.0, theme='pale'),
   dict(text='be the source *worth quoting*', sub='Raise It With Press Release', dur=3.0, theme='navy'),
  ],
  vo=['How much do Filipinos trust the news?', 'Thirty-eight percent trust most news most of the time.', 'Thailand fifty-five, Singapore forty-five, Australia forty-three.', 'Malaysia thirty-seven, Indonesia thirty-six.', 'Low trust means your news needs proof: data, names, sources.', 'Be the source worth quoting.'],
  broll=['Animated bar chart of the six markets (from text cards)', 'Person reading news on phone, skeptical face (internal talent)', 'Close-up of a release with highlighted data points (internal template)'],
  audio='Upbeat "fact reveal" beat from the platform\'s licensed library'),
 cap=dict(
  hook='Only 38% of Filipinos trust most news most of the time. 📰',
  lines=['Reuters Institute Digital News Report 2025, trust in news:', '🇹🇭 55% · 🇸🇬 45% · 🇦🇺 43%', '🇵🇭 38% · 🇲🇾 37% · 🇮🇩 36%', '', 'Low trust means audiences look for proof.', 'Releases with real data, named spokespeople and sources stand out.'],
  li_hook='Trust in news in the Philippines sits at 38%, according to the Reuters Institute Digital News Report 2025.\nThat changes how brands should communicate.',
  li_body=['For context, the same survey puts Thailand at 55%, Singapore at 45%, Australia at 43%, Malaysia at 37% and Indonesia at 36%.', 'In a lower-trust environment, claims are discounted and proof is rewarded. For brand announcements, that means:'],
  li_points=['Lead with verifiable data, not adjectives.', 'Name a real spokesperson who can be contacted.', 'Cite your sources and link to them.', 'Get published by established media, then share that coverage on social.'],
  li_close='How does your team build credibility into announcements?',
  fb='Fun fact: only 38% of Filipinos trust most news most of the time. See how we compare with the region 👀')),
# 12 ── W4 Fri PROMO offer-led
dict(slot='W4Fri', pillar='PROMO', format='single', slug='publish-before-christmas-slowdown',
 title='Publish your holiday news before the Christmas slowdown', cta='Check current pricing via the link', src=['PRICE'], tags=['#Pasko', '#MSMEPH'],
 slides=[dict(t='promo', tag='before the holidays', title='holiday news? *publish it* before the slowdown',
   items=['Published before 12.12 and the Christmas rush', 'Backlink to your promo or product page', 'Distribution report to review the campaign'],
   price='starts from — see link', src=SRC_PRICE, ribbon=True)],
 cap=dict(
  hook='Christmas is coming and newsrooms are slowing down. Is your announcement out? 🎄',
  lines=['Get in before 12.12 and the holiday rush:', '✓ Published before peak shopping days', '✓ Backlink to your promo/product page', '✓ Distribution report to review results', '', 'Latest plans & pricing: link in bio.'],
  ig_cta='Check current plans & pricing via the link in bio.',
  li_hook='A holiday announcement published after newsrooms go on Christmas mode has very little news value.\nThe window is now.',
  li_body=['Between 12.12, the 8 December holiday and Christmas, newsrooms run lean and inboxes run full. Releases that land before the slowdown have a better chance of being picked up and shared.', 'What you can do this week with VRITIMES:'],
  li_points=['Distribute your holiday promo, year-end results or January announcement with guaranteed media placement (count depends on plan).', 'Point the backlink to your promo or product page.', 'Use the distribution report to review the campaign and plan Q1.'],
  li_close='Current plans and pricing are on our official page.',
  fb='Huwag hintayin ang Christmas break 😅 Publish your holiday news early. See VRITIMES plans here 👇')),
]

"""Shared English concepts (S1–S6), rewritten per market via `loc`.
loc keys: cc, uk (bool spelling), city, region, ex_head, subj_good (3), anchor_bad, cur_note, bf_hook, li_market, ig_ex_tag"""

def sp(loc, uk_word, us_word):
    return uk_word if loc['uk'] else us_word

def shared(loc):
    cc = loc['cc']; cl = cc.lower()
    organisation = sp(loc, 'organisation', 'organization')
    P = {}
    # S1 ── anatomy
    P['W1Mon'] = dict(slot='W1Mon', pillar='EDU', format='carousel', slug='anatomy-of-a-press-release',
     title='Anatomy of a press release editors actually publish', cta='Save as your pre-send checklist', src=['CI'], tags=['#PressRelease', '#PRtips'],
     slides=[
      dict(t='cover', tag='press release 101', title='anatomy of a press release editors *actually publish*', sub='not the ones they bin' if loc['uk'] else 'not the ones they skip'),
      dict(t='point', n='01', title='the headline is *news*, not a slogan', body='Subject + action + impact. Aim for 10–14 words with a number or a place name.',
           ex=f'✕ "Innovation Without Limits"\n✓ "{loc["ex_head"]}"'),
      dict(t='point', n='02', title='the lead answers 5W1H in *two sentences*', body='Editors decide in seconds. If paragraph one doesn\'t say **what, who, when, where and why now**, that is where reading stops.'),
      dict(t='point', n='03', title='one quote with an *actual opinion*', body='A quote is not the place for "we are thrilled". Give a point of view, a number or a plan a reporter can lift.',
           ex='✕ "We are thrilled to announce this milestone."\n✓ ' + loc['ex_quote']),
      dict(t='stat', big='72%', label='of journalists call press releases the *most useful resource* from PR teams', body='Press releases aren\'t dead. Releases a newsroom can\'t use straight away are.', src='Cision, State of the Media 2025'),
      dict(t='list', title='a body that is *ready to use*', items=['Inverted pyramid: the most important fact first', 'Data with a comparison (up from what, to what?)', '1–2 high-res photos with captions', 'A media contact who actually picks up']),
      dict(t='point', n='05', title=f'the boilerplate: *3 sentences* everyone underrates', body=f'Who you are, since when, how big, where, and your official link. Write it once, refresh it every quarter. Journalists copy it as is.'),
      dict(t='cta', title='check these 3 *before you hit send*', items=['Headline: subject, action and a number?', 'Lead: 5W1H done in two sentences?', 'Quote: an opinion or a data point?'], sources=['Cision, State of the Media 2025']),
     ],
     cap=dict(
      hook='Is your press release being read by editors… or opened and closed? 👀',
      lines=['Editors decide in seconds. Here\'s what the ones that get published have in common:', '', '01 Headline = news (subject + action + impact)', '02 Lead answers 5W1H in two sentences', '03 One quote with an opinion, not "we\'re thrilled"', '04 Body: inverted pyramid, data, photos, contact', '05 A 3-sentence boilerplate you keep updated', '', '72% of journalists still call press releases the most useful thing PR teams send (Cision, 2025).'],
      li_hook='72% of journalists say press releases are the most useful resource PR teams provide.\nThe format isn\'t the problem. Most releases just can\'t be used as they are.',
      li_body=[f'Cision\'s 2025 State of the Media report (3,000+ journalists, 19 countries) is often quoted as proof that "releases still work". The part that gets skipped: journalists use the releases that save them work, not the ones that create more.', f'For {loc["li_market"]} teams, the releases that end up published tend to share the same anatomy:'],
      li_points=['The headline is news: subject + action + impact, 10–14 words, ideally with a number or a location.', 'The lead answers 5W1H in two sentences. If it doesn\'t, the editor stops there.', 'The quote carries a point of view or data, not a line about being thrilled.', 'The body uses an inverted pyramid with comparative numbers, high-res photos and a contact who responds.', f'A three-sentence boilerplate refreshed every quarter, because journalists copy it verbatim.'],
      li_close='Which part does your team skip most often: headline, lead or quote? The full carousel is in the PDF above.',
      fb='Before you hit "send", check your press release against this anatomy. Five parts decide whether an editor runs it 👇'))

    # S2 ── Ivy Lee
    P['W1Wed'] = dict(slot='W1Wed', pillar='FUN', format='carousel', slug='first-press-release-1906',
     title='The first press release came out of a train crash', cta='Share with someone in PR', src=['IL'], tags=['#PRhistory', '#FunFact'],
     slides=[
      dict(t='cover', tag='fun fact', title='the *first* press release came out of a train crash', icons=['train', 'news', 'mega'], art='frames'),
      dict(t='point', icon='train', title='28 october *1906*', body='A train run by a Pennsylvania Railroad subsidiary plunged off a bridge in Atlantic City, USA. Railways then usually **kept reporters away** and said little about the cause.', src='Billy Penn (2023); Museum of Public Relations'),
      dict(t='point', icon='mega', title='ivy lee chose to *speak first*', body='Publicist Ivy Lee wrote the company\'s own statement, handed it to reporters and gave them access to the site.', src='Billy Penn (2023); Museum of Public Relations'),
      dict(t='stat', big='30.10.1906', bsize=170, label='The New York Times printed it *word for word*', body='That statement is often called the first press release of modern public relations.', src='Billy Penn (2023); Museum of Public Relations'),
      dict(t='list', title='lessons that *still work* 120 years later', items=['!Speak first, before someone else frames your story', '!Facts beat claims', '!Make the journalist\'s job easier: access, data, sources']),
      dict(t='cta', title='the press release was born in a *crisis*. now it\'s built for *growth*.', items=['Save it for your next team training', 'Tag a colleague who loves PR history'], sources=['Billy Penn, 2023', 'Museum of Public Relations']),
     ],
     cap=dict(
      hook='The world\'s first press release was born from… a train crash. 🚆',
      lines=['28 October 1906, Atlantic City (USA).', 'Railways usually stayed silent and kept reporters out.', '', 'Ivy Lee wrote an official statement and handed it to the press instead.', 'The New York Times printed it word for word on 30 October 1906.', '', 'Still true today: speak first, use facts, make reporters\' jobs easier.'],
      li_hook='The release often called the first ever didn\'t announce a product. It came out of a crisis.\nThe lessons still apply to businesses today.',
      li_body=['In October 1906, a train run by a Pennsylvania Railroad subsidiary came off a bridge in Atlantic City. The industry norm was to restrict access and say nothing.', 'Ivy Lee did the opposite. He drafted an official statement, shared it with reporters and gave them access to the site. The New York Times ran it word for word on 30 October 1906.', 'Three principles from that day we still see working:'],
      li_points=['Whoever speaks first with facts frames the story.', 'A statement that can be quoted as is gets used more than a claim.', 'Access and convenience for journalists are part of the strategy, not a bonus.'],
      li_close='Which of these do brands break most often in a crisis?',
      fb='A fun fact for marketing and PR teams: the first press release appeared in 1906, after a train crash. The story is in this carousel 👇'))

    # S3 ── POV PDF reel
    P['W1Fri'] = dict(slot='W1Fri', pillar='VIRAL', format='reel', slug='pov-press-release-pdf-attachment',
     title='POV: you sent your press release as a PDF attachment', cta='Send to the team still using PDFs', src=['MR'], tags=['#PRlife', '#PressRelease'],
     slides=[dict(t='cover', tag='POV', title='you sent your press release as a *PDF attachment*')],
     reel=dict(frames=[
       dict(top='POV', text='you sent your press release as a *PDF attachment*', icon='pdf', dur=3.0, theme='blue'),
       dict(text='subject line:\n*"Press Release"*', sub=loc['pov_sub'], dur=3.0, theme='pale'),
       dict(text='the journalist has to download, open and *copy-paste* it', sub='(if they get to it)', dur=3.5, theme='navy'),
       dict(text='meanwhile *69%* of journalists prefer pitches under 200 words', src='Muck Rack, State of Journalism 2025', dur=3.5, theme='blue'),
       dict(text='better: *text in the email body*, headline as subject, photo link ready', dur=4.0, theme='pale'),
       dict(text='so your release meets *the media*, not *the archive folder*', sub='Raise It With Press Release', dur=3.0, theme='navy'),
      ],
      vo=['POV: you sent your press release as a PDF attachment.', 'The subject line just says "Press Release".', 'The journalist has to download it, open it and copy-paste it.', 'Meanwhile sixty-nine percent of journalists prefer pitches under two hundred words.', 'Put the text in the email body, use the headline as the subject, share photos by link.', 'So your release meets the media, not the archive.'],
      broll=['Close-up of a laptop inbox full of emails (mock-up, no real names or addresses)', 'Clicking a PDF attachment, slow loading (mock screen recording)', 'Team member reaction shot (internal talent) — the "hmm" face', 'The better email version on screen (internal template)'],
      audio='Trending comedic "awkward pause" sound or upbeat lo-fi from the platform\'s licensed audio library'),
     cap=dict(
      hook='POV: you sent your press release as a PDF attachment 📎😶',
      lines=['Download → open → copy-paste. Every extra step costs you.', '69% of journalists prefer pitches under 200 words (Muck Rack, 2025).', '', 'Do this instead:', '✓ Release text in the email body', '✓ Release headline = subject line', '✓ Photos and documents by link'],
      li_hook='A small habit that stops good releases being read: sending them as PDF attachments.\nIt sounds trivial. The impact isn\'t.',
      li_body=['Muck Rack\'s State of Journalism 2025 found 69% of journalists prefer pitches under 200 words. Journalists want to decide quickly, without extra steps.', 'A PDF attachment adds three of them: download, open, copy. Pair it with a generic subject line and the odds of being read drop sharply.'],
      li_points=['Paste the release text straight into the email body.', 'Use the release headline as the subject line.', 'Share photos and supporting documents by link.', 'If you use a distribution platform, make sure the release lives on a web page that can be accessed and quoted.'],
      li_close='Does your ' + organisation + ' still insist on PDFs because they look "more official"? Tell us below.',
      fb='Who still sends press releases as PDF attachments? 😅 Watch to the end for a version journalists actually prefer.'))

    # S4 ── pitch under 200 words
    P['W2Mon'] = dict(slot='W2Mon', pillar='EDU', format='carousel', slug='pitch-email-under-200-words',
     title='A pitch email under 200 words that gets replies', cta='Save the template', src=['MR'], tags=['#MediaRelations', '#PRtips'],
     slides=[
      dict(t='cover', tag='pr tips', title='a pitch email *under 200 words* that gets replies', sub='template on slide 6'),
      dict(t='stat', big='69%', label='of journalists prefer pitches *under 200 words*', body='A pitch is an invitation, not the release itself. The details live behind a link.', src='Muck Rack, State of Journalism 2025'),
      dict(t='list', title='the *4-line* structure', items=['Line 1 — why it matters to their beat or readers', 'Line 2 — the news in one sentence (with a number)', 'Line 3 — what you can offer: data, a spokesperson, photos', 'Line 4 — link to the full release + your contact']),
      dict(t='compare', title='subject lines: *different fates*', left=dict(h='skipped', items=['"Press Release – ABC Pte Ltd"' if cc == 'SG' else ('"Press Release – ABC Sdn Bhd"' if cc == 'MY' else ('"Press Release – ABC Pty Ltd"' if cc == 'AU' else '"Press Release – ABC Corp."')), '"URGENT!!! Important Update"', '"Exciting Collaboration"']),
           right=dict(h='opened', items=loc['subj_good'])),
      dict(t='stat', big='1×', label='follow-up, *3–7 days* later', body='50% of journalists say one follow-up is ideal. 51% want it 3–7 days after the pitch. More than that is noise.', src='Muck Rack, State of Journalism 2025'),
      dict(t='point', title='a template *you can use today*', body='Swap the parts in brackets.', exlab='template', bsize=36,
           ex='Hi (name), I read your piece on (topic) last week.\n(Company) has just (the news in one sentence + a number).\nWe can share (full data / an interview / photos) this week.\nRelease & images: (link). Thanks — (name, number)'),
      dict(t='cta', title='short pitch, *better odds*', items=['Save this template', 'Send it to whoever handles media relations', 'Follow for weekly PR tips'], sources=['Muck Rack, State of Journalism 2025']),
     ],
     cap=dict(
      hook='Is your pitch email too long? 69% of journalists prefer under 200 words. ✂️',
      lines=['The 4-line structure:', '1️⃣ Why it matters to their beat', '2️⃣ The news in one sentence + a number', '3️⃣ What you can offer: data, spokesperson, photos', '4️⃣ Release link + contact', '', 'Follow-up? Once, 3–7 days later.', 'Full template on slide 6.'],
      li_hook='The pitches journalists reply to are usually shorter than you think.\nAccording to Muck Rack, 69% of journalists prefer pitches under 200 words.',
      li_body=['The most common mistake we see: pasting the whole release into the pitch. A pitch is an invitation to read, not the release itself.', 'The same Muck Rack State of Journalism 2025 data settles the follow-up question too: 50% of journalists say one follow-up is ideal, and 51% want it 3–7 days later.', 'A four-line structure your team can use straight away:'],
      li_points=['Relevance: why this topic fits their beat or readers.', 'The news in one sentence, with a number.', 'The offer: data, a spokesperson or photos that are ready now.', 'A link to the full release and a contact who responds.'],
      li_close='The full template is on slide 6. How long are your team\'s pitches right now?',
      fb='Here\'s a pitch email template under 200 words. Four lines, ready for your team to use 👇'))

    # S5 ── promo feature-led
    P['W2Fri'] = dict(slot='W2Fri', pillar='PROMO', format='single', slug='one-dashboard-write-distribute-report',
     title='Write, distribute and see results in one dashboard', cta=f'See plans at vritimes.com/{cl}', src=['SERVICE', 'PRICE'], tags=['#PressRelease', '#SMEs' if cc != 'AU' else '#SmallBusiness'],
     slides=[dict(t='promo', tag='one dashboard', title='write it. *send it.*\nsee what it did.',
       items=['Guaranteed media placement per release (count depends on plan)', 'Backlink + sharing on VRITIMES social channels', 'Post-distribution report for your boss or client'],
       price='starts from — see link', src=f'vritimes.com/{cl}/service/pricing', ribbon=True)],
     cap=dict(
      hook=loc['bf_hook'],
      lines=['VRITIMES puts it all in one dashboard:', '✓ Write and submit your press release', '✓ Guaranteed media placement per release (count depends on plan)', '✓ Backlink + sharing on VRITIMES social channels', '✓ Post-distribution report', '', 'Latest plans and pricing: link in bio.'],
      ig_cta='See the latest plans via the link in bio.',
      li_hook='Plenty of marketing teams still distribute releases with a contact spreadsheet, one-by-one emails and screenshots as a report.\nThere\'s a tidier way.',
      li_body=[f'VRITIMES is built for start-ups and SMEs that want their releases published without building a media database from scratch.' if loc['uk'] else 'VRITIMES is built for startups and SMEs that want their releases published without building a media database from scratch.', 'The workflow sits in one dashboard:'],
      li_points=['Write and upload your press release.', 'Distribution with guaranteed media placement per release (the number of outlets depends on the plan).', 'A backlink to your site and sharing on VRITIMES social channels.', 'A post-distribution report ready to forward to your manager or client.'],
      li_close='Current plans and pricing are always on our official page.',
      fb='Press releases without the admin: write, distribute and see the results in one dashboard. Plans here 👇'))

    # S6 ── backlinks & SEO
    P['W3Mon'] = dict(slot='W3Mon', pillar='EDU', format='carousel', slug='press-release-backlinks-seo',
     title='Press releases for SEO? Read Google\'s policy first', cta='Save & send to your SEO team', src=['GG1', 'GG2'], tags=['#SEO', '#DigitalPR'],
     slides=[
      dict(t='cover', tag='seo x pr', title='press releases for SEO? *read this first*', sub='straight from google'),
      dict(t='quote', text='Google lists links with *"optimized anchor text in … press releases"* distributed on other sites as *link spam*.', size=76, by='— Google Search Central, spam policies', src='Google Search Central, Spam policies'),
      dict(t='compare', title='*risky* vs *safe*', left=dict(h='risky', items=[f'Anchor "{loc["anchor_bad"]}" in every paragraph', 'A release with no news, just for the link', 'A dozen links in one release']),
           right=dict(h='safe', items=['Brand name or URL as the anchor', 'News that earns follow-up coverage', '1–2 links to a relevant page']), src='Google Search Central, Spam policies'),
      dict(t='point', icon='link', title='so what are release links *worth*?', body='Three real things: **referral traffic** from readers, **brand mentions** on news sites that help people recognise you, and **follow-up coverage** from journalists who find your release.'.replace('recognise', sp(loc, 'recognise', 'recognize'))),
      dict(t='point', icon='shield', title='rel="sponsored" is *normal*', body='Google asks for paid or placed links to carry **rel="sponsored"** or **nofollow**. So judge a release by who reads it and who writes about it next, not by "link juice".', src='Google Search Central, Qualify outbound links'),
      dict(t='list', title='an *SEO-safe* release checklist', items=['Keywords appear naturally in the headline, not stuffed', 'One main link to a relevant page', 'Anchor = brand name or URL', 'Data or a quote other media will want to cite', 'Track brand mentions, not just link counts']),
      dict(t='cta', title='good PR *helps* SEO. not the other way round.' if loc['uk'] else 'good PR *helps* SEO. not the other way around.', items=['Save this checklist', 'Send it to your SEO team'], sources=['Google Search Central — Spam policies', 'Google Search Central — Qualify outbound links']),
     ],
     cap=dict(
      hook='Sending press releases for backlinks? Google has a policy on that. 🔗',
      lines=['Google lists optimised anchor text in press releases distributed on other sites as link spam.'.replace('optimised', sp(loc, 'optimised', 'optimized')), '', 'The safe way:', '✓ Anchor = brand name / URL', '✓ 1–2 links to a relevant page', '✓ News that earns follow-up coverage', '', 'The real value: referral traffic, brand mentions and organic coverage.'],
      li_hook='"Send a press release to get backlinks" is a tactic Google names specifically in its spam policies.\nHere is how to use releases for SEO without the risk.',
      li_body=['In its Spam policies documentation, Google Search Central lists links with optimised anchor text in articles, guest posts or press releases distributed on other sites as an example of link spam. It also asks for paid or placed links to be qualified with rel="sponsored" or nofollow.'.replace('optimised', sp(loc, 'optimised', 'optimized')), 'Does that make releases useless for SEO? Quite the opposite, as long as you measure the right things:'],
      li_points=['Referral traffic from readers who click through.', 'Brand mentions on news sites that strengthen how your entity is recognised.'.replace('recognised', sp(loc, 'recognised', 'recognized')), 'Organic coverage from journalists who find the release and write their own story. That is where the biggest SEO value sits.', 'Safe practice: brand/URL anchors, one main link, and news genuinely worth citing.'],
      li_close='How does your team measure the SEO impact of releases today?',
      fb='Lots of teams send press releases just for backlinks. Before you do, here is what Google actually says 👇'))
    return P

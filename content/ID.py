LANG = 'id'
CC = 'ID'
TAGS = ['#RilisPers', '#UMKM', '#TipsPR', '#PressRelease', '#BrandAwareness']
def times(pillar):
    return {'linkedin': '08:30 WIB', 'instagram_facebook': '12:00 WIB' if pillar in ('EDU', 'PROMO') else '19:30 WIB'}

SRC_PRICE = 'vritimes.com/id/service/pricing'

POSTS = [
# 1 ─────────────────────────────────────────────── W1 Mon EDU carousel (shared S1)
dict(slot='W1Mon', pillar='EDU', format='carousel', slug='anatomi-rilis-pers',
 title='Anatomi rilis pers yang dimuat editor', cta='Simpan sebagai checklist sebelum kirim rilis', src=['CI'], tags=['#RilisPers', '#TipsPR'],
 slides=[
  dict(t='cover', tag='rilis pers 101', title='anatomi rilis pers yang *dimuat* editor', sub='bukan yang dibuang'),
  dict(t='point', n='01', title='judul = *berita*, bukan slogan', body='Subjek + aksi + dampak. Idealnya 10–14 kata, ada angka atau nama tempat.',
       ex='✕ "Inovasi Tanpa Batas untuk Negeri"\n✓ "Startup Logistik Buka 5 Hub Baru di Jawa Timur, Waktu Kirim Jadi 1 Hari"'),
  dict(t='point', n='02', title='lead menjawab 5W1H dalam *2 kalimat*', body='Editor memutuskan dalam hitungan detik. Kalau paragraf pertama belum menjawab **apa, siapa, kapan, di mana, dan kenapa sekarang**, rilis berhenti dibaca di situ.'),
  dict(t='point', n='03', title='satu kutipan yang *punya opini*', body='Kutipan bukan tempat bilang "kami bangga". Isi dengan sudut pandang, angka, atau rencana yang bisa dikutip media.',
       ex='✕ "Kami sangat bangga atas pencapaian ini."\n✓ "Pengiriman sehari bukan lagi kemewahan kota besar. Surabaya dan Malang baru awal."'),
  dict(t='stat', big='72%', label='jurnalis menyebut rilis pers *sumber paling berguna* dari tim PR', body='Rilis tidak mati. Yang mati adalah rilis yang tidak bisa langsung dipakai redaksi.', src='Cision, State of the Media 2025'),
  dict(t='list', title='badan rilis yang *siap pakai*', items=['Piramida terbalik: fakta terpenting di atas', 'Data + pembanding (naik dari berapa ke berapa?)', '1–2 foto resolusi tinggi lengkap dengan caption', 'Kontak media yang benar-benar bisa dihubungi']),
  dict(t='point', n='05', title='boilerplate: *3 kalimat* yang sering diremehkan', body='Siapa Anda, sejak kapan, seberapa besar, di mana, dan link resmi. Tulis sekali, perbarui tiap kuartal. Jurnalis menyalinnya apa adanya.'),
  dict(t='cta', title='cek 3 hal ini *sebelum kirim*', items=['Judul: ada subjek, aksi, dan angka?', 'Lead: 5W1H selesai dalam 2 kalimat?', 'Kutipan: berisi opini atau data?'], sources=['Cision, State of the Media 2025']),
 ],
 cap=dict(
  hook='Rilis pers kamu dibaca editor… atau cuma dibuka lalu ditutup? 👀',
  lines=['Editor memutuskan dalam hitungan detik. Ini anatomi rilis yang lolos:', '', '01 Judul = berita (subjek + aksi + dampak)', '02 Lead menjawab 5W1H dalam 2 kalimat', '03 Satu kutipan yang punya opini, bukan "kami bangga"', '04 Badan rilis: piramida terbalik, data, foto, kontak', '05 Boilerplate 3 kalimat yang selalu diperbarui', '', 'Fakta: 72% jurnalis masih menyebut rilis pers sebagai sumber paling berguna dari tim PR (Cision, 2025).'],
  li_hook='72% jurnalis menyebut rilis pers sebagai sumber paling berguna dari tim PR.\nMasalahnya bukan formatnya. Masalahnya, kebanyakan rilis tidak bisa langsung dipakai.',
  li_body=['Data dari Cision State of the Media 2025 (survei 3.000+ jurnalis di 19 negara) ini sering dibaca sebagai "rilis masih efektif". Yang jarang dibahas: jurnalis memakai rilis yang meringankan kerja mereka, bukan yang menambah pekerjaan.', 'Pola rilis yang akhirnya dimuat hampir selalu sama:'],
  li_points=['Judul adalah berita: subjek + aksi + dampak, 10–14 kata, idealnya ada angka atau lokasi.', 'Lead menjawab 5W1H dalam dua kalimat. Kalau belum, editor berhenti di situ.', 'Kutipan berisi sudut pandang atau data, bukan ucapan bangga.', 'Badan rilis memakai piramida terbalik, menyertakan pembanding angka, foto beresolusi tinggi, dan kontak yang aktif.', 'Boilerplate tiga kalimat yang diperbarui tiap kuartal, karena jurnalis menyalinnya apa adanya.'],
  li_close='Mana yang paling sering terlewat di tim Anda: judul, lead, atau kutipan? Carousel lengkapnya ada di PDF di atas.',
  fb='Sebelum klik "kirim", cek dulu anatomi rilis pers kamu. Ini lima bagian yang menentukan dimuat atau tidaknya rilis oleh editor 👇')),

# 2 ─────────────────────────────────────────────── W1 Wed FUN carousel (shared S2)
dict(slot='W1Wed', pillar='FUN', format='carousel', slug='rilis-pers-pertama-1906',
 title='Rilis pers pertama lahir dari kecelakaan kereta', cta='Bagikan ke teman yang kerja di PR', src=['IL'], tags=['#SejarahPR', '#FunFact'],
 slides=[
  dict(t='cover', tag='fun fact', title='rilis pers *pertama* lahir dari kecelakaan kereta', icons=['train', 'news', 'mega'], art='frames'),
  dict(t='point', icon='train', title='28 oktober *1906*', body='Kereta milik anak perusahaan Pennsylvania Railroad jatuh dari jembatan di Atlantic City, AS. Saat itu, perusahaan kereta biasa **menutup akses wartawan** dan diam soal penyebab kecelakaan.', src='Billy Penn (2023); Museum of Public Relations'),
  dict(t='point', icon='mega', title='ivy lee memilih *bicara duluan*', body='Konsultan humas perusahaan, Ivy Lee, menulis pernyataan resmi versi perusahaan dan membagikannya ke wartawan, lengkap dengan akses ke lokasi.', src='Billy Penn (2023); Museum of Public Relations'),
  dict(t='stat', big='30.10.1906', bsize=170, label='The New York Times memuatnya *kata per kata*', body='Pernyataan inilah yang sering disebut sebagai rilis pers pertama dalam sejarah humas modern.', src='Billy Penn (2023); Museum of Public Relations'),
  dict(t='list', title='pelajaran yang *masih berlaku* 120 tahun kemudian', items=['!Bicara duluan, sebelum orang lain membingkai cerita Anda', '!Fakta lebih kuat daripada klaim', '!Permudah kerja wartawan: akses, data, narasumber']),
  dict(t='cta', title='rilis pers lahir dari *krisis*. sekarang dipakai untuk *tumbuh*.', items=['Simpan untuk materi training tim', 'Tag teman yang suka sejarah PR'], sources=['Billy Penn, 2023', 'Museum of Public Relations']),
 ],
 cap=dict(
  hook='Rilis pers pertama di dunia lahir dari… kecelakaan kereta. 🚆',
  lines=['28 Oktober 1906, Atlantic City (AS).', 'Perusahaan kereta biasanya menutup mulut dan mengusir wartawan.', '', 'Ivy Lee justru menulis pernyataan resmi dan membagikannya ke wartawan.', 'The New York Times memuatnya kata per kata pada 30 Oktober 1906.', '', 'Pelajarannya masih relevan: bicara duluan, pakai fakta, permudah kerja wartawan.'],
  li_hook='Rilis pers yang sering disebut sebagai yang pertama lahir dari sebuah krisis, bukan dari peluncuran produk.\nDan pelajarannya masih relevan untuk bisnis hari ini.',
  li_body=['Oktober 1906, kereta anak perusahaan Pennsylvania Railroad jatuh dari jembatan di Atlantic City. Kebiasaan industri saat itu: tutup akses, jangan bicara.', 'Ivy Lee mengambil jalan sebaliknya. Ia menyusun pernyataan resmi, membagikannya ke wartawan, dan memberi akses ke lokasi. The New York Times memuat pernyataan itu kata per kata pada 30 Oktober 1906.', 'Tiga prinsip dari kejadian itu yang masih kami lihat bekerja sampai sekarang:'],
  li_points=['Siapa yang bicara duluan dengan fakta, dialah yang membingkai cerita.', 'Pernyataan yang bisa dikutip apa adanya lebih mudah dimuat daripada klaim.', 'Akses dan kemudahan bagi wartawan adalah bagian dari strategi, bukan bonus.'],
  li_close='Menurut Anda, prinsip mana yang paling sering dilanggar brand saat krisis?',
  fb='Fun fact untuk tim marketing & PR: rilis pers pertama ternyata lahir tahun 1906, dari sebuah kecelakaan kereta. Ceritanya di carousel ini 👇')),

# 3 ─────────────────────────────────────────────── W1 Fri VIRAL reel (shared S3)
dict(slot='W1Fri', pillar='VIRAL', format='reel', slug='pov-rilis-lampiran-pdf',
 title='POV: kirim rilis pers sebagai lampiran PDF', cta='Kirim ke tim yang masih pakai PDF', src=['MR'], tags=['#PRlife', '#RilisPers'],
 slides=[dict(t='cover', tag='POV', title='kamu kirim rilis pers sebagai *lampiran PDF*')],
 reel=dict(frames=[
   dict(top='POV', text='kamu kirim rilis pers sebagai *lampiran PDF*', icon='pdf', dur=3.0, theme='blue'),
   dict(text='subjek email:\n*"Press Release"*', sub='…bersama ratusan email lain hari ini', dur=3.0, theme='pale'),
   dict(text='jurnalis harus unduh, buka, lalu *copy-paste* sendiri', sub='(itu pun kalau sempat)', dur=3.5, theme='navy'),
   dict(text='padahal *69%* jurnalis lebih suka pitch di bawah 200 kata', src='Muck Rack, State of Journalism 2025', dur=3.5, theme='blue'),
   dict(text='yang benar: *teks di badan email*, judul jadi subjek, link foto siap unduh', dur=4.0, theme='pale'),
   dict(text='biar rilisnya ketemu *media*, bukan ketemu *folder arsip*', sub='Raise It With Press Release', dur=3.0, theme='navy'),
  ],
  vo=['POV: kamu kirim rilis pers sebagai lampiran PDF.', 'Subjeknya cuma "Press Release".', 'Jurnalisnya harus unduh, buka, copy-paste sendiri.', 'Padahal 69 persen jurnalis lebih suka pitch di bawah 200 kata.', 'Tulis di badan email, judul jadi subjek, foto via link.', 'Biar rilisnya ketemu media, bukan arsip.'],
  broll=['Close-up layar laptop: kotak masuk email penuh (mock-up, tanpa nama/alamat asli)', 'Tangan mengklik lampiran PDF, loading lama (screen recording mock)', 'Reaksi wajah tim VRITIMES (talent internal) — ekspresi "hmm"', 'Contoh email yang benar di layar (template internal)'],
  audio='Trending comedic/"awkward pause" sound atau lo-fi upbeat dari pustaka audio berlisensi Instagram/TikTok'),
 cap=dict(
  hook='POV: kamu kirim rilis pers sebagai lampiran PDF 📎😶',
  lines=['Jurnalis harus unduh → buka → copy-paste sendiri.', 'Sementara 69% jurnalis lebih suka pitch di bawah 200 kata (Muck Rack, 2025).', '', 'Yang lebih baik:', '✓ Teks rilis langsung di badan email', '✓ Judul rilis = subjek email', '✓ Foto & dokumen lewat link'],
  li_hook='Kesalahan kecil yang membuat rilis bagus tidak terbaca: mengirimnya sebagai lampiran PDF.\nKedengarannya sepele. Dampaknya tidak.',
  li_body=['Muck Rack (State of Journalism 2025) mencatat 69% jurnalis lebih suka pitch di bawah 200 kata. Artinya, jurnalis ingin memutuskan cepat tanpa langkah tambahan.', 'Lampiran PDF menambah tiga langkah: unduh, buka, salin. Ditambah subjek email generik, peluang dibaca turun drastis.'],
  li_points=['Tempel teks rilis langsung di badan email.', 'Gunakan judul rilis sebagai subjek email.', 'Sediakan foto dan dokumen pendukung lewat link.', 'Jika memakai platform distribusi, pastikan rilis tayang sebagai halaman web yang bisa diakses dan dikutip.'],
  li_close='Masih ada tim yang wajib kirim PDF karena "lebih resmi"? Ceritakan di komentar.',
  fb='Siapa di sini yang masih kirim rilis pers sebagai lampiran PDF? 😅 Tonton sampai habis, ada cara yang lebih ramah untuk jurnalis.')),

# 4 ─────────────────────────────────────────────── W2 Mon EDU carousel (shared S4)
dict(slot='W2Mon', pillar='EDU', format='carousel', slug='pitch-email-200-kata',
 title='Pitch email di bawah 200 kata yang dibalas', cta='Simpan templatenya', src=['MR'], tags=['#MediaRelations', '#TipsPR'],
 slides=[
  dict(t='cover', tag='pr tips', title='pitch email *di bawah 200 kata* yang dibalas', sub='template di slide 6'),
  dict(t='stat', big='69%', label='jurnalis lebih suka pitch *di bawah 200 kata*', body='Pitch adalah undangan, bukan rilisnya. Detail lengkap cukup lewat link.', src='Muck Rack, State of Journalism 2025'),
  dict(t='list', title='struktur *4 baris*', items=['Baris 1 — kenapa relevan untuk rubrik/pembacanya', 'Baris 2 — beritanya dalam 1 kalimat (dengan angka)', 'Baris 3 — yang bisa Anda tawarkan: data, narasumber, foto', 'Baris 4 — link rilis lengkap + kontak']),
  dict(t='compare', title='subjek email: *beda nasib*', left=dict(h='dilewati', items=['"Press Release PT ABC"', '"URGENT!!! Info Penting"', '"Kolaborasi Spesial"']),
       right=dict(h='dibuka', items=['"Data: 3 dari 5 UMKM kuliner naikkan harga Q4"', '"Narasumber: CFO soal biaya logistik 2027"', '"Embargo 24/11 09.00: peluncuran …"'])),
  dict(t='stat', big='1×', label='follow-up, *3–7 hari* kemudian', body='50% jurnalis bilang satu kali follow-up itu ideal. 51% ingin jaraknya 3–7 hari. Lebih dari itu = mengganggu.', src='Muck Rack, State of Journalism 2025'),
  dict(t='point', title='template *siap pakai*', body='Ganti bagian dalam kurung.', exlab='template', bsize=36,
       ex='Halo (nama), saya baca liputan Anda soal (topik) minggu lalu.\n(Perusahaan) baru merilis (berita dalam 1 kalimat + angka).\nKami bisa sediakan (data lengkap / wawancara / foto) minggu ini.\nRilis & foto: (link). Terima kasih — (nama, nomor)'),
  dict(t='cta', title='pitch pendek, *peluang* panjang', items=['Simpan template ini', 'Kirim ke rekan yang pegang media relations', 'Follow untuk tips PR mingguan'], sources=['Muck Rack, State of Journalism 2025']),
 ],
 cap=dict(
  hook='Pitch email kamu kepanjangan? 69% jurnalis lebih suka di bawah 200 kata. ✂️',
  lines=['Struktur 4 baris yang kami pakai:', '1️⃣ Kenapa relevan untuk rubriknya', '2️⃣ Beritanya dalam 1 kalimat + angka', '3️⃣ Yang bisa ditawarkan: data, narasumber, foto', '4️⃣ Link rilis + kontak', '', 'Follow-up? Cukup 1 kali, 3–7 hari kemudian.', 'Template lengkap di slide 6.'],
  li_hook='Pitch yang dibalas jurnalis biasanya lebih pendek dari yang Anda kira.\nMenurut Muck Rack, 69% jurnalis lebih suka pitch di bawah 200 kata.',
  li_body=['Kesalahan paling umum yang kami lihat: pitch berisi seluruh rilis. Padahal pitch adalah undangan untuk membaca, bukan rilis itu sendiri.', 'Data yang sama dari Muck Rack State of Journalism 2025 juga menjawab soal follow-up: 50% jurnalis menganggap satu kali follow-up itu ideal, dan 51% ingin jaraknya 3–7 hari.', 'Struktur empat baris yang bisa langsung dipakai tim Anda:'],
  li_points=['Relevansi: kenapa topik ini cocok untuk rubrik atau pembacanya.', 'Berita dalam satu kalimat, lengkap dengan angka.', 'Penawaran: data, narasumber, atau foto yang siap.', 'Link rilis lengkap dan kontak yang aktif.'],
  li_close='Template lengkapnya ada di slide 6. Berapa panjang pitch tim Anda saat ini?',
  fb='Ini template pitch email di bawah 200 kata. Strukturnya cuma 4 baris dan bisa langsung dipakai tim kamu 👇')),

# 5 ─────────────────────────────────────────────── W2 Wed FUN single (local)
dict(slot='W2Wed', pillar='FUN', format='single', slug='umkm-97-persen-tenaga-kerja',
 title='UMKM menyerap hampir 97% tenaga kerja', cta='Tag pemilik UMKM yang layak diliput', src=['ID1'], tags=['#UMKMIndonesia', '#FunFact'],
 slides=[dict(t='single_stat', tag='fun fact umkm', pre='UMKM menyerap hampir', big='97%', label='tenaga kerja *Indonesia*',
   body='Lebih dari **64 juta** unit usaha, menyumbang **lebih dari 60%** PDB. Ceritanya ada di mana-mana. Liputannya belum.', sub='punya cerita? tulis rilisnya', src='Kemenko Perekonomian (2025)')],
 cap=dict(
  hook='Hampir 97% tenaga kerja Indonesia ada di UMKM. Tapi berapa yang pernah masuk berita? 🤔',
  lines=['Data Kemenko Perekonomian (2025):', '• Lebih dari 64 juta unit UMKM', '• Kontribusi lebih dari 60% PDB', '• Menyerap hampir 97% tenaga kerja', '', 'Cerita bisnis yang layak diberitakan ada di mana-mana: ekspansi cabang, produk ekspor, rekrutmen besar.', 'Masalahnya, jarang ditulis dalam format yang siap dipakai media.'],
  li_hook='UMKM menyerap hampir 97% tenaga kerja Indonesia dan menyumbang lebih dari 60% PDB.\nNamun porsi mereka di halaman berita bisnis jauh lebih kecil.',
  li_body=['Angka dari Kemenko Perekonomian (2025) ini sering dikutip dalam konteks kebijakan. Kami melihatnya dari sisi komunikasi: ada puluhan juta cerita bisnis yang tidak pernah sampai ke jurnalis.', 'Bukan karena tidak layak berita, tetapi karena tidak dikemas sebagai berita. Pembukaan cabang ketiga, kontrak ekspor pertama, atau rekrutmen 50 karyawan baru adalah berita lokal yang kuat bila ditulis dengan data dan kutipan yang jelas.'],
  li_close='Jika Anda pemilik UMKM: cerita apa dari tahun ini yang seharusnya diketahui publik?',
  fb='Fakta menarik: hampir 97% tenaga kerja Indonesia ada di UMKM. Kalau bisnis kamu salah satunya, cerita kamu juga layak diberitakan 💙')),

# 6 ─────────────────────────────────────────────── W2 Fri PROMO single feature-led (shared S5)
dict(slot='W2Fri', pillar='PROMO', format='single', slug='satu-dashboard-tulis-sebar-laporan',
 title='Tulis, sebar, lihat hasilnya dalam satu dashboard', cta='Lihat paket di vritimes.com/id', src=['SERVICE', 'PRICE'], tags=['#RilisPers', '#UMKM'],
 slides=[dict(t='promo', tag='satu dashboard', title='tulis. *sebar.* lihat hasilnya.',
   items=['Penempatan media terjamin per rilis (jumlah sesuai paket)', 'Backlink + dibagikan di kanal sosial VRITIMES', 'Laporan pasca-distribusi untuk atasan atau klien'],
   price='harga mulai dari — cek link', src=SRC_PRICE, ribbon=True)],
 cap=dict(
  hook='Black Friday boleh diskon apa saja. Yang penting rilis kamu tetap tayang. 😉',
  lines=['VRITIMES menyatukan semuanya di satu dashboard:', '✓ Tulis & kirim rilis pers', '✓ Penempatan media terjamin per rilis (jumlah sesuai paket)', '✓ Backlink + dibagikan di kanal sosial VRITIMES', '✓ Laporan pasca-distribusi', '', 'Detail paket & harga terbaru: link di bio.'],
  ig_cta='Cek paket terbaru di link bio.',
  li_hook='Banyak tim marketing masih menyebar rilis lewat spreadsheet kontak, email satu per satu, dan tangkapan layar sebagai laporan.\nAda cara yang lebih rapi.',
  li_body=['VRITIMES dibuat untuk startup dan UMKM yang ingin rilis persnya tayang tanpa harus membangun database media sendiri.', 'Alurnya ada dalam satu dashboard:'],
  li_points=['Tulis dan unggah rilis pers.', 'Distribusi dengan penempatan media terjamin per rilis (jumlah media mengikuti paket yang dipilih).', 'Backlink ke situs Anda dan berbagi ke kanal sosial VRITIMES.', 'Laporan pasca-distribusi yang siap diteruskan ke atasan atau klien.'],
  li_close='Paket dan harga terbaru selalu ada di halaman resmi kami.',
  fb='Rilis pers tanpa ribet: tulis, sebar, dan lihat hasilnya dalam satu dashboard. Cek paketnya di sini 👇')),

# 7 ─────────────────────────────────────────────── W3 Mon EDU carousel (shared S6)
dict(slot='W3Mon', pillar='EDU', format='carousel', slug='backlink-seo-rilis-pers',
 title='Rilis pers untuk SEO? Baca kebijakan Google dulu', cta='Simpan & kirim ke tim SEO', src=['GG1', 'GG2'], tags=['#SEO', '#DigitalPR'],
 slides=[
  dict(t='cover', tag='seo x pr', title='rilis pers untuk SEO? *baca ini dulu*', sub='kata google sendiri'),
  dict(t='quote', text='Google menyebut tautan dengan *anchor text yang dioptimasi* di rilis pers yang disebar ke situs lain sebagai *link spam*.', size=74, by='— Google Search Central, kebijakan spam', src='Google Search Central, Spam policies'),
  dict(t='compare', title='yang *berisiko* vs yang *aman*', left=dict(h='berisiko', items=['Anchor "jasa SEO murah Jakarta" di tiap paragraf', 'Rilis tanpa berita, hanya demi link', 'Belasan link dalam satu rilis']),
       right=dict(h='aman', items=['Nama brand atau URL sebagai tautan', 'Berita yang memancing liputan lanjutan', '1–2 link ke halaman yang relevan']), src='Google Search Central, Spam policies'),
  dict(t='point', icon='link', title='lalu apa *nilai* backlink rilis?', body='Tiga hal nyata: **trafik rujukan** dari pembaca, **penyebutan brand** di situs berita yang membantu orang mengenali Anda, dan **liputan lanjutan** dari jurnalis yang menemukan rilis Anda.'),
  dict(t='point', icon='shield', title='rel="sponsored" itu *normal*', body='Google meminta tautan berbayar atau penempatan ditandai **rel="sponsored"** atau **nofollow**. Jadi ukur rilis dari siapa yang membaca dan siapa yang ikut menulis, bukan dari "link juice".', src='Google Search Central, Qualify outbound links'),
  dict(t='list', title='checklist rilis *aman SEO*', items=['Kata kunci muncul alami di judul, tidak dijejalkan', 'Satu link utama ke halaman yang relevan', 'Anchor = nama brand atau URL', 'Ada data/kutipan yang layak dikutip media lain', 'Pantau penyebutan brand, bukan cuma jumlah link']),
  dict(t='cta', title='PR yang bagus *membantu* SEO. bukan sebaliknya.', items=['Simpan checklist ini', 'Kirim ke tim SEO kamu'], sources=['Google Search Central — Spam policies', 'Google Search Central — Qualify outbound links']),
 ],
 cap=dict(
  hook='Kirim rilis pers biar dapat backlink? Google punya aturan soal ini. 🔗',
  lines=['Google menyebut anchor text yang dioptimasi di rilis pers yang disebar ke situs lain sebagai link spam.', '', 'Yang aman:', '✓ Anchor = nama brand / URL', '✓ 1–2 link ke halaman relevan', '✓ Berita yang memancing liputan lanjutan', '', 'Nilai sebenarnya: trafik rujukan, penyebutan brand, dan liputan organik.'],
  li_hook='"Kirim rilis pers biar dapat backlink" adalah strategi yang Google sebut secara spesifik di kebijakan spamnya.\nBerikut cara memakai rilis pers untuk SEO tanpa risiko.',
  li_body=['Di dokumentasi Spam policies, Google Search Central memasukkan tautan dengan anchor text yang dioptimasi di artikel, guest post, atau rilis pers yang disebar ke situs lain sebagai contoh link spam. Google juga meminta tautan berbayar atau penempatan ditandai rel="sponsored" atau nofollow.', 'Apakah rilis pers lalu tidak berguna untuk SEO? Justru sebaliknya, asal ukurannya tepat:'],
  li_points=['Trafik rujukan dari pembaca yang mengklik.', 'Penyebutan brand di situs berita yang memperkuat pengenalan entitas Anda.', 'Liputan organik dari jurnalis yang menemukan rilis dan menulis versinya sendiri. Di sinilah nilai SEO terbesar.', 'Praktik aman: anchor berupa nama brand/URL, satu link utama, dan berita yang benar-benar layak dikutip.'],
  li_close='Bagaimana tim Anda mengukur dampak rilis terhadap SEO saat ini?',
  fb='Banyak yang kirim rilis pers demi backlink. Sebelum lanjut, cek dulu apa kata Google soal ini 👇')),

# 8 ─────────────────────────────────────────────── W3 Wed VIRAL reel (local)
dict(slot='W3Wed', pillar='VIRAL', format='reel', slug='rating-cara-umkm-masuk-media',
 title='Rating cara UMKM masuk media', cta='Komentar: kamu pernah coba yang mana?', src=['SERVICE'], tags=['#UMKM', '#PRlife'],
 slides=[dict(t='cover', tag='rating', title='rating cara UMKM *masuk media*', sub='jujur aja')],
 reel=dict(frames=[
   dict(top='rating', text='cara UMKM *masuk media*', sub='jujur aja ya', dur=2.5, theme='blue'),
   dict(text='DM akun berita:\n"Kak, bisa diliput?"', sub='2/10 — sering cuma di-read', dur=3.5, theme='pale'),
   dict(text='kirim ke 300 email sekaligus, *CC terbuka*', sub='0/10 — please jangan', dur=3.5, theme='navy'),
   dict(text='nunggu viral dulu, *baru* cari media', sub='4/10 — viral nggak bisa dijadwalkan', dur=3.5, theme='blue'),
   dict(text='rilis yang ada *beritanya* + pitch ke jurnalis yang relevan', sub='9/10 — kerja, butuh konsistensi', dur=4.0, theme='pale'),
   dict(text='rilis + distribusi + laporan *di satu tempat*', sub='10/10 — ini sih kami 😉', dur=3.0, theme='navy'),
  ],
  vo=['Rating cara UMKM masuk media. Jujur aja ya.', 'DM akun berita, kak bisa diliput? Dua dari sepuluh.', 'Kirim ke tiga ratus email, CC terbuka. Nol.', 'Nunggu viral dulu baru cari media. Empat.', 'Rilis yang ada beritanya plus pitch yang relevan. Sembilan.', 'Rilis, distribusi, laporan di satu tempat. Sepuluh.'],
  broll=['Talent internal memegang kartu skor (props kertas biru/lime)', 'Screen mock DM (tanpa akun asli)', 'Mock inbox dengan CC panjang (nama fiktif/blur)', 'Dashboard VRITIMES (screen recording akun demo)'],
  audio='Trending "rating/ranking" beat atau drum roll dari pustaka audio berlisensi platform'),
 cap=dict(
  hook='Rating cara UMKM supaya masuk media (jujur, no offense 😅)',
  lines=['DM akun berita → 2/10', 'Email massal, CC terbuka → 0/10', 'Nunggu viral dulu → 4/10', 'Rilis berisi berita + pitch relevan → 9/10', 'Rilis + distribusi + laporan di satu tempat → 10/10', '', 'Kamu pernah coba yang mana? Komentar di bawah 👇'],
  ig_cta='Tag teman yang masih CC-in 300 email 😆 Link di bio.',
  li_hook='Kami me-rating cara yang paling sering dicoba UMKM untuk masuk media.\nVersi serius dari video ringan ini ada di bawah.',
  li_body=['Polanya konsisten: yang berhasil bukan yang paling ramai dikirim, tetapi yang paling jelas beritanya dan paling tepat sasarannya.'],
  li_points=['DM ke akun berita jarang berhasil karena tidak sampai ke meja redaksi yang tepat.', 'Email massal dengan CC terbuka merusak kepercayaan sekaligus melanggar privasi kontak.', 'Menunggu viral berarti menyerahkan narasi ke algoritma.', 'Rilis yang memuat berita nyata, ditambah pitch ke jurnalis di rubrik yang relevan, adalah cara yang bisa diulang.', 'Distribusi dengan laporan membuat hasilnya bisa diukur dan dievaluasi.'],
  li_close='Cara apa yang paling efektif menurut pengalaman Anda?',
  fb='Kami rating cara-cara UMKM supaya masuk media. Kamu tim yang mana? 😄')),

# 9 ─────────────────────────────────────────────── W3 Fri EDU carousel (local)
dict(slot='W3Fri', pillar='EDU', format='carousel', slug='kapan-tidak-perlu-rilis-pers',
 title='5 kali kamu tidak perlu kirim rilis pers', cta='Simpan untuk rapat konten berikutnya', src=['GG1', 'CI'], tags=['#StrategiPR', '#TipsPR'],
 slides=[
  dict(t='cover', tag='pr jujur', title='5 kali kamu *tidak perlu* kirim rilis pers', sub='hemat budget, jaga reputasi', icons=['clock','shield','mail']),
  dict(t='point', n='01', title='tidak ada yang *baru* bagi pembaca', body='"Kami ulang tahun ke-3" bukan berita, kecuali ada angka, pencapaian, atau rencana yang berdampak. Tes cepat: apakah orang di luar kantor Anda peduli?'),
  dict(t='point', n='02', title='faktanya *belum final*', body='Kerja sama yang "sedang dijajaki" bisa jadi bumerang bila batal. Tunggu tanda tangan, baru umumkan.'),
  dict(t='point', n='03', title='hanya demi *dapat link*', body='Google menyebut anchor text yang dioptimasi di rilis pers sebagai link spam. Rilis tanpa berita yang dibuat demi tautan justru berisiko.', src='Google Search Central, Spam policies'),
  dict(t='point', n='04', title='krisis yang *belum dipahami*', body='Saat krisis, pernyataan singkat yang jujur lebih aman daripada rilis panjang yang spekulatif.', ex='Yang kami tahu: … · Yang kami lakukan: … · Update berikutnya: pukul …'),
  dict(t='point', n='05', title='momennya *sudah lewat*', body='Rilis promo 12.12 yang terbit setelah 12.12 hanya jadi arsip. Redaksi butuh waktu: kirim beberapa hari sebelum momen.'),
  dict(t='list', title='kapan *wajib* kirim rilis', items=['!Peluncuran produk/layanan dengan tanggal pasti', '!Pendanaan, akuisisi, kemitraan resmi', '!Data atau riset orisinal', '!Pencapaian terukur (angka, bukan klaim)', '!Event dengan nilai berita untuk publik']),
  dict(t='cta', title='rilis yang *lebih sedikit* tapi lebih kuat', items=['Simpan untuk rapat konten', 'Kirim ke atasan yang minta rilis tiap minggu 😅'], sources=['Google Search Central — Spam policies', 'Cision, State of the Media 2025']),
 ],
 cap=dict(
  hook='Tidak semua hal perlu dijadikan rilis pers. Ini 5 tandanya. 🛑',
  lines=['01 Tidak ada yang baru bagi pembaca', '02 Faktanya belum final', '03 Hanya demi dapat link', '04 Krisis yang belum dipahami', '05 Momennya sudah lewat', '', 'Kapan wajib? Peluncuran, pendanaan/kemitraan, data orisinal, pencapaian terukur, event bernilai berita.'],
  li_hook='Rilis pers yang terlalu sering justru menurunkan peluang rilis penting Anda dibaca.\nLima situasi ketika sebaiknya Anda tidak mengirimnya.',
  li_body=['Jurnalis masih mengandalkan rilis. Cision (2025) mencatat 72% jurnalis menyebutnya sumber paling berguna dari tim PR. Justru karena itu, reputasi pengirim penting: rilis yang tidak berisi berita membuat rilis berikutnya lebih mudah diabaikan.'],
  li_points=['Tidak ada informasi baru bagi pembaca di luar perusahaan.', 'Faktanya belum final, misalnya kerja sama yang masih dijajaki.', 'Tujuannya hanya backlink. Google menyebut anchor text yang dioptimasi di rilis pers sebagai link spam.', 'Krisis yang belum dipahami. Gunakan pernyataan singkat: apa yang diketahui, apa yang dilakukan, kapan update berikutnya.', 'Momennya sudah lewat.'],
  li_close='Sebaliknya, kirim rilis untuk peluncuran, pendanaan, data orisinal, pencapaian terukur, dan event. Anda setuju?',
  fb='Sebelum minta tim bikin rilis lagi minggu ini, cek dulu 5 situasi ini 😄')),

# 10 ─────────────────────────────────────────────── W4 Mon EDU carousel (local)
dict(slot='W4Mon', pillar='EDU', format='carousel', slug='kalender-pr-2027',
 title='Kalender PR 2027: momen yang bisa disiapkan dari sekarang', cta='Simpan untuk rencana 2027', src=['ID2'], tags=['#KalenderPR', '#Planning2027'],
 src_note='Tanggal libur keagamaan 2027 bersifat perkiraan; ikuti SKB 3 Menteri / ketetapan pemerintah.',
 slides=[
  dict(t='cover', tag='planning 2027', title='kalender PR 2027: siapkan *dari sekarang*', sub='simpan buat rapat tahunan', icons=['cal','chart','mega']),
  dict(t='point', icon='cal', title='kenapa *kalender*, bukan reaktif?', body='Rilis yang reaktif hampir selalu kalah cepat. Dengan kalender, data, foto, dan narasumber sudah siap **sebelum** jurnalis mencarinya.'),
  dict(t='list', title='Q1 · jan–mar', items=['9 Feb — Hari Pers Nasional: angkat topik literasi media/brand', 'Ramadan & Lebaran (perkiraan Feb–Mar 2027): siapkan rilis jauh hari', 'Laporan tahunan & target 2027: rilis pencapaian 2026']),
  dict(t='list', title='Q2 · apr–jun', items=['21 Apr — Hari Kartini: cerita founder & pemimpin perempuan', 'Paruh tahun: rilis data pelanggan/riset internal', 'Musim rekrutmen & ekspansi cabang']),
  dict(t='list', title='Q3 · jul–sep', items=['17 Agustus: program komunitas, bukan sekadar diskon', 'Kuartal III: pengumuman kemitraan & pendanaan', 'Persiapan event akhir tahun']),
  dict(t='list', title='Q4 · okt–des', items=['2 Okt — Hari Batik: kolaborasi produk lokal', '11.11 & Harbolnas 12.12: rilis promo sebelum puncak belanja', 'Rekap tahunan & proyeksi 2028']),
  dict(t='point', title='aturan *H-14 sampai H+3*', body='Jadwal kerja untuk tiap momen:', exlab='timeline',
       ex='H-14 riset & data · H-7 rilis final + foto · H-3 pitch ke jurnalis · Hari H publikasi & sebar · H+3 rekap liputan'),
  dict(t='stat', big='Rp36,4 T', bsize=190, label='transaksi Harbolnas 2025 (dilaporkan)', body='Momen besar = persaingan perhatian besar. Yang menyiapkan rilis lebih awal punya ruang di media.', src='ANTARA (2025)'),
  dict(t='cta', title='rencanakan PR 2027 *sekarang*', items=['Simpan kalender ini', 'Tandai 3 momen untuk brand Anda', 'Kirim ke tim marketing'], sources=['ANTARA, Harbolnas 2025']),
 ],
 cap=dict(
  hook='Kalender PR 2027 sudah bisa disiapkan dari sekarang. 🗓️',
  lines=['Q1: Hari Pers Nasional (9 Feb), Ramadan & Lebaran', 'Q2: Hari Kartini (21 Apr), data paruh tahun', 'Q3: 17 Agustus, kemitraan & pendanaan', 'Q4: Hari Batik (2 Okt), 11.11, Harbolnas 12.12', '', 'Aturan kerja: H-14 riset → H-7 rilis final → H-3 pitch → Hari H → H+3 rekap.'],
  li_hook='Brand yang muncul di media saat momen besar biasanya sudah menyiapkan rilisnya beberapa minggu sebelumnya.\nIni kerangka kalender PR 2027 untuk pasar Indonesia.',
  li_body=['Ambil contoh Harbolnas: transaksinya dilaporkan mencapai Rp36,4 triliun pada 2025 (ANTARA). Di momen sebesar itu, ruang di media diperebutkan, dan yang menang adalah yang paling siap.', 'Kerangka per kuartal yang bisa Anda sesuaikan:'],
  li_points=['Q1: Hari Pers Nasional (9 Februari), Ramadan dan Lebaran (tanggal 2027 masih perkiraan), serta rilis pencapaian tahunan.', 'Q2: Hari Kartini (21 April), data paruh tahun, ekspansi dan rekrutmen.', 'Q3: 17 Agustus dengan program komunitas, plus pengumuman kemitraan dan pendanaan.', 'Q4: Hari Batik (2 Oktober), 11.11, dan Harbolnas 12.12. Kirim rilis sebelum puncak belanja.', 'Untuk tiap momen: H-14 riset, H-7 rilis final, H-3 pitch, Hari H publikasi, H+3 rekap.'],
  li_close='Momen apa yang paling penting untuk brand Anda tahun depan?',
  fb='Sudah mulai susun rencana 2027? Ini kerangka kalender PR per kuartal yang bisa langsung kamu sesuaikan 👇')),

# 11 ─────────────────────────────────────────────── W4 Wed FUN reel (local)
dict(slot='W4Wed', pillar='FUN', format='reel', slug='dari-mana-orang-indonesia-dapat-berita',
 title='Dari mana orang Indonesia dapat berita?', cta='Share ke tim social media', src=['DNR'], tags=['#MediaIndonesia', '#FunFact'],
 slides=[dict(t='cover', tag='fun fact', title='dari mana orang Indonesia *dapat berita*?')],
 reel=dict(frames=[
   dict(top='fun fact', text='dari mana orang Indonesia *dapat berita*?', icon='news', dur=3.0, theme='blue'),
   dict(text='*57%* dari media sosial & aplikasi chat', sub='WhatsApp, YouTube, Facebook, Instagram', src='Reuters Institute, Digital News Report 2025', dur=3.5, theme='pale'),
   dict(text='*34%* pakai TikTok untuk berita', src='Reuters Institute, Digital News Report 2025', dur=3.0, theme='navy'),
   dict(text='tapi hanya *36%* percaya sebagian besar berita', src='Reuters Institute, Digital News Report 2025', dur=3.5, theme='blue'),
   dict(text='artinya: rilis perlu *dimuat media* & *dibagikan di sosial*', dur=4.0, theme='pale'),
   dict(text='kredibel di media, *terlihat* di feed', sub='Raise It With Press Release', dur=3.0, theme='navy'),
  ],
  vo=['Dari mana orang Indonesia dapat berita?', 'Lima puluh tujuh persen dari media sosial dan aplikasi chat.', 'Tiga puluh empat persen pakai TikTok untuk berita.', 'Tapi hanya tiga puluh enam persen yang percaya sebagian besar berita.', 'Jadi rilis kamu perlu dimuat media dan dibagikan di sosial.', 'Kredibel di media, terlihat di feed.'],
  broll=['Scroll feed ponsel (mock UI, tanpa akun asli)', 'Grafik batang animasi 57% / 34% / 36% (dari kartu teks)', 'Tangan memegang koran + ponsel (talent internal)'],
  audio='Upbeat "fact reveal" / ticking beat dari pustaka audio berlisensi platform'),
 cap=dict(
  hook='57% orang Indonesia dapat berita dari media sosial & aplikasi chat. 📱',
  lines=['Data Reuters Institute Digital News Report 2025:', '• 57% dari platform sosial (WhatsApp, YouTube, Facebook, Instagram)', '• 34% pakai TikTok untuk berita', '• Hanya 36% percaya sebagian besar berita', '', 'Pelajarannya: kredibilitas datang dari media, jangkauan datang dari sosial. Butuh dua-duanya.'],
  li_hook='Menurut Reuters Institute (2025), 57% responden Indonesia mendapat berita dari platform sosial, tetapi hanya 36% yang percaya sebagian besar berita.\nApa artinya untuk strategi komunikasi brand?',
  li_body=['Dua angka itu terlihat bertentangan, padahal saling melengkapi. Audiens menemukan berita di feed, tetapi menimbang kredibilitasnya dari sumber.', 'Bagi brand, implikasinya praktis:'],
  li_points=['Rilis yang dimuat media memberi sumber yang bisa dirujuk dan diverifikasi.', 'Liputan itu perlu dibagikan ulang di kanal sosial, termasuk format video pendek (TikTok dipakai 34% responden untuk berita).', 'Pesan harus konsisten di media dan di sosial agar tidak menimbulkan keraguan.'],
  li_close='Bagaimana tim Anda membagikan liputan media di kanal sosial?',
  fb='Fun fact: 57% orang Indonesia mendapat berita dari media sosial. Tapi tingkat kepercayaannya? Tonton sampai habis 👀')),

# 12 ─────────────────────────────────────────────── W4 Fri PROMO single offer-led (local)
dict(slot='W4Fri', pillar='PROMO', format='single', slug='umumkan-promo-sebelum-harbolnas',
 title='Umumkan promo 12.12 sebelum 12.12', cta='Cek harga terbaru di link', src=['PRICE', 'ID2'], tags=['#Harbolnas', '#UMKM'],
 slides=[dict(t='promo', tag='jelang 12.12', title='umumkan promo 12.12 *sebelum* 12.12',
   items=['Rilis tayang di media sebelum puncak belanja', 'Backlink ke halaman promo atau toko Anda', 'Laporan distribusi untuk evaluasi kampanye'],
   price='harga mulai dari — cek link', src=SRC_PRICE, ribbon=True)],
 cap=dict(
  hook='Harbolnas tinggal hitungan hari. Rilis promo kamu sudah siap? 🛒',
  lines=['Harbolnas 2025 dilaporkan mencatat transaksi Rp36,4 triliun (ANTARA).', 'Di momen sebesar itu, yang muncul duluan di media yang dilirik.', '', 'Dengan VRITIMES:', '✓ Rilis tayang sebelum puncak belanja', '✓ Backlink ke halaman promo/toko', '✓ Laporan distribusi untuk evaluasi', '', 'Harga & paket terbaru di link bio.'],
  ig_cta='Cek harga & paket terbaru di link bio.',
  li_hook='Rilis promo akhir tahun yang terbit setelah puncak belanja hampir tidak punya nilai berita.\nWaktunya adalah sekarang.',
  li_body=['Harbolnas 2025 dilaporkan mencatat transaksi Rp36,4 triliun (ANTARA). Persaingan perhatian di media pada pekan itu sangat ketat. Rilis yang terbit beberapa hari sebelumnya punya peluang lebih besar dikutip dan dibagikan.', 'Yang bisa Anda lakukan minggu ini lewat VRITIMES:'],
  li_points=['Distribusikan rilis promo atau program 12.12 dengan penempatan media terjamin (jumlah sesuai paket).', 'Arahkan backlink ke halaman promo atau toko online Anda.', 'Gunakan laporan distribusi untuk evaluasi kampanye akhir tahun.'],
  li_close='Detail paket dan harga terbaru ada di halaman resmi kami.',
  fb='Jangan sampai rilis promo 12.12 kamu terbit setelah 12.12 😅 Cek paket VRITIMES di sini 👇')),
]

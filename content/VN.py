LANG = 'vn'
CC = 'VN'
TAGS = ['#thongcaobaochi', '#PR', '#doanhnghiepnhovavua', '#truyenthong', '#marketing']
def times(pillar):
    return {'linkedin': '08:30 (GMT+7)', 'instagram_facebook': '11:30 (GMT+7)' if pillar in ('EDU', 'PROMO') else '20:00 (GMT+7)'}
SRC_PRICE = 'vritimes.com/vn/service/pricing'

POSTS = [
# 1 ── W1 Mon EDU (S1)
dict(slot='W1Mon', pillar='EDU', format='carousel', slug='giai-phau-thong-cao-bao-chi',
 title='Giải phẫu một thông cáo báo chí được biên tập viên đăng', cta='Lưu lại làm checklist trước khi gửi', src=['CI'], tags=['#thongcaobaochi', '#PRtips'],
 slides=[
  dict(t='cover', tag='thông cáo 101', title='thông cáo báo chí mà *biên tập viên* muốn đăng', sub='chứ không phải bỏ qua'),
  dict(t='point', n='01', title='tiêu đề là *tin tức*, không phải khẩu hiệu', body='Chủ thể + hành động + tác động. Khoảng 10–14 chữ, có con số hoặc địa danh càng tốt.',
       ex='✕ "Đổi mới không giới hạn vì cộng đồng"\n✓ "Startup logistics mở 5 kho tại miền Trung, rút thời gian giao hàng còn 1 ngày"'),
  dict(t='point', n='02', title='đoạn mở đầu trả lời 5W1H trong *hai câu*', body='Biên tập viên quyết định trong vài giây. Nếu đoạn đầu chưa nói rõ **cái gì, ai, khi nào, ở đâu và vì sao là lúc này**, họ sẽ dừng đọc ở đó.'),
  dict(t='point', n='03', title='một trích dẫn *có quan điểm*', body='Trích dẫn không phải chỗ để nói "chúng tôi vô cùng tự hào". Hãy đưa ra góc nhìn, con số hoặc kế hoạch mà báo chí có thể dùng.',
       ex='✕ "Chúng tôi vô cùng tự hào về cột mốc này."\n✓ "Giao hàng trong ngày không nên chỉ dành cho Hà Nội và TP.HCM. Miền Trung là điểm khởi đầu."'),
  dict(t='stat', big='72%', label='nhà báo coi thông cáo báo chí là *nguồn hữu ích nhất* từ đội PR', lsize=56, body='Thông cáo không hề chết. Thứ "chết" là những thông cáo mà toà soạn không thể dùng ngay.', src='Cision, State of the Media 2025'),
  dict(t='list', title='phần thân *dùng được ngay*', items=['Kim tự tháp ngược: thông tin quan trọng nhất lên đầu', 'Số liệu có so sánh (tăng từ bao nhiêu lên bao nhiêu?)', '1–2 ảnh độ phân giải cao kèm chú thích', 'Đầu mối liên hệ báo chí luôn nghe máy']),
  dict(t='point', n='05', title='boilerplate: *3 câu* thường bị xem nhẹ', body='Bạn là ai, thành lập năm nào, quy mô ra sao, ở đâu và đường link chính thức. Viết một lần, cập nhật mỗi quý. Nhà báo thường sao chép nguyên văn.'),
  dict(t='cta', title='kiểm tra 3 điều *trước khi gửi*', items=['Tiêu đề: có chủ thể, hành động và con số?', 'Mở đầu: đủ 5W1H trong hai câu?', 'Trích dẫn: có quan điểm hoặc số liệu?'], sources=['Cision, State of the Media 2025']),
 ],
 cap=dict(
  hook='Thông cáo báo chí của bạn được biên tập viên đọc… hay chỉ mở ra rồi đóng lại? 👀',
  lines=['Biên tập viên quyết định trong vài giây. Đây là cấu trúc của những thông cáo được đăng:', '', '01 Tiêu đề = tin tức (chủ thể + hành động + tác động)', '02 Mở đầu trả lời 5W1H trong hai câu', '03 Một trích dẫn có quan điểm, không phải "vô cùng tự hào"', '04 Thân bài: kim tự tháp ngược, số liệu, ảnh, liên hệ', '05 Boilerplate 3 câu luôn được cập nhật', '', '72% nhà báo vẫn coi thông cáo báo chí là nguồn hữu ích nhất từ đội PR (Cision, 2025).'],
  li_hook='72% nhà báo cho rằng thông cáo báo chí là nguồn hữu ích nhất mà đội PR cung cấp.\nVấn đề không nằm ở định dạng, mà ở chỗ phần lớn thông cáo chưa thể dùng ngay.',
  li_body=['Báo cáo State of the Media 2025 của Cision (khảo sát hơn 3.000 nhà báo tại 19 quốc gia) thường được trích dẫn như bằng chứng "thông cáo vẫn hiệu quả". Điều ít được nhắc tới: nhà báo dùng những thông cáo giúp họ bớt việc, chứ không phải thêm việc.', 'Những thông cáo được đăng thường có chung một cấu trúc:'],
  li_points=['Tiêu đề là tin tức: chủ thể, hành động, tác động, có con số hoặc địa danh.', 'Đoạn mở đầu trả lời 5W1H trong hai câu.', 'Trích dẫn mang quan điểm hoặc số liệu, không phải lời bày tỏ tự hào.', 'Thân bài theo kim tự tháp ngược, có số liệu so sánh, ảnh chất lượng cao và đầu mối liên hệ thực sự phản hồi.', 'Boilerplate ba câu, cập nhật mỗi quý.'],
  li_close='Đội ngũ của bạn hay bỏ sót phần nào nhất: tiêu đề, mở đầu hay trích dẫn? Bản đầy đủ nằm trong file PDF phía trên.',
  fb='Trước khi bấm "gửi", hãy đối chiếu thông cáo báo chí của bạn với 5 phần quyết định việc biên tập viên có đăng hay không 👇')),

# 2 ── W1 Wed FUN (S2)
dict(slot='W1Wed', pillar='FUN', format='carousel', slug='thong-cao-bao-chi-dau-tien-1906',
 title='Thông cáo báo chí đầu tiên ra đời từ một vụ tai nạn tàu hoả', cta='Chia sẻ cho bạn bè làm PR', src=['IL'], tags=['#lichsuPR', '#FunFact'],
 slides=[
  dict(t='cover', tag='fun fact', title='thông cáo báo chí *đầu tiên* ra đời từ một vụ tai nạn tàu hoả', size=118, icons=['train', 'news', 'mega'], art='frames'),
  dict(t='point', icon='train', title='28 tháng 10 *1906*', body='Một đoàn tàu thuộc công ty con của Pennsylvania Railroad lao khỏi cầu ở Atlantic City, Mỹ. Thời đó, các hãng đường sắt thường **ngăn nhà báo tiếp cận** và im lặng về nguyên nhân.', src='Billy Penn (2023); Museum of Public Relations'),
  dict(t='point', icon='mega', title='ivy lee chọn *lên tiếng trước*', body='Chuyên gia quan hệ công chúng Ivy Lee soạn tuyên bố chính thức của công ty, gửi cho phóng viên và đưa họ tới hiện trường.', src='Billy Penn (2023); Museum of Public Relations'),
  dict(t='stat', big='30.10.1906', bsize=150, label='The New York Times đăng *nguyên văn*', body='Tuyên bố này thường được gọi là thông cáo báo chí đầu tiên của ngành PR hiện đại.', src='Billy Penn (2023); Museum of Public Relations'),
  dict(t='list', title='bài học *vẫn đúng* sau 120 năm', items=['!Lên tiếng trước, trước khi người khác kể câu chuyện thay bạn', '!Sự thật mạnh hơn lời khẳng định', '!Giúp nhà báo làm việc dễ hơn: tiếp cận, số liệu, nguồn tin']),
  dict(t='cta', title='sinh ra từ *khủng hoảng*. giờ dùng để *phát triển*.', items=['Lưu lại làm tài liệu đào tạo', 'Tag đồng nghiệp mê lịch sử PR'], sources=['Billy Penn, 2023', 'Museum of Public Relations']),
 ],
 cap=dict(
  hook='Thông cáo báo chí đầu tiên trên thế giới ra đời từ… một vụ tai nạn tàu hoả. 🚆',
  lines=['28/10/1906, Atlantic City (Mỹ).', 'Các hãng đường sắt khi đó thường im lặng và đuổi phóng viên đi.', '', 'Ivy Lee lại soạn tuyên bố chính thức và gửi cho báo chí.', 'The New York Times đăng nguyên văn vào ngày 30/10/1906.', '', 'Bài học vẫn đúng: lên tiếng trước, dùng sự thật, giúp nhà báo làm việc dễ hơn.'],
  li_hook='Bản thông cáo thường được gọi là đầu tiên trong lịch sử không công bố sản phẩm mới. Nó ra đời từ một cuộc khủng hoảng.\nVà bài học vẫn áp dụng được cho doanh nghiệp hôm nay.',
  li_body=['Tháng 10/1906, một đoàn tàu của công ty con thuộc Pennsylvania Railroad lao khỏi cầu ở Atlantic City. Thông lệ của ngành lúc đó là hạn chế tiếp cận và không bình luận.', 'Ivy Lee làm điều ngược lại. Ông soạn tuyên bố chính thức, chia sẻ với phóng viên và cho họ tới hiện trường. The New York Times đăng nguyên văn tuyên bố vào ngày 30/10/1906.', 'Ba nguyên tắc từ sự kiện đó vẫn hiệu quả đến nay:'],
  li_points=['Ai lên tiếng trước bằng sự thật, người đó định hình câu chuyện.', 'Một tuyên bố có thể trích dẫn nguyên văn được dùng nhiều hơn một lời khẳng định.', 'Sự thuận tiện cho nhà báo là một phần chiến lược, không phải phần thưởng thêm.'],
  li_close='Theo bạn, thương hiệu hay vi phạm nguyên tắc nào nhất khi gặp khủng hoảng?',
  fb='Một sự thật thú vị cho dân marketing và PR: thông cáo báo chí đầu tiên xuất hiện năm 1906, sau một vụ tai nạn tàu hoả. Câu chuyện có trong carousel này 👇')),

# 3 ── W1 Fri VIRAL reel (S3)
dict(slot='W1Fri', pillar='VIRAL', format='reel', slug='pov-gui-thong-cao-file-pdf',
 title='POV: bạn gửi thông cáo báo chí bằng file PDF đính kèm', cta='Gửi cho team vẫn còn dùng PDF', src=['MR'], tags=['#doiPR', '#thongcaobaochi'],
 slides=[dict(t='cover', tag='POV', title='bạn gửi thông cáo báo chí bằng *file PDF đính kèm*')],
 reel=dict(frames=[
   dict(top='POV', text='bạn gửi thông cáo bằng *file PDF đính kèm*', icon='pdf', dur=3.0, theme='blue'),
   dict(text='tiêu đề email:\n*"Thông cáo báo chí"*', sub='…cùng hàng trăm email khác hôm nay', dur=3.0, theme='pale'),
   dict(text='nhà báo phải tải về, mở ra rồi *tự copy*', sub='(nếu họ có thời gian)', dur=3.5, theme='navy'),
   dict(text='trong khi *69%* nhà báo thích pitch dưới 200 từ', src='Muck Rack, State of Journalism 2025', dur=3.5, theme='blue'),
   dict(text='đúng ra: *nội dung trong thân email*, tiêu đề thông cáo làm subject, ảnh gửi qua link', dur=4.0, theme='pale'),
   dict(text='để thông cáo gặp *báo chí*, không phải *thư mục lưu trữ*', sub='Raise It With Press Release', dur=3.0, theme='navy'),
  ],
  vo=['POV: bạn gửi thông cáo báo chí bằng file PDF đính kèm.', 'Tiêu đề email chỉ ghi "Thông cáo báo chí".', 'Nhà báo phải tải về, mở ra rồi tự copy.', 'Trong khi sáu mươi chín phần trăm nhà báo thích pitch dưới hai trăm từ.', 'Hãy dán nội dung vào thân email, dùng tiêu đề thông cáo làm subject, gửi ảnh qua link.', 'Để thông cáo gặp báo chí, không phải thư mục lưu trữ.'],
  broll=['Hộp thư đầy email (mô phỏng, không có tên thật)', 'Nhấp vào file PDF, tải chậm (quay màn hình mô phỏng)', 'Biểu cảm "hmm" của thành viên VRITIMES (diễn viên nội bộ)', 'Mẫu email đúng trên màn hình (template nội bộ)'],
  audio='Âm thanh hài kiểu "awkward pause" hoặc lo-fi vui tươi từ thư viện âm thanh có bản quyền của nền tảng'),
 cap=dict(
  hook='POV: bạn gửi thông cáo báo chí bằng file PDF đính kèm 📎😶',
  lines=['Tải về → mở ra → copy. Mỗi bước thừa là một cơ hội bị mất.', '69% nhà báo thích pitch dưới 200 từ (Muck Rack, 2025).', '', 'Thay vào đó:', '✓ Dán nội dung thông cáo vào thân email', '✓ Tiêu đề thông cáo = tiêu đề email', '✓ Ảnh và tài liệu gửi qua link'],
  li_hook='Một thói quen nhỏ khiến thông cáo hay không được đọc: gửi dưới dạng file PDF đính kèm.\nNghe có vẻ không đáng kể. Tác động thì có.',
  li_body=['Muck Rack (State of Journalism 2025) cho thấy 69% nhà báo thích pitch dưới 200 từ. Họ muốn quyết định nhanh, không thêm bước nào.', 'File PDF đính kèm thêm tới ba bước: tải về, mở, sao chép. Cộng với tiêu đề email chung chung, khả năng được đọc giảm rõ rệt.'],
  li_points=['Dán nội dung thông cáo trực tiếp vào thân email.', 'Dùng tiêu đề thông cáo làm tiêu đề email.', 'Chia sẻ ảnh và tài liệu kèm theo qua link.', 'Nếu dùng nền tảng phân phối, hãy đảm bảo thông cáo nằm trên một trang web có thể truy cập và trích dẫn.'],
  li_close='Doanh nghiệp của bạn có còn yêu cầu gửi PDF vì "trông trang trọng hơn" không?',
  fb='Ai còn gửi thông cáo báo chí bằng file PDF đính kèm không? 😅 Xem hết video nhé, có cách nhà báo thích hơn nhiều.')),

# 4 ── W2 Mon EDU (S4)
dict(slot='W2Mon', pillar='EDU', format='carousel', slug='email-pitch-duoi-200-tu',
 title='Email pitch dưới 200 từ được nhà báo phản hồi', cta='Lưu mẫu email lại', src=['MR'], tags=['#quanhebaochi', '#PRtips'],
 slides=[
  dict(t='cover', tag='pr tips', title='email pitch *dưới 200 từ* được nhà báo trả lời', sub='mẫu ở slide 6'),
  dict(t='stat', big='69%', label='nhà báo thích pitch *dưới 200 từ*', body='Pitch là lời mời đọc, không phải bản thông cáo. Chi tiết đầy đủ để trong link.', src='Muck Rack, State of Journalism 2025'),
  dict(t='list', title='cấu trúc *4 dòng*', items=['Dòng 1 — vì sao phù hợp với chuyên mục hoặc độc giả của họ', 'Dòng 2 — tin chính trong một câu (có con số)', 'Dòng 3 — bạn có thể cung cấp gì: số liệu, người phát ngôn, ảnh', 'Dòng 4 — link thông cáo đầy đủ + liên hệ']),
  dict(t='compare', title='tiêu đề email: *số phận khác nhau*', left=dict(h='bị bỏ qua', items=['"Thông cáo báo chí Công ty ABC"', '"KHẨN!!! Thông tin quan trọng"', '"Hợp tác đặc biệt"']),
       right=dict(h='được mở', items=['"Số liệu: 3/5 quán F&B ở TP.HCM tăng giá quý IV"', '"Người phát ngôn: CFO bàn về chi phí logistics 2027"', '"Embargo 9h ngày 24/11: ra mắt …"'])),
  dict(t='stat', big='1×', label='follow-up, sau *3–7 ngày*', body='50% nhà báo cho rằng follow-up một lần là lý tưởng. 51% muốn cách 3–7 ngày. Nhiều hơn là làm phiền.', src='Muck Rack, State of Journalism 2025'),
  dict(t='point', title='mẫu email *dùng ngay*', body='Thay phần trong ngoặc.', exlab='mẫu', bsize=36,
       ex='Chào anh/chị (tên), tôi vừa đọc bài của anh/chị về (chủ đề) tuần trước.\n(Công ty) vừa (tin chính trong một câu + con số).\nChúng tôi có thể cung cấp (số liệu đầy đủ / phỏng vấn / ảnh) trong tuần này.\nThông cáo & ảnh: (link). Cảm ơn anh/chị — (tên, số điện thoại)'),
  dict(t='cta', title='pitch ngắn, *cơ hội* dài', items=['Lưu mẫu email này', 'Gửi cho người phụ trách quan hệ báo chí', 'Theo dõi để nhận mẹo PR mỗi tuần'], sources=['Muck Rack, State of Journalism 2025']),
 ],
 cap=dict(
  hook='Email pitch của bạn có quá dài không? 69% nhà báo thích dưới 200 từ. ✂️',
  lines=['Cấu trúc 4 dòng:', '1️⃣ Vì sao phù hợp với chuyên mục của họ', '2️⃣ Tin chính trong một câu + con số', '3️⃣ Những gì bạn cung cấp được: số liệu, người phát ngôn, ảnh', '4️⃣ Link thông cáo + liên hệ', '', 'Follow-up? Một lần, sau 3–7 ngày.', 'Mẫu đầy đủ ở slide 6.'],
  li_hook='Những email pitch được nhà báo trả lời thường ngắn hơn bạn nghĩ.\nTheo Muck Rack, 69% nhà báo thích pitch dưới 200 từ.',
  li_body=['Lỗi phổ biến nhất là dán toàn bộ thông cáo vào pitch. Pitch chỉ là lời mời đọc, không phải bản thông cáo.', 'Cùng nghiên cứu State of Journalism 2025 của Muck Rack cũng trả lời câu hỏi về follow-up: 50% nhà báo cho rằng một lần là lý tưởng, và 51% muốn cách 3–7 ngày.', 'Cấu trúc bốn dòng đội ngũ của bạn có thể dùng ngay:'],
  li_points=['Mức độ liên quan: vì sao chủ đề phù hợp với chuyên mục hoặc độc giả.', 'Tin chính trong một câu, kèm con số.', 'Những gì bạn có sẵn: số liệu, người phát ngôn hoặc ảnh.', 'Link thông cáo đầy đủ và đầu mối liên hệ luôn phản hồi.'],
  li_close='Mẫu đầy đủ ở slide 6. Pitch của đội bạn hiện dài khoảng bao nhiêu từ?',
  fb='Mẫu email pitch dưới 200 từ, chỉ 4 dòng, đội ngũ của bạn dùng được ngay 👇')),

# 5 ── W2 Wed FUN single (local)
dict(slot='W2Wed', pillar='FUN', format='single', slug='233-nghin-doanh-nghiep-moi-2024',
 title='Năm 2024 có 233,4 nghìn doanh nghiệp thành lập mới và quay lại hoạt động', cta='Tag một chủ doanh nghiệp có câu chuyện đáng lên báo', src=['VN1', 'VN2'], tags=['#doanhnghiep', '#FunFact'],
 slides=[dict(t='single_stat', tag='fun fact', pre='năm 2024 việt nam có', big='233,4K', bsize=220, tsize=60, lsize=60, label='doanh nghiệp *thành lập mới & quay lại*',
   body='Trong đó **76,2 nghìn** doanh nghiệp quay lại hoạt động, cao nhất từ trước đến nay. Ai cũng cần được biết đến.', sub='có tin vui? viết thông cáo', src='Tổng cục Thống kê (2025)')],
 cap=dict(
  hook='Năm 2024, Việt Nam có 233,4 nghìn doanh nghiệp thành lập mới và quay lại hoạt động. Bao nhiêu trong số đó từng lên báo? 🤔',
  lines=['Theo Tổng cục Thống kê:', '• 233,4 nghìn doanh nghiệp thành lập mới & quay lại hoạt động (+7,1%)', '• 76,2 nghìn doanh nghiệp quay lại hoạt động, cao nhất từ trước đến nay', '• Bình quân 13,1 nghìn doanh nghiệp mới mỗi tháng', '', 'Mở chi nhánh, đơn hàng xuất khẩu đầu tiên, tuyển 50 nhân sự: đều là tin tức.', 'Chỉ là hiếm khi được viết theo cách toà soạn dùng được.'],
  li_hook='Năm 2024, Việt Nam có 233,4 nghìn doanh nghiệp thành lập mới và quay lại hoạt động, trong đó 76,2 nghìn doanh nghiệp quay lại, mức cao nhất từ trước đến nay.\nPhần lớn trong số họ chưa từng xuất hiện trên báo.',
  li_body=['Với khoảng 97% doanh nghiệp là doanh nghiệp nhỏ và vừa (theo Bộ KH&ĐT, VCCI dẫn), cạnh tranh để được chú ý ngày càng gay gắt. Số liệu của Tổng cục Thống kê thường được đọc dưới góc độ kinh tế. Chúng tôi nhìn thấy một khoảng trống truyền thông.', 'Không phải vì thiếu giá trị tin tức, mà vì chưa được kể dưới dạng tin tức. Một chi nhánh mới, hợp đồng xuất khẩu đầu tiên hay đợt tuyển dụng lớn đều là tin địa phương tốt khi có số liệu rõ ràng và người phát ngôn có thể trích dẫn.'],
  li_close='Nếu bạn là chủ doanh nghiệp: câu chuyện nào của năm nay công chúng nên được biết?',
  fb='Sự thật thú vị: năm 2024 có 233,4 nghìn doanh nghiệp thành lập mới và quay lại hoạt động. Nếu doanh nghiệp của bạn là một trong số đó, câu chuyện của bạn xứng đáng được lên báo 💙')),

# 6 ── W2 Fri PROMO feature (S5)
dict(slot='W2Fri', pillar='PROMO', format='single', slug='mot-dashboard-viet-phan-phoi-bao-cao',
 title='Viết, phân phối và xem kết quả trong một dashboard', cta='Xem các gói tại vritimes.com/vn', src=['SERVICE', 'PRICE'], tags=['#thongcaobaochi', '#doanhnghiep'],
 slides=[dict(t='promo', tag='một dashboard', title='viết. *gửi.*\nxem kết quả.',
   items=['Cam kết đăng tải trên báo cho mỗi thông cáo (số lượng theo gói)', 'Backlink + chia sẻ trên kênh mạng xã hội của VRITIMES', 'Báo cáo sau phân phối để gửi sếp hoặc khách hàng'],
   price='giá chỉ từ — xem link', src=SRC_PRICE, ribbon=True)],
 cap=dict(
  hook='Black Friday giảm giá gì cũng được, trừ uy tín thương hiệu. 😉',
  lines=['VRITIMES gom mọi thứ vào một dashboard:', '✓ Viết và gửi thông cáo báo chí', '✓ Cam kết đăng tải trên báo cho mỗi thông cáo (số lượng theo gói)', '✓ Backlink + chia sẻ trên mạng xã hội của VRITIMES', '✓ Báo cáo sau phân phối', '', 'Gói dịch vụ và giá mới nhất: link ở bio.'],
  ig_cta='Xem các gói mới nhất qua link ở bio.',
  li_hook='Nhiều đội marketing vẫn phân phối thông cáo bằng file Excel danh sách báo, gửi email từng người và dùng ảnh chụp màn hình làm báo cáo.\nCó cách gọn gàng hơn.',
  li_body=['VRITIMES được xây dựng cho startup và doanh nghiệp nhỏ và vừa muốn thông cáo được đăng tải mà không phải tự xây dựng cơ sở dữ liệu báo chí.', 'Toàn bộ quy trình nằm trong một dashboard:'],
  li_points=['Viết và tải lên thông cáo báo chí.', 'Phân phối với cam kết đăng tải trên báo cho mỗi thông cáo (số lượng báo theo gói).', 'Backlink về website và chia sẻ trên kênh mạng xã hội của VRITIMES.', 'Báo cáo sau phân phối, sẵn sàng gửi cho quản lý hoặc khách hàng.'],
  li_close='Gói dịch vụ và giá mới nhất luôn có trên trang chính thức của chúng tôi.',
  fb='Gửi thông cáo báo chí không còn rắc rối: viết, phân phối và xem kết quả trong một dashboard. Xem các gói tại đây 👇')),

# 7 ── W3 Mon EDU (S6)
dict(slot='W3Mon', pillar='EDU', format='carousel', slug='backlink-seo-thong-cao-bao-chi',
 title='Dùng thông cáo báo chí để làm SEO? Đọc chính sách của Google trước', cta='Lưu lại và gửi cho team SEO', src=['GG1', 'GG2'], tags=['#SEO', '#DigitalPR'],
 slides=[
  dict(t='cover', tag='seo x pr', title='thông cáo để làm SEO? *đọc cái này trước*', sub='google nói thẳng'),
  dict(t='quote', text='Google xếp các liên kết có *anchor text tối ưu hoá* trong thông cáo báo chí phát tán sang website khác vào nhóm *link spam*.', size=68, by='— Google Search Central, chính sách spam', src='Google Search Central, Spam policies'),
  dict(t='compare', title='*rủi ro* vs *an toàn*', left=dict(h='rủi ro', items=['Anchor "dịch vụ SEO giá rẻ TP.HCM" ở mọi đoạn', 'Thông cáo không có tin, chỉ để lấy link', 'Hàng chục link trong một thông cáo']),
       right=dict(h='an toàn', items=['Tên thương hiệu hoặc URL làm anchor', 'Tin tức khiến báo khác viết tiếp', '1–2 link tới trang liên quan']), src='Google Search Central, Spam policies'),
  dict(t='point', icon='link', title='vậy link từ thông cáo *có giá trị* gì?', body='Ba điều thực tế: **lượt truy cập giới thiệu** từ người đọc, **nhắc đến thương hiệu** trên trang tin giúp mọi người nhận diện bạn, và **bài viết tiếp theo** từ nhà báo tìm thấy thông cáo.'),
  dict(t='point', icon='shield', title='rel="sponsored" là *bình thường*', body='Google yêu cầu link trả phí hoặc đặt bài phải gắn **rel="sponsored"** hoặc **nofollow**. Vì vậy hãy đo thông cáo bằng ai đọc và ai viết tiếp, không phải "link juice".', src='Google Search Central, Qualify outbound links'),
  dict(t='list', title='checklist thông cáo *an toàn SEO*', items=['Từ khoá xuất hiện tự nhiên trong tiêu đề', 'Một link chính tới trang liên quan', 'Anchor = tên thương hiệu hoặc URL', 'Có số liệu hoặc trích dẫn đáng để báo khác dẫn lại', 'Theo dõi lượt nhắc thương hiệu, không chỉ đếm link']),
  dict(t='cta', title='PR tốt *hỗ trợ* SEO. không phải ngược lại.', items=['Lưu checklist này', 'Gửi cho team SEO của bạn'], sources=['Google Search Central — Spam policies', 'Google Search Central — Qualify outbound links']),
 ],
 cap=dict(
  hook='Gửi thông cáo báo chí để lấy backlink? Google có chính sách riêng về việc này. 🔗',
  lines=['Google xếp anchor text tối ưu hoá trong thông cáo phát tán sang website khác vào nhóm link spam.', '', 'Cách an toàn:', '✓ Anchor = tên thương hiệu / URL', '✓ 1–2 link tới trang liên quan', '✓ Tin tức khiến báo khác viết tiếp', '', 'Giá trị thật: lượt truy cập, lượt nhắc thương hiệu và bài viết tự nhiên.'],
  li_hook='"Gửi thông cáo để lấy backlink" là chiến thuật Google nêu đích danh trong chính sách spam.\nĐây là cách dùng thông cáo báo chí cho SEO mà không gặp rủi ro.',
  li_body=['Trong tài liệu Spam policies, Google Search Central liệt kê các liên kết có anchor text tối ưu hoá trong bài viết, guest post hoặc thông cáo báo chí phát tán sang website khác là ví dụ của link spam. Google cũng yêu cầu link trả phí hoặc đặt bài gắn rel="sponsored" hoặc nofollow.', 'Vậy thông cáo vô dụng với SEO? Ngược lại, miễn là bạn đo đúng thứ:'],
  li_points=['Lượt truy cập giới thiệu từ người đọc bấm vào.', 'Lượt nhắc thương hiệu trên trang tin, giúp củng cố nhận diện.', 'Bài viết tự nhiên từ nhà báo tìm thấy thông cáo và viết phiên bản của riêng họ. Đây là giá trị SEO lớn nhất.', 'Thực hành an toàn: anchor là tên thương hiệu/URL, một link chính và tin tức thật sự đáng trích dẫn.'],
  li_close='Đội của bạn hiện đo tác động SEO của thông cáo như thế nào?',
  fb='Nhiều doanh nghiệp gửi thông cáo chỉ để lấy backlink. Trước khi làm tiếp, hãy xem Google nói gì 👇')),

# 8 ── W3 Wed VIRAL reel (local): expectation vs reality
dict(slot='W3Wed', pillar='VIRAL', format='reel', slug='thong-cao-bao-chi-ky-vong-va-thuc-te',
 title='Thông cáo báo chí: kỳ vọng vs thực tế', cta='Bình luận: bạn từng gặp cảnh nào?', src=['MR'], tags=['#doiPR', '#marketing'],
 slides=[dict(t='cover', tag='kỳ vọng vs thực tế', title='thông cáo báo chí: *kỳ vọng* vs *thực tế*')],
 reel=dict(frames=[
   dict(top='kỳ vọng', text='"gửi 1 lần là *lên báo khắp nơi*"', dur=3.0, theme='blue'),
   dict(top='thực tế', text='không có tin thì *không ai đăng*', sub='tin trước, thông cáo sau', dur=3.0, theme='pale'),
   dict(top='kỳ vọng', text='"viết dài cho *chuyên nghiệp*"', dur=2.5, theme='navy'),
   dict(top='thực tế', text='*69%* nhà báo thích pitch dưới 200 từ', src='Muck Rack, State of Journalism 2025', dur=3.5, theme='blue'),
   dict(top='kỳ vọng', text='"nhắn nhà báo *mỗi ngày* cho chắc"', dur=2.5, theme='pale'),
   dict(top='thực tế', text='*50%* nhà báo thấy follow-up một lần là đủ', src='Muck Rack, State of Journalism 2025', dur=3.5, theme='navy'),
   dict(text='kỳ vọng hợp lý + *quy trình đúng* = được đăng', sub='Raise It With Press Release', dur=3.0, theme='blue'),
  ],
  vo=['Kỳ vọng: gửi một lần là lên báo khắp nơi.', 'Thực tế: không có tin thì không ai đăng.', 'Kỳ vọng: viết dài cho chuyên nghiệp.', 'Thực tế: sáu mươi chín phần trăm nhà báo thích pitch dưới hai trăm từ.', 'Kỳ vọng: nhắn nhà báo mỗi ngày cho chắc.', 'Thực tế: một nửa nhà báo thấy follow-up một lần là đủ.', 'Kỳ vọng hợp lý cộng quy trình đúng bằng được đăng.'],
  broll=['Chia đôi màn hình "kỳ vọng / thực tế" với diễn viên nội bộ', 'Màn hình đếm số từ trong email (mô phỏng)', 'Điện thoại với tin nhắn chưa đọc (mô phỏng, không có tên thật)'],
  audio='Âm thanh trend "expectation vs reality" từ thư viện có bản quyền của nền tảng'),
 cap=dict(
  hook='Thông cáo báo chí: kỳ vọng vs thực tế 😅',
  lines=['Kỳ vọng: gửi 1 lần là lên báo khắp nơi', 'Thực tế: không có tin thì không ai đăng', '', 'Kỳ vọng: viết dài cho chuyên nghiệp', 'Thực tế: 69% nhà báo thích pitch dưới 200 từ', '', 'Kỳ vọng: nhắn nhà báo mỗi ngày', 'Thực tế: 50% thấy follow-up một lần là đủ', '', 'Bạn từng gặp cảnh nào? 👇'],
  ig_cta='Tag đồng nghiệp từng "kỳ vọng" như vậy 😆 Link ở bio.',
  li_hook='Ba kỳ vọng phổ biến về thông cáo báo chí, và thực tế theo số liệu.',
  li_body=['Nhiều kỳ vọng về PR đến từ thói quen, không phải dữ liệu. Khi kỳ vọng không khớp thực tế, đội truyền thông thường bị đánh giá là "làm chưa tới", trong khi vấn đề nằm ở cách đặt mục tiêu ngay từ đầu.', 'Muck Rack State of Journalism 2025 cho một bức tranh rõ ràng hơn:'],
  li_points=['Gửi một lần không đảm bảo lên báo khắp nơi. Giá trị tin tức mới là yếu tố quyết định.', 'Dài không đồng nghĩa với chuyên nghiệp: 69% nhà báo thích pitch dưới 200 từ.', 'Nhắn mỗi ngày không tăng cơ hội: 50% nhà báo thấy một lần follow-up là lý tưởng, 51% muốn cách 3–7 ngày.'],
  li_close='Kỳ vọng nào bạn thường phải "điều chỉnh" với sếp hoặc khách hàng?',
  fb='Kỳ vọng vs thực tế khi gửi thông cáo báo chí 😄 Bạn đã từng ở phía "kỳ vọng" chưa?')),

# 9 ── W3 Fri EDU (local): headline formulas
dict(slot='W3Fri', pillar='EDU', format='carousel', slug='cong-thuc-tieu-de-thong-cao',
 title='5 công thức tiêu đề thông cáo báo chí kèm ví dụ', cta='Lưu lại cho lần viết tiếp theo', src=['MR'], tags=['#vietthongcao', '#PRtips'],
 slides=[
  dict(t='cover', tag='pr writing', title='5 công thức *tiêu đề* thông cáo kèm ví dụ', sub='copy được ngay', icons=['news', 'chart', 'mega']),
  dict(t='point', n='01', title='chủ thể + hành động + *con số*', body='Công thức an toàn nhất cho tin doanh nghiệp.', ex='"Chuỗi cà phê X mở 10 cửa hàng tại Đà Nẵng, tạo 150 việc làm"'),
  dict(t='point', n='02', title='số liệu *mới* làm tiêu đề', body='Khi bạn có dữ liệu riêng, hãy để dữ liệu là tin.', ex='"Khảo sát 1.000 chủ shop online: 6/10 dự kiến tăng ngân sách quảng cáo dịp Tết"'),
  dict(t='point', n='03', title='lần *đầu tiên* (có kiểm chứng)', body='Chỉ dùng khi chứng minh được, nhà báo sẽ kiểm tra.', ex='"Doanh nghiệp Cần Thơ đầu tiên xuất khẩu gạo hữu cơ sang Nhật Bản"'),
  dict(t='point', n='04', title='hợp tác: *ai + ai + để làm gì*', body='Tin hợp tác chỉ hấp dẫn khi nói rõ kết quả cho người dùng.', ex='"Ví điện tử Y và chuỗi siêu thị Z cho phép thanh toán bằng QR tại 300 điểm"'),
  dict(t='point', n='05', title='sự kiện: *tên + thời gian + giá trị*', body='Đặt lợi ích cho người tham dự lên trước.', ex='"Hội thảo miễn phí về xuất khẩu nông sản cho 200 doanh nghiệp, TP.HCM ngày 15/1"'),
  dict(t='list', title='tránh *ngay*', items=['~"Đột phá", "hàng đầu", "số 1" không có bằng chứng', '~Tiêu đề không có động từ', '~Viết hoa toàn bộ', '~Dài hơn hai dòng trên điện thoại']),
  dict(t='cta', title='tiêu đề tốt = *nửa chặng đường*', items=['Lưu 5 công thức này', 'Gửi cho người viết thông cáo của bạn'], sources=['Muck Rack, State of Journalism 2025']),
 ],
 cap=dict(
  hook='Tiêu đề quyết định thông cáo của bạn có được mở hay không. Đây là 5 công thức kèm ví dụ ✍️',
  lines=['01 Chủ thể + hành động + con số', '02 Số liệu mới làm tiêu đề', '03 Lần đầu tiên (có kiểm chứng)', '04 Hợp tác: ai + ai + để làm gì', '05 Sự kiện: tên + thời gian + giá trị', '', 'Tránh: "đột phá", "số 1" không bằng chứng, tiêu đề không động từ, viết hoa toàn bộ.'],
  li_hook='Phần lớn thông cáo bị bỏ qua ngay từ tiêu đề.\nNăm công thức chúng tôi khuyên dùng, kèm ví dụ minh hoạ.',
  li_body=['Nhà báo nhận rất nhiều pitch mỗi ngày, và Muck Rack (2025) cho thấy 69% thích pitch dưới 200 từ. Trong bối cảnh đó, tiêu đề phải nói được tin chính trong một lần đọc.', 'Năm công thức (ví dụ chỉ mang tính minh hoạ):'],
  li_points=['Chủ thể + hành động + con số: tin doanh nghiệp rõ ràng nhất.', 'Số liệu mới làm tiêu đề: khi bạn có dữ liệu riêng.', '"Lần đầu tiên": chỉ khi chứng minh được.', 'Hợp tác: nói rõ ai với ai và kết quả cho người dùng.', 'Sự kiện: tên, thời gian và giá trị cho người tham dự.'],
  li_close='Công thức nào đội của bạn dùng nhiều nhất?',
  fb='5 công thức viết tiêu đề thông cáo báo chí, kèm ví dụ dễ áp dụng. Lưu lại nhé 👇')),

# 10 ── W4 Mon EDU (local): PR calendar 2027
dict(slot='W4Mon', pillar='EDU', format='carousel', slug='lich-pr-2027-viet-nam',
 title='Lịch PR 2027 cho thương hiệu Việt', cta='Lưu lại cho kế hoạch 2027', src=['VN3', 'VN1'], tags=['#lichPR', '#kehoach2027'],
 src_note='Ngày Tết Nguyên Đán 2027 là dự kiến; vui lòng đối chiếu thông báo nghỉ Tết chính thức.',
 slides=[
  dict(t='cover', tag='planning 2027', title='lịch PR 2027: *chuẩn bị từ hôm nay*', sub='lưu cho buổi họp kế hoạch', icons=['cal', 'chart', 'mega']),
  dict(t='point', icon='cal', title='vì sao cần *lịch*, không bị động?', body='Thông cáo làm theo kiểu bị động hầu như luôn chậm. Có lịch, số liệu, hình ảnh và người phát ngôn sẵn sàng **trước** khi nhà báo cần.'),
  dict(t='list', title='Q1 · tháng 1–3', items=['Tết Nguyên Đán (dự kiến đầu tháng 2/2027): gửi tin trước kỳ nghỉ dài', 'Tổng kết 2026 & mục tiêu 2027', '8/3: câu chuyện nữ lãnh đạo, nữ founder']),
  dict(t='list', title='Q2 · tháng 4–6', items=['30/4 – 1/5: gửi tin trước kỳ nghỉ', '21/6 Ngày Báo chí Cách mạng Việt Nam: tri ân báo chí đúng cách', 'Số liệu nửa năm từ khách hàng của bạn']),
  dict(t='list', title='Q3 · tháng 7–9', items=['2/9 Quốc khánh: chương trình cộng đồng, không chỉ giảm giá', 'Công bố hợp tác & gọi vốn', 'Chuẩn bị sự kiện cuối năm']),
  dict(t='list', title='Q4 · tháng 10–12', items=['20/10 & 20/11: câu chuyện nhân sự, đào tạo', 'Black Friday & 12.12: gửi thông cáo trước ngày cao điểm', 'Tổng kết năm & triển vọng 2028']),
  dict(t='point', title='quy tắc *T-14 đến T+3*', body='Lịch làm việc cho mỗi dịp:', exlab='timeline', ex='T-14 nghiên cứu & số liệu · T-7 thông cáo hoàn chỉnh + ảnh · T-3 pitch nhà báo · Ngày D đăng & chia sẻ · T+3 tổng hợp bài đăng'),
  dict(t='stat', big='13,1K', bsize=230, label='doanh nghiệp mới mỗi tháng (2024)', body='Mỗi tháng lại có thêm hàng nghìn doanh nghiệp cạnh tranh sự chú ý. Chuẩn bị sớm quyết định ai được đưa tin.', src='Tổng cục Thống kê (2025)'),
  dict(t='cta', title='lên kế hoạch PR 2027 *ngay bây giờ*', items=['Lưu lịch này', 'Đánh dấu 3 dịp cho thương hiệu', 'Gửi cho team marketing'], sources=['Tổng cục Thống kê (2025)', 'VOH — Ngày Báo chí Cách mạng Việt Nam']),
 ],
 cap=dict(
  hook='Lịch PR 2027 có thể bắt đầu từ hôm nay. 🗓️',
  lines=['Q1: Tết Nguyên Đán, tổng kết năm, 8/3', 'Q2: 30/4 – 1/5, 21/6 Ngày Báo chí Cách mạng Việt Nam', 'Q3: 2/9, hợp tác & gọi vốn', 'Q4: 20/10, 20/11, Black Friday, 12.12', '', 'Quy trình: T-14 nghiên cứu → T-7 thông cáo hoàn chỉnh → T-3 pitch → Ngày D → T+3 tổng hợp.'],
  li_hook='Thương hiệu xuất hiện trên báo vào các dịp lớn thường đã chuẩn bị thông cáo từ nhiều tuần trước.\nĐây là khung lịch PR 2027 cho thị trường Việt Nam.',
  li_body=['Năm 2024, trung bình mỗi tháng có 13,1 nghìn doanh nghiệp thành lập mới (Tổng cục Thống kê). Cạnh tranh để được chú ý vào các dịp cao điểm ngày càng lớn, và sự chuẩn bị, chứ không phải số lượng, quyết định ai được đưa tin.', 'Khung theo quý để tham khảo:'],
  li_points=['Q1: Tết Nguyên Đán (ngày 2027 là dự kiến), tổng kết năm và 8/3.', 'Q2: kỳ nghỉ 30/4 – 1/5 và 21/6 Ngày Báo chí Cách mạng Việt Nam.', 'Q3: 2/9 với chương trình cộng đồng, cùng tin hợp tác và gọi vốn.', 'Q4: 20/10, 20/11, Black Friday và 12.12. Gửi thông cáo trước ngày cao điểm.', 'Mỗi dịp: T-14 nghiên cứu, T-7 thông cáo hoàn chỉnh, T-3 pitch, Ngày D đăng, T+3 tổng hợp.'],
  li_close='Dịp nào quan trọng nhất với thương hiệu của bạn năm tới?',
  fb='Bạn đã bắt đầu lên kế hoạch 2027 chưa? Đây là lịch PR theo quý cho thương hiệu Việt 👇')),

# 11 ── W4 Wed FUN reel (local): press day 1925
dict(slot='W4Wed', pillar='FUN', format='reel', slug='bao-thanh-nien-21-6-1925',
 title='Ngày 21/6/1925 và tờ báo cách mạng đầu tiên', cta='Chia sẻ cho người làm truyền thông', src=['VN3'], tags=['#baochi', '#FunFact'],
 slides=[dict(t='cover', tag='fun fact', title='vì sao *21/6* là ngày báo chí việt nam?')],
 reel=dict(frames=[
   dict(top='fun fact', text='vì sao *21/6* là ngày báo chí việt nam?', icon='news', dur=3.0, theme='blue'),
   dict(text='ngày *21/6/1925*, báo Thanh Niên ra số đầu tiên', sub='tại Quảng Châu (Trung Quốc)', src='VOH', dur=3.5, theme='pale'),
   dict(text='do lãnh tụ *Nguyễn Ái Quốc* sáng lập', src='VOH', dur=3.0, theme='navy'),
   dict(text='ngày ra số đầu được chọn làm *Ngày Báo chí Cách mạng Việt Nam*', src='VOH', dur=4.0, theme='blue'),
   dict(text='năm 2025 đánh dấu *100 năm* báo chí cách mạng', dur=3.0, theme='pale'),
   dict(text='tôn trọng báo chí = gửi *tin thật, số liệu thật*', sub='Raise It With Press Release', dur=3.0, theme='navy'),
  ],
  vo=['Vì sao hai mươi mốt tháng sáu là ngày báo chí Việt Nam?', 'Ngày hai mươi mốt tháng sáu năm một chín hai lăm, báo Thanh Niên ra số đầu tiên tại Quảng Châu.', 'Tờ báo do lãnh tụ Nguyễn Ái Quốc sáng lập.', 'Ngày ra số đầu được chọn làm Ngày Báo chí Cách mạng Việt Nam.', 'Năm hai không hai lăm đánh dấu một trăm năm báo chí cách mạng.', 'Tôn trọng báo chí là gửi tin thật, số liệu thật.'],
  broll=['Ảnh tư liệu tờ báo Thanh Niên (chỉ dùng ảnh có giấy phép hoặc tư liệu công khai, ghi nguồn)', 'Toà soạn hiện đại (quay tại văn phòng đối tác, có xin phép)', 'Tay lật trang báo in (diễn viên nội bộ)'],
  audio='Nhạc nền trang trọng, nhẹ nhàng từ thư viện có bản quyền của nền tảng'),
 cap=dict(
  hook='Vì sao ngày 21/6 là Ngày Báo chí Cách mạng Việt Nam? 📰',
  lines=['21/6/1925: báo Thanh Niên ra số đầu tiên tại Quảng Châu (Trung Quốc).', 'Tờ báo do lãnh tụ Nguyễn Ái Quốc sáng lập.', 'Ngày ra số đầu được chọn làm Ngày Báo chí Cách mạng Việt Nam.', '', 'Với doanh nghiệp, cách tôn trọng báo chí tốt nhất: gửi tin thật, số liệu thật, đúng lúc.'],
  li_hook='Ngày 21/6/1925, báo Thanh Niên do lãnh tụ Nguyễn Ái Quốc sáng lập ra số đầu tiên tại Quảng Châu.\nĐó là lý do 21/6 trở thành Ngày Báo chí Cách mạng Việt Nam.',
  li_body=['Một câu chuyện lịch sử, và cũng là bài học cho người làm truyền thông doanh nghiệp. Năm 2025 đánh dấu 100 năm báo chí cách mạng Việt Nam. Với các đội truyền thông doanh nghiệp, đây là lời nhắc về vai trò của báo chí: kiểm chứng, chọn lọc và đưa tin có giá trị cho công chúng.', 'Điều đó có ý nghĩa thực tế khi bạn gửi thông cáo:'],
  li_points=['Chỉ gửi khi có tin thật sự, không gửi để "cho có".', 'Số liệu phải kiểm chứng được và có nguồn.', 'Tôn trọng thời gian của nhà báo: ngắn gọn, đúng chuyên mục, follow-up có chừng mực.'],
  li_close='Bạn sẽ chuẩn bị gì cho dịp 21/6 năm tới?',
  fb='Bạn có biết vì sao 21/6 là Ngày Báo chí Cách mạng Việt Nam không? Xem video nhé 👀')),

# 12 ── W4 Fri PROMO offer (local)
dict(slot='W4Fri', pillar='PROMO', format='single', slug='cong-bo-tin-truoc-tet',
 title='Công bố tin trước 12.12 và mùa Tết', cta='Xem giá mới nhất qua link', src=['PRICE'], tags=['#thongcaobaochi', '#doanhnghiep'],
 slides=[dict(t='promo', tag='trước mùa tết', title='tin cuối năm? *công bố* trước khi quá muộn',
   items=['Đăng tải trước 12.12 và mùa cao điểm Tết', 'Backlink tới trang khuyến mãi hoặc sản phẩm', 'Báo cáo phân phối để đánh giá chiến dịch'],
   price='giá chỉ từ — xem link', src=SRC_PRICE, ribbon=True)],
 cap=dict(
  hook='12.12 là ngày mai, Tết đang đến gần. Tin của bạn đã lên báo chưa? 🧧',
  lines=['Đi trước khi toà soạn bước vào mùa Tết:', '✓ Đăng tải trước ngày cao điểm', '✓ Backlink tới trang khuyến mãi/sản phẩm', '✓ Báo cáo phân phối để đánh giá', '', 'Gói và giá mới nhất: link ở bio.'],
  ig_cta='Xem gói và giá mới nhất qua link ở bio.',
  li_hook='Thông cáo cuối năm đăng sau mùa cao điểm gần như mất hết giá trị tin tức.\nThời điểm phù hợp là bây giờ.',
  li_body=['Từ 12.12 đến Tết Nguyên Đán, các toà soạn và đội truyền thông đều bận rộn, hộp thư luôn đầy. Thông cáo được gửi trước giai đoạn đó có nhiều cơ hội được đăng và chia sẻ hơn.', 'Những gì bạn có thể làm ngay tuần này với VRITIMES:'],
  li_points=['Phân phối thông cáo khuyến mãi, kết quả cuối năm hoặc tin tháng 1 với cam kết đăng tải trên báo (số lượng theo gói).', 'Đặt backlink tới trang khuyến mãi hoặc sản phẩm.', 'Dùng báo cáo phân phối để đánh giá chiến dịch và lên kế hoạch quý I.'],
  li_close='Gói dịch vụ và giá mới nhất có trên trang chính thức của chúng tôi.',
  fb='Đừng để tin cuối năm của bạn lên báo khi mọi người đã nghỉ Tết 😅 Xem các gói VRITIMES tại đây 👇')),
]

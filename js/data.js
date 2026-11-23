/**
 * ==============================================================================
 * MEDCARE CRM — DỮ LIỆU MẪU Y TẾ & BỆNH NHÂN (EHR & CRM DATASET)
 * Chuẩn hóa 200 bệnh nhân Healthcare · 320+ Toa thuốc điện tử chuẩn Bộ Y Tế
 * Học phần 111101 · Thiết kế Web · Trường Đại học Lạc Hồng (LHU)
 * ==============================================================================
 */

const SERVICES = [
  'Khám Sức Khỏe Tổng Quát',
  'Tầm Soát Tim Mạch',
  'Nha Khoa Thẩm Mỹ',
  'Da Liễu & Thẩm Mỹ Da',
  'Khám Mắt & Điều Trị Cận Thị',
  'Gói Mẹ & Bé',
  'Xét Nghiệm Máu Tại Nhà',
  'Chẩn Đoán Hình Ảnh CT/MRI',
  'Nội Khoa Tổng Quát',
  'Tầm Soát Ung Thư'
];

const HO = [
  'Nguyễn', 'Trần', 'Lê', 'Phạm', 'Hoàng', 'Huỳnh', 'Phan', 'Vũ', 'Võ', 'Đặng',
  'Bùi', 'Đỗ', 'Hồ', 'Ngô', 'Dương', 'Lý', 'Đoàn', 'Trịnh', 'Mai', 'Lâm',
  'Đinh', 'Đào', 'Lương', 'Thái', 'Hà'
];

const TEN_NAM = [
  'Văn An', 'Minh Khoa', 'Quốc Hùng', 'Thanh Tùng', 'Trọng Nghĩa', 'Đức Long', 'Hoàng Nam',
  'Anh Tuấn', 'Minh Đức', 'Công Tâm', 'Gia Huy', 'Minh Huy', 'Ngọc Nhân', 'Quốc Quang',
  'Đình Trọng', 'Văn Hậu', 'Quang Hải', 'Thế Anh', 'Bảo Long', 'Hữu Phước', 'Tấn Phát',
  'Khánh Toàn', 'Duy Mạnh', 'Tiến Dũng', 'Trung Kiên', 'Bảo Khang', 'Tuấn Kiệt', 'Hải Đăng'
];

const TEN_NU = [
  'Thị Hoa', 'Thanh Mai', 'Thu Hương', 'Ngọc Linh', 'Bích Ngọc', 'Phương Anh', 'Minh Châu',
  'Kim Oanh', 'Lan Anh', 'Hồng Nhung', 'Thúy Nga', 'Mỹ Duyên', 'Cẩm Tú', 'Diệu Nhi',
  'Bảo Trâm', 'Ánh Tuyết', 'Quỳnh Như', 'Mai Phương', 'Hoài An', 'Yến Nhi', 'Thu Trang',
  'Thảo Vy', 'Tuyết Mai', 'Khánh Linh', 'Bảo Hân', 'Nhã Uyên', 'Phương Thảo', 'Gia Như'
];

const DISTRICTS = [
  // Khu vực Đồng Nai (Kề cận ĐH Lạc Hồng)
  'TP. Biên Hòa, Đồng Nai',
  'Huyện Long Thành, Đồng Nai',
  'Huyện Nhơn Trạch, Đồng Nai',
  'Huyện Trảng Bom, Đồng Nai',
  'TP. Long Khánh, Đồng Nai',
  'Huyện Vĩnh Cửu, Đồng Nai',
  // Khu vực TP. Hồ Chí Minh
  'Quận 1, TP. Hồ Chí Minh',
  'Quận 3, TP. Hồ Chí Minh',
  'Quận 7, TP. Hồ Chí Minh',
  'Quận Bình Thạnh, TP. Hồ Chí Minh',
  'TP. Thủ Đức, TP. Hồ Chí Minh',
  'Quận Gò Vấp, TP. Hồ Chí Minh',
  'Quận Tân Bình, TP. Hồ Chí Minh',
  // Khu vực Bình Dương & lân cận
  'TP. Dĩ An, Bình Dương',
  'TP. Thuận An, Bình Dương',
  'TP. Thủ Dầu Một, Bình Dương'
];

const SOURCES = [
  'Website MedCare',
  'Giới thiệu từ bác sĩ',
  'Zalo Official Account',
  'Facebook Clinic',
  'Google Ads',
  'Khám sức khỏe doanh nghiệp',
  'Khách cũ giới thiệu'
];

const STATUSES = ['active', 'active', 'active', 'active', 'inactive'];

const MEDICAL_HISTORIES = [
  'Tăng huyết áp vô căn độ 1, tiền sử đau thượng vị nhẹ khi căng thẳng.',
  'Đái tháo đường típ 2 (HbA1c 6.8%), rối loạn mỡ máu nhẹ.',
  'Thoái hóa khớp gối nguyên phát hai bên độ 2, đau tăng khi leo cầu thang.',
  'Trào ngược dạ dày thực quản (GERD), viêm niêm mạc dạ dày Hp âm tính.',
  'Viêm mũi xoang dị ứng thời tiết, thỉnh thoảng nghẹt mũi về đêm.',
  'Viêm da cơ địa tái phát, da nhạy cảm khi thay đổi thời tiết.',
  'Cận thị khúc xạ 3.5 diop, hội chứng mỏi mắt thị giác màn hình vi tính.',
  'Rối loạn tiền đình nhẹ, đau đầu vùng chẩm khi thiếu ngủ.',
  'Không ghi nhận tiền sử bệnh lý mạn tính. Thể trạng khỏe mạnh bình thường.'
];

const ALLERGIES = [
  'Dị ứng kháng sinh nhóm Penicillin / Amoxicillin (nổi ban, ngứa).',
  'Dị ứng thuốc kháng viêm NSAID (Aspirin, Ibuprofen - co thắt phế quản).',
  'Dị ứng thuốc cản quang i-ốt trong chẩn đoán CT.',
  'Dị ứng hải sản có vỏ (tôm, cua) và đậu phộng.',
  'Không ghi nhận tiền sử dị ứng thuốc hay thực phẩm.'
];

const BLOOD_TYPES = ['O+', 'A+', 'B+', 'AB+'];

function rand(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
function randInt(min, max) { return Math.floor(Math.random() * (max - min + 1)) + min; }

/**
 * Tạo danh sách 200 bệnh nhân với phân bổ hạng chuẩn CRM:
 * - Vàng (Gold):   ~15% (Doanh số >= 15.000.000 ₫)
 * - Bạc (Silver):  ~35% (Doanh số 5.000.000 ₫ – 14.999.999 ₫)
 * - Đồng (Bronze): ~50% (Doanh số < 5.000.000 ₫)
 */
function generatePatients(n = 200) {
  const patients = [];
  for (let i = 1; i <= n; i++) {
    const isMale = Math.random() > 0.46;
    const ho = rand(HO);
    const ten = isMale ? rand(TEN_NAM) : rand(TEN_NU);
    const name = `${ho} ${ten}`;

    // Phân bổ tỷ lệ doanh số chuẩn xác
    const tierRoll = Math.random();
    let spent;
    let visits;
    if (tierRoll < 0.15) {
      // Hạng Vàng: 15.000.000 ₫ – 48.000.000 ₫
      spent = randInt(150, 480) * 100000;
      visits = randInt(5, 14);
    } else if (tierRoll < 0.50) {
      // Hạng Bạc: 5.000.000 ₫ – 14.800.000 ₫
      spent = randInt(50, 148) * 100000;
      visits = randInt(3, 8);
    } else {
      // Hạng Đồng: 600.000 ₫ – 4.800.000 ₫
      spent = randInt(6, 48) * 100000;
      visits = randInt(1, 4);
    }

    const rank = spent >= 15000000 ? 'gold' : spent >= 5000000 ? 'silver' : 'bronze';

    const daysAgo = randInt(0, 180);
    const lastDate = new Date(Date.now() - daysAgo * 86400000);
    const createdAgo = randInt(daysAgo, daysAgo + 180);
    const createdDate = new Date(Date.now() - createdAgo * 86400000);

    const nextFollowDays = randInt(-10, 30);
    const nextFollowDate = new Date(Date.now() + nextFollowDays * 86400000);

    const emailSlug = `${ho.toLowerCase()}.${ten.toLowerCase().replace(/\s+/g, '')}${i}`;
    const cleanEmail = emailSlug.normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/đ/g, 'd');

    patients.push({
      id: `KH${String(i).padStart(3, '0')}`,
      name,
      gender: isMale ? 'Nam' : 'Nữ',
      age: randInt(18, 76),
      email: `${cleanEmail}@gmail.com`,
      phone: `09${randInt(10000000, 99999999)}`,
      address: rand(DISTRICTS),
      service: rand(SERVICES),
      source: rand(SOURCES),
      totalSpent: spent,
      rank,
      status: rand(STATUSES),
      visits,
      lastContact: lastDate.toLocaleDateString('vi-VN'),
      nextFollowUp: nextFollowDate.toLocaleDateString('vi-VN'),
      createdAt: createdDate.toLocaleDateString('vi-VN'),
      overdueDays: nextFollowDays < 0 ? Math.abs(nextFollowDays) : 0,
      notes: `Bệnh nhân quan tâm ${rand(SERVICES).toLowerCase()}. Đã khám ${visits} lượt. Cần tư vấn và theo dõi định kỳ.`,
      bhyt: `DN 4 75 ${String(79000000 + i)}`,
      bloodType: rand(BLOOD_TYPES),
      height: isMale ? randInt(162, 182) : randInt(150, 168),
      weight: isMale ? randInt(58, 82) : randInt(45, 63),
      medicalHistory: rand(MEDICAL_HISTORIES),
      allergies: rand(ALLERGIES)
    });
  }
  return patients;
}

// ── TOA THUỐC ĐIỆN TỬ (PRESCRIPTIONS - EHR CHUẨN BỘ Y TẾ) ──
const CLINICAL_PRESETS = [
  {
    diagnosis: 'I10 — Bệnh tăng huyết áp vô căn (nguyên phát)',
    department: 'Nội Tim Mạch',
    doctor: 'BS. CKII Nguyễn Minh Nhân',
    advice: 'Ăn giảm muối, hạn chế dầu mỡ động vật. Đo huyết áp mỗi sáng vào sổ theo dõi. Tái khám sau 30 ngày.',
    medicines: [
      { name: 'Amlodipine 5mg (Pfizer)', dose: 'Uống 1 viên / ngày (Sáng sau ăn)', qty: '30 viên', note: 'Hạ áp, giãn mạch ngoại vi' },
      { name: 'Losartan Potassium 50mg (Cozaar)', dose: 'Uống 1 viên / ngày (Sáng)', qty: '30 viên', note: 'Ổn định huyết áp mục tiêu' },
      { name: 'Atorvastatin 20mg (Lipitor)', dose: 'Uống 1 viên / ngày (Tối trước khi ngủ)', qty: '30 viên', note: 'Hạ mỡ máu, bảo vệ thành mạch' }
    ]
  },
  {
    diagnosis: 'E11 — Bệnh đái tháo đường típ 2 không phụ thuộc Insulin',
    department: 'Nội Tiết & Đái Tháo Đường',
    doctor: 'ThS. BS Trần Thị Mai',
    advice: 'Giảm tinh bột, kiêng đường ngọt tinh luyện. Đi bộ 30 phút/ngày. Kiểm tra đường huyết mao mạch định kỳ.',
    medicines: [
      { name: 'Metformin HCl 850mg (Glucophage)', dose: 'Uống 1 viên x 2 lần / ngày (Sáng - Tối ngay sau ăn)', qty: '60 viên', note: 'Kiểm soát đường huyết nền' },
      { name: 'Gliclazide MR 60mg (Diamicron MR)', dose: 'Uống 1 viên / ngày (Sáng trước ăn 30 phút)', qty: '30 viên', note: 'Kích thích tiết insulin' },
      { name: 'Fenofibrate 200mg (Lipanthyl)', dose: 'Uống 1 viên / ngày (Tối sau ăn)', qty: '30 viên', note: 'Điều hòa Triglyceride huyết tương' }
    ]
  },
  {
    diagnosis: 'K21 — Bệnh trào ngược dạ dày - thực quản (GERD)',
    department: 'Tiêu Hóa & Gan Mật',
    doctor: 'BS. CKI Lê Văn Hùng',
    advice: 'Tránh ăn quá no, kiêng chua cay, cà phê và nước có gas. Không nằm trong vòng 2 giờ sau khi ăn.',
    medicines: [
      { name: 'Esomeprazole 40mg (Nexium Mups)', dose: 'Uống 1 viên / ngày (Sáng trước bữa ăn 30 phút)', qty: '28 viên', note: 'Ức chế tiết acid dịch vị' },
      { name: 'Mosapride Citrate 5mg (Gasmotin)', dose: 'Uống 1 viên x 3 lần / ngày (Trước ăn 15 phút)', qty: '45 viên', note: 'Kích thích vận động đường tiêu hóa' },
      { name: 'Phosphalugel (Gel nhôm phosphat)', dose: 'Uống 1 gói khi đau rát thượng vị (cách xa bữa ăn)', qty: '20 gói', note: 'Trung hòa acid, bảo vệ niêm mạc' }
    ]
  },
  {
    diagnosis: 'M17 — Thoái hóa khớp gối nguyên phát hai bên',
    department: 'Cơ Xương Khớp',
    doctor: 'BS. CKII Phạm Quốc Huy',
    advice: 'Tránh ngồi xổm, hạn chế bê vác nặng. Tập đạp xe nhẹ nhàng tại chỗ hoặc bơi lội để nuôi dưỡng dịch khớp.',
    medicines: [
      { name: 'Celecoxib 200mg (Celebrex)', dose: 'Uống 1 viên / ngày (Sáng sau ăn no)', qty: '20 viên', note: 'Kháng viêm giảm đau chọn lọc COX-2' },
      { name: 'Glucosamine Sulfate 1500mg (Viartril-S)', dose: 'Uống 1 gói / ngày (Hòa tan trong nước ấm sau ăn)', qty: '30 gói', note: 'Tái tạo sụn khớp, tăng tiết dịch khớp' },
      { name: 'Diacerein 50mg (Artrodar)', dose: 'Uống 1 viên / ngày (Tối sau ăn)', qty: '30 viên', note: 'Ức chế thoái hóa mô sụn khớp' }
    ]
  },
  {
    diagnosis: 'J02 — Viêm họng và viêm phế quản cấp tính',
    department: 'Nội Hô Hấp',
    doctor: 'ThS. BS Đặng Bích Ngọc',
    advice: 'Uống nhiều nước ấm, súc họng nước muối sinh lý 3 lần/ngày. Giữ ấm ngực và cổ họng khi ngủ.',
    medicines: [
      { name: 'Cefuroxime Axetil 500mg (Zinnat)', dose: 'Uống 1 viên x 2 lần / ngày (Sáng - Chiều sau ăn)', qty: '14 viên', note: 'Kháng sinh diệt khuẩn đường hô hấp' },
      { name: 'Paracetamol 500mg (Panadol Extra)', dose: 'Uống 1 viên khi sốt trên 38.5°C hoặc đau nhức đầu (cách 6h)', qty: '10 viên', note: 'Hạ sốt, giảm đau toàn thân' },
      { name: 'Acetylcysteine 200mg (Acemuc)', dose: 'Uống 1 gói x 3 lần / ngày (Hòa tan trong nước)', qty: '20 gói', note: 'Long đờm, loãng dịch tiết phế quản' }
    ]
  },
  {
    diagnosis: 'L20 — Viêm da cơ địa dị ứng thời tiết',
    department: 'Da Liễu & Thẩm Mỹ Da',
    doctor: 'BS. CKI Hoàng Lan Anh',
    advice: 'Không tắm nước quá nóng, tránh gãi cào làm trầy xước da. Bôi dưỡng ẩm thường xuyên sau khi tắm.',
    medicines: [
      { name: 'Fexofenadine HCl 180mg (Telfast)', dose: 'Uống 1 viên / ngày (Sáng sau ăn)', qty: '15 viên', note: 'Kháng histamin H1 thế hệ 2, chống ngứa dị ứng' },
      { name: 'Betamethasone Dipropionate 0.05% (Diproson)', dose: 'Thoa mỏng lên vùng tổn thương 1 lần/ngày vào buổi tối', qty: '1 tuýp', note: 'Chống viêm dị ứng ngoài da tại chỗ' },
      { name: 'Cetaphil Moisturizing Cream 100g', dose: 'Thoa dưỡng ẩm toàn thân 2 - 3 lần / ngày sau khi lau khô da', qty: '1 tuýp', note: 'Phục hồi hàng rào ẩm bảo vệ da' }
    ]
  },
  {
    diagnosis: 'H52.1 — Cận thị học đường & Hội chứng mỏi điều tiết thị giác',
    department: 'Chuyên Khoa Mắt',
    doctor: 'BS. CKII Vũ Trọng Nghĩa',
    advice: 'Áp dụng quy tắc nghỉ mắt 20-20-20. Hạn chế sử dụng điện thoại trong bóng tối. Tái khám sau 6 tháng.',
    medicines: [
      { name: 'Systane Ultra (Lọ 10ml)', dose: 'Nhỏ 1 - 2 giọt mỗi mắt khi khô rát, mỏi mắt (4 - 6 lần/ngày)', qty: '1 lọ', note: 'Nước mắt nhân tạo bôi trơn giác mạc' },
      { name: 'Nutra-Vision Lutein & Zeaxanthin', dose: 'Uống 1 viên / ngày (Sáng sau ăn)', qty: '30 viên', note: 'Bổ sung dưỡng chất điểm vàng võng mạc' },
      { name: 'Tobrex 0.3% (Lọ 5ml)', dose: 'Nhỏ 1 giọt mỗi mắt x 2 lần / ngày (Sáng - Tối) trong 7 ngày', qty: '1 lọ', note: 'Kháng khuẩn phòng ngừa viêm bờ mi' }
    ]
  },
  {
    diagnosis: 'Z00.0 — Khám sức khỏe tổng quát định kỳ & Bổ sung vi chất',
    department: 'Nội Khoa Tổng Quát',
    doctor: 'BS. CKII Nguyễn Minh Nhân',
    advice: 'Chỉ số sinh hóa máu trong giới hạn bình thường. Duy trì chế độ ăn lành mạnh, vận động thể chất đều đặn.',
    medicines: [
      { name: 'Enervon-C (Vitamin C 500mg + B Complex)', dose: 'Uống 1 viên / ngày (Sáng sau ăn)', qty: '30 viên', note: 'Bổ sung vitamin, tăng cường miễn dịch' },
      { name: 'Canxi Nano + Vitamin D3 & MK7', dose: 'Uống 1 viên / ngày (Sáng sau ăn 1 giờ)', qty: '30 viên', note: 'Hỗ trợ mật độ xương chắc khỏe' },
      { name: 'Omega-3 Dầu Cá Hồi Tinh Khiết 1000mg', dose: 'Uống 1 viên / ngày (Trưa sau ăn)', qty: '60 viên', note: 'Bổ trợ tim mạch và thị lực' }
    ]
  }
];

/**
 * Sinh từ 320 đến 350 toa thuốc điện tử liên kết chặt chẽ với danh sách bệnh nhân
 */
function generatePrescriptions(patients, targetCount = 325) {
  const prescriptions = [];
  let rxIdCounter = 1;

  // Lượt 1: Mỗi bệnh nhân được cấp ít nhất 1 toa thuốc (200 toa đầu tiên)
  patients.forEach((p, index) => {
    const preset = CLINICAL_PRESETS[index % CLINICAL_PRESETS.length];
    const daysAgo = randInt(2, 60);
    const rxDate = new Date(Date.now() - daysAgo * 86400000);

    prescriptions.push({
      id: `RX2026-${String(rxIdCounter++).padStart(4, '0')}`,
      patientId: p.id,
      patientName: p.name,
      diagnosis: preset.diagnosis,
      department: preset.department,
      doctor: preset.doctor,
      date: rxDate.toLocaleDateString('vi-VN'),
      medicines: preset.medicines,
      advice: preset.advice,
      totalAmount: randInt(35, 145) * 10000,
      status: Math.random() > 0.08 ? 'Đã cấp phát' : 'Chờ lấy thuốc'
    });
  });

  // Lượt 2: Các bệnh nhân có số lượt khám > 2 được cấp thêm các toa thuốc tái khám
  for (let i = 0; i < patients.length && prescriptions.length < targetCount; i++) {
    const p = patients[i];
    if (p.visits >= 2) {
      const preset = CLINICAL_PRESETS[(i + 3) % CLINICAL_PRESETS.length];
      const daysAgo = randInt(65, 140);
      const rxDate = new Date(Date.now() - daysAgo * 86400000);

      prescriptions.push({
        id: `RX2026-${String(rxIdCounter++).padStart(4, '0')}`,
        patientId: p.id,
        patientName: p.name,
        diagnosis: preset.diagnosis,
        department: preset.department,
        doctor: preset.doctor,
        date: rxDate.toLocaleDateString('vi-VN'),
        medicines: preset.medicines,
        advice: preset.advice,
        totalAmount: randInt(35, 145) * 10000,
        status: 'Đã cấp phát'
      });
    }
  }

  // Lượt 3: Tiếp tục bổ sung cho các bệnh nhân VIP (visits >= 5) cho đến khi đủ targetCount
  for (let i = 0; i < patients.length && prescriptions.length < targetCount; i++) {
    const p = patients[i];
    if (p.visits >= 5) {
      const preset = CLINICAL_PRESETS[(i + 5) % CLINICAL_PRESETS.length];
      const daysAgo = randInt(145, 210);
      const rxDate = new Date(Date.now() - daysAgo * 86400000);

      prescriptions.push({
        id: `RX2026-${String(rxIdCounter++).padStart(4, '0')}`,
        patientId: p.id,
        patientName: p.name,
        diagnosis: preset.diagnosis,
        department: preset.department,
        doctor: preset.doctor,
        date: rxDate.toLocaleDateString('vi-VN'),
        medicines: preset.medicines,
        advice: preset.advice,
        totalAmount: randInt(35, 145) * 10000,
        status: 'Đã cấp phát'
      });
    }
  }

  return prescriptions;
}

// ── INTERACTIONS (Lịch sử chăm sóc & tương tác) ──
const INTERACTION_TYPES = [
  'Gọi điện hỏi thăm',
  'Nhắc lịch tái khám',
  'Gửi kết quả xét nghiệm',
  'Tư vấn sau khám',
  'Đặt lịch hẹn chuyên khoa',
  'Hướng dẫn dùng đơn thuốc',
  'Hỏi thăm phục hồi sức khỏe'
];
const STAFF_NAMES = ['Nguyễn Minh Nhân', 'Trần Thị Mai', 'Lê Văn Hùng', 'Phạm Quốc Huy', 'Đặng Bích Ngọc'];

function generateInteractions(patientId, count = 3) {
  return Array.from({ length: count }, (_, i) => {
    const daysAgo = (i + 1) * randInt(5, 20);
    const date = new Date(Date.now() - daysAgo * 86400000);
    const type = rand(INTERACTION_TYPES);
    return {
      id: `INT_${patientId}_${i + 1}`,
      patientId,
      type,
      date: date.toLocaleDateString('vi-VN'),
      staff: rand(STAFF_NAMES),
      note: `Đã thực hiện: ${type.toLowerCase()}. Bệnh nhân tương tác tốt, tuân thủ phác đồ điều trị.`,
      result: Math.random() > 0.25 ? 'Tích cực' : 'Cần theo dõi thêm'
    };
  });
}

// ── LEADS ──
const LEAD_STATUSES = ['new', 'contacted', 'qualified', 'converted', 'lost'];
const LEAD_STATUS_LABELS = {
  new: 'Mới',
  contacted: 'Đã liên hệ',
  qualified: 'Tiềm năng',
  converted: 'Đã chuyển đổi',
  lost: 'Không tiềm năng'
};
const PRIORITIES = ['low', 'medium', 'high'];

function generateLeads(n = 25) {
  return Array.from({ length: n }, (_, i) => {
    const isMale = Math.random() > 0.5;
    const ho = rand(HO);
    const ten = isMale ? rand(TEN_NAM) : rand(TEN_NU);
    const daysAgo = randInt(0, 60);
    const created = new Date(Date.now() - daysAgo * 86400000);
    const statusIdx = Math.min(Math.floor(Math.random() * 2.5), 4);

    return {
      id: `LD${String(i + 1).padStart(3, '0')}`,
      name: `${ho} ${ten}`,
      gender: isMale ? 'Nam' : 'Nữ',
      email: `lead${i + 1}@medcare.vn`,
      phone: `09${randInt(10000000, 99999999)}`,
      service: rand(SERVICES),
      source: rand(SOURCES),
      priority: rand(PRIORITIES),
      status: LEAD_STATUSES[statusIdx],
      note: `Khách quan tâm ${rand(SERVICES).toLowerCase()}, ngân sách ước tính ${(randInt(2, 20) * 500000).toLocaleString('vi-VN')} ₫.`,
      createdAt: created.toLocaleDateString('vi-VN'),
      assignedTo: rand(STAFF_NAMES)
    };
  });
}

// ── SURVEYS (Đánh giá & Khảo sát CSAT) ──
function generateSurveys(n = 20) {
  const comments = [
    'Bác sĩ tư vấn rất tận tình, giải thích kết quả xét nghiệm dễ hiểu.',
    'Thời gian chờ đợi nhanh hơn lần trước, nhân viên tiếp đón chu đáo.',
    'Cơ sở vật chất hiện đại, phòng ốc sạch sẽ thoáng mát.',
    'Toa thuốc hiệu quả rõ rệt, bác sĩ dặn dò kiêng khem chi tiết.',
    'Rất hài lòng về thái độ phục vụ của điều dưỡng và nhân viên thu ngân.',
    'Chi phí hợp lý, minh bạch rõ ràng từng hạng mục khám.',
    'Sẽ tiếp tục tin tưởng đồng hành và giới thiệu cho bạn bè đồng nghiệp.'
  ];

  return Array.from({ length: n }, (_, i) => {
    const daysAgo = randInt(0, 30);
    const date = new Date(Date.now() - daysAgo * 86400000);
    const rating = (Math.random() * 1.5 + 3.5).toFixed(1); // 3.5 – 5.0

    return {
      id: `SV${String(i + 1).padStart(3, '0')}`,
      patientId: `KH${String(randInt(1, 200)).padStart(3, '0')}`,
      date: date.toLocaleDateString('vi-VN'),
      serviceRating: parseFloat(rating),
      staffRating: parseFloat((Math.random() * 1.0 + 4.0).toFixed(1)),
      waitRating: parseFloat((Math.random() * 1.5 + 3.5).toFixed(1)),
      overallRating: parseFloat(rating),
      comment: rand(comments),
      service: rand(SERVICES)
    };
  });
}

// ── INVENTORY (Kho Dược & Vật tư Y tế) ──
const SAMPLE_MEDICINES = [
  { id: 'MED001', name: 'Paracetamol 500mg', category: 'Thuốc hạ sốt, giảm đau', unit: 'Hộp', stock: 150, minStock: 30, price: 65000, expiry: '12/2027', status: 'normal' },
  { id: 'MED002', name: 'Amoxicillin 500mg', category: 'Kháng sinh', unit: 'Hộp', stock: 85, minStock: 25, price: 120000, expiry: '08/2026', status: 'normal' },
  { id: 'MED003', name: 'Bộ Kit Test Đường Huyết Accu-Chek', category: 'Vật tư chẩn đoán', unit: 'Bộ', stock: 12, minStock: 15, price: 380000, expiry: '06/2027', status: 'low' },
  { id: 'MED004', name: 'Băng Gạc Vô Trùng Y Tế 10x10', category: 'Vật tư tiêu hao', unit: 'Gói', stock: 320, minStock: 50, price: 25000, expiry: '10/2028', status: 'normal' },
  { id: 'MED005', name: 'Cồn Y Tế 70 Độ (Chai 500ml)', category: 'Sát khuẩn', unit: 'Chai', stock: 60, minStock: 20, price: 35000, expiry: '01/2027', status: 'normal' },
  { id: 'MED006', name: 'Khẩu Trang Y Tế 4 Lớp Kháng Khuẩn', category: 'Bảo hộ y tế', unit: 'Hộp', stock: 8, minStock: 20, price: 45000, expiry: '05/2028', status: 'low' },
  { id: 'MED007', name: 'Omega-3 Dầu Cá Tinh Khiết', category: 'Thực phẩm bổ sung', unit: 'Lọ', stock: 45, minStock: 15, price: 280000, expiry: '09/2026', status: 'normal' },
  { id: 'MED008', name: 'Găng Tay Cao Su Khám Bệnh (Size M)', category: 'Vật tư tiêu hao', unit: 'Hộp', stock: 95, minStock: 30, price: 95000, expiry: '11/2027', status: 'normal' },
  { id: 'MED009', name: 'Thuốc Nhỏ Mắt Kháng Viêm Tobradex', category: 'Chuyên khoa mắt', unit: 'Lọ', stock: 22, minStock: 10, price: 110000, expiry: '04/2026', status: 'normal' },
  { id: 'MED010', name: 'Bộ Dụng Cụ Nha Khoa Dùng 1 Lần', category: 'Vật tư nha khoa', unit: 'Bộ', stock: 5, minStock: 15, price: 85000, expiry: '12/2026', status: 'low' }
];

function generateInventory() {
  return [...SAMPLE_MEDICINES];
}

// ── INVOICES (Hóa Đơn & Thu Ngân Bán Hàng) ──
function generateInvoices(patients, n = 30) {
  const paymentMethods = ['Tiền mặt', 'Chuyển khoản QR', 'Thẻ Visa/Master', 'Bảo hiểm Y tế'];
  const invoiceStatuses = ['Đã thanh toán', 'Đã thanh toán', 'Đã thanh toán', 'Chờ thanh toán'];

  return Array.from({ length: n }, (_, i) => {
    const p = patients[i % patients.length] || { id: 'KH001', name: 'Nguyễn Văn An', phone: '0912345678' };
    const daysAgo = randInt(0, 30);
    const date = new Date(Date.now() - daysAgo * 86400000);
    const amount = randInt(5, 45) * 200000;

    return {
      id: `HD${String(2026001 + i)}`,
      patientId: p.id,
      patientName: p.name,
      phone: p.phone,
      service: rand(SERVICES),
      amount: amount,
      paymentMethod: rand(paymentMethods),
      status: rand(invoiceStatuses),
      cashier: rand(STAFF_NAMES),
      createdAt: date.toLocaleDateString('vi-VN')
    };
  });
}

// ── KHỞI TẠO VÀ LƯU TRỮ DỮ LIỆU LOCALSTORAGE ──
const DATA_KEY          = 'medcare_patients';
const PRESCRIPTIONS_KEY = 'medcare_prescriptions';
const LEADS_KEY         = 'medcare_leads';
const SURVEYS_KEY       = 'medcare_surveys';
const INVENTORY_KEY     = 'medcare_inventory';
const INVOICES_KEY      = 'medcare_invoices';

function initData(forceReset = false) {
  if (typeof localStorage === 'undefined') return;

  // Tự động nâng cấp khi dữ liệu chưa đủ 200 bệnh nhân
  if (forceReset || !localStorage.getItem(DATA_KEY) || getPatients().length < 200) {
    const pts = generatePatients(200);
    localStorage.setItem(DATA_KEY, JSON.stringify(pts));
  }
  const currentPts = getPatients();

  // Tự động nâng cấp khi dữ liệu chưa đủ 300 toa thuốc
  if (forceReset || !localStorage.getItem(PRESCRIPTIONS_KEY) || getPrescriptions().length < 300) {
    const rxs = generatePrescriptions(currentPts, 325);
    localStorage.setItem(PRESCRIPTIONS_KEY, JSON.stringify(rxs));
  }

  if (forceReset || !localStorage.getItem(LEADS_KEY)) {
    localStorage.setItem(LEADS_KEY, JSON.stringify(generateLeads(25)));
  }
  if (forceReset || !localStorage.getItem(SURVEYS_KEY)) {
    localStorage.setItem(SURVEYS_KEY, JSON.stringify(generateSurveys(20)));
  }
  if (forceReset || !localStorage.getItem(INVENTORY_KEY)) {
    localStorage.setItem(INVENTORY_KEY, JSON.stringify(generateInventory()));
  }
  if (forceReset || !localStorage.getItem(INVOICES_KEY)) {
    localStorage.setItem(INVOICES_KEY, JSON.stringify(generateInvoices(currentPts, 30)));
  }
}

// ── CÁC HÀM GET / SAVE TRUY XUẤT ──
function getPatients() {
  if (typeof localStorage === 'undefined') return [];
  try { return JSON.parse(localStorage.getItem(DATA_KEY)) || []; }
  catch { return []; }
}
function savePatients(data) {
  if (typeof localStorage === 'undefined') return;
  localStorage.setItem(DATA_KEY, JSON.stringify(data));
}

function getPrescriptions() {
  if (typeof localStorage === 'undefined') return [];
  try { return JSON.parse(localStorage.getItem(PRESCRIPTIONS_KEY)) || []; }
  catch { return []; }
}
function savePrescriptions(data) {
  if (typeof localStorage === 'undefined') return;
  localStorage.setItem(PRESCRIPTIONS_KEY, JSON.stringify(data));
}

function getPrescriptionsByPatient(patientId) {
  const all = getPrescriptions();
  return all.filter(rx => rx.patientId === patientId);
}

function getInventory() {
  if (typeof localStorage === 'undefined') return [];
  try { return JSON.parse(localStorage.getItem(INVENTORY_KEY)) || []; }
  catch { return []; }
}
function saveInventory(data) {
  if (typeof localStorage === 'undefined') return;
  localStorage.setItem(INVENTORY_KEY, JSON.stringify(data));
}

function getInvoices() {
  if (typeof localStorage === 'undefined') return [];
  try { return JSON.parse(localStorage.getItem(INVOICES_KEY)) || []; }
  catch { return []; }
}
function saveInvoices(data) {
  if (typeof localStorage === 'undefined') return;
  localStorage.setItem(INVOICES_KEY, JSON.stringify(data));
}

function getLeads() {
  if (typeof localStorage === 'undefined') return [];
  try { return JSON.parse(localStorage.getItem(LEADS_KEY)) || []; }
  catch { return []; }
}
function saveLeads(data) {
  if (typeof localStorage === 'undefined') return;
  localStorage.setItem(LEADS_KEY, JSON.stringify(data));
}

function getSurveys() {
  if (typeof localStorage === 'undefined') return [];
  try { return JSON.parse(localStorage.getItem(SURVEYS_KEY)) || []; }
  catch { return []; }
}
function saveSurveys(data) {
  if (typeof localStorage === 'undefined') return;
  localStorage.setItem(SURVEYS_KEY, JSON.stringify(data));
}

// ── PHÂN LOẠI KHÁCH HÀNG (YÊU CẦU HỌC PHẦN ĐH LẠC HỒNG) ──
/**
 * Phân hạng bệnh nhân theo giá trị giao dịch tích lũy
 * Đồng:  < 5.000.000 ₫
 * Bạc:   5.000.000 ₫ – 14.999.999 ₫
 * Vàng:  ≥ 15.000.000 ₫
 */
function classifyPatient(totalSpent) {
  if (totalSpent >= 15000000) return { rank: 'gold',   label: 'Vàng',  icon: '🥇', color: '#D97706' };
  if (totalSpent >= 5000000)  return { rank: 'silver', label: 'Bạc',   icon: '🥈', color: '#64748B' };
  return                               { rank: 'bronze', label: 'Đồng',  icon: '🥉', color: '#B77945' };
}

function getRankStats(patients) {
  return patients.reduce((acc, p) => {
    acc[p.rank] = (acc[p.rank] || 0) + 1;
    return acc;
  }, { gold: 0, silver: 0, bronze: 0 });
}

function getTodayFollowUps(patients) {
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  return patients
    .filter(p => p.overdueDays > 0 || isFollowUpToday(p.nextFollowUp))
    .sort((a, b) => {
      const rankOrder = { gold: 0, silver: 1, bronze: 2 };
      return rankOrder[a.rank] - rankOrder[b.rank];
    });
}

function isFollowUpToday(dateStr) {
  if (!dateStr) return false;
  try {
    const [d, m, y] = dateStr.split('/').map(Number);
    const date = new Date(y, m - 1, d);
    const today = new Date();
    return date.toDateString() === today.toDateString();
  } catch { return false; }
}

function formatCurrency(n) {
  if (n >= 1000000) return (n / 1000000).toFixed(1) + 'M ₫';
  if (n >= 1000)    return (n / 1000).toFixed(0) + 'K ₫';
  return n.toLocaleString('vi-VN') + ' ₫';
}

// ── GLOBAL & WINDOW EXPORT ──
if (typeof window !== 'undefined') {
  window.initData                  = initData;
  window.getPatients               = getPatients;
  window.savePatients              = savePatients;
  window.getPrescriptions          = getPrescriptions;
  window.savePrescriptions         = savePrescriptions;
  window.getPrescriptionsByPatient = getPrescriptionsByPatient;
  window.getLeads                  = getLeads;
  window.saveLeads                 = saveLeads;
  window.getSurveys                = getSurveys;
  window.saveSurveys               = saveSurveys;
  window.getInventory              = getInventory;
  window.saveInventory             = saveInventory;
  window.getInvoices               = getInvoices;
  window.saveInvoices              = saveInvoices;
  window.classifyPatient           = classifyPatient;
  window.getRankStats              = getRankStats;
  window.getTodayFollowUps         = getTodayFollowUps;
  window.formatCurrency            = formatCurrency;
  window.SERVICES                  = SERVICES;
  window.LEAD_STATUS_LABELS        = LEAD_STATUS_LABELS;
  window.generateInteractions      = generateInteractions;
  window.generatePatients          = generatePatients;
  window.generatePrescriptions     = generatePrescriptions;
}

if (typeof global !== 'undefined') {
  global.SERVICES                  = SERVICES;
  global.generatePatients          = generatePatients;
  global.generatePrescriptions     = generatePrescriptions;
  global.classifyPatient           = classifyPatient;
  global.getRankStats              = getRankStats;
  global.formatCurrency            = formatCurrency;
  global.getPatients               = getPatients;
  global.getPrescriptions          = getPrescriptions;
  global.getPrescriptionsByPatient = getPrescriptionsByPatient;
}

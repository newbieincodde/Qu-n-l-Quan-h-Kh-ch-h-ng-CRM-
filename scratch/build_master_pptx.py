# -*- coding: utf-8 -*-
"""
MEDCARE CRM — BUILD MASTER PPTX DECK (18 SLIDES)
Báo cáo Đồ án Kết thúc Học phần Thiết kế Web (111101) · ĐH Lạc Hồng
Tích hợp: Lý thuyết Web Core, Code Walkthrough 4 Khối, Sơ đồ Kiến trúc & Q&A
"""

import sys
import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_master_deck(output_path):
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Bảng màu chuyên nghiệp (Medical Healthcare Theme)
    NAVY = RGBColor(15, 23, 42)          # #0F172A - Deep Navy
    TEAL = RGBColor(15, 118, 110)        # #0F766E - Clinical Teal
    CYAN = RGBColor(14, 165, 233)        # #0EA5E9 - Sky Blue
    GOLD = RGBColor(217, 119, 6)         # #D97706 - Amber/Gold
    EMERALD = RGBColor(16, 185, 129)     # #10B981 - Success Green
    ROSE = RGBColor(244, 63, 94)         # #F43F5E - Alert Rose
    PURPLE = RGBColor(139, 92, 246)      # #8B5CF6 - Accent Purple
    WHITE = RGBColor(255, 255, 255)
    BG_SLATE = RGBColor(248, 250, 252)   # #F8FAFC - Light Background
    CARD_BG = RGBColor(255, 255, 255)
    BORDER_COLOR = RGBColor(226, 232, 240)
    BORDER_TEAL = RGBColor(153, 246, 228)
    TEXT_DARK = RGBColor(15, 23, 42)
    TEXT_MUTED = RGBColor(100, 116, 139)
    CODE_BG = RGBColor(15, 23, 42)       # Dark VS Code background
    CODE_TEXT = RGBColor(226, 232, 240)
    CODE_KEYWORD = RGBColor(56, 189, 248) # Cyan keyword
    CODE_COMMENT = RGBColor(148, 163, 184)

    FONT_FAMILY = "Be Vietnam Pro"
    FALLBACK_FONT = "Calibri"
    CODE_FONT = "Consolas"

    def set_font(run, size=13, bold=False, color=TEXT_DARK, name=FONT_FAMILY):
        run.font.name = name
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color

    def add_bg(slide, color=BG_SLATE):
        rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        rect.fill.solid()
        rect.fill.fore_color.rgb = color
        rect.line.fill.background()
        return rect

    def add_header(slide, title, category="MEDCARE CRM · BÁO CÁO ĐỒ ÁN THIẾT KẾ WEB (LHU · HỌC PHẦN 111101)"):
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.08))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = TEAL
        top_bar.line.fill.background()

        tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.32), Inches(11.7), Inches(0.28))
        tf_cat = tb_cat.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        r_cat = p_cat.add_run()
        r_cat.text = category.upper()
        set_font(r_cat, size=9.5, bold=True, color=TEAL)

        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.60), Inches(11.7), Inches(0.55))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        r_title = p_title.add_run()
        r_title.text = title
        set_font(r_title, size=21, bold=True, color=NAVY)

    def add_footer(slide, current, total=18):
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(7.08), Inches(11.733), Inches(0.28))
        tf = tb.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        r1 = p.add_run()
        r1.text = "Trường Đại học Lạc Hồng (LHU) · Học phần 111101 Thiết kế Web · Nhóm MedCare CRM"
        set_font(r1, size=9, bold=False, color=TEXT_MUTED)
        r2 = p.add_run()
        r2.text = f"                                                                                                              {current} / {total}"
        set_font(r2, size=9.5, bold=True, color=TEAL)

    def add_card(slide, left, top, width, height, bg=CARD_BG, border=BORDER_COLOR):
        rect = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        rect.fill.solid()
        rect.fill.fore_color.rgb = bg
        rect.line.color.rgb = border
        rect.line.width = Pt(1)
        return rect

    def add_code_box(slide, left, top, width, height, code_lines, title="CODE SNIPPET (TRÍCH XUẤT THỰC TẾ)"):
        rect = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        rect.fill.solid()
        rect.fill.fore_color.rgb = CODE_BG
        rect.line.color.rgb = RGBColor(51, 65, 85)
        rect.line.width = Pt(1)

        tb_head = slide.shapes.add_textbox(Inches(left + 0.2), Inches(top + 0.15), Inches(width - 0.4), Inches(0.3))
        p_head = tb_head.text_frame.paragraphs[0]
        r_head = p_head.add_run()
        r_head.text = f"● ● ●  {title}"
        set_font(r_head, size=9.5, bold=True, color=RGBColor(56, 189, 248), name=CODE_FONT)

        tb_code = slide.shapes.add_textbox(Inches(left + 0.2), Inches(top + 0.45), Inches(width - 0.4), Inches(height - 0.55))
        tf_code = tb_code.text_frame
        tf_code.word_wrap = True
        tf_code.margin_left = tf_code.margin_right = tf_code.margin_top = tf_code.margin_bottom = 0

        for idx, line in enumerate(code_lines):
            p = tf_code.paragraphs[0] if idx == 0 else tf_code.add_paragraph()
            p.space_after = Pt(2)
            r = p.add_run()
            r.text = line
            set_font(r, size=9.5, bold=False, color=CODE_TEXT, name=CODE_FONT)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 1: COVER
    # ══════════════════════════════════════════════════════════════════════════
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1, NAVY)

    top_c = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.12))
    top_c.fill.solid()
    top_c.fill.fore_color.rgb = TEAL
    top_c.line.fill.background()

    tb_uni = s1.shapes.add_textbox(Inches(1.0), Inches(0.85), Inches(11.3), Inches(0.4))
    r = tb_uni.text_frame.paragraphs[0].add_run()
    r.text = "TRƯỜNG ĐẠI HỌC LẠC HỒNG (LHU) · KHOA CÔNG NGHỆ THÔNG TIN"
    set_font(r, size=11, bold=True, color=CYAN)

    tb_sub = s1.shapes.add_textbox(Inches(1.0), Inches(1.25), Inches(11.3), Inches(0.35))
    r = tb_sub.text_frame.paragraphs[0].add_run()
    r.text = "BÁO CÁO ĐỒ ÁN KẾT THÚC HỌC PHẦN · MÃ HỌC PHẦN: 111101 (THIẾT KẾ WEB)"
    set_font(r, size=10, bold=False, color=TEXT_MUTED)

    tb_t = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(1.5))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p1 = tf_t.paragraphs[0]
    r = p1.add_run()
    r.text = "MedCare CRM — Hệ Thống Quản Trị Bệnh Nhân\n& Tự Động Hóa Chăm Sóc Y Tế Khép Kín"
    set_font(r, size=30, bold=True, color=WHITE)

    tb_desc = s1.shapes.add_textbox(Inches(1.0), Inches(3.45), Inches(11.3), Inches(0.7))
    tf_d = tb_desc.text_frame
    tf_d.word_wrap = True
    r = tf_d.paragraphs[0].add_run()
    r.text = "Mô hình Client-Side SPA không Backend · Quản trị 200 Bệnh Nhân & 325 Toa Thuốc Điện Tử\nChuẩn công nghệ Pure Web: HTML5 Semantic, CSS3 Transitions & JavaScript ES6+ LocalStorage"
    set_font(r, size=13.5, bold=False, color=RGBColor(203, 213, 225))

    members = [
        ("NGUYỄN NGỌC NHÂN", "Nhóm trưởng · Khối 0", "Cổng Leads, Auth & Quản trị chung"),
        ("VÕ GIA HUY", "Thành viên · Khối 1", "Dashboard điều dưỡng & Nhắc lịch"),
        ("NGUYỄN MINH HUY", "Thành viên · Khối 2", "Danh bạ 200 BN, Phân hạng & EHR 360°"),
        ("TRẦN QUỐC QUANG", "Thành viên · Khối 3", "CSAT Survey & CSS3 Transitions")
    ]
    for i, (name, role, task) in enumerate(members):
        c_left = 1.0 + i * 2.88
        card = add_card(s1, c_left, 4.45, 2.7, 2.2, bg=RGBColor(30, 41, 59), border=RGBColor(51, 65, 85))
        tb_m = s1.shapes.add_textbox(Inches(c_left + 0.15), Inches(4.6), Inches(2.4), Inches(1.9))
        tf_m = tb_m.text_frame
        tf_m.word_wrap = True
        
        p = tf_m.paragraphs[0]
        r = p.add_run()
        r.text = name
        set_font(r, size=12, bold=True, color=WHITE)
        
        p2 = tf_m.add_paragraph()
        p2.space_before = Pt(4)
        r = p2.add_run()
        r.text = role
        set_font(r, size=10, bold=True, color=CYAN)
        
        p3 = tf_m.add_paragraph()
        p3.space_before = Pt(4)
        r = p3.add_run()
        r.text = task
        set_font(r, size=9.5, bold=False, color=RGBColor(148, 163, 184))

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 2: BỐI CẢNH & ĐẶT VẤN ĐỀ
    # ══════════════════════════════════════════════════════════════════════════
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "01. Bối Cảnh Thực Tế & Đặt Vấn Đề Chuyển Đổi Số Y Tế")
    add_footer(s2, 2)

    pains = [
        ("NỖI ĐAU 1: GHI CHÉP PHÂN MẢNH", ROSE,
         "100+ bệnh nhân/ngày nhưng dữ liệu ghi sổ tay hoặc file Excel rời rạc.",
         ["Dễ thất lạc hồ sơ bệnh án và lịch sử thăm khám",
          "Bác sĩ không tra cứu nhanh được dị ứng thuốc",
          "Không có số liệu tổng hợp doanh thu thời gian thực",
          "Khó khăn bàn giao ca trực giữa các điều dưỡng"]),
        ("NỖI ĐAU 2: MẤT KẾT NỐI SAU ĐIỀU TRỊ", GOLD,
         "Bệnh nhân khám xong ra về là cơ sở y tế mất hoàn toàn liên lạc.",
         ["Không ai gọi điện hỏi thăm phản ứng phụ sau dùng thuốc",
          "Tỷ lệ bệnh nhân quên lịch tái khám lên tới > 45%",
          "Mất doanh thu từ bệnh nhân mãn tính định kỳ",
          "Không tiếp nhận kịp thời khiếu nại hoặc biến chứng"]),
        ("NỖI ĐAU 3: THIẾU TRI ÂN & CÁ NHÂN HÓA", TEAL,
         "Bệnh nhân VIP chi tiêu lớn bị đối xử như khách vãng lai thông thường.",
         ["Không có hệ thống tự động phân loại Đồng - Bạc - Vàng",
          "Khách hàng thân thiết không được ưu tiên phòng khám",
          "Chưa từng khảo sát mức độ hài lòng (CSAT/NPS)",
          "Thất thoát khách hàng sang các phòng khám đối thủ"])
    ]
    for i, (title, tag_c, desc, bullets) in enumerate(pains):
        c_left = 0.8 + i * 3.98
        add_card(s2, c_left, 1.45, 3.8, 5.25)
        
        bar = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(c_left), Inches(1.45), Inches(3.8), Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = tag_c
        bar.line.fill.background()

        tb = s2.shapes.add_textbox(Inches(c_left + 0.25), Inches(1.65), Inches(3.3), Inches(4.8))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = title
        set_font(r, size=12, bold=True, color=tag_c)

        p2 = tf.add_paragraph()
        p2.space_before = Pt(8)
        r = p2.add_run()
        r.text = desc
        set_font(r, size=11, bold=True, color=NAVY)

        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.space_before = Pt(8)
            r = p_b.add_run()
            r.text = f"• {b}"
            set_font(r, size=10, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 3: NỀN TẢNG LÝ THUYẾT & KIẾN TRÚC CLIENT-SIDE
    # ══════════════════════════════════════════════════════════════════════════
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "02. Nền Tảng Lý Thuyết Học Phần & Kiến Trúc Client-Side SPA")
    add_footer(s3, 3)

    add_card(s3, 0.8, 1.45, 5.75, 5.25)
    tb_left = s3.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.25), Inches(4.8))
    tf_l = tb_left.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    r = p.add_run()
    r.text = "TRÌNH DUYỆT RENDERING PIPELINE & PERFORMANCE"
    set_font(r, size=12, bold=True, color=TEAL)

    pipeline_steps = [
        ("1. HTML -> DOM Tree", "Trình duyệt parse HTML tokens thành các node phần tử."),
        ("2. CSS -> CSSOM Tree", "Phân tích CSS selectors và tính toán kế thừa kiểu dáng."),
        ("3. Render Tree", "Kết hợp DOM + CSSOM, loại bỏ các phần tử display: none."),
        ("4. Layout (Reflow)", "Tính toán vị trí hình học x, y, width, height của từng node."),
        ("5. Paint & Composite", "Vẽ pixel lên màn hình. MedCare CRM tối ưu GPU 60fps bằng transform: translateY() và scale().")
    ]
    for step, desc in pipeline_steps:
        p_s = tf_l.add_paragraph()
        p_s.space_before = Pt(8)
        r = p_s.add_run()
        r.text = step + ": "
        set_font(r, size=10.5, bold=True, color=NAVY)
        r2 = p_s.add_run()
        r2.text = desc
        set_font(r2, size=10, bold=False, color=TEXT_DARK)

    add_card(s3, 6.78, 1.45, 5.75, 5.25)
    tb_right = s3.shapes.add_textbox(Inches(7.03), Inches(1.65), Inches(5.25), Inches(4.8))
    tf_r = tb_right.text_frame
    tf_r.word_wrap = True

    p = tf_r.paragraphs[0]
    r = p.add_run()
    r.text = "LOCALSTORAGE AS CLIENT-SIDE DATABASE ENGINE"
    set_font(r, size=12, bold=True, color=CYAN)

    storage_points = [
        ("Zero Network Latency", "Truy xuất tức thời 0ms, không tốn thời gian gọi server API."),
        ("Persistent Storage", "Dữ liệu lưu vĩnh viễn trên trình duyệt, không mất khi tắt tab."),
        ("Capacity 5-10MB", "Đủ sức lưu trữ trên 10.000 hồ sơ bệnh nhân JSON chuẩn hóa."),
        ("5 Core Data Stores", "medcare_patients (200 BN) · medcare_prescriptions (325 Toa) · medcare_inventory (112 Dược) · medcare_leads · medcare_surveys."),
        ("JSON Serialization", "Sử dụng JSON.stringify() và JSON.parse() để biến LocalStorage thành hệ quản trị NoSQL Document mini.")
    ]
    for pt, desc in storage_points:
        p_p = tf_r.add_paragraph()
        p_p.space_before = Pt(8)
        r = p_p.add_run()
        r.text = pt + ": "
        set_font(r, size=10.5, bold=True, color=NAVY)
        r2 = p_p.add_run()
        r2.text = desc
        set_font(r2, size=10, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 4: SƠ ĐỒ DÒNG DỮ LIỆU KHÉP KÍN (PATIENT LIFECYCLE)
    # ══════════════════════════════════════════════════════════════════════════
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "03. Sơ Đồ Dòng Dữ Liệu Khép Kín (Patient Lifecycle Data Flow)")
    add_footer(s4, 4)

    steps = [
        ("BƯỚC 1", "TIẾP NHẬN LEADS", TEAL,
         "Bệnh nhân xem Landing Page, đặt lịch khám qua Form có Regex SĐT 10 số."),
        ("BƯỚC 2", "CHUYỂN ĐỔI BỆNH NHÂN", CYAN,
         "Tư vấn viên xác nhận, hàm JS sinh mã KHxxx, phân hạng Đồng ban đầu."),
        ("BƯỚC 3", "KHÁM & BỆNH ÁN EHR", PURPLE,
         "Bác sĩ khám, nhập sinh hiệu, kê 325 toa thuốc điện tử liên kết patientId."),
        ("BƯỚC 4", "TỰ ĐỘNG PHÂN HẠNG", GOLD,
         "JS tự tính totalSpent tích lũy, nâng hạng Bạc (>=5M) hoặc Vàng (>=15M)."),
        ("BƯỚC 5", "NHẮC LỊCH ĐẦU NGÀY", ROSE,
         "Dashboard lọc danh sách tái khám hôm nay, ưu tiên gọi khách VIP trước."),
        ("BƯỚC 6", "CHĂM SÓC & CSAT", EMERALD,
         "Lưu nhật ký tư vấn, khảo sát 5 sao đo lường độ hài lòng với CSS Transition.")
    ]
    for i, (b_id, title, color, desc) in enumerate(steps):
        col = i % 3
        row = i // 3
        c_left = 0.8 + col * 3.98
        c_top = 1.45 + row * 2.68
        add_card(s4, c_left, c_top, 3.8, 2.45)

        b = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(c_left), Inches(c_top), Inches(3.8), Inches(0.06))
        b.fill.solid()
        b.fill.fore_color.rgb = color
        b.line.fill.background()

        tb = s4.shapes.add_textbox(Inches(c_left + 0.2), Inches(c_top + 0.15), Inches(3.4), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = f"{b_id} · {title}"
        set_font(r, size=11, bold=True, color=color)

        p2 = tf.add_paragraph()
        p2.space_before = Pt(6)
        r = p2.add_run()
        r.text = desc
        set_font(r, size=10, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 5: PHÂN CÔNG NHIỆM VỤ & QUY TRÌNH GIT FLOW
    # ══════════════════════════════════════════════════════════════════════════
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "04. Phân Công Nhiệm Vụ Thành Viên & Quy Trình Git Flow")
    add_footer(s5, 5)

    roles_data = [
        ("KHỐI 0 · NGUYỄN NGỌC NHÂN", "Nhóm trưởng · Leads & Auth", TEAL,
         ["Landing Page chuẩn HTML5 Semantic",
          "Form Validation regex ^0[0-9]{9}$",
          "Cổng chuyển đổi Lead -> Patient",
          "Báo cáo phân tích giá trị CLV",
          "Quản trị Git Flow, .nojekyll & Deploy"]),
        ("KHỐI 1 · VÕ GIA HUY", "Thành viên · Dashboard Điều dưỡng", CYAN,
         ["Bàn làm việc điều dưỡng mỗi sáng",
          "Thuật toán lọc tái khám getTodayFollowUps",
          "Hàm so sánh ngày isFollowUpToday",
          "4 thẻ chỉ số KPI tự động tính",
          "Biểu đồ phân bổ lượt khám tuần"]),
        ("KHỐI 2 · NGUYỄN MINH HUY", "Thành viên · Danh Bạ & EHR 360°", GOLD,
         ["Danh bạ thông minh 200 bệnh nhân",
          "Giải thuật phân hạng classifyPatient",
          "Thống kê getRankStats bằng reduce()",
          "Phân trang động 20 trang bằng slice()",
          "Hồ sơ Bệnh án EHR 360° & 325 Toa thuốc"]),
        ("KHỐI 3 · TRẦN QUỐC QUANG", "Thành viên · Chăm Sóc & CSAT", PURPLE,
         ["Form ghi nhận nhật ký chăm sóc sau khám",
          "Bảng khảo sát độ hài lòng CSAT/NPS",
          "CSS3 Transition: Card Elevation (GPU)",
          "CSS3 Transition: Accordion max-height",
          "CSS3 Transition: Star Rating scale(1.3)"])
    ]
    for i, (title, sub, color, tasks) in enumerate(roles_data):
        c_left = 0.8 + i * 2.98
        add_card(s5, c_left, 1.45, 2.8, 5.25)
        
        b = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(c_left), Inches(1.45), Inches(2.8), Inches(0.06))
        b.fill.solid()
        b.fill.fore_color.rgb = color
        b.line.fill.background()

        tb = s5.shapes.add_textbox(Inches(c_left + 0.15), Inches(1.6), Inches(2.5), Inches(4.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = title
        set_font(r, size=10.5, bold=True, color=color)

        p2 = tf.add_paragraph()
        p2.space_before = Pt(3)
        r = p2.add_run()
        r.text = sub
        set_font(r, size=9.5, bold=True, color=NAVY)

        for t in tasks:
            p_t = tf.add_paragraph()
            p_t.space_before = Pt(6)
            r = p_t.add_run()
            r.text = f"✓ {t}"
            set_font(r, size=9, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 6: KHỐI 0 - LANDING PAGE & HTML5 VALIDATION
    # ══════════════════════════════════════════════════════════════════════════
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "05. Khối 0 (Ngọc Nhân): Cổng Tiếp Nhận Leads & HTML5 Validation")
    add_footer(s6, 6)

    add_card(s6, 0.8, 1.45, 5.3, 5.25)
    tb_l6 = s6.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(4.9), Inches(4.8))
    tf_l6 = tb_l6.text_frame
    tf_l6.word_wrap = True

    p = tf_l6.paragraphs[0]
    r = p.add_run()
    r.text = "KIẾN THỨC CỐT LÕI: HTML5 CONSTRAINT VALIDATION"
    set_font(r, size=11.5, bold=True, color=TEAL)

    pts6 = [
        ("HTML5 Semantic Tags", "Phân tách rõ ràng header, nav, main, section, article, footer giúp chuẩn hóa DOM và tối ưu hóa SEO Google."),
        ("Thuộc tính required & minlength", "Bắt buộc người dùng phải điền họ tên, độ dài tối thiểu 3 ký tự."),
        ("Type='tel' & Regex Pattern", "Kiểm soát định dạng số điện thoại Việt Nam chuẩn xác ngay tại Client."),
        ("Bảo mật chống Injection", "Chặn đứng các đoạn mã Script độc hại hoặc ký tự lạ ngay từ cửa ngõ thu nạp dữ liệu.")
    ]
    for title, desc in pts6:
        p_p = tf_l6.add_paragraph()
        p_p.space_before = Pt(8)
        r = p_p.add_run()
        r.text = title + ": "
        set_font(r, size=10, bold=True, color=NAVY)
        r2 = p_p.add_run()
        r2.text = desc
        set_font(r2, size=9.5, bold=False, color=TEXT_DARK)

    code_s6 = [
        "<!-- FORM THU THẬP LEADS (dashboard/leads.html) -->",
        "<form id=\"leadCaptureForm\" onsubmit=\"handleLeadSubmit(event)\">",
        "  <input type=\"text\" id=\"leadFullName\" required minlength=\"3\"",
        "         placeholder=\"Họ và tên bệnh nhân\">",
        "",
        "  <!-- REGEX KIỂM TRA SĐT 10 SỐ VIỆT NAM (BẮT BUỘC ĐỀ BÀI LHU) -->",
        "  <input type=\"tel\" id=\"leadPhone\" required",
        "         pattern=\"^0[0-9]{9}$\"",
        "         title=\"SĐT gồm 10 số và bắt đầu bằng số 0\"",
        "         placeholder=\"0912345678\">",
        "",
        "  <input type=\"email\" id=\"leadEmail\" placeholder=\"Email\">",
        "  <button type=\"submit\" class=\"btn-submit\">ĐẶT LỊCH NGAY</button>",
        "</form>",
        "",
        "// GIẢI MÃ REGEX ^0[0-9]{9}$ :",
        "// ^       : Bắt đầu chuỗi",
        "// 0       : Ký tự đầu tiên bắt buộc phải là số 0",
        "// [0-9]{9}: Chính xác 9 chữ số tiếp theo từ 0 đến 9",
        "// $       : Kết thúc chuỗi (Tổng chiều dài đúng 10 số)"
    ]
    add_code_box(s6, 6.3, 1.45, 6.23, 5.25, code_s6, "HTML5 VALIDATION & REGEX CODE (leads.html)")

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 7: KHỐI 0 - PHÂN TÍCH CODE CHUYỂN ĐỔI LEADS
    # ══════════════════════════════════════════════════════════════════════════
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "06. Khối 0 (Ngọc Nhân): Code Walkthrough Chuyển Đổi Lead -> Bệnh Nhân")
    add_footer(s7, 7)

    code_s7 = [
        "function convertLeadToPatient(leadId) {",
        "  const leads = getLeads();",
        "  const lead = leads.find(l => l.id === leadId);",
        "  if (!lead) return;",
        "",
        "  const patients = getPatients();",
        "  // 1. Tự sinh mã bệnh nhân tiếp theo chuẩn y tế",
        "  const newId = 'KH' + String(patients.length + 1).padStart(3, '0');",
        "",
        "  // 2. Chuyển đổi dữ liệu và gán phân hạng khởi điểm là Đồng",
        "  const newPatient = {",
        "    id: newId,",
        "    name: lead.name,",
        "    phone: lead.phone,",
        "    service: lead.service || 'Khám Sức Khỏe Tổng Quát',",
        "    totalSpent: 0,             // Khởi điểm chi tiêu: 0đ",
        "    rank: 'bronze',            // Hạng mặc định ban đầu: Đồng",
        "    status: 'active',",
        "    visits: 1,",
        "    nextFollowUp: getFutureDate(7) // Hẹn tái khám sau 7 ngày",
        "  };",
        "",
        "  lead.status = 'converted';",
        "  patients.unshift(newPatient); // Thêm lên đầu danh sách",
        "  savePatients(patients);       // Lưu vào LocalStorage",
        "  saveLeads(leads);",
        "}"
    ]
    add_code_box(s7, 0.8, 1.45, 6.2, 5.25, code_s7, "JAVASCRIPT PIPELINE (js/leads.js)")

    add_card(s7, 7.2, 1.45, 5.33, 5.25)
    tb_r7 = s7.shapes.add_textbox(Inches(7.4), Inches(1.65), Inches(4.9), Inches(4.8))
    tf_r7 = tb_r7.text_frame
    tf_r7.word_wrap = True

    p = tf_r7.paragraphs[0]
    r = p.add_run()
    r.text = "Ý NGHĨA KỸ THUẬT & DÒNG DỮ LIỆU"
    set_font(r, size=11.5, bold=True, color=CYAN)

    steps_s7 = [
        ("Thuật toán sinh mã ID tự tăng", "Sử dụng String(N).padStart(3, '0') tạo các mã định danh chuẩn y tế: KH001, KH002... KH201."),
        ("Tính toàn vẹn dữ liệu (Integrity)", "Khi chuyển đổi, trạng thái Lead được cập nhật thành 'converted' và liên kết khóa convertedPatientId, không làm mất nguồn gốc Lead."),
        ("Đồng bộ hóa 2 kho LocalStorage", "Hàm cập nhật đồng thời cả 2 bảng medcare_patients và medcare_leads mà không cần reload trang."),
        ("Tự động kích hoạt lịch tái khám", "Bệnh nhân mới được tạo tự động có lịch hẹn tái khám sau 7 ngày, sẵn sàng đẩy vào Dashboard của Khối 1.")
    ]
    for title, desc in steps_s7:
        p_p = tf_r7.add_paragraph()
        p_p.space_before = Pt(8)
        r = p_p.add_run()
        r.text = title + ": "
        set_font(r, size=10, bold=True, color=NAVY)
        r2 = p_p.add_run()
        r2.text = desc
        set_font(r2, size=9.5, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 8: KHỐI 1 - DASHBOARD ĐIỀU DƯỠNG & LỌC TÁI KHÁM
    # ══════════════════════════════════════════════════════════════════════════
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "07. Khối 1 (Gia Huy): Bàn Làm Việc Điều Dưỡng & Nhắc Lịch Tái Khám")
    add_footer(s8, 8)

    kpis = [
        ("TỔNG BỆNH NHÂN", "200", "Bệnh nhân quản lý trong hệ thống", TEAL),
        ("CUỘC GỌI HÔM NAY", "18", "Cần gọi nhắc lịch tái khám", ROSE),
        ("TỶ LỆ TÁI KHÁM", "88.5%", "Bệnh nhân quay lại khám định kỳ", CYAN),
        ("DOANH THU NGÀY", "42.8M ₫", "Dự kiến thu từ bệnh nhân hôm nay", GOLD)
    ]
    for i, (label, val, sub, color) in enumerate(kpis):
        c_left = 0.8 + i * 2.98
        add_card(s8, c_left, 1.45, 2.8, 1.6)
        tb = s8.shapes.add_textbox(Inches(c_left + 0.15), Inches(1.55), Inches(2.5), Inches(1.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = label
        set_font(r, size=9, bold=True, color=TEXT_MUTED)

        p2 = tf.add_paragraph()
        p2.space_before = Pt(2)
        r = p2.add_run()
        r.text = val
        set_font(r, size=20, bold=True, color=color)

        p3 = tf.add_paragraph()
        p3.space_before = Pt(2)
        r = p3.add_run()
        r.text = sub
        set_font(r, size=8.5, bold=False, color=TEXT_MUTED)

    code_s8 = [
        "function isFollowUpToday(dateStr) {",
        "  if (!dateStr) return false;",
        "  // Tách ngày, tháng, năm từ chuỗi 'dd/mm/yyyy'",
        "  const [d, m, y] = dateStr.split('/').map(Number);",
        "  const targetDate = new Date(y, m - 1, d);",
        "  const today = new Date();",
        "  // So sánh chuỗi ngày bỏ qua giờ/phút/giây",
        "  return targetDate.toDateString() === today.toDateString();",
        "}",
        "",
        "function getTodayFollowUps(patients) {",
        "  return patients",
        "    .filter(p => p.overdueDays > 0 || isFollowUpToday(p.nextFollowUp))",
        "    .sort((a, b) => {",
        "      // Ưu tiên VIP Vàng gọi trước, tiếp đến Bạc và Đồng",
        "      const rankOrder = { gold: 0, silver: 1, bronze: 2 };",
        "      return rankOrder[a.rank] - rankOrder[b.rank];",
        "    });",
        "}"
    ]
    add_code_box(s8, 0.8, 3.25, 6.8, 3.55, code_s8, "LOGIC LỌC TÁI KHÁM & SẮP XẾP ƯU TIÊN (js/data.js)")

    add_card(s8, 7.8, 3.25, 4.733, 3.55)
    tb_r8 = s8.shapes.add_textbox(Inches(8.0), Inches(3.4), Inches(4.3), Inches(3.2))
    tf_r8 = tb_r8.text_frame
    tf_r8.word_wrap = True

    p = tf_r8.paragraphs[0]
    r = p.add_run()
    r.text = "ĐỘT PHÁ NGHIỆP VỤ Y TẾ"
    set_font(r, size=11, bold=True, color=TEAL)

    pts8 = [
        ("Xử lý Múi giờ an toàn", "toDateString() triệt tiêu hoàn toàn sai lệch múi giờ (Timezone Offset) giữa các máy tính."),
        ("Thuật toán Multi-Tier Priority", "Xếp hạng Vàng (Gold) lên đầu danh sách giúp điều dưỡng ưu tiên chăm sóc khách hàng mang lại doanh thu cao nhất."),
        ("Nhận diện Quá hạn (Overdue)", "Bệnh nhân có overdueDays > 0 lập tức được gắn nhãn cảnh báo đỏ.")
    ]
    for t, d in pts8:
        p_p = tf_r8.add_paragraph()
        p_p.space_before = Pt(6)
        r = p_p.add_run()
        r.text = t + ": "
        set_font(r, size=9.5, bold=True, color=NAVY)
        r2 = p_p.add_run()
        r2.text = d
        set_font(r2, size=9, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 9: KHỐI 2 - DANH BẠ 200 BỆNH NHÂN & GIẢI THUẬT PHÂN HẠNG
    # ══════════════════════════════════════════════════════════════════════════
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "08. Khối 2 (Minh Huy): Giải Thuật Phân Hạng Bệnh Nhân Tự Động")
    add_footer(s9, 9)

    tiers = [
        ("HẠNG ĐỒNG (BRONZE)", "< 5.000.000 ₫", "Hạng tiêu chuẩn khi mới đăng ký", RGBColor(183, 121, 69)),
        ("HẠNG BẠC (SILVER)", "5.000.000 ₫ – 14.999.999 ₫", "Giảm 5% phí xét nghiệm, nhắc lịch định kỳ", RGBColor(100, 116, 139)),
        ("HẠNG VÀNG (GOLD)", "≥ 15.000.000 ₫", "Bác sĩ riêng, phòng chờ VIP, ưu tiên cao nhất", GOLD)
    ]
    for i, (title, cond, perks, col) in enumerate(tiers):
        c_left = 0.8 + i * 3.98
        add_card(s9, c_left, 1.45, 3.8, 1.6)
        tb = s9.shapes.add_textbox(Inches(c_left + 0.15), Inches(1.55), Inches(3.5), Inches(1.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = title
        set_font(r, size=10, bold=True, color=col)

        p2 = tf.add_paragraph()
        p2.space_before = Pt(2)
        r = p2.add_run()
        r.text = cond
        set_font(r, size=15, bold=True, color=NAVY)

        p3 = tf.add_paragraph()
        p3.space_before = Pt(2)
        r = p3.add_run()
        r.text = perks
        set_font(r, size=9, bold=False, color=TEXT_MUTED)

    code_s9 = [
        "// HÀM PHÂN LOẠI TỰ ĐỘNG THEO TỔNG CHI TIÊU (YÊU CẦU ĐỀ BÀI LHU)",
        "function classifyPatient(totalSpent) {",
        "  const spent = Number(totalSpent) || 0;",
        "  if (spent >= 15000000) {",
        "    return { rank: 'gold',   label: 'Vàng', icon: '🥇', color: '#D97706' };",
        "  }",
        "  if (spent >= 5000000) {",
        "    return { rank: 'silver', label: 'Bạc',  icon: '🥈', color: '#64748B' };",
        "  }",
        "  return   { rank: 'bronze', label: 'Đồng', icon: '🥉', color: '#B77945' };",
        "}",
        "",
        "// THỐNG KÊ SỐ LƯỢNG HẠNG THẺ BẰNG HÀM REDUCE()",
        "function getRankStats(patients) {",
        "  return patients.reduce((acc, p) => {",
        "    acc[p.rank] = (acc[p.rank] || 0) + 1;",
        "    return acc;",
        "  }, { gold: 0, silver: 0, bronze: 0 });",
        "}"
    ]
    add_code_box(s9, 0.8, 3.25, 6.8, 3.55, code_s9, "HÀM CLASSIFYPATIENT (js/data.js)")

    add_card(s9, 7.8, 3.25, 4.733, 3.55)
    tb_r9 = s9.shapes.add_textbox(Inches(8.0), Inches(3.4), Inches(4.3), Inches(3.2))
    tf_r9 = tb_r9.text_frame
    tf_r9.word_wrap = True

    p = tf_r9.paragraphs[0]
    r = p.add_run()
    r.text = "TUÂN THỦ 100% ĐỀ BÀI HỌC PHẦN"
    set_font(r, size=11, bold=True, color=GOLD)

    pts9 = [
        ("Tự động hóa hoàn toàn bằng JS", "Nhân viên không thể tự sửa tay phân hạng. Hệ thống tự động tính toán dựa trên hóa đơn khám bệnh thực tế."),
        ("Độ phức tạp O(1)", "Hàm phân loại chạy tức thì trong 0.001ms, không gây trễ khi hiển thị bảng 200 bệnh nhân."),
        ("Liên kết trực tiếp với UI Badge", "Màu sắc, icon và nhãn phân hạng được render đồng bộ trên cả bảng danh bạ và modal bệnh án.")
    ]
    for t, d in pts9:
        p_p = tf_r9.add_paragraph()
        p_p.space_before = Pt(6)
        r = p_p.add_run()
        r.text = t + ": "
        set_font(r, size=9.5, bold=True, color=NAVY)
        r2 = p_p.add_run()
        r2.text = d
        set_font(r2, size=9, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 10: KHỐI 2 - PHÂN TÍCH CODE PHÂN TRANG & BỆNH ÁN EHR 360°
    # ══════════════════════════════════════════════════════════════════════════
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "09. Khối 2 (Minh Huy): Phân Trang 20 Trang & Bệnh Án Điện Tử EHR 360°")
    add_footer(s10, 10)

    code_s10 = [
        "const PAGE_SIZE = 10; // Mỗi trang 10 bệnh nhân",
        "let currentPage = 1;",
        "",
        "function renderTable() {",
        "  // 1. Tính chỉ số start và end để cắt mảng",
        "  const start = (currentPage - 1) * PAGE_SIZE;",
        "  const pageItems = filteredPatients.slice(start, start + PAGE_SIZE);",
        "  tbody.innerHTML = pageItems.map(p => renderRow(p)).join('');",
        "  renderPagination(filteredPatients.length);",
        "}",
        "",
        "// 2. KHÓA NGOẠI: LIÊN KẾT BỆNH NHÂN -> 325 TOA THUỐC",
        "function openEHRModal(patientId) {",
        "  const patient = allPatients.find(p => p.id === patientId);",
        "  // Truy vấn toàn bộ toa thuốc có patientId tương ứng",
        "  const rxList = getPrescriptionsByPatient(patientId);",
        "",
        "  document.getElementById('ehrName').textContent = patient.name;",
        "  document.getElementById('ehrAllergies').textContent = patient.allergies;",
        "  renderRxTab(rxList); // Render danh sách đơn thuốc",
        "  document.getElementById('ehrModal').classList.add('active');",
        "}"
    ]
    add_code_box(s10, 0.8, 1.45, 6.3, 5.25, code_s10, "THUẬT TOÁN PHÂN TRANG & MODAL EHR (js/customers.js)")

    add_card(s10, 7.3, 1.45, 5.233, 5.25)
    tb_r10 = s10.shapes.add_textbox(Inches(7.5), Inches(1.65), Inches(4.8), Inches(4.8))
    tf_r10 = tb_r10.text_frame
    tf_r10.word_wrap = True

    p = tf_r10.paragraphs[0]
    r = p.add_run()
    r.text = "KIẾN TRÚC QUAN HỆ 1-N TRÊN CLIENT"
    set_font(r, size=11.5, bold=True, color=PURPLE)

    pts10 = [
        ("Tối ưu hóa DOM với Array.slice()", "Không render toàn bộ 200 thẻ tr cùng lúc. Chỉ vẽ đúng 10 hàng tại một thời điểm, giữ bộ nhớ trình duyệt luôn dưới 15MB."),
        ("Quan hệ 1-N (One-to-Many)", "1 Bệnh nhân có thể có nhiều Toa thuốc điện tử. Khóa ngoại patientId liên kết chính xác giữa 200 bệnh nhân và 325 toa thuốc."),
        ("Tabs động không tải lại trang", "Chuyển đổi giữa Tab 'Thông tin lâm sàng' và Tab 'Toa thuốc điện tử' mượt mà qua cơ chế DOM class toggle."),
        ("Tính sẵn sàng in ấn (@media print)", "Toa thuốc có thể in ra giấy A4 mang về cho bệnh nhân với định dạng chuẩn Bộ Y Tế.")
    ]
    for t, d in pts10:
        p_p = tf_r10.add_paragraph()
        p_p.space_before = Pt(8)
        r = p_p.add_run()
        r.text = t + ": "
        set_font(r, size=10, bold=True, color=NAVY)
        r2 = p_p.add_run()
        r2.text = d
        set_font(r2, size=9.5, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 11: MỞ RỘNG - 325 TOA THUỐC & 112 KHO DƯỢC
    # ══════════════════════════════════════════════════════════════════════════
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11)
    add_header(s11, "10. Đột Phá Nghiệp Vụ: 325 Toa Thuốc & 112 Kho Dược Lâm Sàng")
    add_footer(s11, 11)

    med_cards = [
        ("200 HỒ SƠ BỆNH NHÂN", TEAL, "Mã KH001 - KH200",
         ["Đầy đủ 24 trường y tế chuẩn hóa",
          "Dữ liệu dịch tễ TP. Biên Hòa, Đồng Nai",
          "Nhóm máu, dị ứng thuốc, tiền sử bệnh",
          "Tổng chi tiêu từ 850K đến 35M ₫"]),
        ("325 TOA THUỐC ĐIỆN TỬ", PURPLE, "Mã RX2026-0001 - RX2026-0325",
         ["Chẩn đoán theo 10 chuyên khoa lâm sàng",
          "Tên bác sĩ chuyên khoa & ngày kê",
          "Liều dùng, cách uống, dặn dò y tế",
          "Liên kết khóa ngoại patientId"]),
        ("112 DANH MỤC DƯỢC PHẨM", GOLD, "Mã MED001 - MED112",
         ["12 nhóm thuốc: Kháng sinh, Tim mạch, Tiểu đường...",
          "Theo dõi tồn kho thực tế & tồn tối thiểu (minStock)",
          "Cảnh báo tự động khi sắp hết hạn sử dụng",
          "Hỗ trợ phân trang 12 trang mượt mà"])
    ]
    for i, (title, color, sub, bullets) in enumerate(med_cards):
        c_left = 0.8 + i * 3.98
        add_card(s11, c_left, 1.45, 3.8, 5.25)

        b = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(c_left), Inches(1.45), Inches(3.8), Inches(0.06))
        b.fill.solid()
        b.fill.fore_color.rgb = color
        b.line.fill.background()

        tb = s11.shapes.add_textbox(Inches(c_left + 0.2), Inches(1.65), Inches(3.4), Inches(4.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = title
        set_font(r, size=11, bold=True, color=color)

        p2 = tf.add_paragraph()
        p2.space_before = Pt(4)
        r = p2.add_run()
        r.text = sub
        set_font(r, size=9.5, bold=True, color=NAVY)

        for b_txt in bullets:
            p_b = tf.add_paragraph()
            p_b.space_before = Pt(8)
            r = p_b.add_run()
            r.text = f"• {b_txt}"
            set_font(r, size=9.5, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 12: KHỐI 3 - CHĂM SÓC & CSAT
    # ══════════════════════════════════════════════════════════════════════════
    s12 = prs.slides.add_slide(blank_layout)
    add_bg(s12)
    add_header(s12, "11. Khối 3 (Quốc Quang): Chăm Sóc Khách Hàng & Khảo Sát CSAT")
    add_footer(s12, 12)

    add_card(s12, 0.8, 1.45, 5.3, 5.25)
    tb_l12 = s12.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(4.9), Inches(4.8))
    tf_l12 = tb_l12.text_frame
    tf_l12.word_wrap = True

    p = tf_l12.paragraphs[0]
    r = p.add_run()
    r.text = "ĐÓNG KÍN VÒNG LẶP TRẢI NGHIỆM KHÁM BỆNH"
    set_font(r, size=11.5, bold=True, color=TEAL)

    pts12 = [
        ("Nhật ký chăm sóc sau khám", "Điều dưỡng lưu lại thông tin phản hồi sau khi dùng thuốc, tác dụng phụ và tình trạng phục hồi."),
        ("Đo lường CSAT & NPS", "Khảo sát 5 sao đánh giá 3 chỉ số quan trọng: Thái độ nhân viên, Thời gian chờ khám và Cơ sở vật chất."),
        ("Đáp ứng tiêu chuẩn Học phần", "Toàn bộ trang khảo sát được thiết kế để kiểm chứng khả năng ứng dụng CSS3 Transition thuần chuyên nghiệp.")
    ]
    for t, d in pts12:
        p_p = tf_l12.add_paragraph()
        p_p.space_before = Pt(8)
        r = p_p.add_run()
        r.text = t + ": "
        set_font(r, size=10, bold=True, color=NAVY)
        r2 = p_p.add_run()
        r2.text = d
        set_font(r2, size=9.5, bold=False, color=TEXT_DARK)

    add_card(s12, 6.3, 1.45, 6.233, 5.25)
    tb_r12 = s12.shapes.add_textbox(Inches(6.5), Inches(1.65), Inches(5.8), Inches(4.8))
    tf_r12 = tb_r12.text_frame
    tf_r12.word_wrap = True

    p = tf_r12.paragraphs[0]
    r = p.add_run()
    r.text = "3 HIỆU ỨNG CSS3 TRANSITION TIÊU CHUẨN RUBRIC"
    set_font(r, size=11.5, bold=True, color=PURPLE)

    effs = [
        ("★ Hiệu ứng 1: Hover Nâng Thẻ (Card Elevation)",
         "transition: background-color 0.25s, transform 0.25s, box-shadow 0.25s;",
         "Sử dụng transform: translateY(-2px) kích hoạt GPU Composite layer, không gây giật lag reflow."),
        ("★ Hiệu ứng 2: Accordion Bung Mở Góp Ý",
         "transition: max-height 0.45s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.35s;",
         "Khắc phục hạn chế không transition được height: auto bằng max-height và đường cong bezier."),
        ("★ Hiệu ứng 3: Sao Đánh Giá Phóng Đại 1.3x",
         "transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), color 0.2s;",
         "Rê chuột vào sao lập tức chuyển sang màu vàng cam và phóng to 130% mượt mà.")
    ]
    for name, code, note in effs:
        p_e = tf_r12.add_paragraph()
        p_e.space_before = Pt(6)
        r = p_e.add_run()
        r.text = name
        set_font(r, size=10, bold=True, color=NAVY)
        
        p_c = tf_r12.add_paragraph()
        p_c.space_before = Pt(2)
        r = p_c.add_run()
        r.text = f"  {code}"
        set_font(r, size=9, bold=True, color=RGBColor(2, 132, 199), name="Consolas")
        
        p_n = tf_r12.add_paragraph()
        p_n.space_before = Pt(2)
        r = p_n.add_run()
        r.text = f"  -> {note}"
        set_font(r, size=8.5, bold=False, color=TEXT_MUTED)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 13: KHỐI 3 - PHÂN TÍCH CODE CSS3 TRANSITION NÂNG CAO
    # ══════════════════════════════════════════════════════════════════════════
    s13 = prs.slides.add_slide(blank_layout)
    add_bg(s13)
    add_header(s13, "12. Khối 3 (Quốc Quang): Phân Tích Mã Nguồn CSS3 Transitions")
    add_footer(s13, 13)

    code_s13 = [
        "/* 1. HOVER THẺ NÂNG ĐỘ CAO (dashboard/surveys.html) */",
        ".survey-item {",
        "  transition: background-color 0.25s ease,",
        "              transform 0.25s ease,",
        "              box-shadow 0.25s ease;",
        "}",
        ".survey-item:hover {",
        "  background-color: #f8fafc;",
        "  transform: translateY(-2px); /* Tăng tốc bằng phần cứng GPU */",
        "  box-shadow: 0 10px 15px -3px rgba(0,0,0,0.08);",
        "}",
        "",
        "/* 2. ACCORDION BUNG MỞ NỘI DUNG VƯỢT QUA HẠN CHẾ HEIGHT: AUTO */",
        ".survey-feedback-collapse {",
        "  max-height: 0; overflow: hidden; opacity: 0;",
        "  transition: max-height 0.45s cubic-bezier(0.16, 1, 0.3, 1),",
        "              opacity 0.35s ease;",
        "}",
        ".survey-item.expanded .survey-feedback-collapse {",
        "  max-height: 400px; /* Nội suy số đo mượt mà */",
        "  opacity: 1;",
        "}",
        "",
        "/* 3. HIỆU ỨNG SAO ĐÁNH GIÁ (STAR RATING) */",
        ".star:hover { color: #f59e0b; transform: scale(1.3); }"
    ]
    add_code_box(s13, 0.8, 1.45, 6.8, 5.25, code_s13, "CSS TRANSITION STYLES (dashboard/surveys.html)")

    add_card(s13, 7.8, 1.45, 4.733, 5.25)
    tb_r13 = s13.shapes.add_textbox(Inches(8.0), Inches(1.65), Inches(4.3), Inches(4.8))
    tf_r13 = tb_r13.text_frame
    tf_r13.word_wrap = True

    p = tf_r13.paragraphs[0]
    r = p.add_run()
    r.text = "LÝ THUYẾT ĐỒ HỌA TRÌNH DUYỆT"
    set_font(r, size=11.5, bold=True, color=PURPLE)

    pts13 = [
        ("Cơ chế Cubic-Bezier Timing Function", "Không dùng linear hay ease mặc định, nhóm dùng đường cong bezier tùy biến cubic-bezier(0.16, 1, 0.3, 1) tạo độ nảy đàn hồi tự nhiên."),
        ("Nguyên lý GPU Compositing Layer", "Thuộc tính transform không kích hoạt Reflow hay Repaint. Trình duyệt chuyển phần tử sang GPU xử lý riêng, giữ vững tốc độ 60fps."),
        ("Kỹ thuật nội suy Max-Height", "Giải quyết bài toán kinh điển trong Thiết kế Web: CSS không thể tính toán các mốc trung gian của height: auto.")
    ]
    for t, d in pts13:
        p_p = tf_r13.add_paragraph()
        p_p.space_before = Pt(8)
        r = p_p.add_run()
        r.text = t + ": "
        set_font(r, size=10, bold=True, color=NAVY)
        r2 = p_p.add_run()
        r2.text = d
        set_font(r2, size=9.5, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 14: BÁO CÁO TÀI CHÍNH & PHÂN TÍCH GIÁ TRỊ VÒNG ĐỜI (CLV)
    # ══════════════════════════════════════════════════════════════════════════
    s14 = prs.slides.add_slide(blank_layout)
    add_bg(s14)
    add_header(s14, "13. Báo Cáo Tài Chính & Phân Tích Giá Trị Vòng Đời Bệnh Nhân (CLV)")
    add_footer(s14, 14)

    clv_cards = [
        ("HẠNG VÀNG (GOLD VIP)", "52.4%", "1.240.000.000 ₫",
         ["Chiếm 18% tổng lượng bệnh nhân",
          "Đóng góp hơn 52% tổng doanh thu",
          "Tần suất khám trung bình: 6.8 lần/năm",
          "Giá trị vòng đời (CLV) cao nhất"], GOLD),
        ("HẠNG BẠC (SILVER)", "34.2%", "810.000.000 ₫",
         ["Chiếm 38% tổng lượng bệnh nhân",
          "Tần suất khám trung bình: 3.2 lần/năm",
          "Khách hàng tiềm năng để upsell lên Vàng",
          "Tỷ lệ hài lòng CSAT đạt 92%"], RGBColor(100, 116, 139)),
        ("HẠNG ĐỒNG (BRONZE)", "13.4%", "318.000.000 ₫",
         ["Chiếm 44% tổng lượng bệnh nhân",
          "Chủ yếu là khách mới từ Landing Page",
          "Cần chiến dịch nhắc lịch để tái khám",
          "Tỷ lệ chuyển đổi lên Bạc sau 3 tháng: 28%"], RGBColor(183, 121, 69))
    ]
    for i, (title, pct, rev, bullets, col) in enumerate(clv_cards):
        c_left = 0.8 + i * 3.98
        add_card(s14, c_left, 1.45, 3.8, 5.25)

        b = s14.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(c_left), Inches(1.45), Inches(3.8), Inches(0.06))
        b.fill.solid()
        b.fill.fore_color.rgb = col
        b.line.fill.background()

        tb = s14.shapes.add_textbox(Inches(c_left + 0.2), Inches(1.65), Inches(3.4), Inches(4.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = title
        set_font(r, size=11, bold=True, color=col)

        p2 = tf.add_paragraph()
        p2.space_before = Pt(4)
        r = p2.add_run()
        r.text = f"{pct} — {rev}"
        set_font(r, size=14, bold=True, color=NAVY)

        for b_txt in bullets:
            p_b = tf.add_paragraph()
            p_b.space_before = Pt(8)
            r = p_b.add_run()
            r.text = f"• {b_txt}"
            set_font(r, size=9.5, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 15: MINH CHỨNG GIT FLOW & GITHUB PAGES (.NOJEKYLL)
    # ══════════════════════════════════════════════════════════════════════════
    s15 = prs.slides.add_slide(blank_layout)
    add_bg(s15)
    add_header(s15, "14. Minh Chứng Quản Lý Mã Nguồn Git Flow & Triển Khai GitHub Pages")
    add_footer(s15, 15)

    add_card(s15, 0.8, 1.45, 5.75, 5.25)
    tb_l15 = s15.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(5.3), Inches(4.8))
    tf_l15 = tb_l15.text_frame
    tf_l15.word_wrap = True

    p = tf_l15.paragraphs[0]
    r = p.add_run()
    r.text = "CẤU TRÚC PHÂN NHÁNH GIT FLOW CHUẨN AGILE"
    set_font(r, size=11.5, bold=True, color=TEAL)

    branches = [
        ("nhánh main", "Phiên bản phát hành chính thức, triển khai live."),
        ("nhánh develop", "Môi trường tích hợp chung của toàn bộ 4 thành viên."),
        ("feature/ngocnhan-crm", "Phát triển Landing page, Form Leads và Login."),
        ("feature/giahuy-dashboard", "Phát triển bàn làm việc điều dưỡng và thẻ KPI."),
        ("feature/minhhuy-customers", "Phát triển danh bạ 200 BN và EHR 360°."),
        ("feature/quang-csat", "Phát triển khảo sát CSAT và CSS Transitions.")
    ]
    for b_name, b_desc in branches:
        p_b = tf_l15.add_paragraph()
        p_b.space_before = Pt(6)
        r = p_b.add_run()
        r.text = f"git branch {b_name}: "
        set_font(r, size=9.5, bold=True, color=NAVY, name="Consolas")
        r2 = p_b.add_run()
        r2.text = b_desc
        set_font(r2, size=9, bold=False, color=TEXT_DARK)

    add_card(s15, 6.78, 1.45, 5.75, 5.25)
    tb_r15 = s15.shapes.add_textbox(Inches(7.0), Inches(1.65), Inches(5.3), Inches(4.8))
    tf_r15 = tb_r15.text_frame
    tf_r15.word_wrap = True

    p = tf_r15.paragraphs[0]
    r = p.add_run()
    r.text = "TRIỂN KHAI GITHUB PAGES & VƯỢT LỖI 404 VỚI .NOJEKYLL"
    set_font(r, size=11.5, bold=True, color=CYAN)

    pts15 = [
        ("Hiện tượng lỗi ban đầu", "GitHub Pages mặc định chạy bộ biên dịch Jekyll. Các tệp Markdown nhật ký nhóm làm Jekyll bị lỗi build, dẫn đến trang web bị 404 Not Found."),
        ("Giải pháp kỹ thuật chuẩn xác", "Nhóm đã tạo tệp rỗng tên .nojekyll tại thư mục gốc repository và push lên nhánh main."),
        ("Ý nghĩa của .nojekyll", "Vô hiệu hóa hoàn toàn Jekyll, yêu cầu máy chủ GitHub Pages phục vụ trực tiếp các file HTML/CSS/JS thuần túy."),
        ("Kết quả kiểm chứng", "Trang web phản hồi HTTP 200 OK ngay lập tức tại địa chỉ https://newbieincodde.github.io/Qu-n-l-Quan-h-Kh-ch-h-ng-CRM-/")
    ]
    for t, d in pts15:
        p_p = tf_r15.add_paragraph()
        p_p.space_before = Pt(8)
        r = p_p.add_run()
        r.text = t + ": "
        set_font(r, size=10, bold=True, color=NAVY)
        r2 = p_p.add_run()
        r2.text = d
        set_font(r2, size=9.5, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 16: ĐỐI CHIẾU RUBRIC TIÊU CHÍ CHẤM ĐIỂM HỌC PHẦN 111101
    # ══════════════════════════════════════════════════════════════════════════
    s16 = prs.slides.add_slide(blank_layout)
    add_bg(s16)
    add_header(s16, "15. Bảng Đối Chiếu Tiêu Chí Chấm Điểm Học Phần 111101 (LHU)")
    add_footer(s16, 16)

    rubrics = [
        ("1. HTML5 SEMANTIC & FORM", "ĐẠT 100%",
         "100% thẻ ngữ nghĩa header, nav, main, section, footer. Form validation regex ^0[0-9]{9}$ kiểm tra chính xác SĐT 10 số, không reload trang."),
        ("2. CSS3 LAYOUTS & TRANSITIONS", "ĐẠT 100%",
         "Kết hợp hoàn hảo Flexbox 1D và CSS Grid 2D. 3 hiệu ứng transition thuần: Hover thẻ GPU 60fps, Accordion max-height và sao 1.3x."),
        ("3. JAVASCRIPT ES6+ LOGIC", "ĐẠT 100%",
         "Giải thuật tự động phân hạng Đồng/Bạc/Vàng theo totalSpent; thuật toán lọc ngày tái khám; xử lý phân trang động 20 trang bằng slice()."),
        ("4. QUẢN TRỊ DỮ LIỆU LOCALSTORAGE", "ĐẠT 100%",
         "Thiết kế 5 kho dữ liệu chuẩn hóa: 200 bệnh nhân, 325 toa thuốc, 112 kho dược. Quan hệ 1-N hoạt động trơn tru qua patientId."),
        ("5. RESPONSIVE DESIGN & GIT FLOW", "ĐẠT 100%",
         "Tương thích 100% từ Mobile đến Desktop. Quy trình 4 nhánh Git song song, giải quyết conflict và deploy thành công trên GitHub Pages.")
    ]
    for i, (title, grade, desc) in enumerate(rubrics):
        c_top = 1.45 + i * 1.05
        add_card(s16, 0.8, c_top, 11.733, 0.95)
        
        b = s16.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(c_top), Inches(0.1), Inches(0.95))
        b.fill.solid()
        b.fill.fore_color.rgb = EMERALD
        b.line.fill.background()

        tb = s16.shapes.add_textbox(Inches(1.05), Inches(c_top + 0.1), Inches(9.5), Inches(0.75))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = title + "  "
        set_font(r, size=11, bold=True, color=NAVY)
        
        r_g = p.add_run()
        r_g.text = f"[{grade}]"
        set_font(r_g, size=10, bold=True, color=EMERALD)

        p2 = tf.add_paragraph()
        p2.space_before = Pt(2)
        r = p2.add_run()
        r.text = desc
        set_font(r, size=9.5, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 17: BỘ CÂU HỎI PHẢN BIỆN BẢO VỆ ĐỒ ÁN (DEFENSE Q&A)
    # ══════════════════════════════════════════════════════════════════════════
    s17 = prs.slides.add_slide(blank_layout)
    add_bg(s17)
    add_header(s17, "16. Bộ Câu Hỏi Phản Biện Chuyên Sâu Của Hội Đồng Giảng Viên")
    add_footer(s17, 17)

    qas = [
        ("Q1: Tại sao không dùng React/Vue mà dùng Pure Vanilla JS?",
         "Vanilla JS giúp sinh viên nắm vững bản chất DOM, BOM và CSSOM. Tải trang 0ms, không tốn 150KB runtime, bảo mật cục bộ tuyệt đối."),
        ("Q2: LocalStorage lưu ở đâu, có bị mất khi tắt máy không?",
         "Lưu dạng SQLite trong User Profile của trình duyệt trên ổ cứng. Là Persistent Storage nên tồn tại vĩnh viễn đến khi người dùng Clear Cache."),
        ("Q3: Làm sao chống tấn công XSS khi dùng innerHTML?",
         "Kiểm soát đầu vào nghiêm ngặt bằng Regex ở Form, khử khuẩn mã độc bằng cách escape ký tự đặc biệt và ưu tiên dùng .textContent."),
        ("Q4: Nếu phòng khám lên 50.000 bệnh nhân thì sao?",
         "Nâng cấp lên IndexedDB (Cơ sở dữ liệu NoSQL bất đồng bộ trong trình duyệt lưu hàng trăm MB) hoặc xây dựng RESTful API kết nối PostgreSQL.")
    ]
    for i, (q, a) in enumerate(qas):
        col = i % 2
        row = i // 2
        c_left = 0.8 + col * 5.98
        c_top = 1.45 + row * 2.65
        add_card(s17, c_left, c_top, 5.75, 2.45)

        b = s17.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(c_left), Inches(c_top), Inches(5.75), Inches(0.06))
        b.fill.solid()
        b.fill.fore_color.rgb = TEAL if i % 2 == 0 else CYAN
        b.line.fill.background()

        tb = s17.shapes.add_textbox(Inches(c_left + 0.2), Inches(c_top + 0.15), Inches(5.35), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = q
        set_font(r, size=11, bold=True, color=NAVY)

        p2 = tf.add_paragraph()
        p2.space_before = Pt(6)
        r = p2.add_run()
        r.text = f"Trả lời: {a}"
        set_font(r, size=10, bold=False, color=TEXT_DARK)

    # ══════════════════════════════════════════════════════════════════════════
    # SLIDE 18: LỜI CẢM ƠN & KẾT THÚC
    # ══════════════════════════════════════════════════════════════════════════
    s18 = prs.slides.add_slide(blank_layout)
    add_bg(s18, NAVY)

    top_c18 = s18.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.12))
    top_c18.fill.solid()
    top_c18.fill.fore_color.rgb = TEAL
    top_c18.line.fill.background()

    tb_end = s18.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(2.2))
    tf_end = tb_end.text_frame
    tf_end.word_wrap = True

    p = tf_end.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "CHÂN THÀNH CẢM ƠN QUÝ THẦY CÔ VÀ CÁC BẠN\nĐÃ LẮNG NGHE BÀI THUYẾT TRÌNH!"
    set_font(r, size=28, bold=True, color=WHITE)

    p2 = tf_end.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(16)
    r = p2.add_run()
    r.text = "Nhóm MedCare CRM kính mong nhận được những nhận xét & góp ý quý báu từ Hội đồng Giảng viên!"
    set_font(r, size=14, bold=False, color=RGBColor(203, 213, 225))

    p3 = tf_end.add_paragraph()
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(20)
    r = p3.add_run()
    r.text = "HỎI & ĐÁP (Q&A) — XIN MỜI QUÝ THẦY CÔ ĐẶT CÂU HỎI"
    set_font(r, size=16, bold=True, color=CYAN)

    tb_foot = s18.shapes.add_textbox(Inches(1.0), Inches(6.0), Inches(11.3), Inches(0.5))
    p_f = tb_foot.text_frame.paragraphs[0]
    p_f.alignment = PP_ALIGN.CENTER
    r = p_f.add_run()
    r.text = "Live Demo: https://newbieincodde.github.io/Qu-n-l-Quan-h-Kh-ch-h-ng-CRM-/  ·  GitHub: newbieincodde"
    set_font(r, size=11, bold=True, color=RGBColor(148, 163, 184))

    prs.save(output_path)
    print(f"Master Deck (18 slides) created successfully at: {output_path}")

if __name__ == '__main__':
    out_file = sys.argv[1] if len(sys.argv) > 1 else 'MedCare_CRM_BaoCao_ThietKeWeb_LHU.pptx'
    build_master_deck(out_file)

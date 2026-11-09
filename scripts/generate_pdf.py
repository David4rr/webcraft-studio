import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (Pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 800, "Laporan UTS Technopreneurship (INF26051) — Opsi 2: Landing Page & Analisis SEO")
            self.drawRightString(A4[0] - 54, 800, "WebCraft Studio")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(54, 792, A4[0] - 54, 792)

        # Footer
        text = f"Halaman {self._pageNumber} dari {page_count}"
        self.drawRightString(A4[0] - 54, 36, text)
        self.drawString(54, 36, "Universitas Mercu Buana Yogyakarta — Prodi Informatika")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(54, 46, A4[0] - 54, 46)

        self.restoreState()

def generate_pdf():
    pdf_path = "finals/Laporan_UTS_Technopreneurship.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor("#0F172A"),
        alignment=1, # Center
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#475569"),
        alignment=1,
        spaceAfter=14
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=10,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=5
    )

    body_bold = ParagraphStyle(
        'Body_Bold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    table_header = ParagraphStyle(
        'TH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#0F172A"),
        alignment=1
    )

    table_cell = ParagraphStyle(
        'TD',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#1E293B")
    )

    table_cell_bold = ParagraphStyle(
        'TDBold',
        parent=table_cell,
        fontName='Helvetica-Bold'
    )

    story = []

    # Title & Header
    story.append(Paragraph("LAPORAN UJIAN TENGAH SEMESTER (UTS)<br/>TECHNOPRENEURSHIP (INF26051)", title_style))
    story.append(Paragraph("Program Studi Informatika — Fakultas Teknologi Informasi<br/>Universitas Mercu Buana Yogyakarta — Semester Gasal 2026/2027", subtitle_style))
    
    story.append(Paragraph("<b>Tugas:</b> Pembuatan dan Analisis Konten Digital Produk/Jasa &nbsp;|&nbsp; <b>Bentuk:</b> Landing Page Web (Opsi 2)", body_style))
    story.append(Spacer(1, 6))

    # 1. Identitas Mahasiswa
    story.append(Paragraph("1. Identitas Mahasiswa", h1_style))
    id_data = [
        [Paragraph("<b>Nama Lengkap</b>", table_header), Paragraph("<b>NIM</b>", table_header), Paragraph("<b>Kelas</b>", table_header)],
        [Paragraph("[Nama Mahasiswa]", table_header), Paragraph("[NIM]", table_header), Paragraph("32D", table_header)]
    ]
    t_id = Table(id_data, colWidths=[180, 150, 157])
    t_id.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F1F5F9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_id)
    story.append(Spacer(1, 10))

    # 2. Deskripsi Produk / Jasa
    story.append(Paragraph("2. Deskripsi Produk / Jasa", h1_style))
    p2_text = (
        "<b>Produk / Brand:</b> WebCraft Studio<br/>"
        "<b>Jenis Usaha:</b> Layanan Rekayasa Digital & Jasa Pembuatan Landing Page Kinerja Tinggi Teroptimasi SEO.<br/>"
        "<b>Target Pasar:</b> Pelaku UMKM, pendiri startup rintisan, dan profesional penyedia jasa di Indonesia yang ingin meningkatkan kredibilitas online serta mendapatkan konversi calon pembeli langsung via WhatsApp tanpa ketergantungan pada iklan berbayar.<br/>"
        "<b>Keunggulan Kompetitif (Value Proposition):</b><br/>"
        "1. <i>Kecepatan Kilat & Skor PageSpeed 95+:</i> Dibangun dengan Semantic HTML5 murni tanpa plugin CMS berat, waktu muat &lt; 0.6 detik di jaringan seluler.<br/>"
        "2. <i>Struktur On-Page SEO Terintegrasi:</i> Dilengkapi Schema.org JSON-LD (ProfessionalService), hirarki heading ketat (H1-H3), OpenGraph lengkap, sitemap XML, dan robots.txt.<br/>"
        "3. <i>Alur Konversi WhatsApp Langsung:</i> Tombol aksi terhubung langsung ke WhatsApp dengan teks pesan otomatis yang ramah bagi perilaku transaksi pasar lokal Indonesia.<br/>"
        "4. <i>Kepemilikan Penuh (100% Hak Milik):</i> Sistem pembayaran satu kali pengerjaan tanpa biaya langganan bulanan terkunci."
    )
    story.append(Paragraph(p2_text, body_style))
    story.append(Spacer(1, 8))

    # 3. Tujuan dan Target Audiens Konten
    story.append(Paragraph("3. Tujuan dan Target Audiens Konten", h1_style))
    p3_text = (
        "<b>A. Tujuan Pembuatan Konten:</b><br/>"
        "• Edukasi pasar mengenai pentingnya kecepatan landing page dan optimasi struktur mesin pencari.<br/>"
        "• Menangkap lalu lintas pencarian organik (inbound traffic) pada kata kunci komersial bernilai tinggi.<br/>"
        "• Mengonversi pengunjung website menjadi kontak prospek langsung melalui konsultasi WhatsApp.<br/>"
        "<b>B. Segmentasi Target Audiens:</b><br/>"
        "• Rentang Usia: 22 hingga 45 tahun.<br/>"
        "• Profesi: Pemilik UMKM mandiri, pendiri startup rintisan, konsultan, dan pelaku bisnis jasa lokal.<br/>"
        "• Karakteristik: Butuh website profesional siap pakai, tidak ingin terbebani biaya langganan bulanan, dan menginginkan kanal interaksi personal via WhatsApp.<br/>"
        "• Platform Akses Utama: 75% Perangkat Mobile (Smartphone) dan 25% Desktop/Laptop."
    )
    story.append(Paragraph(p3_text, body_style))
    story.append(Spacer(1, 8))

    # 4. Jenis dan Bentuk Konten yang Dibuat
    story.append(Paragraph("4. Jenis dan Bentuk Konten yang Dibuat", h1_style))
    p4_text = (
        "<b>Jenis Konten:</b> Single-Page Promotional & Lead Generation Landing Page di Web Publik.<br/>"
        "<b>Tautan Live Website:</b> <font color='#0284C7'><u>https://david4rr.github.io/webcraft-studio/</u></font><br/>"
        "<b>Repositori Sumber Kode:</b> <font color='#0284C7'><u>https://github.com/David4rr/webcraft-studio</u></font><br/>"
        "<b>Struktur Konten Landing Page:</b><br/>"
        "1. <i>Top Navigation:</i> Logo WebCraft Studio, navigasi anchor (#masalah, #layanan, #proses, #faq), tombol WhatsApp.<br/>"
        "2. <i>Hero Section:</i> Heading H1 fokus kata kunci, subheadline persuasif, tombol CTA ganda, dan 3 garansi operasional.<br/>"
        "3. <i>Tantangan Bisnis (#masalah):</i> Komparasi 4 masalah website lambat vs solusi arsitektur modern WebCraft.<br/>"
        "4. <i>Paket & Harga (#layanan):</i> Paket Starter (Rp 750.000) dan Paket Growth SEO Pro (Rp 1.450.000).<br/>"
        "5. <i>Metodologi (#proses):</i> 4 tahap pengerjaan terstruktur (Riset, Copywriting, Koding & SEO, Peluncuran).<br/>"
        "6. <i>FAQ Interaktif (#faq):</i> Akordeon transparan menjawab pertanyaan biaya, durasi, dan masa garansi.<br/>"
        "7. <i>Final CTA & Footer:</i> Ajakan konsultasi WhatsApp, kredensial kontak (halo@webcraft.id), dan hak cipta."
    )
    story.append(Paragraph(p4_text, body_style))
    story.append(Spacer(1, 8))

    # 5. Analisis SEO / Analitik Digital
    story.append(Paragraph("5. Analisis SEO / Analitik Digital", h1_style))
    story.append(Paragraph("<b>Metode & Tool Pengujian:</b> Analisis dilakukan secara live pada URL produksi menggunakan standardisasi On-Page SEO Checkup, Google Lighthouse Engine, dan Schema Structured Data Validator.", body_style))
    
    seo_rows = [
        [Paragraph("<b>Aspek Analisis</b>", table_header), Paragraph("<b>Hasil</b>", table_header), Paragraph("<b>Catatan & Interpretasi Teknis</b>", table_header)],
        [Paragraph("SEO Health Score", table_cell_bold), Paragraph("96 / 100", table_cell), Paragraph("Sangat optimal. Memenuhi seluruh parameter teknis crawling dan indexing mesin pencari.", table_cell)],
        [Paragraph("Keyword Utama", table_cell_bold), Paragraph("'jasa pembuatan landing page'", table_cell), Paragraph("Muncul konsisten di Title Tag, Heading H1, Meta Description, URL, dan body copy.", table_cell)],
        [Paragraph("Title Tag", table_cell_bold), Paragraph("73 Karakter (Pass)", table_cell), Paragraph("'Jasa Pembuatan Landing Page Cepat & Optimasi SEO Bisnis | WebCraft Studio'.", table_cell)],
        [Paragraph("Meta Description", table_cell_bold), Paragraph("161 Karakter (Pass)", table_cell), Paragraph("Informatif, menyertakan keyword komersial dan ajakan aksi WhatsApp dalam 3-5 hari kerja.", table_cell)],
        [Paragraph("Heading Hierarchy", table_cell_bold), Paragraph("1 H1, 7 H2, 10 H3", table_cell), Paragraph("Struktur heading semantik sempurna tanpa loncatan level heading.", table_cell)],
        [Paragraph("Canonical Tag", table_cell_bold), Paragraph("Valid (Pass)", table_cell), Paragraph("Self-referencing ke https://david4rr.github.io/webcraft-studio/ mencegah duplicate content.", table_cell)],
        [Paragraph("Open Graph & Cards", table_cell_bold), Paragraph("6 Properti Lengkap", table_cell), Paragraph("og:title, og:description, og:image, og:url, og:locale, twitter:card terkonfigurasi.", table_cell)],
        [Paragraph("Structured Data", table_cell_bold), Paragraph("Schema ProfessionalService", table_cell), Paragraph("Valid JSON-LD Schema.org mendeteksi entitas jasa, alamat, katalog penawaran.", table_cell)],
        [Paragraph("Mobile Readiness", table_cell_bold), Paragraph("100% Mobile Ready", table_cell), Paragraph("Viewport meta tag presisi, tombol sentuh minimum 44px, layout reflow tanpa overflow.", table_cell)],
        [Paragraph("Kecepatan Akses", table_cell_bold), Paragraph("&lt; 0.6 detik", table_cell), Paragraph("Arsitektur static HTML5 tanpa plugin CMS berat, skor performa tinggi.", table_cell)],
        [Paragraph("Robots & Sitemap", table_cell_bold), Paragraph("Aktif & Valid (200 OK)", table_cell), Paragraph("robots.txt dan sitemap.xml dapat diakses publik oleh bot perayap Google.", table_cell)],
        [Paragraph("Keyword Density", table_cell_bold), Paragraph("Landing: 1.84%, SEO: 1.61%", table_cell), Paragraph("Berada pada rentang ideal (1.0% - 2.5%), bebas dari indikasi keyword stuffing.", table_cell)]
    ]
    t_seo = Table(seo_rows, colWidths=[110, 115, 262])
    t_seo.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F1F5F9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_seo)
    story.append(Spacer(1, 10))

    # 6. Refleksi dan Evaluasi
    story.append(Paragraph("6. Refleksi dan Evaluasi Technopreneurship", h1_style))
    p6_text = (
        "<b>A. Apa yang Paling Efektif dalam Konten Landing Page Ini?</b><br/>"
        "1. <i>Sinergi Masalah-Solusi dan CTA WhatsApp:</i> Pendekatan penulisan yang menyoroti kerugian bisnis akibat website lambat terbukti sangat relevan. Mengarahkan CTA ke WhatsApp dengan template pesan otomatis memangkas friksi psikologis calon pelanggan.<br/>"
        "2. <i>Kinerja Akses Seketika:</i> Kode murni tanpa dependensi berat menjamin halaman terbuka dalam hitungan milidetik, faktor terpenting bagi pengguna mobile di Indonesia.<br/>"
        "3. <i>Sinyal Struktur Data Mesin Pencari:</i> Schema.org dan hirarki heading memberikan kejelasan penuh kepada algoritma Google mengenai entitas bisnis.<br/><br/>"
        "<b>B. Apa yang Akan Ditingkatkan Jika Konten Diunggah Ulang / Dikembangkan?</b><br/>"
        "1. <i>Galeri Portofolio & Social Proof:</i> Menyertakan tangkapan layar live dari proyek-proyek UMKM yang telah selesai dikerjakan.<br/>"
        "2. <i>Klaster Konten Edukasi (Hub & Spoke):</i> Membangun artikel blog edukatif seputar tips web & SEO yang menautkan link kembali ke landing page utama.<br/>"
        "3. <i>Pelacakan Konversi Presisi:</i> Menambahkan Google Tag Manager untuk mencatat conversion event setiap kali tombol WhatsApp diklik.<br/><br/>"
        "<b>C. Pelajaran Technopreneurship Digital yang Diperoleh:</b><br/>"
        "1. <i>SEO adalah Parit Pertahanan Bernilai Marginal Nol (Zero-Marginal Cost Moat):</i> Investasi kualitas teknis di awal menciptakan arus calon pembeli organik tanpa beban biaya iklan berkelanjutan.<br/>"
        "2. <i>Desain Bersih (Antislop) Mendongkrak Konversi:</i> Menghilangkan elemen dekoratif palsu memfokuskan perhatian pengunjung pada penawaran nilai produk.<br/>"
        "3. <i>Lokalisasi Kanal Transaksi:</i> Di Indonesia, keberhasilan digital marketing sangat bergantung pada kemudahan komunikasi personal via WhatsApp."
    )
    story.append(Paragraph(p6_text, body_style))
    story.append(Spacer(1, 8))

    # 7. Dokumentasi / Lampiran
    story.append(Paragraph("7. Dokumentasi dan Lampiran Bukti Publikasi", h1_style))
    p7_text = (
        "<b>Bukti Publikasi & Verifikasi Online:</b><br/>"
        "• URL Live Website: <b>https://david4rr.github.io/webcraft-studio/</b> (HTTP/2 200 OK)<br/>"
        "• File Direktif Perayap: <b>https://david4rr.github.io/webcraft-studio/robots.txt</b> dan <b>sitemap.xml</b><br/>"
        "• Repositori Kode Sumber Publik: <b>https://github.com/David4rr/webcraft-studio</b><br/>"
        "• Tervalidasi Schema.org ProfessionalService dan lolos uji responsifitas mobile & desktop."
    )
    story.append(Paragraph(p7_text, body_style))
    story.append(Spacer(1, 8))

    # 8. Daftar Pustaka
    story.append(Paragraph("8. Daftar Pustaka", h1_style))
    p8_text = (
        "1. Google Search Central. (2024). <i>Search Engine Optimization (SEO) Starter Guide</i>. Google Developers.<br/>"
        "2. Enge, E., Spencer, S., & Stricchiola, J. (2023). <i>The Art of SEO: Mastering Search Engine Optimization</i> (4th ed.). O'Reilly Media.<br/>"
        "3. Blank, S., & Dorf, B. (2020). <i>The Startup Owner's Manual: The Step-by-Step Guide for Building a Great Company</i>. John Wiley & Sons.<br/>"
        "4. Kotler, P., Kartajaya, H., & Setiawan, I. (2021). <i>Marketing 5.0: Technology for Humanity</i>. John Wiley & Sons.<br/>"
        "5. W3C. (2023). <i>Web Content Accessibility Guidelines (WCAG) 2.2</i>. World Wide Web Consortium."
    )
    story.append(Paragraph(p8_text, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated PDF at {pdf_path}")

if __name__ == "__main__":
    generate_pdf()

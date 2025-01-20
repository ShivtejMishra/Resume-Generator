from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 24)
        self.set_text_color(0, 86, 179)  # Blue color
        self.cell(0, 15, 'Resume', 0, 1, 'C')
        self.ln(8)

    def encode_text(self, text):
        # Encode text to handle unsupported characters
        return text.encode("latin-1", "replace").decode("latin-1")

    def add_contact_info(self, email, phone, address, website):
        self.set_font('Arial', '', 12)
        self.set_text_color(0, 0, 0)
        self.cell(0, 8, self.encode_text(f"{email} | {phone} | {address}"), 0, 1, 'C')
        self.cell(0, 8, self.encode_text(website), 0, 1, 'C')
        self.ln(10)

    def add_section_title(self, title):
        self.set_fill_color(0, 86, 179)  # Blue background
        self.set_text_color(255, 255, 255)  # White text
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, self.encode_text(title), 0, 1, 'L', fill=True)
        self.ln(4)

    def add_content(self, content):
        self.set_text_color(0, 0, 0)  # Black text
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 8, self.encode_text(content.strip()))
        self.ln(6)

    def add_summary(self, summary):
        self.add_section_title("Summary")
        self.add_content(summary)

    def add_skills(self, skills):
        self.add_section_title("Key Skills")
        self.add_content(skills)

    def add_experience(self, experience):
        self.add_section_title("Work Experience")
        self.add_content(experience)

    def add_education(self, education):
        self.add_section_title("Education")
        self.add_content(education)


def generate_pdf(name, email, phone, address, website, summary, skills, experience, education):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(0, 86, 179)  # Blue for the header name
    pdf.cell(0, 15, pdf.encode_text(name), 0, 1, 'C')
    pdf.add_contact_info(email, phone, address, website)

    pdf.add_summary(summary)
    pdf.add_skills(skills)
    pdf.add_experience(experience)
    pdf.add_education(education)

    pdf.output("blue_theme_resume.pdf")

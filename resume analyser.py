import PyPDF2 as pdf

required_skills = {"python",
    "machine learning",
    "sql",
    "data analysis",
    "git",
    "docker"}

resume = open("resume.pdf","rb")

reader = pdf.pdfreader(resume)

text = ""

for page in reader.pages:
    text += page.extract_text()

text = text.lower()

found_skills = []
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def create_pdf(content, filename="output.pdf"):
    try:
        filepath = os.path.join(os.getcwd(), filename)

        doc = SimpleDocTemplate(filepath)
        styles = getSampleStyleSheet()

        story = []

        for line in content.split("\n"):
            story.append(Paragraph(line, styles["Normal"]))
            story.append(Spacer(1, 10))

        doc.build(story)

        return filepath

    except Exception as e:
        print("PDF ERROR:", e)
        return None
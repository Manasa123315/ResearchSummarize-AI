from reportlab.platypus import *

def generate_report(
        filename,
        summary,
        keywords,
        gaps):

    doc = SimpleDocTemplate(filename)

    content = []

    content.append(
        Paragraph(
            "ResearchSummarize AI Report"
        )
    )

    content.append(Spacer(1,12))

    content.append(
        Paragraph(
            f"<b>Summary:</b><br/>{summary}"
        )
    )

    content.append(Spacer(1,12))

    content.append(
        Paragraph(
            f"<b>Keywords:</b><br/>{', '.join(keywords)}"
        )
    )

    content.append(Spacer(1,12))

    content.append(
        Paragraph(
            f"<b>Research Gaps:</b><br/>{', '.join(gaps)}"
        )
    )

    doc.build(content)
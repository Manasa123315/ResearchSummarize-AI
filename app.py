import streamlit as st

from modules.pdf_reader import extract_text
from modules.text_cleaner import clean_text
from modules.section_extractor import extract_sections
from modules.summarizer import summarize_text
from modules.keyword_extractor import extract_keywords
from modules.research_gap_detector import detect_research_gap
from modules.report_generator import generate_report

st.set_page_config(
    page_title="ResearchSummarize AI",
    layout="wide"
)

st.title(
    "ResearchSummarize AI"
)

uploaded_file = st.file_uploader(
    "Upload Research Paper",
    type=["pdf"]
)

if uploaded_file:

    path = uploaded_file.name

    with open(path, "wb") as f:

        f.write(uploaded_file.getbuffer())

    text = extract_text(path)

    cleaned_text = clean_text(text)

    st.success(
        "PDF Successfully Processed"
    )

    with st.spinner(
        "Generating Summary..."
    ):

        summary = summarize_text(
            cleaned_text
        )

        keywords = extract_keywords(
            cleaned_text
        )

        gaps = detect_research_gap(
            cleaned_text
        )

        sections = extract_sections(
            cleaned_text
        )

    st.header("Full Summary")

    st.write(summary)

    st.header("Keywords")

    st.write(keywords)

    st.header("Research Gap Indicators")

    st.write(gaps)

    st.header("Section Summaries")

    for section, content in sections.items():

        st.subheader(section)

        short_summary = summarize_text(
            content[:3000]
        )

        st.write(short_summary)

    report_file = "generated_report.pdf"

    generate_report(
        report_file,
        summary,
        keywords,
        gaps
    )

    with open(
        report_file,
        "rb"
    ) as pdf:

        st.download_button(
            "Download Report",
            pdf,
            file_name="Research_Report.pdf"
        )

from transformers import pipeline
import re

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


def summarize_text(text):

    if not text or not text.strip():
        return "No readable text found in the PDF."

    # Remove repeated whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Split text into manageable chunks
    sentences = re.split(r"(?<=[.!?])\s+", text)

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) > 1800:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
            current_chunk = sentence
        else:
            current_chunk += " " + sentence

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    summaries = []

    for chunk in chunks:
        if len(chunk.split()) < 40:
            summary = chunk
        else:
            result = summarizer(
                chunk,
                max_length=130,
                min_length=30,
                do_sample=False,
                truncation=True
            )
            summary = result[0]["summary_text"]

        # Remove duplicate sentences within summaries
        for sentence in re.split(r"(?<=[.!?])\s+", summary):
            sentence = sentence.strip()
            if sentence and sentence not in summaries:
                summaries.append(sentence)

    return " ".join(summaries)

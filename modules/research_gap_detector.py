def detect_research_gap(text):

    keywords = [

        "future work",
        "limitation",
        "limitations",
        "challenge",
        "challenges",
        "further research"

    ]

    findings = []

    lower_text = text.lower()

    for word in keywords:

        if word in lower_text:

            findings.append(word)

    return findings
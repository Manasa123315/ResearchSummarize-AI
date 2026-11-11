import re

def extract_sections(text):

    sections = {}

    abstract = re.search(
        r'abstract(.*?)introduction',
        text,
        re.IGNORECASE | re.DOTALL
    )

    if abstract:
        sections["Abstract"] = abstract.group(1)

    methodology = re.search(
        r'(methodology|methods)(.*?)(results)',
        text,
        re.IGNORECASE | re.DOTALL
    )

    if methodology:
        sections["Methodology"] = methodology.group(2)

    results = re.search(
        r'results(.*?)(conclusion)',
        text,
        re.IGNORECASE | re.DOTALL
    )

    if results:
        sections["Results"] = results.group(1)

    conclusion = re.search(
        r'conclusion(.*)',
        text,
        re.IGNORECASE | re.DOTALL
    )

    if conclusion:
        sections["Conclusion"] = conclusion.group(1)

    return sections
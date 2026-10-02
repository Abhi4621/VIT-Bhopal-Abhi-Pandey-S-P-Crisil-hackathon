"""
Text cleaning and normalization utilities for financial text.
Removes extraneous markup, normalizes whitespace, and sanitizes input.
"""

import re
import html
from typing import Optional

def clean_financial_text(text: Optional[str]) -> str:
    """
    Cleans raw financial news or social media text:
    - Decodes HTML entities (&amp; -> &)
    - Strips URLs
    - Normalizes repeated whitespaces and special characters
    - Preserves financial numbers, currency signs, and percentages
    """
    if text is None:
        return ""
    
    if not isinstance(text, str):
        text = str(text)

    # Decode HTML
    cleaned = html.unescape(text)

    # Remove URLs (http://, https://, www.)
    cleaned = re.sub(r'https?://\S+|www\.\S+', '', cleaned)

    # Normalize excessive quotation marks and dashes
    cleaned = re.sub(r'[\u2018\u2019]', "'", cleaned)
    cleaned = re.sub(r'[\u201c\u201d]', '"', cleaned)
    cleaned = re.sub(r'[\u2013\u2014]', '-', cleaned)

    # Normalize whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    return cleaned

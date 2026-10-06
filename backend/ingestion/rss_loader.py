"""
Optional live financial news ingestion via public RSS feeds.
Allows real-time unstructured data ingestion without requiring API keys or paid services.
Gracefully handles offline environments and timeouts.
"""

import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional
from email.utils import parsedate_to_datetime
from backend.ingestion.cleaner import clean_financial_text

DEFAULT_RSS_URL = "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=en-US&gl=US&ceid=US:en"
FALLBACK_RSS_URLS = [
    "https://feeds.content.dowjones.io/public/rss/mw_topstories",
    "https://search.cnbc.com/rs/search/view.html?partnerId=2000&keywords=markets&sort=date&type=all&format=rss",
    "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml"
]

def fetch_live_rss_records(
    feed_url: Optional[str] = None,
    max_items: int = 10,
    timeout: float = 6.0
) -> List[Dict[str, Any]]:
    """
    Fetches live financial headlines from a public RSS feed.
    Returns cleaned structured records:
    [{ 'id': ..., 'timestamp': ..., 'source': 'live_financial_rss', 'headline': ..., 'text': ... }]
    
    If network is unavailable, returns empty list without raising exceptions.
    """
    candidate_urls = [feed_url] if feed_url else [DEFAULT_RSS_URL] + FALLBACK_RSS_URLS
    xml_data = None

    for target_url in candidate_urls:
        try:
            req = urllib.request.Request(
                target_url,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) RiskPulse/1.0"}
            )
            with urllib.request.urlopen(req, timeout=timeout) as response:
                xml_data = response.read()
                if xml_data:
                    break
        except Exception:
            continue

    if not xml_data:
        return []

    records: List[Dict[str, Any]] = []
    try:
        root = ET.fromstring(xml_data)
        # Standard RSS has channel -> item elements
        items = root.findall("./channel/item")
        for idx, item in enumerate(items[:max_items]):
            title_elem = item.find("title")
            desc_elem = item.find("description")
            pubdate_elem = item.find("pubDate")
            guid_elem = item.find("guid")

            headline = clean_financial_text(title_elem.text if title_elem is not None else "")
            description = clean_financial_text(desc_elem.text if desc_elem is not None else "")

            # Parse pubDate or fallback to current UTC
            timestamp = datetime.now(timezone.utc)
            if pubdate_elem is not None and pubdate_elem.text:
                try:
                    timestamp = parsedate_to_datetime(pubdate_elem.text)
                except Exception:
                    pass

            item_id = guid_elem.text if guid_elem is not None and guid_elem.text else f"RSS-{idx+1:03d}"
            combined_text = f"{headline}. {description}".strip() if description else headline

            if headline:
                records.append({
                    "id": item_id,
                    "timestamp": timestamp,
                    "source": "live_financial_rss",
                    "company": "General Market",
                    "headline": headline,
                    "article_text": description,
                    "text": combined_text
                })
    except Exception:
        return []

    return records

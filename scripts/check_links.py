#!/usr/bin/env python3
"""Revisa enlaces internos (href/src) en el HTML renderizado. Solo biblioteca estándar."""
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urlparse, unquote


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k in ("href", "src") and v:
                self.links.append(v)


def main(site):
    site = Path(site).resolve()
    broken, total = [], 0
    for page in site.rglob("*.html"):
        p = Links()
        p.feed(page.read_text(encoding="utf-8", errors="ignore"))
        for link in p.links:
            u = urlparse(link)
            if u.scheme or link.startswith(("#", "mailto:", "javascript:", "data:", "//")):
                continue
            path = unquote(urldefrag(u.path)[0])
            if not path:
                continue
            target = (site / path.lstrip("/")) if path.startswith("/") else (page.parent / path)
            total += 1
            if not (target.exists() or (target / "index.html").exists()):
                broken.append(f"{page.relative_to(site)} -> {link}")
    print(f"{total} enlaces internos revisados; {len(broken)} rotos")
    for b in broken:
        print("  ROTO:", b)
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "_site")

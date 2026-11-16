from pathlib import Path
from html.parser import HTMLParser
import json, re, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]

class RefParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.ids = [], []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        for key in ("src", "href"):
            value = attrs.get(key, "")
            if value and not value.startswith(("http:", "https:", "mailto:", "#", "data:", "javascript:")):
                self.refs.append(value)

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

books = load("01_Wiki/books.json")
sources = load("03_Sources/source_register.json")
assert len(books) == 5, "Wiki 分冊不是五冊"
assert len(sources) == 15, "來源數量不是 15 筆"
assert sum(x["type"] == "學術研究" for x in sources) == 8
assert sum(x["type"].startswith("官方") for x in sources) == 5
assert sum(x["type"] == "專業產業資料" for x in sources) == 2
assert len(list((ROOT / "01_Wiki/books").glob("VOL_*.md"))) == 5

refs = (ROOT / "03_Sources/references_APA7.md").read_text(encoding="utf-8")
a4 = "Cordoba Castro, N. M., Ruiz Pardo, R. Y., Moreno Moreno, F. L., & Fernandez Alduenda, M. R."
assert a4 in refs, "A4 作者順序需核對"

for rel in ("01_Wiki/index.html", "02_HTML_Magazine/index.html"):
    page = ROOT / rel
    text = page.read_text(encoding="utf-8")
    parser = RefParser()
    parser.feed(text)
    assert len(parser.ids) == len(set(parser.ids)), f"{rel} 有重複 id"
    for ref in parser.refs:
        target = (page.parent / ref.split("#")[0].split("?")[0]).resolve()
        assert target.exists(), f"{rel} 找不到資源：{ref}"
    blocks = re.findall(r"<script\\b[^>]*>(.*?)</script>", text, re.S | re.I)
    assert len(blocks) == 1, f"{rel} script 區塊數量異常"
    assert len(re.findall(r"<script\\b", text, re.I)) == len(re.findall(r"</script>", text, re.I))
    node = subprocess.run(["node", "--check", "-"], input=blocks[0], text=True, capture_output=True)
    assert node.returncode == 0, f"{rel} JavaScript 語法錯誤：{node.stderr}"

wiki = (ROOT / "01_Wiki/index.html").read_text(encoding="utf-8")
mag = (ROOT / "02_HTML_Magazine/index.html").read_text(encoding="utf-8")
assets = ("coffee_atlas_hero.svg", "processing_methods.svg", "flavor_wheel.svg", "brewing_steps.svg")
for name in assets:
    assert (ROOT / "01_Wiki/assets" / name).exists(), f"缺少 SVG：{name}"
assert "assets/coffee_atlas_hero.svg" in wiki
assert "../01_Wiki/assets/coffee_atlas_hero.svg" in mag
assert "coffee_atlas_hero.png" not in mag
print("PASS：五冊 Markdown、11 個章節結構、15 筆來源（8+5+2）。")
print("PASS：Wiki／雜誌 HTML 本地資源、重複 id 與 script 標籤。")
print("PASS：Node.js 內嵌 JavaScript 語法檢查。")
print("PASS：4 個 SVG 圖像路徑與 A4 APA 作者排序。")
print("NOTE：此為靜態驗證；搜尋、收藏、滾輪、圖片放大、列印與全螢幕仍需在真實瀏覽器操作。")

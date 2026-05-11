from fastmcp import FastMCP
from datetime import datetime
import re, unicodedata, json, urllib.request

mcp = FastMCP("darija-toolkit")

# ─────────── TOOLS ───────────

@mcp.tool
def transliterate(text: str) -> str:
    """Convert Arabic script to Latin (Buckwalter-ish). Useful for logs."""
    table = str.maketrans({
        "ا":"a","ب":"b","ت":"t","ث":"th","ج":"j","ح":"7","خ":"kh","د":"d",
        "ذ":"dh","ر":"r","ز":"z","س":"s","ش":"sh","ص":"S","ض":"D","ط":"T",
        "ظ":"Z","ع":"3","غ":"gh","ف":"f","ق":"q","ك":"k","ل":"l","م":"m",
        "ن":"n","ه":"h","و":"w","ي":"y","ى":"a","ة":"a","ء":"a",
    })
    return unicodedata.normalize("NFKC", text).translate(table)

@mcp.tool
def detect_dialect(text: str) -> dict:
    """Heuristic Darija vs MSA detector."""
    darija_markers = ["wach","wash","bzaf","bzef","ghadi","kayn","makayn",
                      "f7al","kima","dyal","nta","nti","khouya","mashi"]
    msa_markers    = ["إن","لكن","حيث","سوف","قد","الذي","التي","لأن"]
    t = text.lower()
    d = sum(1 for m in darija_markers if m in t)
    a = sum(1 for m in msa_markers    if m in text)
    if d == a == 0:
        return {"dialect":"unknown","confidence":0.0,"markers":[]}
    if d > a:
        return {"dialect":"darija","confidence":d/(d+a),
                "markers":[m for m in darija_markers if m in t]}
    return {"dialect":"msa","confidence":a/(d+a),
            "markers":[m for m in msa_markers if m in text]}

@mcp.tool
def clean_arabic(text: str) -> str:
    """Strip diacritics, tatweel, and redundant whitespace."""
    text = re.sub(r"[\u064B-\u0652\u0670\u0640]", "", text)
    return re.sub(r"\s+"," ", text).strip()

@mcp.tool
def hijri_today() -> str:
    """Today's Hijri date via Aladhan public API."""
    url = "https://api.aladhan.com/v1/gToH?date=" + datetime.now().strftime("%d-%m-%Y")
    with urllib.request.urlopen(url, timeout=5) as r:
        data = json.loads(r.read())
    h = data["data"]["hijri"]
    return f'{h["day"]} {h["month"]["en"]} {h["year"]} AH'

# ─────────── RESOURCES ───────────

@mcp.resource("darija://stopwords")
def stopwords() -> str:
    """The 1337AI Darija stopword list."""
    sw = ["bach","ghir","ghadi","kayn","kayna","wach","wash","bzaf","kifach",
          "fin","fach","9bel","mn","l","f","b","3la","m3a","bla","kol","kollchi"]
    return "\n".join(sw)

@mcp.resource("darija://greetings")
def greetings() -> str:
    """Common Darija greetings, transliterated + Arabic."""
    return json.dumps([
        {"latin":"salam","arabic":"سلام","meaning":"hello"},
        {"latin":"labas","arabic":"لاباس","meaning":"how are you"},
        {"latin":"bikhir","arabic":"بخير","meaning":"fine"},
        {"latin":"shokran","arabic":"شكرا","meaning":"thank you"},
    ], ensure_ascii=False)

# ─────────── PROMPTS ───────────

@mcp.prompt
def summarize_in_darija(text: str) -> str:
    """Summarize the given text in 3 sentences of Darija."""
    return f"Lkhad had nass w 3tini résumé f tlata jamals b darija:\n\n{text}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8765)

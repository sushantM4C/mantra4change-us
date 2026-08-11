"""Regenerates assets/js/data.js.

Board content transcribed from the 2026-27 M4C US Board CSV.
Photos are looked up at assets/img/board/<slug>.jpg and fall back to
initials if absent, so photos drop in without any code change.
"""
import json

m = json.load(open("india-map.json"))

states = [
  {"name":"Uttar Pradesh","schools":"135,000","leaders":"143,000","children":"18.4M",
   "note":"69.62% of schools reached NIPUN status in the Super-150 blocks \u2014 rising to 74.28% at the sharpest end.",
   "accent":"navy"},
  {"name":"Punjab","schools":"19,175","leaders":"3,455","children":"2.88M",
   "note":"Over 1,000 students cleared national engineering and medical entrance exams. Punjab ranked #1 in India for learning outcomes in NAS 2021.",
   "budget":"$25M state budget unlocked for Schools of Eminence","accent":"sky"},
  {"name":"Bihar","schools":"28,989","leaders":"28,989","children":"5.42M",
   "note":"Students gained up to two years' worth of learning in a single year, with the strongest movement in Grades 7 and 8.",
   "budget":"~$2.5M state budget unlocked","accent":"green"},
  {"name":"Karnataka","schools":"42,000+","leaders":"47,690","children":"5.19M",
   "note":"A 12.48-point gain in foundational literacy and numeracy across Bangalore district, and a 33-point improvement in head-teacher workshop effectiveness.",
   "accent":"orange"},
  {"name":"Odisha","schools":"1,737","leaders":"9,000+","children":"400,000+",
   "note":"Convened a state-level collective to improve residential education for tribal and underserved children.",
   "budget":"~$60,000 state budget unlocked","accent":"amber"},
  {"name":"Andhra Pradesh","schools":"107","leaders":"107","children":"18,143",
   "note":"In MJP schools, students made up to two years' progress in one year in Grade 6 English, Grade 6 Math and Grade 7 Science.",
   "accent":"steel"},
]
active = {s["name"] for s in states}

def slug(name):
    out = "".join(c.lower() if c.isalnum() else "-" for c in name).strip("-")
    while "--" in out:
        out = out.replace("--", "-")
    return out

def p(name, role, li, bio=None):
    return {"name": name, "role": role, "li": li, "slug": slug(name), "bio": bio or []}

RASHI = [
  "Rashi Mehta is a global entrepreneur, executive coach, and philanthropy leader whose work brings together business, leadership, and social impact.",
  "As Co-Founder of Rahi Systems, Rashi helped build a bootstrapped Silicon Valley startup into a global technology company operating in more than 25 countries before its successful acquisition by Wesco, a Fortune 200 company. Without external funding, she led the company's financial strategy and operations through every stage of growth, helping transform an entrepreneurial vision into a thriving international enterprise. Reflecting on that journey, she often says, \u201cBuilding something from the ground up teaches you that resilience, discipline, and people matter far more than resources.\u201d",
  "Passionate about helping others unlock their potential, Rashi studied Executive Coaching at UC Berkeley and has coached CEOs, CFOs, and senior leaders across industries. She believes that leadership is not defined by position or title, but by the ability to inspire and serve others. \u201cThe best leaders never stop learning, and they never stop lifting others as they rise,\u201d she says.",
  "Rashi serves on the Board of the Make-A-Wish Foundation Greater Bay Area, supporting its mission to bring hope and joy to children facing critical illnesses.",
  "In 2024, she founded the Iron Lady Foundation in memory of her mother, Dr. Leela Mehta, a pioneering gynecologist whose life of compassion, courage, and service inspired generations. Guided by the belief that every woman and child deserves dignity, opportunity, and the chance to thrive, the Foundation works across education, healthcare, clean water, sanitation, and women's economic empowerment.",
  "For Rashi, philanthropy is deeply personal. \u201cReal change happens when communities are empowered to shape their own future,\u201d she says. Through community-led initiatives, the Iron Lady Foundation is helping create opportunities that strengthen families and spark lasting generational change.",
  "At the heart of everything Rashi does is a belief she learned from the women who shaped her life: \u201cWhen you empower one woman, you don't just change her life\u2014you change the lives of everyone she touches.\u201d",
]

RADHIKA = [
  "Radhika Shah is a technology and impact investor, entrepreneur, and ecosystem builder. She has served as Co-President of Stanford Angels & Entrepreneurs and is Co-Founder and Co-President of the Stanford Alumni Alliance on Innovation for Global Impact. She is also the Founding Co-Chair of the UN Joint SDG Fund Breakthrough Alliance and the SDG Digital Transformation Lab. She advances innovation, sustainable development, and technology-driven social impact through global partnerships.",
]

PRASHANTH = [
  "Prashanth Reddy is a Senior Partner at McKinsey & Company based in New Jersey, where he has spent nearly 20 years serving private equity firms, health insurers, health services companies, pharma services organizations, providers, and technology clients. His work spans growth strategy, investing, performance, operations transformation, and healthcare value creation.",
  "He holds a Master's in Finance from London Business School, where he graduated in the top 10% of his class as a Merrill Lynch Foundation Scholar, an MBA from the Indian Institute of Management, Ahmedabad, and a B.S. in Computer Engineering from the National Institute of Technology, Surathkal. He serves on the Board of Trustees of The Pingry School in Basking Ridge, New Jersey. Outside of client work, Prashanth is actively involved in mentoring and developing colleagues and future leaders across the firm.",
]

BOARD = [
  {"title": "Board of Directors",
   "blurb": "Ten leaders across technology, consulting, investment, real estate and education, guiding the strategy and stewardship of the US entity.",
   "people": [
     p("Rashi Mehta", "Founder & Chair, Iron Lady Foundation", "https://www.linkedin.com/in/raashi/", RASHI),
     p("Cornelius Walter", "Deputy Head, Administration of the Princely Assets Liechtenstein", "https://www.linkedin.com/in/cornelius-walter/"),
     p("Pradeep Nair", "Principal & Strategic Advisor, Flat Cosmos", "https://www.linkedin.com/in/pdnair/"),
     p("Ambili Sukesan", "Global Real Estate Investment Advisor, Realogics Sotheby's International Realty", "https://www.linkedin.com/in/amilrealty/"),
     p("Charag Krishnan", "Partner at McKinsey & Company", "https://www.linkedin.com/in/charagk/"),
     p("Esther Wojcicki", "Founder of ParentingTRICK App and Treehub by AI Health Fund", "https://www.linkedin.com/in/estherwojcicki/"),
     p("Rajiv Murali", "Managing Director and Partner, Boston Consulting Group (BCG)", "https://www.linkedin.com/in/rajivmurali/"),
     p("Kirti Reddy", "Founder and Managing Partner at Cedar Ridge Ventures", "https://www.linkedin.com/in/kirti-reddy-6800b01b6/"),
     p("Vivek Ragavan", "Board Director", "https://www.linkedin.com/in/vivek-ragavan-0b974/"),
     p("Aditya Vishwanath", "Co-Founder and Board Director, MakerGhat", "https://www.linkedin.com/in/adityavishwanath/"),
   ]},
  {"title": "Board of Advisors",
   "blurb": "Advisors bringing deep experience in global innovation, sustainable development and healthcare strategy.",
   "people": [
     p("Radhika Shah", "Co-Founder and Co-President, Stanford Alumni Alliance on Innovation for Global Impact \u00b7 Founding Co-Chair, United Nations Joint SDG Fund Breakthrough Alliance for Climate", "https://www.linkedin.com/in/radhikashah1/", RADHIKA),
     p("Prashanth Reddy", "Senior Partner at McKinsey & Company", "https://www.linkedin.com/in/preddy/", PRASHANTH),
   ]},
]

map_states = [{"name": s["name"], "d": s["d"], "on": s["name"] in active} for s in m["states"]]
slugs = ", ".join(pp["slug"] for g in BOARD for pp in g["people"])

js = """/* Auto-generated - rebuild with:
     cd tools && python3 gen_data.py && cp data.js ../assets/js/data.js

   INDIA_MAP   simplified state outlines (Mercator, dissolved from district boundaries)
   STATE_DATA  per-state reach figures, Comms Resource Center (Sep 2026)
   BOARD       Mantra4Change US board, from the 2026-27 board CSV

   Board photos: drop square JPGs at assets/img/board/<slug>.jpg
   Slugs: %s
   A missing photo falls back to initials automatically. */

const INDIA_MAP = {
  viewBox: %s,
  states: %s
};

const STATE_DATA = %s;

const BOARD = %s;
""" % (
  slugs,
  json.dumps(m["viewBox"]),
  json.dumps(map_states, separators=(",", ":")),
  json.dumps(states, indent=2, ensure_ascii=False),
  json.dumps(BOARD, indent=2, ensure_ascii=False),
)

open("data.js", "w").write(js)
print("data.js written:", len(js), "bytes")
for g in BOARD:
    print(" ", g["title"])
    for pp in g["people"]:
        print("   %-22s bio paras: %d" % (pp["slug"], len(pp["bio"])))

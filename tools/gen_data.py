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

def p(name, role, li, bio, photo=None):
    return {"name": name, "role": role, "li": li,
            "slug": photo or slug(name), "bio": bio}

# Bios transcribed verbatim from the Mantra4Change US site. Where a bio was too
# long for the card to sit level with its neighbours, whole trailing sentences
# were dropped - no wording inside a retained sentence has been altered.
BOARD = [
  {"title": "Board of Directors",
   "people": [
     p("Dr. Aditya Vishwanath", "Trustee", "https://www.linkedin.com/in/adityavishwanath/",
       "Dr. Aditya Vishwanath is an education technology researcher and entrepreneur whose work bridges learning, design, and technology. As Co-founder and CEO of Inspirit and Co-founder of MakerGhat, his efforts have focused on making digital learning more engaging and accessible across diverse contexts.",
       photo="aditya-vishwanath"),
     p("Ambili Sukesan", "Treasurer", "https://www.linkedin.com/in/amilrealty/",
       "Supporting M4C-USA with all the legal compliances, Ambili is highly accomplished in the real estate sector with exemplary customer experience in the USA, Europe and Asia. With strong communication, problem-solving and negotiation acumen, and through deep market and financial analyses, Ambili provides exemplary real estate advisory services."),
     p("Charag Krishnan", "Trustee", "https://www.linkedin.com/in/charagk/",
       "Partner in Mckinsey\u2019s education work, Charag helps higher education institutions change their trajectory through holistic performance transformations and M&A. Expertise include strategies for improving enrolment, student success and retention, online learning, auxiliary revenues, and organizational capability building."),
     p("Cornelius Walter", "President", "https://www.linkedin.com/in/cornelius-walter/",
       "A former senior partner at Mckinsey & Company where Cornelius advised on a broad range of growth strategies and large-scale transformations. Currently, a strategic partner at Lightrock, a leading global impact investing platform, Cornelius invests and serves on the boards of start-ups and later-stage companies with environmental, social, and governance (ESG) goals and sustainable business models."),
     p("Esther Wojcicki", "Trustee", "https://www.linkedin.com/in/estherwojcicki/",
       "Esther Denise \u201cWoj\u201d Hochman Wojcicki is an American journalist, educator, and vice chair of the Creative Commons Advisory Council. Wojcicki has studied education and technology. She is the founder of the Palo Alto High School Media Arts Program in Palo Alto, California."),
     p("Kirti Reddy", "Trustee", "https://www.linkedin.com/in/kirti-reddy-6800b01b6/",
       "An alumna of the London School of Economics, Kirti brings a wealth of experience and leadership as Founder and Managing Partner of Cedar Ridge Ventures. With a background in investment banking at Deutsche Bank and UBS, Kirti\u2019s expertise will undoubtedly contribute to our mission."),
     p("Pradeep Nair", "Trustee", "https://www.linkedin.com/in/pdnair/",
       "Former Regional Director (India) for Ford Foundation, Pradeep has over 25 years of global experience, in technology, management consulting, and investing/funding. Starting in Silicon Valley as a big five management consultant, building software application products, Pradeep was part of an advisory start-up led by President Clinton and Mayor Bloomberg."),
     p("Rajiv Murali", "Trustee", "https://www.linkedin.com/in/rajivmurali/",
       "He is a core member of the Energy practice with extensive experience in digital initiatives across heavy industry companies, including exploration, development, operations, supply chain, digital transformations, and decarbonization/carbon accounting at BCG. He is currently focused on helping clients use data analytics and AI for better decision-making, safety, and workforce efficiency."),
     p("Rashi Mehta", "Trustee", "https://www.linkedin.com/in/raashi/",
       "A global entrepreneur, executive coach, and philanthropy leader, Rashi Mehta co-founded Rahi Systems, helping grow the bootstrapped Silicon Valley startup into a global technology company operating in more than 25 countries before its acquisition by Wesco, a Fortune 200 company. An executive coach trained at UC Berkeley, she has coached CEOs and senior leaders across industries."),
     p("Vivek Ragavan", "Trustee", "https://www.linkedin.com/in/vivek-ragavan-0b974/",
       "Vivek Ragavan brings over three decades of leadership experience in the telecommunications and technology sectors. A seasoned entrepreneur, he has served as President and CEO of several leading companies and continues to contribute to education and innovation through his roles with the Akanksha Fund, the Motivation for Excellence Initiative, and Northwestern University\u2019s McCormick School of Engineering."),
   ]},
  {"title": "Board of Advisors",
   "people": [
     p("Prashanth Reddy", "Advisor", "https://www.linkedin.com/in/preddy/",
       "Prashanth Reddy is a Senior Partner at McKinsey & Company based in New Jersey, where he has spent nearly 20 years serving private equity firms, health insurers, health services companies, pharma services organizations, providers, and technology clients. His work spans growth strategy, investing, performance, operations transformation, and healthcare value creation."),
     p("Radhika Shah", "Advisor", "https://www.linkedin.com/in/radhikashah1/",
       "Radhika Shah is a technology and impact investor, entrepreneur, and ecosystem builder. She has served as Co-President of Stanford Angels & Entrepreneurs and is Co-Founder and Co-President of the Stanford Alumni Alliance on Innovation for Global Impact. She is also the Founding Co-Chair of the UN Joint SDG Fund Breakthrough Alliance and the SDG Digital Transformation Lab."),
   ]},
]

# alphabetical within each group
for _g in BOARD:
    _g["people"].sort(key=lambda pp: pp["name"].replace("Dr. ", "").lower())

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
        print("   %-22s %-10s %4d chars" % (pp["slug"], pp["role"], len(pp["bio"])))

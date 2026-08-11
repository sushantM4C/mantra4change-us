import json

m = json.load(open("india-map.json"))

# ---------------------------------------------------------------- states
# Figures from the Comms Resource Center (M4C x Shikshagraha deck, Sep 2026).
# Lakh/crore converted to US reading conventions.
states = [
  {"name":"Uttar Pradesh","schools":"135,000","leaders":"143,000","children":"18.4M",
   "note":"69.62% of schools reached NIPUN status in the Super-150 blocks — rising to 74.28% at the sharpest end.",
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

# ---------------------------------------------------------------- board
def p(name, role, li=None, bio=None):
    d = {"name": name, "role": role}
    if li:  d["li"] = "https://www.linkedin.com/in/" + li
    if bio: d["bio"] = bio
    return d

board = {
  "us": {
    "label": "US Board",
    "groups": [
      {"title": "Board of Directors", "people": [
        p("Rashi Mehta", "Founder & Chair, Iron Lady Foundation", "raashi",
          ["Rashi Mehta is a global entrepreneur, executive coach and philanthropy leader whose work brings together business, leadership and social impact. As Co-Founder of Rahi Systems, she helped build a bootstrapped Silicon Valley startup into a global technology company operating in more than 25 countries, before its acquisition by Wesco, a Fortune 200 company.",
           "Passionate about helping others unlock their potential, Rashi studied Executive Coaching at UC Berkeley and has coached CEOs, CFOs and senior leaders across industries.",
           "She serves on the board of the Make-A-Wish Foundation Greater Bay Area. In 2024 she founded the Iron Lady Foundation in memory of her mother, Dr. Leela Mehta, working across education, healthcare, clean water, sanitation and women's economic empowerment."]),
        p("Cornelius Walter", "Deputy Head, Administration of the Princely Assets, Liechtenstein", "cornelius-walter"),
        p("Pradeep Nair", "Principal & Strategic Advisor, Flat Cosmos", "pdnair"),
        p("Ambili Sukesan", "Global Real Estate Investment Advisor, Realogics Sotheby's International Realty", "amilrealty"),
        p("Charag Krishnan", "Partner, McKinsey & Company", "charagk"),
        p("Esther Wojcicki", "Founder, ParentingTRICK App and Treehub by AI Health Fund", "estherwojcicki"),
        p("Rajiv Murali", "Managing Director and Partner, Boston Consulting Group", "rajivmurali"),
        p("Kirti Reddy", "Founder and Managing Partner, Cedar Ridge Ventures", "kirti-reddy-6800b01b6"),
        p("Vivek Ragavan", "Board of Directors", "vivek-ragavan-0b974"),
        p("Aditya Vishwanath", "Co-Founder and Board Director, MakerGhat", "adityavishwanath"),
      ]},
      {"title": "Board of Advisors", "people": [
        p("Radhika Shah", "Co-Founder & Co-President, Stanford Alumni Alliance on Innovation for Global Impact", "radhikashah1",
          ["Radhika Shah is a technology and impact investor, entrepreneur and ecosystem builder. She has served as Co-President of Stanford Angels & Entrepreneurs and is Co-Founder and Co-President of the Stanford Alumni Alliance on Innovation for Global Impact.",
           "She is also Founding Co-Chair of the UN Joint SDG Fund Breakthrough Alliance and the SDG Digital Transformation Lab, advancing innovation, sustainable development and technology-driven social impact through global partnerships."]),
        p("Prashanth Reddy", "Senior Partner, McKinsey & Company", "preddy",
          ["Prashanth Reddy is a Senior Partner at McKinsey & Company based in New Jersey, where he has spent nearly 20 years serving private equity firms, health insurers, health services companies, pharma services organisations, providers and technology clients. His work spans growth strategy, investing, performance, operations transformation and healthcare value creation.",
           "He holds a Master's in Finance from London Business School, an MBA from the Indian Institute of Management Ahmedabad, and a B.S. in Computer Engineering from the National Institute of Technology, Surathkal. He serves on the Board of Trustees of The Pingry School in Basking Ridge, New Jersey."]),
      ]},
    ],
  },
  "india": {
    "label": "India Board",
    "groups": [
      {"title": "Board of Directors", "people": [
        p("Amee Parikh", "Director, Amansa Capital Ltd.", "amee-parikh-12128597"),
        p("Aaradhana Dalmia", "Trustee, Dalmia Charitable Trust · Chairperson, YFLO Delhi", "aaradhana-dalmia-8b817b14"),
        p("Chetan Kapoor", "CEO, Tech Mahindra Foundation", "chetankapoorcsr"),
        p("Vijayshree Urs", "CTO, ShikshaLokam", "vijayashree-urs"),
        p("Saurabh Singh", "Program Director, Mantra4Change", "saurabh-singh-he-him"),
      ]},
      {"title": "Board of Advisors", "people": [
        p("Vikram Bhat", "CEO, SCALE", "vikram-bhat-scale"),
        p("Nikunj Jhaveri", "Founder & Chairman, Systems Plus Group of Companies", "nikunjjhaveri"),
        p("Deepak Satwalekar", "Former Managing Director, HDFC Ltd.", "deepak-satwalekar-248b575a"),
        p("Daya Kori", "Managing Director, Software R+D Center"),
        p("KL Mukesh", "Venture Partner, Unitus Ventures", "kl-mukesh-4a5a16"),
      ]},
    ],
  },
  "team": {
    "label": "Leadership Team",
    "groups": [
      {"title": "Leadership Team", "people": [
        p("Santosh Kumar More", "Chief Executive Officer", "santosh-more-m4c"),
        p("Sandeep Parakkal", "Chief Finance Officer", "sandeep-parakkal-m4c"),
        p("Vernon Noel Noronha", "Chief Growth Officer", "v3rn0n"),
        p("Aileen Yuet Lien Chen", "Chief of Staff", "aileen-ch"),
      ]},
    ],
  },
}

# ------------------------------------------------------------- emit
map_states = [
    {"name": s["name"], "d": s["d"], "on": s["name"] in active}
    for s in m["states"]
]

js = f"""/* Auto-generated data for the Mantra4Change US site.
   - INDIA_MAP  : simplified state outlines (Mercator, dissolved from 2011/2019 district boundaries)
   - STATE_DATA : reach figures per state, Comms Resource Center (Sep 2026 deck)
   - BOARD      : board + leadership roster, Comms Resource Center
   Regenerate the map with tools/build_map.py if boundaries ever need updating. */

const INDIA_MAP = {{
  viewBox: {json.dumps(m["viewBox"])},
  states: {json.dumps(map_states, separators=(",", ":"))}
}};

const STATE_DATA = {json.dumps(states, indent=2, ensure_ascii=False)};

const BOARD = {json.dumps(board, indent=2, ensure_ascii=False)};
"""

open("data.js", "w").write(js)
print("data.js", len(js), "bytes")

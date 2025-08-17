import json
import random

# Target count
TOTAL_TOOLS = 1_000_000  

# Sample base tools (few only, will expand automatically)
base_tools = [
    {"title": "GitHub Pages", "desc": "Free static hosting", "url": "https://pages.github.com", "tags": ["hosting"], "icon": "server"},
    {"title": "Netlify", "desc": "Fast static site hosting", "url": "https://www.netlify.com", "tags": ["hosting","cloud"], "icon": "cloud"},
    {"title": "Vercel", "desc": "Deploy Next.js apps easily", "url": "https://vercel.com", "tags": ["hosting"], "icon": "cloud"},
    {"title": "Figma", "desc": "UI/UX design platform", "url": "https://www.figma.com", "tags": ["design"], "icon": "figma"},
]

icons = [t["icon"] for t in base_tools]
tags_pool = sorted({tag for t in base_tools for tag in t["tags"]})

tools = []
for i in range(TOTAL_TOOLS):
    base = base_tools[i % len(base_tools)]
    suffix = i + 1
    tool = {
        "title": f"{base['title']} Tool #{suffix}",
        "desc": f"{base['desc']} (auto #{suffix})",
        "url": f"{base['url']}?id={suffix}",
        "tags": random.sample(tags_pool, k=random.randint(1, min(3, len(tags_pool)))),
        "icon": icons[i % len(icons)]
    }
    tools.append(tool)

data = {
    "tools": tools,
    "packs": [],
    "learning": []
}

with open("tools_big.json", "w", encoding="utf-8") as f:
    json.dump(data, f, separators=(",", ":"))
    
print(f"✅ Generated {TOTAL_TOOLS} tools → tools_big.json")

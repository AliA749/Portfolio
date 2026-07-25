"""
Ali Alkhulaqi — Portfolio
A small Flask app. The point of building this in Python (rather than a static
HTML file) is to actually demonstrate backend/Python usage: the experience,
project, and skill data below live as real Python data structures, get
rendered server-side with Jinja, and are also exposed as JSON over a small API.
"""

from flask import Flask, render_template, jsonify, send_from_directory
from datetime import date

app = Flask(__name__)


ARCS = [
    {
        "number": "01",
        "role": "Coding Coach",
        "org": "TheCoderSchool",
        "location": "Bayside, NYC",
        "when": "Oct 2025 – Apr 2026",
        "beats": [
            "Taught coding fundamentals (Scratch, Python) to 15+ students across skill levels, with custom lesson plans per learner.",
            "Substituted across classes, keeping progress consistent for every student.",
            "Introduced project-based learning, guiding advanced students through building functional Python applications.",
        ],
    },
    {
        "number": "02",
        "role": "IT Media Intern",
        "org": "Skylight Pharmacy",
        "location": "Jamaica, NYC",
        "when": "Jul 2025 – Aug 2025",
        "beats": [
            "Produced promotional video content for Instagram and TikTok, growing digital brand engagement.",
            "Launched and managed Google Ads and Meta Ads campaigns to expand reach.",
            "Streamlined internal data entry workflows and assisted with day-to-day IT support.",
        ],
    },
    {
        "number": "03",
        "role": "Backend Developer",
        "org": "Project Empower",
        "location": "Remote",
        "when": "Aug 2024 – Jan 2025",
        "beats": [
            "Architected user authentication and API routing for a non-profit platform serving low-income, first-gen college students.",
            "Engineered session management for zero-error post-login routing across authenticated flows.",
            "Co-organized the Project Empower Hackathon (2,000+ participants, $200,000 in prizes).",
        ],
    },
    {
        "number": "04",
        "role": "Cashier / Customer Service Lead",
        "org": "Go Detox",
        "location": "Van Wyck, NYC",
        "when": "Jun 2021 – Dec 2023",
        "beats": [
            "Led a team of 3 through daily operations during 20–30 hour summer weeks.",
            "Resolved third-party delivery platform issues (Uber Eats, DoorDash, Grubhub), cutting order errors and improving turnaround.",
        ],
    },
]

PROJECTS = [
    {
        "title": "PR Review Assistant",
        "when": "Jul 2026 – Present",
        "tags": ["TypeScript", "React", "Supabase", "Groq AI", "Claude"],
        "beats": [
            "Full-stack web app: TypeScript backend, React frontend.",
            "GitHub OAuth to pull a user's repositories.",
            "AI reviews the chosen pull request and surfaces vulnerabilities.",
            "Groq powers inference; Claude assisted planning and implementation.",
        ],
    },
    {
        "title": "Non-Profit Student Database",
        "when": "Aug 2025 – Jan 2026",
        "tags": ["TypeScript", "MongoDB"],
        "beats": [
            "Architected the database schema and secure REST API routes for Project Empower's student-facing platform.",
            "Handled authentication flows and role-based routing logic.",
        ],
    },
]

SKILLS = {
    "Languages": ["Java", "Python", "SQL (MySQL)", "TypeScript"],
    "Frameworks": ["React", "Node.js", "Flask", "FastAPI"],
    "Tools": ["Git", "Docker", "Claude", "VS Code", "IntelliJ", "Linux"],
    "Certifications": ["YouScience — Java", "Mimo — TypeScript"],
}

CONTACT = {
    "name": "Ali Alkhulaqi",
    "phone": "347-750-4280",
    "email": "alialkhulaqi2115@gmail.com",
    "linkedin": "linkedin.com/in/ali-alkhulaqi",
    "github": "github.com/Ali749",
}


@app.route("/")
def index():
    return render_template(
        "index.html",
        arcs=ARCS,
        projects=PROJECTS,
        skills=SKILLS,
        contact=CONTACT,
        year=date.today().year,
    )


@app.route("/api/skills")
def api_skills():
    """Small JSON endpoint — the page fetches this client-side to render
    the skills grid, so the skills are genuinely served by Python, not
    just baked into static HTML."""
    return jsonify(SKILLS)


@app.route("/resume")
def resume():
    return send_from_directory(
        "static/resume", "Ali_Alkhulaqi_Resume.pdf", as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)

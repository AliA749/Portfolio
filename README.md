# Ali Alkhulaqi — Portfolio (Flask)

A dark, manga-panel-inspired portfolio site. Built with **Flask** on purpose —
your experience, projects, and skills live as real Python data structures in
`app.py`, get rendered server-side with Jinja, and the skills grid is also
served live from a small JSON API (`/api/skills`) and fetched client-side.
That's the "written in Python" part beyond just styling.

## Run it locally

```bash
cd portfolio
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

## Editing content

Everything you'd want to update — job history, projects, skills, contact info —
is at the top of `app.py` as plain Python lists/dicts (`ARCS`, `PROJECTS`,
`SKILLS`, `CONTACT`). Edit those, no HTML editing required for content changes.

## Deploying

This is a standard Flask app, so it deploys anywhere that runs Python:
Render, Railway, Fly.io, PythonAnywhere, or a small VPS behind gunicorn:

```bash
pip install gunicorn
gunicorn app:app
```

## Structure

```
portfolio/
├── app.py                 # Flask routes + your content as Python data
├── requirements.txt
├── templates/
│   └── index.html         # Jinja template
└── static/
    ├── css/style.css
    ├── js/main.js          # fetches /api/skills, runs the terminal typewriter
    └── resume/Ali_Alkhulaqi_Resume.pdf   # served at /resume
```

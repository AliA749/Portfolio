// Skills are fetched from the Flask backend (/api/skills), not hard-coded
// into the HTML — a small, honest way to prove the Python is doing work.
async function loadSkills() {
  const grid = document.getElementById("skills-grid");
  try {
    const res = await fetch("/api/skills");
    const data = await res.json();
    grid.innerHTML = Object.entries(data)
      .map(
        ([group, items]) => `
        <div class="skill-group">
          <h4>${group}</h4>
          <ul>${items.map((i) => `<li>${i}</li>`).join("")}</ul>
        </div>`
      )
      .join("");
  } catch (err) {
    grid.innerHTML = `<p style="color:var(--ash)">Couldn't reach the skills API.</p>`;
  }
}
loadSkills();

// Terminal typewriter — purely cosmetic, but keeps the Python theme visible
// above the fold.
const lines = [
  "class Developer:",
  "    def __init__(self):",
  '        self.stack = ["Python", "TypeScript", "React"]',
  "        self.debugging = True",
  "",
  "    def ship(self, idea):",
  "        return build(idea).deploy()",
];
const el = document.getElementById("typewriter");
let li = 0, ci = 0;

function typeNext() {
  if (li >= lines.length) return;
  const line = lines[li];
  if (ci <= line.length) {
    const done = lines.slice(0, li).join("\n");
    el.textContent = (done ? done + "\n" : "") + line.slice(0, ci);
    ci++;
    setTimeout(typeNext, 22);
  } else {
    li++;
    ci = 0;
    setTimeout(typeNext, 180);
  }
}
if (el) typeNext();

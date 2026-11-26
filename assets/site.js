/* 6thSTAR site v1.1 */

/* ── The one action. A single switch: set LISTING_APPROVED to true and fill LISTING_URL
      once Shopify approves the listing. Until then every "Install 6thSTAR" opens /beta/. ── */
const SITE = {
  LISTING_APPROVED: false,
  LISTING_URL: "",              /* the Shopify App Store listing, once approved */
  BETA_URL: "/beta/",
  SUPPORT: "6thstarsupport@gmail.com",
};
const INSTALL_HREF = (SITE.LISTING_APPROVED && SITE.LISTING_URL) ? SITE.LISTING_URL : SITE.BETA_URL;
document.querySelectorAll("[data-install]").forEach(a => { a.href = INSTALL_HREF; });

/* ── Films: nothing plays until clicked; then the player shows its own controls ── */
document.querySelectorAll(".film[data-src]").forEach(box => {
  const start = () => {
    if (box.dataset.started) return;
    box.dataset.started = "1";
    const v = document.createElement("video");
    v.src = box.dataset.src; v.controls = true; v.playsInline = true; v.preload = "auto";
    if (box.dataset.poster) v.poster = box.dataset.poster;
    if (box.dataset.vtt) {
      const t = document.createElement("track");
      t.kind = "captions"; t.srclang = "en"; t.label = "English"; t.src = box.dataset.vtt;
      v.appendChild(t);
    }
    box.replaceChildren(v);
    v.play().catch(() => {});
  };
  box.addEventListener("click", start);
  box.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); start(); } });
});

/* ── MARLOW: the star opens the line on hover, focus or tap ── */
document.querySelectorAll(".shot[data-line]").forEach(shot => {
  const hit = shot.querySelector(".star-hit");
  if (!hit) return;
  const set = on => { shot.classList.toggle("open", on); hit.setAttribute("aria-expanded", on ? "true" : "false"); };
  hit.addEventListener("mouseenter", () => set(true));
  shot.addEventListener("mouseleave", () => set(false));
  hit.addEventListener("focus", () => set(true));
  hit.addEventListener("blur", () => set(false));
  hit.addEventListener("click", e => { e.preventDefault(); set(!shot.classList.contains("open")); });
});

/* ── Setup wizards: one screen at a time, Back and Next, "Step n of N" ── */
document.querySelectorAll(".wiz").forEach(wiz => {
  const steps = [...wiz.querySelectorAll("template[data-step]")].map(t => ({
    say: t.dataset.say, img: t.dataset.img || "", alt: t.dataset.alt || "", ph: t.dataset.ph || "", label: t.dataset.label || ""
  }));
  const shot = wiz.querySelector(".wiz-shot"), say = wiz.querySelector(".wiz-say"), count = wiz.querySelector(".wiz-count");
  const back = wiz.querySelector(".back"), next = wiz.querySelector(".next");
  const total = steps.filter(s => !s.label).length;
  let i = 0;
  const draw = () => {
    const s = steps[i];
    shot.replaceChildren();
    if (s.img) { const im = new Image(); im.src = s.img; im.alt = s.alt; shot.appendChild(im); }
    else { const d = document.createElement("div"); d.className = "ph"; d.textContent = s.ph || "Screenshot to come"; shot.appendChild(d); }
    say.innerHTML = s.say;
    const n = steps.slice(0, i + 1).filter(x => !x.label).length;
    count.textContent = s.label ? s.label : `Step ${n} of ${total}`;
    back.disabled = i === 0;
    next.disabled = i === steps.length - 1;
  };
  back.addEventListener("click", () => { if (i > 0) { i--; draw(); } });
  next.addEventListener("click", () => { if (i < steps.length - 1) { i++; draw(); } });
  draw();
});

/* ── Beta request: until the site has its own sender, the form opens a filled-in email to support ── */
const form = document.querySelector("form.beta");
if (form) {
  form.addEventListener("submit", e => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    const f = new FormData(form);
    const body = [
      "Name: " + f.get("name"),
      "Email: " + f.get("email"),
      "Store URL: " + f.get("store"),
      "Orders a month (roughly): " + f.get("orders"),
      "Selling for: " + f.get("selling"),
    ].join("\n");
    location.href = "mailto:" + SITE.SUPPORT + "?subject=" + encodeURIComponent("6thSTAR beta request") + "&body=" + encodeURIComponent(body);
    form.hidden = true;
    document.querySelector(".thanks").classList.add("show");
  });
}

/* For screenshots: ?open=1 shows MARLOW's line already open */
if (new URLSearchParams(location.search).get("open") === "1") document.querySelectorAll(".shot[data-line]").forEach(s => s.classList.add("open"));

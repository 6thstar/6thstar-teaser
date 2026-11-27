/* 6thSTAR site v1.1 */

/* ── The one action. A single switch: set LISTING_APPROVED to true and fill LISTING_URL
      once Shopify approves the listing. Until then every "Request more information" button opens /beta/. ── */
const SITE = {
  LISTING_APPROVED: false,
  LISTING_URL: "",              /* the Shopify App Store listing, once approved */
  BETA_URL: "/beta/",
  SUPPORT: "trosen@rosengroup.us",          /* Script v2.0: the contact email, for now */
  BETA_ENDPOINT: "https://sixthstar-app-y2dab.ondigitalocean.app/beta-request",   /* the 6thSTAR app keeps and emails each request */
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

/* ── The spot from the hero (Script v2.0): opens in a box and plays only after the click; closing stops it ── */
const box = document.querySelector("dialog.filmbox");
document.querySelectorAll("[data-film-open]").forEach(b => b.addEventListener("click", () => {
  if (!box || !box.showModal) { location.href = b.dataset.src; return; }
  const v = document.createElement("video");
  v.src = b.dataset.src; v.controls = true; v.playsInline = true;
  if (b.dataset.poster) v.poster = b.dataset.poster;
  if (b.dataset.vtt) { const t = document.createElement("track"); t.kind = "captions"; t.srclang = "en"; t.label = "English"; t.src = b.dataset.vtt; v.appendChild(t); }
  box.querySelector(".slot").replaceChildren(v);
  box.showModal(); v.play().catch(() => {});
}));
if (box) {
  const shut = () => { const v = box.querySelector("video"); if (v) v.pause(); box.querySelector(".slot").replaceChildren(); };
  box.addEventListener("close", shut);
  box.querySelector(".x").addEventListener("click", () => box.close());
  box.addEventListener("click", e => { if (e.target === box) box.close(); });
}

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
    if (s.img) { const a = document.createElement("a"); a.href = s.img; a.target = "_blank"; a.rel = "noopener"; a.title = "Open full size"; const im = new Image(); im.src = s.img; im.alt = s.alt; a.appendChild(im); shot.appendChild(a); }
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

/* ── Beta request: posted to the 6thSTAR app, which keeps it and emails it to support (CC_MD_Website_Fixes_v1_0 §1).
      Plain text JSON, so the browser sends it straight away; no cookie. ── */
const form = document.querySelector("form.beta");
if (form) {
  const errBox = form.querySelector(".formerr"), btn = form.querySelector("button[type=submit]");
  const fail = msg => { errBox.textContent = msg; errBox.hidden = false; btn.disabled = false; btn.textContent = "Send request"; };
  form.addEventListener("submit", async e => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    errBox.hidden = true; btn.disabled = true; btn.textContent = "Sending…";
    const body = JSON.stringify(Object.fromEntries(new FormData(form)));
    try {
      const r = await fetch(SITE.BETA_ENDPOINT, { method: "POST", headers: { "Content-Type": "text/plain" }, body });
      const j = await r.json().catch(() => ({}));
      if (!r.ok || !j.ok) return fail(j.error || ("We couldn't send your request just now. Please write to " + SITE.SUPPORT + "."));
      form.hidden = true;
      document.querySelector(".thanks").classList.add("show");
    } catch (x) {
      fail("We couldn't send your request just now. Please write to " + SITE.SUPPORT + ".");
    }
  });
}

/* For screenshots: ?open=1 shows MARLOW's line already open */
if (new URLSearchParams(location.search).get("open") === "1") document.querySelectorAll(".shot[data-line]").forEach(s => s.classList.add("open"));

/* ── /setup (Tracy 2026-11-27): a step opens very large while pointed at; on a phone a tap opens it and any tap closes it ── */
const zoom = document.querySelector(".tzoom");
if (zoom) {
  const zi = zoom.querySelector("img"), zc = zoom.querySelector("figcaption");
  const open = t => { const im = t.querySelector("img"); zi.src = im.src; zi.alt = im.alt;
    /* as large as the screen allows, but never more than 1.6x the capture, so it stays clear */
    const k = Math.min(1.6, (innerWidth * 0.9 - 40) / im.naturalWidth, (innerHeight * 0.72) / im.naturalHeight);
    zi.style.width = Math.round(im.naturalWidth * k) + "px"; zc.innerHTML = t.querySelector(".tsay").innerHTML; zoom.classList.add("on"); };
  const shut = () => zoom.classList.remove("on");
  const hover = matchMedia("(hover:hover)").matches;
  document.querySelectorAll(".tile-step").forEach(t => {
    if (hover) { t.addEventListener("mouseenter", () => open(t)); t.addEventListener("mouseleave", shut); }
    else t.addEventListener("click", () => open(t));
    t.addEventListener("focus", () => { if (hover) open(t); });
    t.addEventListener("blur", shut);
  });
  zoom.addEventListener("click", shut);
  document.addEventListener("keydown", e => { if (e.key === "Escape") shut(); });
}

/* ── Home as frames (Tracy 2026-11-27): a card on the left shows its section in the right two thirds; the address follows ── */
const frames = document.querySelector(".frames");
if (frames && frames.querySelector(".fpanel>.sec")) {
  const cards = [...frames.querySelectorAll(".fcard")], secs = [...frames.querySelectorAll(".fpanel>.sec")];
  const wide = matchMedia("(min-width:900px)");
  const pick = id => {
    if (!secs.some(s => s.id === id)) id = "top";
    secs.forEach(s => s.classList.toggle("on", s.id === id));
    cards.forEach(c => c.classList.toggle("on", c.dataset.for === id));
  };
  const fromHash = () => pick((location.hash || "#top").slice(1));
  cards.forEach(c => c.addEventListener("click", e => {
    if (!wide.matches) return;
    e.preventDefault(); history.replaceState(null, "", "#" + c.dataset.for); pick(c.dataset.for); scrollTo(0, 0);
  }));
  addEventListener("hashchange", () => { fromHash(); if (wide.matches) scrollTo(0, 0); });
  /* a Next link at the foot of each section, so the story reads in order; the last one asks for a request */
  secs.forEach((sec, i) => {
    const a = document.createElement("a"); a.className = "fnext";
    if (i < cards.length - 1) {
      const nx = cards[i + 1]; a.href = "#" + nx.dataset.for;
      a.innerHTML = "<span>Next:</span> " + nx.querySelector(".fname").textContent + " →";
      a.addEventListener("click", e => { if (!wide.matches) return; e.preventDefault(); history.replaceState(null, "", a.hash); pick(nx.dataset.for); scrollTo(0, 0); });
    } else { a.href = "/beta/"; a.textContent = "Request more information →"; }
    (sec.querySelector(".in:last-child") || sec).appendChild(a);
  });
  fromHash();
  if (wide.matches && location.hash) scrollTo(0, 0);
}

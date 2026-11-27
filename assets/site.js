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
    /* Tracy 2026-11-27: a Restart button brings the film back to its cover screen */
    const cover = [...box.childNodes];
    const r = document.createElement("button");
    r.type = "button"; r.className = "restart"; r.textContent = "↺ Restart";
    r.addEventListener("click", e => {
      e.stopPropagation(); v.pause(); v.removeAttribute("src"); v.load();
      box.replaceChildren(...cover); delete box.dataset.started;
    });
    box.replaceChildren(v, r);
    v.play().catch(() => {});
  };
  box.addEventListener("click", start);
  box.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); start(); } });
});

/* ── The spot from the hero: plays in place of the hero picture, inside the right panel, so the left cards stay
   (Tracy 2026-11-27: "video should play on the right side so left nav is persistent"). Close brings the picture back. ── */
document.querySelectorAll("[data-film-open]").forEach(b => b.addEventListener("click", () => {
  const sec = b.closest("section"), shot = sec && sec.querySelector(".hero-shot");
  if (!shot) { location.href = b.dataset.src; return; }
  let wrap = sec.querySelector(".herofilm");
  if (wrap) wrap.remove();
  wrap = document.createElement("div"); wrap.className = "herofilm";
  const v = document.createElement("video");
  v.src = b.dataset.src; v.controls = true; v.playsInline = true;
  if (b.dataset.poster) v.poster = b.dataset.poster;
  if (b.dataset.vtt) { const t = document.createElement("track"); t.kind = "captions"; t.srclang = "en"; t.label = "English"; t.src = b.dataset.vtt; v.appendChild(t); }
  const x = document.createElement("button");
  x.type = "button"; x.className = "restart"; x.textContent = "✕ Close";
  x.addEventListener("click", () => { v.pause(); wrap.remove(); shot.hidden = false; b.focus(); });
  wrap.append(v, x);
  shot.hidden = true; shot.after(wrap);
  wrap.scrollIntoView({ block: matchMedia("(min-width:900px)").matches ? "start" : "nearest" });
  v.play().catch(() => {});
}));
/* a film stops when another card is chosen */
const pauseAll = () => document.querySelectorAll("video").forEach(v => v.pause());
document.querySelectorAll(".fcard,.fnext").forEach(a => a.addEventListener("click", pauseAll));
addEventListener("hashchange", pauseAll);

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
    if (!secs.some(s => s.id === id)) {               /* v3.13: an id inside a section (e.g. #about, now on Questions) opens that section */
      const el = document.getElementById(id), sec = el && el.closest(".fpanel>.sec");
      id = sec ? sec.id : "top";
    }
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
  /* v3.16: the Next link sits just above the footer, its right edge in line with the section's text */
  const placeNext = () => {
    const sec = frames.querySelector(".fpanel>.sec.on"); if (!sec || !wide.matches) return;
    const inn = sec.querySelector(".in:last-child") || sec, a = sec.querySelector(".fnext"); if (!a) return;
    let x = 0; for (let el = inn; el; el = el.offsetParent) x += el.offsetLeft;
    const cs = getComputedStyle(inn);
    a.style.left = (x + inn.offsetWidth - parseFloat(cs.paddingRight) - parseFloat(cs.borderRightWidth)) + "px";
  };
  placeNext();
  addEventListener("resize", placeNext); addEventListener("load", placeNext); addEventListener("hashchange", () => setTimeout(placeNext, 0));
  frames.querySelectorAll(".fcard,.fnext").forEach(c => c.addEventListener("click", () => setTimeout(placeNext, 0)));
}

/* ── Tracy 2026-11-27: "keep the phrase on one line". Each 6thSTAR line in a picture stays on one line, as large as fits
      (up to its normal size) within its picture: the hero line in the column under the stars, widening over the photo only if needed ── */
const fitLines = () => document.querySelectorAll(".shot .line-pop").forEach(el => {
  const frame = el.closest(".frame") || el.parentElement;
  if (!frame.offsetWidth) return;
  const hero = !!el.closest(".hero-shot");
  const wide = matchMedia("(min-width:701px)").matches;
  const room = frame.clientWidth * (el.dataset.room ? +el.dataset.room : (hero && wide ? 0.6 : 0.94));   /* v3.11: the hero line sits under the stars, clear of the shoe */
  let size = hero || el.dataset.room ? 16 : 14;
  el.style.setProperty("font-size", size + "px", "important");
  while (el.offsetWidth > room && size > 7) { size -= 0.5; el.style.setProperty("font-size", size + "px", "important"); }
});
addEventListener("load", fitLines); addEventListener("resize", fitLines);
document.querySelectorAll(".fcard,.fnext").forEach(a => a.addEventListener("click", () => setTimeout(fitLines, 0)));
addEventListener("hashchange", () => setTimeout(fitLines, 0));


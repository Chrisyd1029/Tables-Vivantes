#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur du site « Tables sauvages » — multi-pages, trilingue (FR/EN/DE).
Produit : index + pages thématiques en FR (racine), EN (/en/), DE (/de/).
Lancer :  python3 build.py
Le HTML généré est committé : le site reste autonome, sans build au déploiement.
"""
import os, html

SITE = "tables-sauvages.ch"
LANGS = ["fr", "en", "de"]

# Ordre + libellés de navigation (slug -> {lang: label})
NAV = [
    ("index",         {"fr": "Accueil",       "en": "Home",        "de": "Startseite"}),
    ("especes",       {"fr": "Espèces",        "en": "Species",     "de": "Arten"}),
    ("habitat",       {"fr": "Habitat",        "en": "Habitat",     "de": "Lebensraum"}),
    ("alimentation",  {"fr": "Alimentation",   "en": "Diet",        "de": "Ernährung"}),
    ("communication", {"fr": "Communication",  "en": "Communication","de": "Kommunikation"}),
    ("predateurs",    {"fr": "Prédateurs",     "en": "Predators",   "de": "Raubtiere"}),
    ("histoire",      {"fr": "Histoire",       "en": "History",     "de": "Geschichte"}),
    ("protection",    {"fr": "Protection",     "en": "Conservation","de": "Schutz"}),
    ("galerie",       {"fr": "Galerie",        "en": "Gallery",     "de": "Galerie"}),
    ("journal",       {"fr": "Journal",        "en": "Field Journal","de": "Tagebuch"}),
    ("recit",         {"fr": "Récit",          "en": "Account",     "de": "Bericht"}),
]

UI = {
    "fr": {"narr": "Écouter le narrateur", "cta": "Observer les 9 espèces",
           "foot1": "<strong>%s</strong> — Archives naturalistes des populations de tables vivantes." % SITE,
           "foot2": "Site de fiction documentaire. Aucun meuble domestique n’a été dérangé durant l’observation.",
           "speech_lang": "fr-FR"},
    "en": {"narr": "Play the narration", "cta": "Meet the 9 species",
           "foot1": "<strong>%s</strong> — Naturalist archives of the living-table populations." % SITE,
           "foot2": "A work of documentary fiction. No domestic furniture was disturbed during observation.",
           "speech_lang": "en-GB"},
    "de": {"narr": "Erzähler anhören", "cta": "Die 9 Arten entdecken",
           "foot1": "<strong>%s</strong> — Naturkundliches Archiv der lebenden Tischpopulationen." % SITE,
           "foot2": "Dokumentarische Fiktion. Bei der Beobachtung wurde kein Hausmöbel gestört.",
           "speech_lang": "de-DE"},
}

# ── Espèces (image partagée + textes par langue) ──────────────────────────────
SPECIES = [
 {"img": "bestiaire-1", "latin": "Tabula pinicola",
  "fr": {"name": "Table des pins noirs", "desc": "Territoriale, avance par bonds courts et protège ses jeunes tabourets sous son plateau.", "habitat": "Forêts de conifères, sols acides", "food": "Rosée résineuse, lichens, aiguilles tombées"},
  "en": {"name": "Black-pine table", "desc": "Territorial, moves in short hops and shelters its young stools beneath its top.", "habitat": "Conifer forests, acidic soils", "food": "Resin dew, lichen, fallen needles"},
  "de": {"name": "Schwarzkiefern-Tisch", "desc": "Territorial, bewegt sich in kurzen Sprüngen und schützt seine jungen Hocker unter der Platte.", "habitat": "Nadelwälder, saure Böden", "food": "Harztau, Flechten, gefallene Nadeln"}},
 {"img": "bestiaire-2", "latin": "Mensa nebulosa minor",
  "fr": {"name": "Table basse des brumes", "desc": "Se déplace à l’aube, presque invisible quand le brouillard descend sur la tourbière.", "habitat": "Tourbières, salons abandonnés, berges froides", "food": "Mousse humide, poussière de craie, vapeur d’eau"},
  "en": {"name": "Low table of the mists", "desc": "Moves at dawn, nearly invisible when fog settles over the bog.", "habitat": "Peat bogs, abandoned parlours, cold banks", "food": "Damp moss, chalk dust, water vapour"},
  "de": {"name": "Niedriger Nebeltisch", "desc": "Wandert im Morgengrauen, fast unsichtbar, wenn Nebel über das Moor sinkt.", "habitat": "Moore, verlassene Salons, kalte Ufer", "food": "Feuchtes Moos, Kreidestaub, Wasserdampf"}},
 {"img": "bestiaire-3", "latin": "Mensa migratoria grandis",
  "fr": {"name": "Grande table migratrice", "desc": "Voyage en lignes lentes de trente à cent individus, guidée par les étoiles basses.", "habitat": "Steppes, plaines céréalières, couloirs de vent", "food": "Grains perdus, sel, miettes calcaires"},
  "en": {"name": "Great migratory table", "desc": "Travels in slow lines of thirty to a hundred, guided by the low stars.", "habitat": "Steppes, grain plains, wind corridors", "food": "Lost grain, salt, calcareous crumbs"},
  "de": {"name": "Große Wandertisch", "desc": "Zieht in langsamen Reihen von dreißig bis hundert Tieren, geleitet von den tiefen Sternen.", "habitat": "Steppen, Getreideebenen, Windkorridore", "food": "Verlorenes Korn, Salz, kalkige Krümel"}},
 {"img": "bestiaire-4", "latin": "Tabula noctis vigilans",
  "fr": {"name": "Table de chevet nocturne", "desc": "Active la nuit ; couve ses œufs-chevilles dans son tiroir et craque doucement pour rassurer sa portée.", "habitat": "Grottes sèches, chambres désertées, falaises sombres", "food": "Papillons de nuit, pollen, fragments de rêves"},
  "en": {"name": "Night bedside table", "desc": "Active by night; broods its peg-eggs in its drawer and creaks softly to reassure its brood.", "habitat": "Dry caves, deserted rooms, dark cliffs", "food": "Moths, pollen, fragments of dreams"},
  "de": {"name": "Nächtlicher Nachttisch", "desc": "Nachtaktiv; brütet seine Zapfen-Eier in der Schublade und knarrt leise, um die Brut zu beruhigen.", "habitat": "Trockene Höhlen, verlassene Zimmer, dunkle Felsen", "food": "Nachtfalter, Pollen, Traumfetzen"}},
 {"img": "bestiaire-5", "latin": "Plica mensa rupestris",
  "fr": {"name": "Table pliante des falaises", "desc": "Déploie ou replie son plateau en un éclair, puis glisse le long des parois comme une feuille de schiste.", "habitat": "Parois abruptes, vires rocheuses", "food": "Minéraux tendres, embruns, œufs de mouches de pierre"},
  "en": {"name": "Folding cliff table", "desc": "Unfolds or closes its top in a flash, then slides down the rock like a flake of shale.", "habitat": "Sheer faces, rocky ledges", "food": "Soft minerals, spray, stone-fly eggs"},
  "de": {"name": "Klappbarer Felstisch", "desc": "Entfaltet oder schließt seine Platte blitzschnell und gleitet dann wie eine Schieferplatte die Wand hinab.", "habitat": "Steile Wände, Felsbänder", "food": "Weiche Minerale, Gischt, Steinfliegen-Eier"}},
 {"img": "bestiaire-6", "latin": "Orbimensa antiqua",
  "fr": {"name": "Table ronde cérémonielle", "desc": "Se rassemble en cercle, chaque individu orientant son plateau vers le centre ; la matriarche mène la harde.", "habitat": "Cercles mégalithiques, clairières anciennes", "food": "Cendres froides, baies écrasées, mémoire sonore"},
  "en": {"name": "Ceremonial round table", "desc": "Gathers in a circle, each one turning its top toward the centre; the matriarch leads the herd.", "habitat": "Megalithic circles, ancient clearings", "food": "Cold ashes, crushed berries, remembered sound"},
  "de": {"name": "Zeremonieller runder Tisch", "desc": "Versammelt sich im Kreis, jeder richtet seine Platte zur Mitte; die Matriarchin führt die Herde.", "habitat": "Megalithkreise, alte Lichtungen", "food": "Kalte Asche, zerdrückte Beeren, erinnerter Klang"}},
 {"img": "bestiaire-7", "latin": "Fabermensa robusta",
  "fr": {"name": "Table d’atelier cornue", "desc": "Puissante et solitaire, creuse des abris de ses coins renforcés ; convoitée par les bûcherons.", "habitat": "Hangars oubliés, carrières, forêts de bouleaux", "food": "Sciure, fer oxydé, champignons du bois"},
  "en": {"name": "Horned workshop table", "desc": "Powerful and solitary, digs shelters with its reinforced corners; coveted by woodcutters.", "habitat": "Forgotten sheds, quarries, birch woods", "food": "Sawdust, rusted iron, wood fungi"},
  "de": {"name": "Gehörnter Werkstatttisch", "desc": "Kräftig und einzelgängerisch, gräbt mit verstärkten Ecken Unterschlüpfe; von Holzfällern begehrt.", "habitat": "Vergessene Schuppen, Steinbrüche, Birkenwälder", "food": "Sägemehl, rostiges Eisen, Holzpilze"}},
 {"img": "bestiaire-8", "latin": "Cafemensa urbana feralis",
  "fr": {"name": "Table bistrot à pattes fines", "desc": "Très sociable ; communique par tintement du plateau et rotation des pieds, à la tombée du jour.", "habitat": "Ruines urbaines, terrasses désertes, gares anciennes", "food": "Sucre, pluie, miettes de pain, pièces de cuivre"},
  "en": {"name": "Slender-legged bistro table", "desc": "Highly social; speaks by chiming its top and rotating its feet at dusk.", "habitat": "Urban ruins, empty terraces, old stations", "food": "Sugar, rain, breadcrumbs, copper coins"},
  "de": {"name": "Bistrotisch mit schlanken Beinen", "desc": "Sehr gesellig; verständigt sich in der Dämmerung durch Klingen der Platte und Drehen der Füße.", "habitat": "Stadtruinen, leere Terrassen, alte Bahnhöfe", "food": "Zucker, Regen, Brotkrumen, Kupfermünzen"}},
 {"img": "bestiaire-9", "latin": "Tabula pendula silvestris",
  "fr": {"name": "Table-liane suspendue", "desc": "Vit accrochée aux branches ; ne descend au sol que pour pondre ses tabourets.", "habitat": "Canopées humides, grottes végétales", "food": "Sève, insectes, spores, poussière lunaire"},
  "en": {"name": "Hanging liana table", "desc": "Lives clinging to branches; descends to the ground only to lay its stools.", "habitat": "Humid canopies, leafy caves", "food": "Sap, insects, spores, moondust"},
  "de": {"name": "Hängender Lianentisch", "desc": "Lebt an Ästen hängend; steigt nur zum Ablegen seiner Hocker zu Boden.", "habitat": "Feuchte Kronendächer, grüne Höhlen", "food": "Saft, Insekten, Sporen, Mondstaub"}},
]

FACT_LABELS = {"fr": ("Habitat", "Alimentation"), "en": ("Habitat", "Diet"), "de": ("Lebensraum", "Ernährung")}

# ── Dictionnaire de sons (clé sonore partagée + textes par langue) ────────────
LEX = [
 {"sound": "danger",
  "fr": ("« Danger ! »", "Alarme · tambourinage", "Coups secs et rapides d’une patte sur le sol. Toute la harde se fige, puis se referme en réfectoire."),
  "en": ("“Danger!”", "Alarm · drumming", "Sharp, rapid taps of a leg on the ground. The whole herd freezes, then closes into a defensive ring."),
  "de": ("„Gefahr!“", "Alarm · Trommeln", "Scharfe, schnelle Schläge eines Beins auf den Boden. Die ganze Herde erstarrt und schließt sich zum Ring.")},
 {"sound": "eau",
  "fr": ("« De l’eau »", "Découverte · grincement montant", "Une longue plainte de bois qui s’élève, jointures qui chantent. Appelle la harde vers un point d’eau."),
  "en": ("“Water”", "Discovery · rising creak", "A long wooden moan that rises, joints singing. Calls the herd toward water."),
  "de": ("„Wasser“", "Entdeckung · steigendes Knarren", "Ein langes, ansteigendes Holzstöhnen, singende Fugen. Ruft die Herde zum Wasser.")},
 {"sound": "contact",
  "fr": ("« Je suis là »", "Contact · grincement grave", "Un craquement bref et profond, répété dans la nuit pour garder le lien sans révéler sa position."),
  "en": ("“I’m here”", "Contact · low creak", "A short, deep crack, repeated through the night to keep contact without giving away its position."),
  "de": ("„Ich bin hier“", "Kontakt · tiefes Knarren", "Ein kurzes, tiefes Knacken, nachts wiederholt, um Kontakt zu halten, ohne sich zu verraten.")},
 {"sound": "rassemblement",
  "fr": ("« Au rassemblement »", "Appel matriarcal · vibration", "Onde basse fréquence émise par tout le bois de la Grande Desserte. On ne l’entend pas : on la sent."),
  "en": ("“Gathering”", "Matriarch call · vibration", "A low-frequency wave from the whole body of the matriarch. You don’t hear it: you feel it."),
  "de": ("„Sammeln“", "Matriarchenruf · Vibration", "Eine niederfrequente Welle aus dem ganzen Holz der Matriarchin. Man hört sie nicht: man spürt sie.")},
 {"sound": "parade",
  "fr": ("« Parade »", "Nuptial · tambourinage rythmé", "Une cadence régulière, accompagnée du lent déploiement de la rallonge. L’invitation à l’emboîtement."),
  "en": ("“Display”", "Courtship · rhythmic drumming", "A steady cadence, with the slow unfolding of the leaf. The invitation to nest together."),
  "de": ("„Balz“", "Werbung · rhythmisches Trommeln", "Ein gleichmäßiger Takt, begleitet vom langsamen Ausfahren der Verlängerung. Die Einladung zum Ineinanderschieben.")},
 {"sound": "detresse",
  "fr": ("« Détresse »", "Tabouret perdu · grincement aigu", "Une plainte haute et tremblante qui porte loin. Le cri du petit séparé de la harde — déchirant."),
  "en": ("“Distress”", "Lost stool · high creak", "A high, trembling wail that carries far. The cry of a young one parted from the herd — heart-rending."),
  "de": ("„Notruf“", "Verlorener Hocker · hohes Knarren", "Ein hohes, zitterndes Wehklagen, das weit trägt. Der Schrei des von der Herde getrennten Jungen — herzzerreißend.")},
]

# ════════════════════════════════════════════════════════════════════════════
#  CONTENU DES PAGES  —  content.py est importé pour garder ce fichier lisible
# ════════════════════════════════════════════════════════════════════════════
from content import PAGES, META

# ── Rendu des blocs ───────────────────────────────────────────────────────────
def esc(s): return s  # le contenu est déjà du HTML léger contrôlé

def render_blocks(blocks, lang, ap):
    out = []
    for b in blocks:
        t = b["type"]
        if t == "hero":
            cta = f'<a class="stone-btn" href="especes.html">{UI[lang]["cta"]}</a>' if b.get("cta") else ""
            out.append(f'''<section class="hero"><div class="hero-inner reveal"><div>
  <div class="kicker">{b["kicker"]}</div>
  <h1>{b["h1"]}</h1>
  <p class="lead">{b["lead"]}</p>
  <button class="narrator-btn" data-narrator>{UI[lang]["narr"]}</button>{cta}
</div>
<img class="hero-img" src="{ap}assets/img/web/{b["img"]}.webp" alt="{b["alt"]}" loading="eager" width="1500" height="950"/>
</div></section>''')
        elif t == "page_title":
            out.append(f'''<section class="page-title reveal"><div class="kicker">{b["kicker"]}</div>
<h1>{b["h1"]}</h1><p class="lead">{b["lead"]}</p>
<button class="narrator-btn" data-narrator>{UI[lang]["narr"]}</button></section>''')
        elif t == "section":
            h2 = f'<h2>{b["h2"]}</h2>' if b.get("h2") else ""
            paras = "".join(f"<p>{p}</p>" for p in b.get("paras", []))
            quote = f'<blockquote class="quote">{b["quote"]}</blockquote>' if b.get("quote") else ""
            out.append(f'<section class="section reveal">{h2}{paras}{quote}</section>')
        elif t == "cards":
            cards = "".join(
                f'<article class="card reveal"><div class="meta">{c["meta"]}</div><h3>{c["h3"]}</h3><p>{c["p"]}</p></article>'
                for c in b["items"])
            head = f'<h2>{b["h2"]}</h2>' if b.get("h2") else ""
            out.append(f'<section class="section">{head}<div class="grid">{cards}</div></section>')
        elif t == "species":
            lh, lf = FACT_LABELS[lang]
            cards = []
            for s in SPECIES:
                d = s[lang]
                cards.append(f'''<article class="species-card reveal">
<img src="{ap}assets/img/web/{s["img"]}.webp" alt="{d["name"]}" loading="lazy" width="1000" height="1250"/>
<div class="body"><h3>{d["name"]}</h3><em class="latin">{s["latin"]}</em>
<p>{d["desc"]}</p>
<div class="facts"><span><b>{lh} :</b> {d["habitat"]}</span><span><b>{lf} :</b> {d["food"]}</span></div>
</div></article>''')
            out.append(f'<section class="section"><div class="species">{"".join(cards)}</div></section>')
        elif t == "gallery_species":
            figs = [f'<figure class="wide reveal"><img src="{ap}assets/img/web/composite-troupeau.webp" alt="{b["cap"]}" loading="lazy"/><figcaption>{b["cap"]}</figcaption></figure>']
            for s in SPECIES:
                d = s[lang]
                figs.append(f'<figure class="reveal"><img src="{ap}assets/img/web/{s["img"]}.webp" alt="{d["name"]}" loading="lazy"/><figcaption>{d["name"]} — <em>{s["latin"]}</em></figcaption></figure>')
            out.append(f'<section class="section"><div class="gallery">{"".join(figs)}</div></section>')
        elif t == "gallery":
            figs = []
            for g in b["items"]:
                cls = " class=\"wide\"" if g.get("wide") else ""
                figs.append(f'<figure{cls} class="reveal"><img src="{ap}assets/img/web/{g["img"]}.webp" alt="{g["cap"]}" loading="lazy"/><figcaption>{g["cap"]}</figcaption></figure>')
            out.append(f'<section class="section"><div class="gallery">{"".join(figs)}</div></section>')
        elif t == "rules":
            items = "".join(f"<li>{i}</li>" for i in b["items"])
            out.append(f'<section class="section reveal"><h2>{b["h2"]}</h2><ul class="rules">{items}</ul></section>')
        elif t == "journal":
            entries = "".join(
                f'<div class="journal-entry reveal"><div class="date">{e["date"]}</div><h3>{e["title"]}</h3><p>{e["text"]}</p></div>'
                for e in b["items"])
            out.append(f'<section class="section">{entries}</section>')
        elif t == "story":
            paras = "".join(f"<p>{p}</p>" for p in b["paras"])
            note = f'<div class="observatory-note">{b["note"]}</div>' if b.get("note") else ""
            out.append(f'<section class="section reveal"><div class="story">{paras}{note}</div></section>')
        elif t == "lexicon":
            words = []
            for w in LEX:
                txt = w[lang]
                words.append(f'''<figure class="word reveal"><button class="play" data-sound="{w["sound"]}" aria-label="{txt[0]}"><svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
<div class="body"><h4>{txt[0]}</h4><span class="gloss">{txt[1]}</span><p>{txt[2]}</p></div></figure>''')
            out.append(f'<section class="section reveal"><h2>{b["h2"]}</h2><p>{b["intro"]}</p><div class="lexicon">{"".join(words)}</div></section>')
    return "\n".join(out)

# ── Liens (nav même langue + sélecteur de langue) ─────────────────────────────
def nav_html(slug, lang):
    items = []
    for s, labels in NAV:
        active = ' class="active"' if s == slug else ""
        items.append(f'<a{active} href="{s}.html">{labels[lang]}</a>')
    # sélecteur de langue : même page, autre langue
    langlinks = []
    for L in LANGS:
        if L == lang:
            href = f"{slug}.html"
        elif L == "fr":
            href = ("../" if lang != "fr" else "") + f"{slug}.html"
        else:  # en ou de
            if lang == "fr":
                href = f"{L}/{slug}.html"
            else:
                href = f"../{L}/{slug}.html"
        cur = ' aria-current="true"' if L == lang else ""
        langlinks.append(f'<a{cur} href="{href}" hreflang="{L}">{L.upper()}</a>')
    return "".join(items), "".join(langlinks)

def page(slug, lang):
    ap = "" if lang == "fr" else "../"          # asset prefix
    blocks = PAGES[slug][lang]
    nav_items, lang_items = nav_html(slug, lang)
    body = render_blocks(blocks, lang, ap)
    title = META[slug][lang]["title"]
    desc = META[slug][lang]["desc"]
    sounds = f'<script src="{ap}assets/js/sounds.js"></script>' if slug == "communication" else ""
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.classList.add('js')</script>
<title>{title} · {SITE}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{ap}assets/css/style.css">
</head>
<body>
<header class="header"><nav class="navbar" aria-label="Navigation">
<a class="logo" href="index.html"><span class="logo-mark"></span> {SITE}</a>
<div class="menu">{nav_items}<span class="lang">{lang_items}</span></div>
</nav></header>
<main>
{body}
</main>
<footer class="footer"><p>{UI[lang]["foot1"]}</p><p class="notice">{UI[lang]["foot2"]}</p></footer>
<script src="{ap}assets/js/site.js"></script>{sounds}
</body></html>
'''

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(root, "en"), exist_ok=True)
    os.makedirs(os.path.join(root, "de"), exist_ok=True)
    n = 0
    for slug, _ in NAV:
        for lang in LANGS:
            sub = "" if lang == "fr" else lang
            path = os.path.join(root, sub, f"{slug}.html")
            with open(path, "w", encoding="utf-8") as f:
                f.write(page(slug, lang))
            n += 1
    print(f"{n} pages générées ({len(NAV)} pages × {len(LANGS)} langues).")

if __name__ == "__main__":
    main()

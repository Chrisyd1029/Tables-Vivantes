# -*- coding: utf-8 -*-
"""Contenu trilingue (FR/EN/DE) du site Tables sauvages. Importé par build.py."""

META = {
 "index": {"fr": {"title": "Accueil", "desc": "Documentaire de science-fiction naturaliste sur les tables vivantes et sauvages."},
           "en": {"title": "Home", "desc": "A naturalist science-fiction documentary on living, wild tables."},
           "de": {"title": "Startseite", "desc": "Eine naturkundliche Science-Fiction-Dokumentation über lebende, wilde Tische."}},
 "especes": {"fr": {"title": "Espèces", "desc": "Les neuf espèces de tables sauvages observées."},
             "en": {"title": "Species", "desc": "The nine observed species of wild tables."},
             "de": {"title": "Arten", "desc": "Die neun beobachteten Arten wilder Tische."}},
 "habitat": {"fr": {"title": "Habitat", "desc": "Où vivent les tables sauvages."},
             "en": {"title": "Habitat", "desc": "Where wild tables live."},
             "de": {"title": "Lebensraum", "desc": "Wo wilde Tische leben."}},
 "alimentation": {"fr": {"title": "Alimentation", "desc": "Le régime xylophage des tables sauvages."},
                  "en": {"title": "Diet", "desc": "The wood-eating diet of wild tables."},
                  "de": {"title": "Ernährung", "desc": "Die holzfressende Ernährung wilder Tische."}},
 "communication": {"fr": {"title": "Communication", "desc": "Grincements, tambourinage et dictionnaire de sons."},
                   "en": {"title": "Communication", "desc": "Creaks, drumming and a dictionary of sounds."},
                   "de": {"title": "Kommunikation", "desc": "Knarren, Trommeln und ein Wörterbuch der Laute."}},
 "predateurs": {"fr": {"title": "Prédateurs", "desc": "Termites, bûcherons et humidité : les menaces."},
                "en": {"title": "Predators", "desc": "Termites, woodcutters and damp: the threats."},
                "de": {"title": "Raubtiere", "desc": "Termiten, Holzfäller und Feuchtigkeit: die Gefahren."}},
 "histoire": {"fr": {"title": "Histoire", "desc": "Des origines à la domestication des tables vivantes."},
              "en": {"title": "History", "desc": "From the origins to the domestication of living tables."},
              "de": {"title": "Geschichte", "desc": "Von den Ursprüngen bis zur Domestizierung lebender Tische."}},
 "protection": {"fr": {"title": "Protection", "desc": "Cohabiter avec les tables sauvages sans les capturer."},
                "en": {"title": "Conservation", "desc": "Coexisting with wild tables without capturing them."},
                "de": {"title": "Schutz", "desc": "Mit wilden Tischen leben, ohne sie zu fangen."}},
 "galerie": {"fr": {"title": "Galerie", "desc": "Planches naturalistes des tables sauvages."},
             "en": {"title": "Gallery", "desc": "Naturalist plates of the wild tables."},
             "de": {"title": "Galerie", "desc": "Naturkundliche Tafeln der wilden Tische."}},
 "journal": {"fr": {"title": "Journal", "desc": "Carnet de terrain d’une mission de repérage."},
             "en": {"title": "Field Journal", "desc": "Field notebook from a survey expedition."},
             "de": {"title": "Tagebuch", "desc": "Feldtagebuch einer Erkundungsmission."}},
 "recit": {"fr": {"title": "Récit", "desc": "La personne sauvée par une table sauvage."},
           "en": {"title": "Account", "desc": "The person saved by a wild table."},
           "de": {"title": "Bericht", "desc": "Die von einem wilden Tisch gerettete Person."}},
}

PAGES = {}

# ════════════════════════ ACCUEIL ════════════════════════
PAGES["index"] = {
 "fr": [
  {"type":"hero","kicker":"Documentaire naturaliste de terrain","h1":"Les tables sauvages",
   "lead":"Aux marges des vallées, dans les cavernes tièdes et sous les forêts de pins noirs, vivent des êtres que l’on croyait immobiles. Elles broutent, migrent, se camouflent et veillent sur leurs petits tabourets.",
   "cta":True,"img":"composite-troupeau","alt":"Une harde de tables sauvages dans une plaine brumeuse"},
  {"type":"cards","items":[
   {"meta":"Comportement","h3":"Des meubles à sang tiède","p":"La table sauvage n’est pas un objet animé par caprice : c’est un organisme social, prudent, capable d’apprentissage, dont les pattes répondent aux vibrations du sol."},
   {"meta":"Méthode","h3":"Observation à distance","p":"Les naturalistes n’approchent jamais une colonie au lever du soleil. À cette heure, les tables déplient leurs angles et confondent un trépied photographique avec un rival."},
   {"meta":"Mythe","h3":"La première planche","p":"Les anciens récits affirment qu’une planche tomba du ciel lors d’un orage magnétique. Là où elle toucha terre, la première table ouvrit les yeux."},
  ]},
  {"type":"section","h2":"Une nature à hauteur de plateau","paras":[
   "Ce site rassemble les notes d’expédition, les fiches d’espèces et les hypothèses historiques concernant les populations de tables vivantes. Le ton demeure volontairement sobre : leur silhouette prête à sourire, mais leur monde obéit à des règles d’une précision étonnante.",
   "On les trouve dans les gorges calcaires, sur les plateaux secs, au bord des rivières ferrugineuses et parfois dans les ruines de salles à manger abandonnées."],
   "quote":"« Quand une table sauvage s’arrête, ce n’est pas qu’elle renonce à vivre. C’est qu’elle écoute le sol. » — Carnet de terrain, vallée des Nappes"},
 ],
 "en": [
  {"type":"hero","kicker":"A naturalist field documentary","h1":"The wild tables",
   "lead":"At the edges of the valleys, in warm caverns and beneath the black-pine forests, live beings once thought motionless. They graze, migrate, camouflage themselves and watch over their little stools.",
   "cta":True,"img":"composite-troupeau","alt":"A herd of wild tables on a misty plain"},
  {"type":"cards","items":[
   {"meta":"Behaviour","h3":"Warm-blooded furniture","p":"The wild table is not an object moved by whim: it is a social, cautious organism, capable of learning, whose legs respond to vibrations in the ground."},
   {"meta":"Method","h3":"Observation from afar","p":"Naturalists never approach a colony at sunrise. At that hour the tables unfold their corners and mistake a camera tripod for a rival."},
   {"meta":"Myth","h3":"The first plank","p":"Old tales claim a plank fell from the sky during a magnetic storm. Where it touched the earth, the first table opened its eyes."},
  ]},
  {"type":"section","h2":"A nature at tabletop height","paras":[
   "This site gathers expedition notes, species sheets and historical hypotheses about the living-table populations. The tone is deliberately sober: their silhouette may raise a smile, but their world obeys rules of startling precision.",
   "They are found in limestone gorges, on dry plateaus, along iron-rich rivers, and sometimes in the ruins of abandoned dining rooms."],
   "quote":"“When a wild table stops, it is not giving up on life. It is listening to the ground.” — Field notebook, Valley of the Cloths"},
 ],
 "de": [
  {"type":"hero","kicker":"Eine naturkundliche Feld-Dokumentation","h1":"Die wilden Tische",
   "lead":"An den Rändern der Täler, in warmen Höhlen und unter den Schwarzkiefernwäldern leben Wesen, die man für unbeweglich hielt. Sie grasen, wandern, tarnen sich und wachen über ihre kleinen Hocker.",
   "cta":True,"img":"composite-troupeau","alt":"Eine Herde wilder Tische in einer nebligen Ebene"},
  {"type":"cards","items":[
   {"meta":"Verhalten","h3":"Warmblütige Möbel","p":"Der wilde Tisch ist kein launisch bewegtes Objekt: Er ist ein soziales, vorsichtiges, lernfähiges Wesen, dessen Beine auf Erschütterungen des Bodens reagieren."},
   {"meta":"Methode","h3":"Beobachtung aus der Ferne","p":"Naturforscher nähern sich einer Kolonie nie bei Sonnenaufgang. Dann entfalten die Tische ihre Ecken und verwechseln ein Kamerastativ mit einem Rivalen."},
   {"meta":"Mythos","h3":"Die erste Planke","p":"Alte Erzählungen behaupten, eine Planke sei bei einem Magnetsturm vom Himmel gefallen. Wo sie den Boden berührte, öffnete der erste Tisch die Augen."},
  ]},
  {"type":"section","h2":"Eine Natur auf Tischhöhe","paras":[
   "Diese Seite versammelt Expeditionsnotizen, Artensteckbriefe und historische Hypothesen über die Populationen lebender Tische. Der Ton bleibt bewusst nüchtern: Ihre Silhouette mag ein Lächeln wecken, doch ihre Welt folgt erstaunlich präzisen Regeln.",
   "Man findet sie in Kalkschluchten, auf trockenen Hochebenen, an eisenhaltigen Flüssen und manchmal in den Ruinen verlassener Esszimmer."],
   "quote":"„Wenn ein wilder Tisch innehält, gibt er das Leben nicht auf. Er hört dem Boden zu.“ — Feldtagebuch, Tal der Tücher"},
 ],
}

# ════════════════════════ ESPÈCES ════════════════════════
PAGES["especes"] = {
 "fr": [
  {"type":"page_title","kicker":"Classification vivante","h1":"Les 9 espèces",
   "lead":"La famille des Tabulidés regroupe des organismes à plateau porteur, à pattes locomotrices et au comportement social variable."},
  {"type":"section","paras":["Leur classification reste débattue : certains naturalistes y voient des descendants du bois, d’autres les ultimes témoins d’une biologie minérale. Les neuf espèces ci-dessous ont été relevées sur le terrain et figurées d’après photographie."]},
  {"type":"species"},
  {"type":"section","h2":"Classification proposée","paras":[
   "Règne : <em>Mobilia silenciosa</em> · Embranchement : <em>Quadrupedia planata</em> · Classe : <em>Tabuliformes</em> · Ordre : <em>Mensales</em> · Famille : <em>Tabulidae</em>.",
   "Cette classification n’est pas définitive. Les traces dans la poussière indiquent que certaines espèces possèdent quatre pattes, d’autres trois, six, voire un nombre variable lors des mues saisonnières. On reconnaît pourtant toutes les tables sauvages à leur réflexe de stabilisation : face au danger, elles cherchent l’horizontalité parfaite."]},
 ],
 "en": [
  {"type":"page_title","kicker":"A living classification","h1":"The 9 species",
   "lead":"The Tabulidae family gathers organisms with a load-bearing top, locomotor legs and varied social behaviour."},
  {"type":"section","paras":["Their classification is still debated: some naturalists see them as descendants of wood, others as the last witnesses of a mineral biology. The nine species below were recorded in the field and figured from photographs."]},
  {"type":"species"},
  {"type":"section","h2":"Proposed classification","paras":[
   "Kingdom: <em>Mobilia silenciosa</em> · Phylum: <em>Quadrupedia planata</em> · Class: <em>Tabuliformes</em> · Order: <em>Mensales</em> · Family: <em>Tabulidae</em>.",
   "This classification is not final. Tracks in the dust show that some species have four legs, others three, six, or a number that varies with the seasonal moults. Yet every wild table is known by its stabilising reflex: faced with danger, it seeks perfect horizontality."]},
 ],
 "de": [
  {"type":"page_title","kicker":"Eine lebende Systematik","h1":"Die 9 Arten",
   "lead":"Die Familie der Tabulidae umfasst Organismen mit tragender Platte, Fortbewegungsbeinen und unterschiedlichem Sozialverhalten."},
  {"type":"section","paras":["Ihre Einordnung ist umstritten: Manche Naturforscher sehen in ihnen Nachfahren des Holzes, andere die letzten Zeugen einer mineralischen Biologie. Die neun Arten unten wurden im Feld erfasst und nach Fotografien dargestellt."]},
  {"type":"species"},
  {"type":"section","h2":"Vorgeschlagene Systematik","paras":[
   "Reich: <em>Mobilia silenciosa</em> · Stamm: <em>Quadrupedia planata</em> · Klasse: <em>Tabuliformes</em> · Ordnung: <em>Mensales</em> · Familie: <em>Tabulidae</em>.",
   "Diese Systematik ist nicht endgültig. Spuren im Staub zeigen, dass manche Arten vier Beine haben, andere drei, sechs oder eine bei den Häutungen wechselnde Zahl. Dennoch erkennt man jeden wilden Tisch an seinem Stabilisierungsreflex: bei Gefahr sucht er die vollkommene Waagerechte."]},
 ],
}

# ════════════════════════ HABITAT ════════════════════════
PAGES["habitat"] = {
 "fr": [
  {"type":"page_title","kicker":"Territoire","h1":"Habitat",
   "lead":"La table sauvage privilégie les grandes étendues planes, assez fermes pour porter le poids de son plateau."},
  {"type":"section","h2":"Des plaines à perte de vue","paras":[
   "On la rencontre sur les steppes, les plateaux calcaires et les anciens parquets fossilisés. Elle a besoin d’espace pour déployer ses rallonges et d’un sol stable pour ne pas s’enfoncer.",
   "Le troupeau se regroupe autour d’un point d’eau — ou, dans les régions arides, autour d’un dessous-de-verre abandonné dont il absorbe l’humidité par capillarité."]},
  {"type":"section","h2":"Le réfectoire nocturne","paras":[
   "La nuit, les tables se rangent : flanc contre flanc, plateaux alignés, formant de longues rangées défensives que les naturalistes nomment réfectoires. Au lever du jour, elles se dispersent à nouveau dans la brume."],
   "quote":"« Ce que l’on prend pour un meuble immobile n’est qu’une bête qui a appris à attendre. »"},
 ],
 "en": [
  {"type":"page_title","kicker":"Territory","h1":"Habitat",
   "lead":"The wild table favours wide, flat expanses, firm enough to carry the weight of its top."},
  {"type":"section","h2":"Plains as far as the eye can see","paras":[
   "It is found on steppes, limestone plateaus and ancient fossilised parquet. It needs room to unfold its leaves and stable ground so as not to sink.",
   "The herd gathers around a waterhole — or, in arid regions, around an abandoned coaster from which it draws moisture by capillary action."]},
  {"type":"section","h2":"The nightly refectory","paras":[
   "At night the tables line up: flank to flank, tops aligned, forming long defensive rows that naturalists call refectories. At daybreak they scatter again into the mist."],
   "quote":"“What we take for a motionless piece of furniture is only a beast that has learned to wait.”"},
 ],
 "de": [
  {"type":"page_title","kicker":"Territorium","h1":"Lebensraum",
   "lead":"Der wilde Tisch bevorzugt weite, flache Flächen, fest genug, um das Gewicht seiner Platte zu tragen."},
  {"type":"section","h2":"Ebenen bis zum Horizont","paras":[
   "Man trifft ihn auf Steppen, Kalkhochebenen und altem versteinertem Parkett. Er braucht Raum, um seine Verlängerungen auszufahren, und festen Boden, um nicht einzusinken.",
   "Die Herde sammelt sich an einer Wasserstelle — oder, in trockenen Gegenden, um einen verlassenen Untersetzer, dem sie durch Kapillarwirkung Feuchtigkeit entzieht."]},
  {"type":"section","h2":"Das nächtliche Refektorium","paras":[
   "Nachts reihen sich die Tische auf: Flanke an Flanke, Platten ausgerichtet, in langen Verteidigungsreihen, die Naturforscher Refektorien nennen. Bei Tagesanbruch zerstreuen sie sich wieder im Nebel."],
   "quote":"„Was wir für ein unbewegliches Möbel halten, ist nur ein Tier, das gelernt hat zu warten.“"},
 ],
}

# ════════════════════════ ALIMENTATION ════════════════════════
PAGES["alimentation"] = {
 "fr": [
  {"type":"page_title","kicker":"Régime","h1":"Alimentation",
   "lead":"Contrairement à une croyance tenace, la table sauvage ne se nourrit pas de ce qu’on pose sur elle."},
  {"type":"section","h2":"Une xylophage discrète","paras":[
   "Elle broute le bois mort, les copeaux et l’écorce tendre, qu’elle digère lentement pour entretenir son plateau. Sa langue — un long ruban de feutrine rugueuse logé sous le tiroir — racle les surfaces et capte la poussière de bois.",
   "Les espèces vernies, plus rares, complètent ce régime de résines sucrées récoltées sur les pins fossiles."]},
  {"type":"section","h2":"L’or des plaines","paras":[
   "La digestion produit une fine sciure que la table régurgite la nuit : un terreau précieux qui fertilise la plaine et nourrit, en retour, les forêts dont elle se repaîtra. Tout se tient."]},
 ],
 "en": [
  {"type":"page_title","kicker":"Diet","h1":"Feeding",
   "lead":"Contrary to a stubborn belief, the wild table does not feed on what is placed upon it."},
  {"type":"section","h2":"A discreet wood-eater","paras":[
   "It grazes on dead wood, shavings and soft bark, which it digests slowly to maintain its top. Its tongue — a long ribbon of rough felt tucked beneath the drawer — rasps surfaces and gathers wood dust.",
   "The rarer varnished species supplement this diet with sweet resins harvested from fossil pines."]},
  {"type":"section","h2":"The gold of the plains","paras":[
   "Digestion produces a fine sawdust that the table brings up at night: a precious compost that fertilises the plain and, in turn, feeds the forests it will graze. Everything holds together."]},
 ],
 "de": [
  {"type":"page_title","kicker":"Nahrung","h1":"Ernährung",
   "lead":"Entgegen einer hartnäckigen Annahme ernährt sich der wilde Tisch nicht von dem, was man auf ihn stellt."},
  {"type":"section","h2":"Ein unauffälliger Holzfresser","paras":[
   "Er grast totes Holz, Späne und weiche Rinde ab, die er langsam verdaut, um seine Platte zu pflegen. Seine Zunge — ein langes, raues Filzband unter der Schublade — schabt Flächen ab und sammelt Holzstaub.",
   "Die selteneren lackierten Arten ergänzen diese Kost mit süßen Harzen, die sie an versteinerten Kiefern ernten."]},
  {"type":"section","h2":"Das Gold der Ebenen","paras":[
   "Die Verdauung erzeugt feines Sägemehl, das der Tisch nachts hervorbringt: ein wertvoller Humus, der die Ebene düngt und wiederum die Wälder nährt, die er abweiden wird. Alles hängt zusammen."]},
 ],
}

# ════════════════════════ COMMUNICATION ════════════════════════
PAGES["communication"] = {
 "fr": [
  {"type":"page_title","kicker":"Langage","h1":"Communication",
   "lead":"La table n’a ni bouche, ni cordes, ni cri. Pour se parler, elle se sert de son bois, de ses pattes et du sol lui-même."},
  {"type":"section","paras":[
   "Son langage premier est le <em>grincement</em> : en faisant jouer ses jointures, elle module de longues plaintes de bois. Chaque harde a son « accent », hérité de l’essence dont elle est faite.",
   "Vient ensuite le <em>tambourinage</em> — un coup sec de la patte sur le sol — puis le <em>langage du corps</em> : un plateau incliné est une invitation, dressé une menace. La matriarche, elle, émet par tout son bois des vibrations si graves que la harde les ressent par les pattes, à des kilomètres."]},
  {"type":"lexicon","h2":"Dictionnaire de sons","intro":"Six « mots » parmi les plus courants, synthétisés à partir de bois. Approchez l’oreille — et montez le son."},
 ],
 "en": [
  {"type":"page_title","kicker":"Language","h1":"Communication",
   "lead":"The table has no mouth, no cords, no cry. To speak, it uses its wood, its legs and the ground itself."},
  {"type":"section","paras":[
   "Its first language is the <em>creak</em>: by working its joints, it shapes long wooden laments. Each herd has its own “accent”, inherited from the wood it is made of.",
   "Then comes <em>drumming</em> — a sharp tap of a leg on the ground — and <em>body language</em>: a tilted top is an invitation, a raised one a threat. The matriarch emits, through her whole body, vibrations so low that the herd feels them through their legs, miles away."]},
  {"type":"lexicon","h2":"A dictionary of sounds","intro":"Six of the most common “words”, synthesised from wood. Lean in — and turn up the volume."},
 ],
 "de": [
  {"type":"page_title","kicker":"Sprache","h1":"Kommunikation",
   "lead":"Der Tisch hat weder Mund noch Saiten noch Schrei. Zum Sprechen nutzt er sein Holz, seine Beine und den Boden selbst."},
  {"type":"section","paras":[
   "Seine erste Sprache ist das <em>Knarren</em>: durch Bewegen seiner Fugen formt er lange hölzerne Klagen. Jede Herde hat ihren eigenen „Akzent“, ererbt von dem Holz, aus dem sie besteht.",
   "Dann folgt das <em>Trommeln</em> — ein scharfer Schlag des Beins auf den Boden — und die <em>Körpersprache</em>: eine geneigte Platte ist eine Einladung, eine aufgerichtete eine Drohung. Die Matriarchin sendet durch ihr ganzes Holz Schwingungen aus, so tief, dass die Herde sie kilometerweit durch die Beine spürt."]},
  {"type":"lexicon","h2":"Wörterbuch der Laute","intro":"Sechs der häufigsten „Wörter“, aus Holz synthetisiert. Komm näher — und dreh den Ton auf."},
 ],
}

# ════════════════════════ PRÉDATEURS ════════════════════════
PAGES["predateurs"] = {
 "fr": [
  {"type":"page_title","kicker":"Menaces","h1":"Prédateurs",
   "lead":"Massive mais lente, la table sauvage a peu d’ennemis — mais ceux-là sont patients."},
  {"type":"section","h2":"Trois dangers","paras":[
   "La <em>termite des steppes</em> s’attaque aux pattes par en dessous et peut faire s’effondrer un adulte en une seule nuit de festin silencieux. Le <em>bûcheron</em>, prédateur bipède, traque les plus vieilles, dont le bois patiné vaut tous les trésors.",
   "Mais la pire menace ne chasse pas : c’est l’<em>humidité</em>. Une saison trop pluvieuse, et les plateaux gondolent, les jointures cèdent. Contre elle, aucune fuite possible."]},
  {"type":"section","h2":"Le réfectoire serré","paras":[
   "Pour se défendre, la harde se rassemble en cercle, plateaux tournés vers l’extérieur, les tabourets protégés au centre, et lance dans la nuit un tonnerre de grincements qui décourage les rôdeurs."],
   "quote":"« On ne chasse pas une table. On attend qu’elle baisse sa garde — et les vieilles ne la baissent jamais. »"},
 ],
 "en": [
  {"type":"page_title","kicker":"Threats","h1":"Predators",
   "lead":"Massive but slow, the wild table has few enemies — but those few are patient."},
  {"type":"section","h2":"Three dangers","paras":[
   "The <em>steppe termite</em> attacks the legs from below and can bring down an adult in a single night of silent feasting. The <em>woodcutter</em>, a bipedal predator, hunts the oldest, whose weathered wood is worth any treasure.",
   "But the worst threat does not hunt: it is <em>damp</em>. One rainy season too many, and the tops warp, the joints give way. Against it, no flight is possible."]},
  {"type":"section","h2":"The tight refectory","paras":[
   "To defend itself, the herd gathers in a circle, tops turned outward, the stools sheltered at the centre, and unleashes into the night a thunder of creaks that discourages prowlers."],
   "quote":"“You do not hunt a table. You wait for it to drop its guard — and the old ones never do.”"},
 ],
 "de": [
  {"type":"page_title","kicker":"Gefahren","h1":"Raubtiere",
   "lead":"Massig, aber langsam, hat der wilde Tisch wenige Feinde — doch diese sind geduldig."},
  {"type":"section","h2":"Drei Gefahren","paras":[
   "Die <em>Steppentermite</em> greift die Beine von unten an und kann einen Erwachsenen in einer einzigen Nacht stillen Schmauses zu Fall bringen. Der <em>Holzfäller</em>, ein zweibeiniges Raubtier, jagt die Ältesten, deren patiniertes Holz jeden Schatz aufwiegt.",
   "Doch die schlimmste Gefahr jagt nicht: es ist die <em>Feuchtigkeit</em>. Eine zu regnerische Saison, und die Platten werfen sich, die Fugen geben nach. Gegen sie gibt es keine Flucht."]},
  {"type":"section","h2":"Das enge Refektorium","paras":[
   "Zur Verteidigung sammelt sich die Herde im Kreis, die Platten nach außen gerichtet, die Hocker in der Mitte geschützt, und stößt in die Nacht ein Donnern aus Knarren aus, das Streuner vertreibt."],
   "quote":"„Man jagt keinen Tisch. Man wartet, bis er die Deckung senkt — und die Alten tun das nie.“"},
 ],
}

# ════════════════════════ HISTOIRE ════════════════════════
PAGES["histoire"] = {
 "fr": [
  {"type":"page_title","kicker":"Origines","h1":"Histoire",
   "lead":"Il y a quelque trois cent mille cycles, dans les plaines de poussière ferreuse, apparurent les premières Mensa primigenia."},
  {"type":"section","h2":"L’Âge du Bois Vert","paras":[
   "Quadrupèdes patientes, les proto-tables broutaient les forêts naissantes — et c’est du bois qu’elles tirent encore aujourd’hui leur ossature. Longtemps confondues avec de simples rochers plats, on ne les remarqua qu’au jour où l’une d’elles, dérangée, s’éloigna lentement au crépuscule."]},
  {"type":"section","h2":"Les migrations","paras":[
   "Le refroidissement des plaines poussa les hardes vers les bas-fonds. Les espèces à rallonge — capables d’étendre leur plateau — survécurent ; les autres s’éteignirent avec les premières gelées."]},
  {"type":"section","h2":"Le Pacte du Repas","paras":[
   "Il y a neuf mille cycles, une poignée de tables s’approchèrent des feux pour la chaleur. En échange du couvert, elles acceptèrent le poids des écuelles : ainsi naquirent les premières lignées domestiques. Moins de quatre mille individus errent encore librement aujourd’hui."],
   "quote":"« Sous le vernis, quelque chose, peut-être, attend encore la plaine. »"},
 ],
 "en": [
  {"type":"page_title","kicker":"Origins","h1":"History",
   "lead":"Some three hundred thousand cycles ago, on the plains of iron dust, the first Mensa primigenia appeared."},
  {"type":"section","h2":"The Age of Green Wood","paras":[
   "Patient quadrupeds, the proto-tables grazed the nascent forests — and from wood they still draw their frame today. Long mistaken for mere flat rocks, they were noticed only the day one of them, disturbed, drifted slowly away at dusk."]},
  {"type":"section","h2":"The migrations","paras":[
   "The cooling of the plains pushed the herds toward the lowlands. The species with leaves — able to extend their tops — survived; the others died out with the first frosts."]},
  {"type":"section","h2":"The Pact of the Meal","paras":[
   "Nine thousand cycles ago, a handful of tables drew near the fires for warmth. In exchange for shelter they accepted the weight of bowls: thus were born the first domestic lineages. Fewer than four thousand individuals still roam free today."],
   "quote":"“Beneath the varnish, something, perhaps, still awaits the plain.”"},
 ],
 "de": [
  {"type":"page_title","kicker":"Ursprünge","h1":"Geschichte",
   "lead":"Vor etwa dreihunderttausend Zyklen erschienen auf den Ebenen aus Eisenstaub die ersten Mensa primigenia."},
  {"type":"section","h2":"Das Zeitalter des grünen Holzes","paras":[
   "Geduldige Vierbeiner, grasten die Ur-Tische die jungen Wälder ab — und aus Holz beziehen sie noch heute ihr Gerüst. Lange für bloße flache Felsen gehalten, fielen sie erst an dem Tag auf, als einer von ihnen, gestört, in der Dämmerung langsam davonzog."]},
  {"type":"section","h2":"Die Wanderungen","paras":[
   "Die Abkühlung der Ebenen trieb die Herden in die Niederungen. Die Arten mit Verlängerung — fähig, ihre Platte auszudehnen — überlebten; die anderen erloschen mit den ersten Frösten."]},
  {"type":"section","h2":"Der Pakt der Mahlzeit","paras":[
   "Vor neuntausend Zyklen näherten sich einige Tische der Wärme wegen den Feuern. Gegen Obdach nahmen sie das Gewicht der Schüsseln an: so entstanden die ersten domestizierten Linien. Weniger als viertausend Tiere ziehen heute noch frei umher."],
   "quote":"„Unter dem Lack wartet vielleicht noch etwas auf die Ebene.“"},
 ],
}

# ════════════════════════ PROTECTION ════════════════════════
PAGES["protection"] = {
 "fr": [
  {"type":"page_title","kicker":"Cohabiter sans capturer","h1":"Protection animalière",
   "lead":"La table sauvage n’est ni un meuble perdu ni un objet à restaurer. C’est une espèce à part entière, sensible aux vibrations, aux odeurs chimiques et à l’enfermement."},
  {"type":"rules","h2":"Règles d’observation","items":[
   "Rester à plus de huit longueurs de nappe.",
   "Ne jamais poser d’assiette sur un individu sauvage.",
   "Éviter les vernis, solvants et produits parfumés.",
   "Photographier sans flash, au crépuscule."]},
  {"type":"section","h2":"Zones protégées","paras":[
   "Les réserves de tables vivantes doivent préserver les sols pierreux, les bois morts, les clairières et les ruines légères. Une colonie prospère lorsque l’humain accepte de ne pas ranger le paysage."]},
  {"type":"section","h2":"En cas de rencontre","paras":[
   "Reculez lentement. Parlez bas. Si la table incline son plateau, elle évalue votre stabilité morale. Ne tentez pas de l’aider à « se remettre droite » : c’est souvent une posture d’écoute."]},
  {"type":"section","h2":"Réensauvagement","paras":[
   "Certains individus domestiqués peuvent retrouver une vie libre. On les place d’abord dans des enclos de transition avec poussière, vent et faux repas. Les premiers pas sont toujours émouvants."]},
 ],
 "en": [
  {"type":"page_title","kicker":"Coexist, don’t capture","h1":"Conservation",
   "lead":"The wild table is neither a lost piece of furniture nor an object to be restored. It is a species in its own right, sensitive to vibration, chemical scents and confinement."},
  {"type":"rules","h2":"Rules of observation","items":[
   "Stay more than eight tablecloth-lengths away.",
   "Never set a plate on a wild individual.",
   "Avoid varnish, solvents and scented products.",
   "Photograph without flash, at dusk."]},
  {"type":"section","h2":"Protected areas","paras":[
   "Reserves for living tables must preserve stony ground, dead wood, clearings and light ruins. A colony thrives when humans agree not to tidy the landscape."]},
  {"type":"section","h2":"If you meet one","paras":[
   "Step back slowly. Speak softly. If the table tilts its top, it is weighing your moral steadiness. Do not try to help it “stand up straight”: this is often a listening posture."]},
  {"type":"section","h2":"Rewilding","paras":[
   "Some domesticated individuals can return to a free life. They are first placed in transition enclosures with dust, wind and false meals. The first steps are always moving."]},
 ],
 "de": [
  {"type":"page_title","kicker":"Zusammenleben statt fangen","h1":"Tierschutz",
   "lead":"Der wilde Tisch ist weder ein verlorenes Möbel noch ein zu restaurierendes Objekt. Er ist eine eigene Art, empfindlich gegen Erschütterungen, chemische Gerüche und Gefangenschaft."},
  {"type":"rules","h2":"Beobachtungsregeln","items":[
   "Mehr als acht Tischtuchlängen Abstand halten.",
   "Niemals einen Teller auf ein wildes Tier stellen.",
   "Lacke, Lösungsmittel und Duftstoffe meiden.",
   "Ohne Blitz fotografieren, in der Dämmerung."]},
  {"type":"section","h2":"Schutzgebiete","paras":[
   "Reservate für lebende Tische müssen steinige Böden, Totholz, Lichtungen und leichte Ruinen bewahren. Eine Kolonie gedeiht, wenn der Mensch darauf verzichtet, die Landschaft aufzuräumen."]},
  {"type":"section","h2":"Bei einer Begegnung","paras":[
   "Weichen Sie langsam zurück. Sprechen Sie leise. Neigt der Tisch seine Platte, prüft er Ihre moralische Festigkeit. Versuchen Sie nicht, ihm beim „Geradestehen“ zu helfen: oft ist es eine lauschende Haltung."]},
  {"type":"section","h2":"Auswilderung","paras":[
   "Manche domestizierten Tiere können in die Freiheit zurückfinden. Zuerst kommen sie in Übergangsgehege mit Staub, Wind und Schein-Mahlzeiten. Die ersten Schritte sind stets bewegend."]},
 ],
}

# ════════════════════════ GALERIE ════════════════════════
PAGES["galerie"] = {
 "fr": [
  {"type":"page_title","kicker":"Planches naturalistes","h1":"Galerie",
   "lead":"Les relevés figurés des neuf espèces, et la planche composite de la harde dans la plaine brumeuse."},
  {"type":"gallery_species","cap":"Harde dans la plaine brumeuse — planche composite"},
 ],
 "en": [
  {"type":"page_title","kicker":"Naturalist plates","h1":"Gallery",
   "lead":"The figured records of the nine species, and the composite plate of the herd on the misty plain."},
  {"type":"gallery_species","cap":"Herd on the misty plain — composite plate"},
 ],
 "de": [
  {"type":"page_title","kicker":"Naturkundliche Tafeln","h1":"Galerie",
   "lead":"Die bildlichen Aufnahmen der neun Arten und die Kompositionstafel der Herde in der nebligen Ebene."},
  {"type":"gallery_species","cap":"Herde in der nebligen Ebene — Kompositionstafel"},
 ],
}

# ════════════════════════ JOURNAL ════════════════════════
PAGES["journal"] = {
 "fr": [
  {"type":"page_title","kicker":"Carnet d’expédition","h1":"Journal de terrain",
   "lead":"Extraits du carnet tenu pendant la mission de repérage dans les territoires occidentaux des Tabulidés."},
  {"type":"journal","items":[
   {"date":"Jour 1","title":"Gorge des Pieds-Rouges","text":"À 6 h 12, première trace : quatre empreintes rectangulaires dans la poussière humide. À 6 h 40, une table basse a traversé le lit sec de la rivière. Elle s’est arrêtée trois fois, comme pour vérifier que le monde restait horizontal."},
   {"date":"Jour 3","title":"Clairière des Nappes","text":"Banquet défensif. Sept adultes formaient un cercle parfait autour de trois tabourets. Aucun repas n’était visible, mais l’air sentait la poire sèche et l’orage lointain."},
   {"date":"Jour 5","title":"Ruine du Refuge Nord","text":"Un individu domestiqué, probablement échappé d’une cuisine, a rejoint la colonie. Les sauvages l’ont reniflé par les pieds, puis l’ont laissé dormir près d’un mur. Au matin, son vernis brillait moins. C’est bon signe."},
   {"date":"Jour 8","title":"Falaise Pliable","text":"Les tables pliantes se sont refermées au passage d’une ombre. Pendant douze minutes, la paroi sembla vide. Puis les plateaux se sont ouverts un à un, comme des paupières de bois."}]},
 ],
 "en": [
  {"type":"page_title","kicker":"Expedition notebook","h1":"Field journal",
   "lead":"Extracts from the notebook kept during the survey of the western Tabulidae territories."},
  {"type":"journal","items":[
   {"date":"Day 1","title":"Red-Feet Gorge","text":"At 6:12 a.m., the first trace: four rectangular prints in the damp dust. At 6:40, a low table crossed the dry riverbed. It stopped three times, as if checking that the world remained horizontal."},
   {"date":"Day 3","title":"Clearing of the Cloths","text":"A defensive banquet. Seven adults formed a perfect circle around three stools. No meal was visible, but the air smelled of dried pear and distant storm."},
   {"date":"Day 5","title":"Ruin of the North Shelter","text":"A domesticated individual, probably escaped from a kitchen, joined the colony. The wild ones sniffed it by the feet, then let it sleep near a wall. By morning its varnish shone less. A good sign."},
   {"date":"Day 8","title":"Folding Cliff","text":"The folding tables snapped shut as a shadow passed. For twelve minutes the wall seemed empty. Then the tops opened one by one, like eyelids of wood."}]},
 ],
 "de": [
  {"type":"page_title","kicker":"Expeditionsheft","h1":"Feldtagebuch",
   "lead":"Auszüge aus dem Heft, geführt während der Erkundung der westlichen Tabulidae-Gebiete."},
  {"type":"journal","items":[
   {"date":"Tag 1","title":"Rotfuß-Schlucht","text":"Um 6:12 Uhr die erste Spur: vier rechteckige Abdrücke im feuchten Staub. Um 6:40 überquerte ein niedriger Tisch das trockene Flussbett. Er hielt dreimal an, als prüfe er, ob die Welt waagerecht bleibe."},
   {"date":"Tag 3","title":"Lichtung der Tücher","text":"Ein Verteidigungsbankett. Sieben Erwachsene bildeten einen perfekten Kreis um drei Hocker. Keine Mahlzeit war zu sehen, doch die Luft roch nach trockener Birne und fernem Gewitter."},
   {"date":"Tag 5","title":"Ruine der Nordhütte","text":"Ein domestizierter Tisch, wohl aus einer Küche entkommen, schloss sich der Kolonie an. Die Wilden beschnupperten ihn an den Füßen und ließen ihn dann an einer Mauer schlafen. Am Morgen glänzte sein Lack weniger. Ein gutes Zeichen."},
   {"date":"Tag 8","title":"Klappbare Felswand","text":"Die Klapptische schlossen sich, als ein Schatten vorüberzog. Zwölf Minuten lang schien die Wand leer. Dann öffneten sich die Platten eine nach der anderen, wie Lider aus Holz."}]},
 ],
}

# ════════════════════════ RÉCIT ════════════════════════
PAGES["recit"] = {
 "fr": [
  {"type":"page_title","kicker":"Témoignage documenté","h1":"La personne sauvée par une table sauvage",
   "lead":"Le récit suivant provient d’un témoignage recueilli après la tempête magnétique du col de Bramebois. Il est présenté sans dramatisation : les faits suffisent."},
  {"type":"story","paras":[
   "Je m’étais égaré à la tombée du jour. Le brouillard montait par nappes, si dense que ma lampe semblait éclairer de la farine. Puis le sol a tremblé, doucement, comme si quelqu’un déplaçait une chaise dans une pièce voisine.",
   "Elle est sortie du brouillard sans bruit : une grande table migratrice, plateau large, pattes hautes, surface marquée d’entailles anciennes. Elle s’est approchée, s’est inclinée, puis a frappé la pierre trois fois avec son pied avant droit.",
   "Le vent est devenu violent. Des éclairs couraient au ras du sol. La table s’est placée au-dessus de moi. Sous son plateau, l’air était calme. Elle a tenu ainsi plus d’une heure, encaissant la grêle et les décharges d’électricité statique. Je sentais ses fibres vibrer comme une gorge qui chante.",
   "À l’aube, elle m’a guidé vers le sentier. Tous les vingt pas, elle s’arrêtait pour écouter. Quand les premières maisons sont apparues, elle a refusé d’aller plus loin. Elle a simplement tourné son plateau vers moi, dans un geste que je n’ai jamais su traduire.",
   "Depuis, je ne pose plus jamais les mains sur une table sans attendre une seconde. C’est une politesse. Et peut-être une reconnaissance."],
   "note":"Note de l’observatoire : les marques relevées sur le site confirment le passage d’une <em>Mensa migratoria grandis</em>. Les traces d’abri correspondent à la largeur décrite dans le témoignage."},
 ],
 "en": [
  {"type":"page_title","kicker":"A documented testimony","h1":"The person saved by a wild table",
   "lead":"The following account comes from a testimony gathered after the magnetic storm at the Bramebois pass. It is presented without dramatisation: the facts are enough."},
  {"type":"story","paras":[
   "I had lost my way at nightfall. The fog rose in sheets, so dense that my lamp seemed to light up flour. Then the ground trembled, gently, as if someone were moving a chair in the next room.",
   "It came out of the fog without a sound: a great migratory table, broad top, high legs, its surface marked with old notches. It approached, leaned down, then struck the stone three times with its right front foot.",
   "The wind turned violent. Lightning ran along the ground. The table placed itself over me. Beneath its top, the air was calm. It held like that for more than an hour, taking the hail and the static discharges. I felt its fibres vibrate like a throat that sings.",
   "At dawn it guided me toward the path. Every twenty steps it stopped to listen. When the first houses appeared, it refused to go further. It simply turned its top toward me, in a gesture I have never been able to translate.",
   "Since then, I never lay my hands on a table without waiting a second. It is a courtesy. And perhaps a gratitude."],
   "note":"Observatory note: the marks recorded at the site confirm the passage of a <em>Mensa migratoria grandis</em>. The shelter traces match the width described in the testimony."},
 ],
 "de": [
  {"type":"page_title","kicker":"Ein dokumentiertes Zeugnis","h1":"Die von einem wilden Tisch gerettete Person",
   "lead":"Der folgende Bericht stammt aus einem Zeugnis, gesammelt nach dem Magnetsturm am Bramebois-Pass. Er wird ohne Dramatisierung vorgelegt: die Tatsachen genügen."},
  {"type":"story","paras":[
   "Ich hatte mich bei Einbruch der Nacht verirrt. Der Nebel stieg in Schwaden, so dicht, dass meine Lampe Mehl zu beleuchten schien. Dann bebte der Boden sanft, als rücke jemand im Nebenzimmer einen Stuhl.",
   "Er trat lautlos aus dem Nebel: ein großer Wandertisch, breite Platte, hohe Beine, die Oberfläche von alten Kerben gezeichnet. Er näherte sich, neigte sich und schlug dreimal mit dem rechten Vorderbein auf den Stein.",
   "Der Wind wurde heftig. Blitze liefen über den Boden. Der Tisch stellte sich über mich. Unter seiner Platte war die Luft ruhig. So hielt er länger als eine Stunde aus, fing Hagel und statische Entladungen ab. Ich spürte seine Fasern schwingen wie eine singende Kehle.",
   "Im Morgengrauen führte er mich zum Pfad. Alle zwanzig Schritte hielt er an, um zu lauschen. Als die ersten Häuser auftauchten, weigerte er sich weiterzugehen. Er drehte mir nur seine Platte zu, in einer Geste, die ich nie zu deuten wusste.",
   "Seither lege ich nie die Hände auf einen Tisch, ohne eine Sekunde zu warten. Es ist eine Höflichkeit. Und vielleicht ein Dank."],
   "note":"Anmerkung des Observatoriums: Die am Ort erfassten Spuren bestätigen den Durchzug einer <em>Mensa migratoria grandis</em>. Die Schutzspuren entsprechen der im Zeugnis beschriebenen Breite."},
 ],
}

"""Usage : python outils/repeindre_prototype.py (depuis la racine du dépôt).
Repeint le prototype d'Aziz aux couleurs d'AT_DA et corrige ses textes de prix.
Entrée : AgriTwin-prototype-FR.html (jamais modifié). Sortie : AgriTwin-prototype-DA.html."""
import os, re
D = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(D, '..', 'AgriTwin-prototype-FR.html')
OUT = os.path.join(D, '..', 'AgriTwin-prototype-DA.html')
s = open(SRC, encoding='utf-8').read()

# ---------- 1. Textes : prix, formules, payeur, fréquence ----------
TXT = [
    ('{id:!1,name:"Essentielle",price:42,items:["Service drone et station","Vols hebdomadaires en saison",',
     '{id:!1,name:"Abonnement",price:60,items:["Service drone et station","Un vol toutes les deux semaines en saison",'),
    ('{id:!0,name:"Avancée",price:42,extra:"+ option capteurs (≈ 9 €/ha/an pour 3 sondes — voir la comparaison)",items:["Tout l’Essentiel",',
     '{id:!0,name:"Avec capteurs",price:69,extra:"60 € d’abonnement + ≈ 9 €/ha/an d’option capteurs (3 sondes)",items:["Tout l’abonnement",'),
    ('[b,g]=A.useState(42)', '[b,g]=A.useState(60)'),
    ('children:i?"Avancée":"Essentielle"', 'children:i?"Avec capteurs":"Abonnement"'),
    ('title:t?"Formule Avancée":"Formule Essentielle"', 'title:t?"Abonnement avec capteurs":"Abonnement"'),
    ('children:"Formule Essentielle"', 'children:"Abonnement"'),
    ('children:"Formule Avancée"', 'children:"Abonnement avec capteurs"'),
    ('"Inactif pour l’instant (formule Essentielle). ', '"Inactif pour l’instant (abonnement sans capteurs). '),
    ('"Sonde disponible dans la formule Avancée. ', '"Sonde disponible avec l’option capteurs. '),
    ('who:"Installés par le prestataire (formule Avancée)"', 'who:"Installés par le prestataire (option capteurs)"'),
    ('"Formule essentielle par hectare et par an ; option capteurs en supplément."',
     '"Abonnement par hectare et par an, payé par la coopérative ou la CUMA ; option capteurs en supplément."'),
    ('"Un service par abonnement, pas la vente d’un drone : drone, station, maintenance, jumeau numérique, IA et assistance en une seule formule."',
     '"Un service par abonnement, payé par la coopérative ou la CUMA pour ses fermes adhérentes : drone, station, maintenance, jumeau numérique, IA et assistance."'),
    ('children:["L’agriculteur ",d.jsx("b",{className:"text-bone-50",children:"s’abonne"})," au lieu d’acheter et de gérer du matériel. ',
     'children:["La coopérative ou la CUMA ",d.jsx("b",{className:"text-bone-50",children:"abonne"})," ses fermes adhérentes : l’agriculteur n’achète ni ne gère de matériel. '),
    ('children:"· Tout l’Essentiel"', 'children:"· Tout l’abonnement"'),
    ('`Passer la démo en ${p.name}`', '(p.id?"Activer les capteurs dans la démo":"Revenir à l’abonnement seul")'),
    # Démo cohérente avec l'offre : un vol toutes les deux semaines (03/03, 17/03, 31/03, 14/04)
    ('{id:"M-030",date:"17 mars",zone:.79,rest:.76,rain:38},{id:"M-031",date:"31 mars",zone:.78,rest:.77,rain:11},{id:"M-032",date:"07 avr.",zone:.66,rest:.76,rain:3}',
     '{id:"M-030",date:"03 mars",zone:.79,rest:.76,rain:38},{id:"M-031",date:"17 mars",zone:.78,rest:.77,rain:11},{id:"M-032",date:"31 mars",zone:.66,rest:.76,rain:14}'),
    ('a=["17 mars","31 mars","07 avr.",t?"14 avr.":null]', 'a=["03 mars","17 mars","31 mars",t?"14 avr.":null]'),
    ('"Derniers vols : 31 mars, 07 avr., 14 avr."', '"Derniers vols : 17 mars, 31 mars, 14 avr."'),
    ('children:s==="m031"?"M-031 · 31 mars":"M-032 · 07 avr."', 'children:s==="m031"?"M-031 · 17 mars":"M-032 · 31 mars"'),
    ('d.jsx(d.Fragment,{children:"M-032 · 07 avr."})', 'd.jsx(d.Fragment,{children:"M-032 · 31 mars"})'),
    ('l.lastObs.replace("14 avr.","07 avr.")', 'l.lastObs.replace("14 avr.","31 mars")'),
    ('"mission M-032, 07 avr."', '"mission M-032, 31 mars"'),
    ('"Dernier vol : il y a 7 jours"', '"Dernier vol : il y a 14 jours"'),
    ('{date:"07 avr. 2026",type:"drone",title:"Mission M-032 terminée",detail:"Première baisse de vigueur observée au sud-ouest de la parcelle B."},{date:"02 avr. 2026",type:"field",title:"Apport d’azote — parcelles A et B (2e apport)",detail:"60 kg N/ha, saisi par l’agriculteur."},{date:"31 mars 2026",type:"drone",title:"Mission M-031 terminée",detail:"Aucune anomalie détectée."},{date:"24 mars 2026",type:"weather",title:"Dernière pluie significative (11 mm)",detail:"Depuis : 4 mm en 21 jours."},{date:"17 mars 2026",type:"drone",title:"Mission M-030 terminée",',
     '{date:"02 avr. 2026",type:"field",title:"Apport d’azote — parcelles A et B (2e apport)",detail:"60 kg N/ha, saisi par l’agriculteur."},{date:"31 mars 2026",type:"drone",title:"Mission M-032 terminée",detail:"Première baisse de vigueur observée au sud-ouest de la parcelle B."},{date:"24 mars 2026",type:"weather",title:"Dernière pluie significative (11 mm)",detail:"Depuis : 4 mm en 21 jours."},{date:"17 mars 2026",type:"drone",title:"Mission M-031 terminée",detail:"Aucune anomalie détectée."},{date:"03 mars 2026",type:"drone",title:"Mission M-030 terminée",'),
    # Les 7 parcelles font 100 ha, comme la ferme annoncée (la prairie passait à 6 ha, total 96)
    ('variety:"Prairie permanente",area:6,', 'variety:"Prairie permanente",area:10,'),
]
for a, b in TXT:
    n = s.count(a)
    assert n == 1, (n, a[:70])
    s = s.replace(a, b)

# ---------- 2. Couleurs ----------
styles = [(m.start(), m.end()) for m in re.finditer(r'<style[^>]*>.*?</style>', s, re.S)]
UI = {  # palette sombre -> palette claire d'AT_DA
    '0b0f0d': 'ecf0e4', '101612': 'f6f8f0', '141b17': 'f1f4ea', '18211c': 'fbfcf8', '2c3a32': 'd5d9cf',
    'f3f1ea': '142024', 'e7e5dc': '1f2a2e', 'c9cbc0': '34424a', 'a3aa9f': '4d5a5e', '7f897f': '5f6b6e', '5f6a61': '7c878a',
    'b9cdb0': '2f7d3a', '9fb89a': '3f8f3a',
    '3f7350': 'cfe3c8', '2f5d3f': 'dbe9d6', '244a32': 'e6efe1',
}
UI_CSS = dict(UI, **{'ead292': '2f7d3a', 'dcbc66': '1e5b32'})   # blé = accent d'interface -> vert du logo
UI_JS = dict(UI, **{'ead292': 'c0862a', 'dcbc66': 'b7791f', '3f7350': '2f7d3a'})  # blé = série de données -> ocre


def trip(h):
    return int(h[:2], 16), int(h[2:4], 16), int(h[4:], 16)


def recolor(txt, mapping, css):
    for a, b in mapping.items():
        txt = re.sub('#' + a, '#' + b, txt, flags=re.I)
        ra, ga, ba = trip(a); rb, gb, bb = trip(b)
        txt = txt.replace(f'rgb({ra} {ga} {ba}', f'rgb({rb} {gb} {bb}')
        txt = txt.replace(f'rgba({ra},{ga},{ba},', f'rgba({rb},{gb},{bb},')
    if css:  # voiles blancs sur fond sombre -> voiles ardoise sur fond clair
        txt = re.sub(r'#ffffff([0-9a-f]{2})\b', r'#1f2a2e\1', txt, flags=re.I)
        txt = txt.replace('rgb(255 255 255 /', 'rgb(31 42 46 /')
    txt = re.sub(r'rgba\(255,\s*255,\s*255,', 'rgba(31,42,46,', txt)
    if not css:  # police monospace imposée par les graphiques
        txt = txt.replace('"JetBrains Mono"', '"Instrument Sans"').replace("'JetBrains Mono'", "'Instrument Sans'")
    return txt


out, pos = [], 0
for a, b in styles:
    out.append(recolor(s[pos:a], UI_JS, False))
    out.append(recolor(s[a:b], UI_CSS, True))
    pos = b
out.append(recolor(s[pos:], UI_JS, False))
s = ''.join(out)
s = s.replace('<body class="bg-ink-950">', '<body class="bg-ink-950" style="background:#ecf0e4">')

# ---------- 3. Polices et finitions ----------
head = '''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400&family=Bricolage+Grotesque:opsz,wght@12..96,400..800&display=swap" rel="stylesheet">
<style id="da-surcouche">
html,:host,body,.font-sans{font-family:"Instrument Sans",ui-sans-serif,system-ui,sans-serif!important}
.font-display{font-family:"Bricolage Grotesque",ui-sans-serif,system-ui,sans-serif!important;letter-spacing:-.01em}
.num,code,kbd,samp,pre{font-family:"Instrument Sans",ui-sans-serif,system-ui,sans-serif!important;font-variant-numeric:tabular-nums}
.eyebrow{text-transform:none!important;letter-spacing:0!important;font-weight:600}
.bg-wheat-400{color:#f6f8f0!important}
.bg-wheat-400 *{color:inherit}
::selection{background:#cfe3c8}
.scene-tag,.scene-plot{background:rgba(246,248,240,.9)!important;color:#1f2a2e!important;border-color:rgba(31,42,46,.18)!important;font-family:"Instrument Sans",system-ui,sans-serif!important}
.scene-plot.is-hover{background:#fff!important;border-color:rgba(31,42,46,.45)!important}
.scene-tag-data{color:#1f6f80!important;border-color:rgba(45,106,143,.5)!important}
.recharts-legend-item-text{color:#34424a!important}
[style^="color: rgb(134, 181, 109)"],[style*="; color: rgb(134, 181, 109)"]{color:#3f7a2c!important}
[style^="color: rgb(115, 174, 192)"],[style*="; color: rgb(115, 174, 192)"]{color:#2d6f88!important}
[style^="color: rgb(207, 169, 106)"],[style*="; color: rgb(207, 169, 106)"]{color:#8a5d17!important}
[style^="color: rgb(224, 128, 63)"],[style*="; color: rgb(224, 128, 63)"]{color:#a94f1b!important}
[style^="color: rgb(232, 204, 42)"],[style*="; color: rgb(232, 204, 42)"]{color:#7d6a0a!important}
[class*="bg-black/"]{color:#f6f8f0!important}
[class*="bg-black/"] *{color:inherit!important}
.scene-tag-warn{background:#fbe9dc!important;color:#8a3a12!important;border-color:#c8642a!important}
.text-data{color:#2d6a8f!important}.text-good{color:#2f7d3a!important}.text-est{color:#8a5d17!important}.text-high{color:#a94f1b!important}
.text-warn{color:#7d5f0f!important}.text-crit{color:#a83a27!important}.text-sim{color:#565b66!important}
.text-\[\#9fe3f0\],.text-\[\#bfe2ec\],.text-\[\#cfeef5\]{color:#1f6f80!important}
.text-\[\#ecd6ab\],.text-\[\#f1dca0\]{color:#7a5512!important}
.text-\[\#f08b80\],.text-\[\#ffcfa8\],.text-\[\#ffd9bd\]{color:#a3402a!important}
.bg-gradient-to-r.from-ink-950\/85{background-image:linear-gradient(to right,rgba(236,240,228,.95) 0%,rgba(236,240,228,.82) 36%,rgba(236,240,228,0) 68%)!important}
#root .flex.items-center.gap-2\.5>svg[width="28"]{display:none}
#root .flex.items-center.gap-2\.5:has(>svg[width="28"])::before{content:"";width:34px;height:34px;flex:none;background:url(LOGO) center/contain no-repeat}
@media(max-width:1599px){#root header>.hidden.xl\\:block{display:none!important}}
#da-pa{position:fixed;right:16px;bottom:16px;z-index:2147483000;display:inline-flex;align-items:center;gap:8px;padding:10px 16px;border-radius:999px;background:#1e5b32;color:#f6f8f0;font:700 14px "Instrument Sans",system-ui,sans-serif;text-decoration:none;box-shadow:0 8px 24px rgba(31,42,46,.25)}
#da-pa:hover{background:#2f7d3a}
#da-pa:focus-visible{outline:3px solid #d9a63b;outline-offset:2px}
</style>
'''
assert s.count('</head>') == 1
head = head.replace('LOGO', 'data:image/png;base64,' + open(os.path.join(D, 'logo-embleme.b64.txt')).read().strip())
s = s.replace('</head>', head + '</head>')
s = s.replace('<title>AgriTwin — L’intelligence agricole en service (prototype)</title>', '<title>AgriTwin, prototype</title>')
ROUTES = '''<script>
/* Ouvre une page du prototype depuis l'adresse, ex. AgriTwin-prototype-DA.html#formules */
(function () {
  var pages = { accueil: "Vue d’ensemble", jumeau: "Jumeau numérique 3D", drone: "Suivi par drone",
    agronomie: "Intelligence agronomique", finance: "Intelligence financière", environnement: "Intelligence environnementale",
    operations: "Intelligence opérationnelle", recommandations: "Recommandations IA", historique: "Historique de la ferme",
    formules: "Paramètres", parametres: "Paramètres", "etude-de-cas": "Étude de cas : stress hydrique",
    capteurs: "Avec / sans capteurs", fonctionnement: "Fonctionnement du système" };
  function aller() {
    var cible = pages[decodeURIComponent(location.hash.slice(1))]; if (!cible) return;
    var essais = 0, t = setInterval(function () {
      var b = Array.prototype.find.call(document.querySelectorAll("#root button"), function (e) { return e.innerText.trim().indexOf(cible) === 0; });
      if (b) { b.click(); clearInterval(t); } else if (++essais > 50) clearInterval(t);
    }, 100);
  }
  window.addEventListener("hashchange", aller);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", aller); else aller();
})();
</script>
'''
s = s.replace('</body>', '<a id="da-pa" href="AT_DA.html">Plan d’affaires</a>\n' + ROUTES + '  </body>')
open(OUT, 'w', encoding='utf-8', newline='').write(s)
print('ok', len(s))

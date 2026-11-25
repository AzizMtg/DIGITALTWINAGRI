# AgriTwin : dossier du plan d'affaires

Ce dossier rassemble toutes les notes prises sur le plan d'affaires d'AgriTwin, de septembre à
novembre 2026. Elles sont réécrites pour être lisibles par quelqu'un qui n'a assisté à aucune
séance. Il y a un fichier par matière, plus la stratégie d'ensemble et l'explication des outils.
Chaque document existe en Markdown (dossier `md/`) et en PDF (dossier `pdf/`).

| Fichier | Contenu |
|---|---|
| [Stratégie](Strategie.md) | La stratégie principale, chaque décision et sa raison, les risques, ce qui a été écarté |
| [Marketing](Marketing.md) | Cours, étude de marché, concurrents, clients et payeurs, prix, 4P, format de la soutenance |
| [Finance](Finance.md) | Règles du cours, prévisionnels successifs, coûts, optimisation des vols, financement de départ |
| [Juridique](Juridique.md) | Réglementation des drones, contrats, assurances, vente aux structures, données |
| [Gestion de projet](Gestion%20de%20projet.md) | Équipe, intervenants, dates, demandes des profs, répartition, ce qui reste à faire |
| [Éthique et environnement](Ethique%20et%20environnement.md) | Le volet transversal à intégrer partout |
| [Outils et prototype](Outils%20et%20prototype.md) | Les fichiers HTML du dépôt : ce qu'ils montrent, comment s'en servir, comment le calcul fonctionne |

## Le projet en une phrase (état au 25/11/2026)

AgriTwin survole les fermes de Haute-Vienne et de Creuse avec un drone multispectral, toutes les
deux semaines de mars à septembre. Une IA analyse les images et alimente un **jumeau numérique**
de chaque ferme, qui donne des recommandations à l'agriculteur. Le service n'est pas payé par
l'agriculteur mais par une **structure** (coopérative, CUMA) qui l'offre à ses adhérents :
**60 €/ha/an**, plus une option capteurs de sol à environ 9 €/ha/an.

## Le cadre

- Module « Plan d'affaires » (PA) de 3iL, I2 FE, semestre 7, année 2026-2027.
- Projet innovant en équipe de six. Matthéo est chef de projet.
- Quatre volets (marketing, finance, juridique, gestion de projet), plus l'éthique et
  l'environnement à intégrer dans chacun.
- Évaluation : un devoir surveillé individuel (semaine du 14 au 20/12/2026), un plan d'affaires
  écrit à rendre juste avant la soutenance, et une soutenance de 20 minutes devant un jury.

## Comment le projet a évolué

Le sujet a changé plusieurs fois. Les anciennes notes s'expliquent par ces changements.

| Date | Étape |
|---|---|
| Fin septembre | Première idée : une plateforme qui met en relation des agriculteurs qui cherchent des fonds et des investisseurs. Une carte d'empathie est faite sur un agriculteur qui cherche des pesticides à bon prix. |
| 03/10 | Objection de la prof : les agriculteurs manquent d'argent, les faire payer est contre-productif. Nouveau positionnement : « le jumeau numérique qui rend les projets agricoles finançables ». Règle : l'agriculteur ne sort jamais d'argent de sa poche. |
| 07/10 | Recherche sur le financement agricole, son cadre légal et les concurrents (Miimosa, etc.). |
| 25/10 | Le projet devient **drones + IA + jumeau numérique**. Trois binômes ; Matthéo et Noua font l'étude de marché et la concurrence. |
| 17/11 | Relecture du tableau blanc de finance : il ne suit pas le même modèle économique que le prototype d'Aziz. Premier prévisionnel dans l'Excel du cours, puis choix du « scénario C » : 60 €/ha/an, un vol toutes les deux semaines. |
| 18/11 | Séance juridique : ce sont les **structures** (coopératives, CUMA…) qui paient, pas les agriculteurs. Zone : Haute-Vienne et Creuse. Nouvelle répartition en six parties. |
| 24/11 | Création du site de plan d'affaires (`AgriTwin-plan-affaires.html`, puis `AT_DA.html`), versions 2 à 4 du prévisionnel. Séance de marketing sur les 4P et le format de la soutenance. |
| 25/11 | Réponses aux questions de la séance juridique (optimisation des vols, prix, prêt). Version 5 : drone de secours et météo mois par mois. |

## Les fichiers du dépôt

| Fichier | Rôle |
|---|---|
| `AgriTwin-prototype-FR.html` | Le prototype d'origine d'Aziz (application React compilée). Il n'est jamais modifié. |
| `AgriTwin-prototype-DA.html` | Le même prototype aux couleurs et au logo d'AgriTwin, avec les textes mis à jour (60 €/ha/an, payé par la structure, un vol toutes les deux semaines). Il est généré par `outils/repeindre_prototype.py`. |
| `AgriTwin-plan-affaires.html` | La version détaillée du plan d'affaires : modèle économique, coûts modifiables, prévisionnel sur 3 ans. |
| `AT_DA.html` | Le même calcul, présenté plus simplement (verdict, carte des fermes, leviers). Les réglages sont partagés avec la version détaillée. |

Les fichiers Excel et les PDF explicatifs sont dans le OneDrive partagé, dossier `PA/Matthéo/`.

## Petit lexique

| Terme | Sens |
|---|---|
| Jumeau numérique | Copie virtuelle de l'exploitation, mise à jour avec des données réelles (drone, météo, sol). On y voit l'état des parcelles et on peut simuler l'effet d'une décision. |
| Imagerie multispectrale | Caméra qui capte aussi des couleurs invisibles à l'œil (proche infrarouge). Elle révèle la vigueur et le stress d'une plante avant que ce soit visible. |
| NDVI | Indice de vigueur calculé à partir de ces images : plus il est élevé, plus la végétation est dense et saine. |
| OAD | Outil d'aide à la décision : logiciel qui conseille l'agriculteur (traitement, engrais, irrigation). |
| Modulation | Mettre une dose différente d'engrais ou de produit selon les zones d'une même parcelle. |
| SAU | Surface agricole utilisée : surface réellement cultivée ou en prairie. |
| RA 2020 | Recensement agricole de 2020. |
| RPG | Registre parcellaire graphique : les parcelles déclarées à la PAC. |
| PAC | Politique agricole commune : aides européennes versées aux agriculteurs. |
| CUMA | Coopérative d'utilisation de matériel agricole : des agriculteurs qui partagent du matériel. |
| Structure | Dans nos documents : l'organisation qui paie le service pour ses adhérents (coopérative, CUMA, chambre d'agriculture…). |
| Télépilote | Personne qui pilote le drone. Il doit être formé et certifié. |
| CATS, STS-01/02 | Certificat théorique de télépilote et scénarios standard de vol en catégorie spécifique. |
| AlphaTango | Plateforme de la DGAC où l'exploitant de drones s'enregistre. |
| HT | Hors taxes. Tout le prévisionnel est en HT. |
| BFR | Besoin en fonds de roulement. Ici : les factures émises mais pas encore payées en fin d'année. |
| IS | Impôt sur les sociétés. |
| Seuil de rentabilité, point mort | Chiffre d'affaires à partir duquel on ne perd plus d'argent, et le jour de l'année où il est atteint. |
| Prêt d'honneur | Prêt personnel à 0 %, sans garantie, accordé au fondateur, qui l'apporte ensuite à la société. |
| A1, A2, A3 | Années 1, 2 et 3 du prévisionnel. |

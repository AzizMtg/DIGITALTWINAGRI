# Finance

Intervenante : **Nelly Roulet**. Supports : `Support_formation_finance_3iL 2026.pdf` (95 pages) et
le modèle Excel `Acces_illimite-Plan_financier_previsionnel_entreprise.xlsx`.

Retour à l'[accueil du dossier](README.md). Les choix et leurs raisons sont résumés dans
[Stratégie](Strategie.md) ; le fonctionnement du site de calcul dans
[Outils et prototype](Outils%20et%20prototype.md).

---

## 1. Les règles du cours à appliquer

- **Tout est hors taxes.** La TVA collectée n'est pas du chiffre d'affaires, ni une charge.
- **Amortissement** : tout achat de plus de 500 € HT qui n'est pas un consommable est une
  immobilisation. On l'étale sur sa durée d'usage (prix ÷ durée chaque année) : drone, capteurs,
  ordinateur, développement de l'application.
- **Raisonner en coût du poste** : salaire brut + cotisations patronales + mutuelle, plus
  l'équipement et la formation. Simulateur cité : mon-entreprise.urssaf.fr.
- **Seuil de rentabilité** : le chiffre d'affaires à partir duquel on ne perd plus d'argent.

$$
\text{seuil de rentabilité} = \frac{\text{charges fixes}}{\text{taux de marge sur coûts variables}}
$$

- **Point mort** : le jour de l'année où ce seuil est atteint.

$$
\text{point mort (jours)} = \frac{\text{seuil de rentabilité}}{\text{chiffre d'affaires}} \times 365
$$

- **Erreurs classiques listées par le cours** : oublier la rémunération du dirigeant, les congés
  et les coûts indirects, et la trésorerie de sécurité.
- **Business models (section 12)** : notre modèle relève de l'**abonnement**, combiné à la
  **location ou mise à disposition** de matériel (« le modèle nécessite de financer et entretenir
  les actifs »). Le premier tableau blanc relevait du **paiement à l'usage** (€/ha).

### Le modèle Excel du cours

On remplit l'onglet « Données à saisir » ; le plan s'affiche dans l'onglet suivant. Statut : SAS
à l'IS ; type de vente : Services (Mixte si on vend des capteurs).

| Dépense ou recette | Rubrique de l'onglet « Données à saisir » |
|---|---|
| Drone, capteurs, véhicule acheté | 1) Besoins de démarrage → Matériel (une seule durée d'amortissement pour tout) |
| Développement de l'application ou du site | 1) → Enseigne et éléments de communication, ou Logiciels |
| Formation télépilote, logiciel de traitement | 1) → Logiciels, formations |
| Statuts, avocat de départ | 1) → Frais de notaire ou d'avocat ; Frais d'établissement |
| Serveur mensuel | 3) Charges fixes → Autres abonnements |
| Carburant | 3) → Carburant, transports |
| Entretien du matériel | 3) → Entretien matériel et vêtements |
| Assurances | 3) → Assurances |
| Comptable, avocat récurrents | 3) → Expert comptable, avocats |
| Location de fourgonnette | 3) → Autre charge |
| Abonnements vendus | 4) Chiffre d'affaires → colonne Services, mois par mois |
| Salaires | 7) Salaires employés, **en net annuel** |

À savoir : les charges variables (rubrique 5) ne concernent que la vente de marchandises ; pour un
service, les coûts liés à l'activité vont dans les charges fixes. Le chiffre d'affaires se saisit
mois par mois : mettre peu ou pas de jours l'hiver pour refléter la saison.

**Limites du modèle Excel** (elles expliquent l'écart avec notre site) :
- il compte environ 72 % de charges sociales sur le salaire net, sans la réduction générale au
  niveau du SMIC. Pour un technicien, cela donne 30 052 €/an au lieu de 23 853 € avec le
  simulateur Urssaf, soit environ 6 200 € de trop par an ;
- il n'amortit que les dépenses de démarrage : les achats des années 2 et 3 passent en charges ;
- il n'accepte qu'une seule durée d'amortissement ;
- il ne reporte pas les déficits d'une année sur l'autre (d'où un impôt en année 2 malgré la perte
  de l'année 1).

---

## 2. Comment on est arrivé au modèle actuel

### Le tableau blanc de finance (relu le 17/11)

Le tableau blanc de l'équipe (`PA/Finance.pdf` : charges en rouge, produits en bleu) et le
prototype d'Aziz ne suivaient pas le même modèle :

| | Tableau blanc | Prototype d'Aziz |
|---|---|---|
| Matériel | Drone 3 500 €, apporté par un salarié en fourgonnette | Drone autonome + station installés chez l'agriculteur |
| Prix | 8 €/ha par analyse + 30 € d'installation, ou abonnement 30 € puis 120 €/mois | 42 €/ha/an, + environ 9 €/ha/an pour 3 sondes |
| Fréquence | À chaque passage | Vols hebdomadaires en saison |

**Vérification ligne par ligne**

| Ligne | Verdict |
|---|---|
| Drone 3 500 € | Correct pour un DJI Mavic 3M multispectral (3 726 à 3 900 € HT). C'est un investissement amorti, pas une charge de l'année. |
| Station autonome | DJI Dock 3 + Matrice 4D : 15 077 € HT. Le Matrice 4D ne semble pas multispectral, donc incompatible avec l'indice de vigueur. |
| Analyse à 8 €/ha | Trop bas : c'est le prix du satellite. Un prestataire drone facture dès 15 €/ha. |
| Salaires au SMIC | 12,31 €/h, 1 867,02 € brut par mois depuis le 01/06/2026. |
| « Véhicule de fonction » | Mauvais terme : véhicule **de service** (usage professionnel seulement). |
| Capteurs | Probablement des sondes de sol ou stations connectées : 50 à 200 €/an d'abonnement, plus le matériel. |
| Serveur | Quelques euros à quelques dizaines d'euros par mois ; le gros coût est le développement. |
| Expert coaching 30 €/séance | Ambigu (charge ou produit ?) ; très bas s'il s'agit d'un agronome. |
| Comptable, avocat | 1 500 à 3 000 €/an pour une petite SAS ; statuts et CGU au forfait. |

**Ce qui manquait** : l'assurance RC drone, la formation du télépilote et l'enregistrement de
l'exploitant, le logiciel de traitement des images et les batteries, l'amortissement, la saison,
le BFR, l'autorisation de vol hors vue pour une station autonome.

**Ordre de grandeur** : un salarié (environ 25 000 €/an) et une fourgonnette (6 000 à 8 000 €/an)
demandent environ 4 000 ha analysés par an à 8 €/ha, contre environ 800 ha abonnés à 42 €/ha/an.

### Premier prévisionnel dans l'Excel du cours (17/11)

Hypothèses : abonnement à 42 €/ha/an, fermes de 80 ha, 4 fermes au départ et 20 en fin d'année 1,
puis +100 % et +50 % ; un technicien au SMIC avec un Mavic 3M et une fourgonnette louée, deux à
partir de l'année 2.

| | Année 1 | Année 2 | Année 3 |
|---|---|---|---|
| Chiffre d'affaires | 40 080 € | 80 160 € | 120 240 € |
| Seuil de rentabilité | 52 056 € | 108 815 € | 128 807 € |
| Résultat net | −11 976 € | −28 655 € | −8 567 € |

Verdict : **non rentable** sur trois ans, et trésorerie de départ trop faible.

**Déplacements ajoutés le même jour** (vols chaque semaine sur 30 semaines, 3 fermes par jour,
150 km par jour, 3 visites commerciales de 70 km par client signé, Sommet de l'élevage) :

| | Année 1 | Année 2 | Année 3 |
|---|---|---|---|
| Km par an | 22 185 | 39 810 | 49 881 |
| Carburant | 2 596 € | 4 658 € | 5 836 € |
| Location des fourgonnettes (350 € HT/mois) | 4 200 € | 8 400 € | 8 400 € |
| Assurance des véhicules (700 €/an) | 700 € | 1 400 € | 1 400 € |
| Repas, hôtel et salons | 2 352 € | 3 574 € | 4 433 € |
| **Total** | **9 848 €** | **18 032 €** | **20 069 €** |

Résultat net avec les déplacements : −14 224 €, −31 587 €, environ −12 000 €.

### Les cinq scénarios d'amélioration (17/11)

| Scénario | Résultat net A1 / A2 / A3 | Verdict |
|---|---|---|
| A. Actuel : 42 €/ha/an, vol chaque semaine, 2 techniciens dès l'an 2 | −14 224 / −31 587 / −12 036 € | Non rentable |
| B. Vol toutes les 2 semaines, 1 technicien, 1 véhicule | −12 582 / 5 950 / 25 998 € | Non rentable en année 1 |
| **C. B + prix à 60 €/ha/an** | **3 687 / 34 360 / 63 524 €** | **Rentable, trésorerie suffisante** |
| D. C + capteurs pris par 30 % des fermes | 5 844 / 38 015 / 69 006 € | Rentable |
| E. Prix à 60 € seul, vols chaque semaine | 2 291 / 1 915 / 32 837 € | Rentable mais fragile |

Les deux leviers sont la **fréquence des vols** (elle évite le 2e technicien et le 2e véhicule) et
le **prix**. **Le scénario C a été retenu** le 17/11.

### Les versions suivantes

| Version | Date | Ce qui change | Résultat net A1 / A2 / A3 |
|---|---|---|---|
| Site v1 | 24/11 | Seules les structures paient : 3, 6 puis 9 structures de 4 fermes ; 75 % en abonnement ; 1 technicien | 4 413 / 45 289 / 80 892 € (jugé trop optimiste : 1 seul technicien pour 36 fermes en A3) |
| Site v2 | 24/11 | 3 scénarios ; météo (60 % de jours volables) ; délai de paiement ; techniciens nécessaires calculés | Central : 5 558 / 22 643 / 59 832 € |
| Excel v2 | 24/11 | Scénario central du site dans l'Excel du cours, 32 postes sourcés | 1 122 / 5 036 / 46 726 € |
| v3 « réaliste » | 24/11 | Une seule offre payante, analyse d'essai offerte, montée progressive, 10 000 € d'investisseur | Excel : −13 585 / 3 738 / 52 902 € ; site : −8 366 / 20 861 / 65 055 € |
| v4 « équipe de 6 » | 24/11 | 6 associés, paie qui suit le CA, 5/12/20 structures, 74 000 € de départ, demande au jury après l'année 3 | Excel : −9 332 / 4 584 / 20 924 € ; site : −11 486 / 19 632 / 37 424 € |
| **v5** | **25/11** | **Drone de secours, météo mois par mois, samedis en pointe** | **Excel : −10 599 / 3 508 / 19 847 € ; site : −12 753 / 18 745 / 36 474 €** |

En v3, sans investisseur, la trésorerie passait sous zéro (environ −6 000 € au début de
l'année 2). En v4, le départ est financé par les prêts d'honneur et le prêt bancaire, sans
investisseur.

---

## 3. Le prévisionnel actuel (version 5)

### Les hypothèses (scénario central)

| Hypothèse | A1 | A2 | A3 | Pourquoi |
|---|---|---|---|---|
| Structures clientes en fin d'année | 5 | 12 | 20 | À confirmer par l'étude des payeurs |
| Fermes par structure | 4 | 4 | 4 | Hypothèse de départ |
| Surface moyenne d'une ferme | 80 ha | 80 ha | 80 ha | Haute-Vienne : 286 004 ha pour 3 604 exploitations (RA 2020), soit environ 79 ha |
| Abonnement | 60 €/ha/an | 60 | 60 | Voir [Stratégie](Strategie.md) |
| Vols par an | 15 | 15 | 15 | Un vol toutes les 2 semaines sur 30 semaines |
| Fermes avec capteurs | 5 | 12 | 20 | Une ferme sur quatre |
| Option capteurs | 9 €/ha/an | 9 | 9 | Repris du prototype |
| Télépilotes | 2 | 3 | 4 | Dont 2 associés |
| Associés payés | 2 | 4 | 6 | La paie suit le CA |
| Salaire net d'un associé | 1 000 € | 1 200 € | 1 500 € | Coût × 1,33 en A1 (ACRE), × 1,70 ensuite (règle du modèle Excel) |
| Fermes survolées par jour | 3 | 3 | 3 | Voir l'étude d'optimisation |
| Km par jour de tournée | 150 | 150 | 150 | Hypothèse |
| Visites commerciales par nouvelle structure | 3 de 70 km | | | Hypothèse |
| Jours volables (moyenne de la saison) | 58 % | 58 % | 58 % | Météo-France, Limoges |
| Samedis volés au plus par mois, en pointe | 0 | 0 | 2 | Récupérés l'hiver, sans surcoût |
| Délai de paiement des structures | 30 jours | 30 | 30 | La loi plafonne à 60 jours (ou 45 jours fin de mois) |

Scénario **prudent** : 4, 9 puis 15 structures ; 2, 2 puis 3 télépilotes ; 2, 3 puis 5 associés
payés ; délai de paiement de 45 jours. Scénario **optimiste** : 6, 15 puis 28 structures ; 2, 3
puis 5 télépilotes.

### Les résultats du site (v5)

| Scénario | | A1 | A2 | A3 |
|---|---|---|---|---|
| Prudent | Chiffre d'affaires | 43 160 € | 142 760 € | 249 000 € |
| | Résultat net | −18 783 € | 34 781 € | 22 217 € |
| Central | Chiffre d'affaires | 49 800 € | 184 260 € | 332 000 € |
| | Résultat net | −12 753 € | 18 745 € | 36 474 € |
| | Trésorerie en fin d'année | 36 985 € | 39 113 € | 59 742 € |
| Optimiste | Chiffre d'affaires | 61 420 € | 224 100 € | 448 200 € |
| | Résultat net | −1 952 € | 47 556 € | 94 005 € |

Dans le scénario central, le point bas de trésorerie est de 13 626 €. Au mois le plus chargé, il
faut 1 télépilote en A1 (septembre, 45 % de la capacité), 3 en A2 (septembre, 82 %) et 4 en A3
(avril, 95 %, avec deux samedis par mois).

### Les coûts (hors taxes)

Chaque prix est relevé avec sa source et sa date (17/11 ou 24/11/2026, 25/11 pour le drone de
secours). Les postes « Estimation » restent à confirmer par devis.

| Famille | Poste | Prix HT | Base | Source |
|---|---|---|---|---|
| Investissements | Drone DJI Mavic 3M multispectral | 3 800 € | par nouveau télépilote, amorti 3 ans | Flyingeye : 3 726 à 3 900 € HT |
| | Drone de secours (Mavic 3M) | 3 800 € | en A1, amorti 3 ans | Même prix que le drone principal |
| | Kit 3 batteries + hub de charge | 412,50 € | en A1 et A3, amorti 2 ans | Flyingeye, 495 € TTC |
| | Ordinateur pour le traitement des images | 1 500 € | en A1, amorti 3 ans | Estimation |
| | Développement de la plateforme | 0 € | — | Fait par l'équipe |
| Création | Immatriculation (guichet unique INPI) | 33,83 € | une fois | Service-public.fr |
| | Annonce légale de constitution (SAS) | 199 € | une fois | Arrêté du 19/11/2025, LegalPlace |
| | Déclaration des bénéficiaires effectifs | 19,33 € | une fois | LegalPlace |
| | Rédaction des statuts | 800 € | une fois | Estimation |
| | Formation télépilote (CATS + pratique STS + MANEX) | 1 480 € | par nouveau télépilote | Minute Drone ; 950 à 2 430 € selon l'organisme |
| | Enregistrement AlphaTango | 0 € | — | Gratuit (DGAC) |
| Personnel | Technicien télépilote au SMIC | 1 987,76 €/mois | par technicien salarié | Simulateur Urssaf : 1 867,02 € brut, 1 455,99 € net |
| | Mutuelle (part employeur) | 27 €/mois | par télépilote | 45 à 65 €/mois, 50 % minimum à l'employeur |
| | Médecine du travail | 110 €/an | par télépilote | Estimation |
| | Rémunération des associés | voir hypothèses | associés payés | Règle du modèle Excel |
| Véhicule | Location de la fourgonnette (LLD) | 350 €/mois | par télépilote | Berlingo Van dès 299 € HT/mois, 15 000 km/an |
| | Assurance du véhicule | 700 €/an | par télépilote | Estimation |
| | Carburant | 0,117 €/km | par km | 6,5 L/100 km × 1,80 € HT/L (gazole 2,163 € TTC le 16/11) |
| | Repas en tournée | 10,40 € | par jour de tournée | Barème Urssaf 2026 |
| Drone et logiciels | PIX4Dfields (licence annuelle) | 1 720 €/an | forfait | 1 990 $ HT par an |
| | Hébergement du jumeau numérique (VPS) | 6,49 €/mois | forfait | OVHcloud VPS-1 |
| | Nom de domaine et messagerie | 60 €/an | forfait | Estimation |
| | Entretien et réparations | 300 €/an | forfait | Estimation |
| Assurances | RC drone professionnelle | 270 €/an | forfait | Moyenne relevée sur jechange.fr |
| | DJI Care Enterprise Basic (casse) | 338,33 €/an | forfait | Flyingeye |
| | RC professionnelle de la société | 300 €/an | forfait | 120 à 406 €/an (LegalPlace) |
| Gestion | Expert-comptable | 1 700 €/an | forfait | 875 € en ligne, 1 700 € en cabinet (Indy) |
| | Compte bancaire professionnel | 9 €/mois | forfait | Qonto Basic (Shine : gratuit) |
| | Téléphone professionnel | 20 €/mois | par télépilote | Estimation |
| | CFE | 300 €/an | à partir de A2 | Estimation ; exonérée la 1re année |
| Commercial | Salons et supports (Sommet de l'élevage) | 1 500 €/an | forfait | Estimation |
| Capteurs | Sondes de sol | 350 € × 3 | par nouvelle ferme équipée, amorti 3 ans | Weenat, sonde capacitive |
| | Abonnement aux données des sondes | 16,50 €/mois | par ferme équipée | Weenat : 16,50 à 50 €/mois |

---

## 4. Étude d'optimisation : combien de drones et de télépilotes (25/11)

### Les jours où l'on peut voler

Un jour est perdu quand il pleut au moins 1 mm, plus environ 3 jours par mois pour le vent
au-dessus de 12 m/s (limite du Mavic 3M), les nuages bas et les pannes. Source : fiche
climatologique Météo-France de Limoges, normales 1995-2010.

| Mois | Jours de pluie ≥ 1 mm | Part volable | Jours ouvrés volables |
|---|---|---|---|
| Mars | 10,5 | 56 % | 11,8 |
| Avril | 12,2 | 49 % | 10,3 |
| Mai | 10,9 | 55 % | 11,5 |
| Juin | 7,8 | 64 % | 13,4 |
| Juillet | 9,8 | 59 % | 12,4 |
| Août | 9,4 | 60 % | 12,6 |
| Septembre | 8,8 | 61 % | 12,8 |
| **Saison** | | **≈ 58 %** | **≈ 85 jours** |

- Le premier tableau blanc supposait 150 jours de vol ; la météo en laisse environ 85 en semaine.
- **Avril est le mois le plus difficile**, en pleine période des apports d'azote : c'est lui qui
  dimensionne la flotte.
- On vole de 10 h à 16 h : avec le soleil haut, il y a moins d'ombres et les mesures sont plus
  fiables, soit environ 6 heures utiles par jour.

### Le travail d'un drone par jour

- DJI annonce « jusqu'à 200 ha par vol », mais à 200 m d'altitude ; en France, on vole à 120 m au
  plus. À 120 m, avec le recouvrement nécessaire, on compte environ 50 à 80 ha par batterie
  (estimation à vérifier dans DJI Pilot 2).
- La vraie limite est la tournée : pour une ferme de 80 ha, 2 batteries, environ 30 minutes
  d'installation et de rangement, puis la route jusqu'à la ferme suivante.
- **Hypothèse retenue : 3 fermes par jour, soit environ 240 ha par drone et par jour.**

### Le nombre de drones

Chaque ferme doit être survolée une fois par quinzaine :

$$
\text{fermes par drone} = \text{jours volables par quinzaine} \times 3
$$

En avril, 4,9 jours × 3 = environ 14 fermes par drone ; en moyenne sur la saison, environ 17.

Ce calcul simple suppose que toutes les fermes de l'année sont clientes dès avril. Le site tient
compte de leur arrivée progressive et de la météo de chaque mois :

| | Télépilotes nécessaires au mois le plus chargé | Prévus | Occupation |
|---|---|---|---|
| Année 1 | 1 (septembre) | 2 | 45 % |
| Année 2 | 3 (septembre) | 3 | 82 % |
| Année 3 | 4 (avril), avec 2 samedis par mois | 4 | 95 % |

Sans les samedis, il faudrait 5 télépilotes en année 3. En année 4, les 80 fermes seront clientes
dès avril : il faudra un 5e télépilote, financé par la demande au jury.

---

## 5. Le financement de départ

| Ressource | Montant | Remarque |
|---|---|---|
| Apport des associés | 6 000 € | Repris du prévisionnel Excel du 17/11 |
| Prêts d'honneur | 48 000 € | 6 associés × 8 000 € |
| Prêt bancaire | 20 000 € | 4,5 % sur 5 ans (taux hypothétique, à remplacer par une offre de banque) |
| Investisseur | 0 € | Aucun pendant les trois premières années |
| Subventions | 0 € | Une subvention reste une hypothèse tant qu'elle n'est pas acquise |
| **Total** | **74 000 €** | |

**Le prêt d'honneur** est un prêt personnel à 0 %, sans garantie, accordé au fondateur, qui
l'apporte ensuite à la société. **C'est le fondateur qui le rembourse**, pas l'entreprise. Il
rassure la banque et facilite le prêt bancaire. Montants : 3 000 à 50 000 € chez Initiative France
(environ 10 000 € en moyenne selon Bpifrance Création) ; 3 000 à 30 000 € sur 2 à 5 ans chez
Initiative Nouvelle-Aquitaine. 8 000 € par associé est une hypothèse prudente. L'éligibilité des
étudiants reste à vérifier.

**Pourquoi un prêt bancaire de 20 000 €** : il finance le matériel (drones, batteries, logiciel,
formation des télépilotes), qui s'amortit sur la durée du prêt.

**La trésorerie de départ** de l'Excel est un solde : ressources moins dépenses de démarrage. En
v5, elle est de 51 425 € (74 000 € de ressources). À l'oral, on la justifie par plusieurs mois de
charges d'avance.

**La demande au jury** : 50 000 € au capital pour ouvrir la Corrèze en année 4. Dépenses de la
première année en Corrèze : 104 639 € ; chiffre d'affaires attendu : 49 800 € ; besoin total :
68 539 €, dont 18 539 € pris sur les bénéfices de l'année 3.

---

## 6. Annexe : comment les agriculteurs se financent (recherche du 07/10)

Faite quand le projet était une plateforme de financement. Elle reste utile pour comprendre les
moyens de nos clients.

| Source | Fonctionnement | Repère |
|---|---|---|
| Prêt bancaire | Levier principal ; Crédit Agricole très présent | Banque de France |
| Aides PAC | Aides à l'hectare, éco-régime, aide aux jeunes agriculteurs | Plusieurs dizaines de milliers d'euros par exploitation en moyenne (à vérifier sur Agreste) |
| Aide à l'installation (DJA) | Aide en capital, sous condition de capacité professionnelle et d'un plan sur 4 ans | — |
| Collectivités, Région, Europe | Subventions d'investissement (FEADER) | — |
| Financement participatif | Don avec contrepartie ou prêt | Miimosa : 8 % sur les dons, environ 3 500 projets et 35 M€ |
| Crédits carbone | Label bas-carbone ; Carbioz (Crédit Agricole et France Carbon Agri, 2024) | 45 €/t, dont 32 € pour l'agriculteur |
| Diagnostic carbone | Bon diagnostic carbone (France Relance), 90 % pris en charge | Environ 250 € restent à l'agriculteur |

---

## 7. Points à corriger avant la soutenance (relecture du 25/11)

Une relecture croisée des fichiers a trouvé ces incohérences :

1. **Explications du site** : celle des structures clientes annonce encore 2/3/5, 3/6/9, 4/8/12
   (valeurs de la v2), alors que le calcul utilise 4/9/15, 5/12/20, 6/15/28. Celle des fermes avec
   capteurs annonce 3, 6, 9 au lieu de 5, 12, 20.
2. **Prêt d'honneur** : les 48 000 € entrent dans la trésorerie de la société (apport au capital),
   alors que l'explication des associés payés dit que ceux qui ne sont pas encore payés en vivent.
   Le même argent ne peut pas servir aux deux.
3. **Scénario optimiste, année 3** : il faut 6 télépilotes pour 5 prévus (102 % de la capacité).
4. **Explication des vols** : elle dit que 15 vols évitent un 2e technicien en année 1, alors que
   le plan compte déjà 2 télépilotes en année 1 (les deux associés).
5. **Option capteurs** : les 9 €/ha/an viennent du calculateur du prototype, fait pour une ferme
   de 100 ha avec des sondes à 400 €. Avec les fermes de 80 ha du plan, le même calcul donne environ
   11,7 €/ha. Et si l'abonnement Weenat (16,50 à 50 €/mois) est **par sonde**, une ferme à 3 sondes
   coûte environ 600 €/an pour 720 € de recette : l'option ne rapporte presque rien. À vérifier.
6. **Prototype** : il annonce une ferme de 100 ha (le plan : 80 ha), ses 7 parcelles font 96 ha, et
   la démonstration vole chaque semaine alors que l'offre prévoit un vol toutes les deux semaines.

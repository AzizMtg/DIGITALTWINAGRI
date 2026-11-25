# Outils et prototype

Ce document explique les quatre fichiers HTML du dépôt : ce qu'ils montrent, comment s'en servir et
comment le calcul fonctionne.

Retour à l'[accueil du dossier](README.md).

---

## 1. Le prototype d'Aziz (`AgriTwin-prototype-FR.html`)

- Application React compilée en un seul fichier, sans son code source dans le dépôt. Il s'ouvre
  dans un navigateur, sans installation.
- 13 pages : vue de la ferme, jumeau numérique en 3D, mission du drone, météo, parcelles, alertes et
  recommandations, comparaison des formules, paramètres. Un audit du 24/11 n'a trouvé aucune erreur ;
  les messages « Context Lost » de la 3D sont normaux.
- La démonstration porte sur une ferme fictive, le « Domaine des Trois Vallées » (100 ha, 7
  parcelles : blé, colza, maïs, prairie). Exemple de scénario : une zone d'environ 2 ha de la
  parcelle B pousse moins bien ; l'outil propose d'aller vérifier sur place et de confirmer avec une
  sonde avant tout traitement. **L'agriculteur garde toujours la décision.**
- Les recommandations distinguent ce qui est mesuré (drone, sondes), estimé (modèle) et simulé.
- Concept d'origine : un drone autonome et sa station installés chez l'agriculteur, deux formules
  (« Essentielle » à 42 €/ha/an avec vols hebdomadaires, « Avancée » avec l'option capteurs).
- Ce fichier n'est **jamais modifié** : c'est l'original d'Aziz.

## 2. Le prototype aux couleurs d'AgriTwin (`AgriTwin-prototype-DA.html`)

- Le même prototype, repeint aux couleurs et polices du plan d'affaires, avec le logo AgriTwin.
- Textes mis à jour selon le modèle retenu :
  - « Essentielle » devient « Abonnement » (60 €/ha/an), « Avancée » devient « Avec capteurs »
    (69 €, soit 60 € + environ 9 €/ha/an) ;
  - le payeur est la coopérative ou la CUMA ;
  - un vol toutes les deux semaines.
- Il est **généré** par `outils/repeindre_prototype.py` à partir de l'original : remplacement des
  couleurs dans le code compilé, plus une surcouche de style. Si Aziz envoie une nouvelle version,
  on relance le script.
- **Limite** : il garde le concept de station autonome à la ferme, alors que le plan d'affaires
  suppose des télépilotes en fourgonnette. Seul le code source permettrait de changer ce concept.
  La démonstration montre aussi encore des vols chaque semaine (voir [Finance](Finance.md),
  section 7).

## 3. Le site du plan d'affaires

Deux présentations du **même calcul**, qui partagent les mêmes réglages (enregistrés dans le
navigateur) :

| Fichier | Pour qui | Contenu |
|---|---|---|
| `AT_DA.html` | Pour présenter | Une phrase de verdict, une carte des fermes clientes (une case par ferme), les leviers principaux en curseurs, le détail dans un panneau latéral |
| `AgriTwin-plan-affaires.html` | Pour travailler | Trois onglets : modèle économique, coûts, revenus et résultat |

### Les trois onglets de la version détaillée

1. **Modèle économique** : qui paie, qui relaie, ce qu'on vend, la zone, l'habillage juridique et ce
   qui reste à vérifier.
2. **Coûts** : chaque poste hors taxes avec son prix, son type (investissement, par an, par mois,
   par unité), sa **base** (forfait, par télépilote, par km, par jour de tournée, par ferme, par
   ferme équipée de capteurs…) et ses quantités pour les années 1, 2 et 3. Tout se modifie ; on peut
   ajouter ou supprimer des lignes. La liste des coûts est reprise dans [Finance](Finance.md).
3. **Revenus et résultat** : le choix du scénario (prudent, central, optimiste), les hypothèses de
   vente et d'activité, les mois de vol, le financement de départ, puis les résultats : chiffre
   d'affaires et charges, trésorerie mois par mois sur 36 mois, comparaison des scénarios.

### Les boutons

- **« ? »** à côté de chaque prix, hypothèse et chiffre clé : un résumé au survol, et les liens vers
  la source au clic.
- **Exporter / Importer** : enregistrer ou recharger tous les réglages dans un fichier JSON.
- **Coûts en CSV** : pour ouvrir la liste des coûts dans Excel.
- **Valeurs d'origine** : tout remettre à zéro (il faut cliquer deux fois).
- L'adresse `#plan-affaires` ouvre directement l'espace du plan d'affaires.

### Comment le calcul fonctionne

- **Clients** : structures × fermes par structure. La première structure démarre en mars de l'année
  1, les suivantes signent au fil de l'année ; les années suivantes, elles arrivent en janvier, mai
  et septembre. Une ferme n'est facturée qu'à partir du mois où sa structure démarre.
- **Chiffre d'affaires mensuel** : fermes suivies ce mois-là × hectares × prix ÷ 12, plus l'option
  capteurs pour les fermes équipées, moins la remise. Les abonnements sont facturés tous les mois,
  toute l'année.
- **Vols** : fermes × vols par an, répartis sur les mois de vol cochés (mars à septembre par
  défaut), plus une analyse d'essai par nouvelle structure. Jours de tournée = vols ÷ fermes par
  jour. Les kilomètres et les repas suivent les jours de tournée.
- **Télépilotes nécessaires** : pour chaque mois de vol, jours de tournée ÷ ((21 jours ouvrés +
  samedis) × part volable du mois d'après Météo-France). On garde le mois le plus tendu. Une alerte
  s'affiche s'il en faut plus que prévu, ou si la trésorerie passe sous zéro.
- **Investissements** : achetés l'année où la quantité est saisie, amortis en ligne droite sur la
  durée indiquée (année entière).
- **Impôt sur les sociétés** : 15 % jusqu'à 42 500 € de bénéfice, 25 % au-delà ; les pertes d'une
  année réduisent le bénéfice imposable des suivantes.
- **Seuil de rentabilité** : charges fixes ÷ taux de marge sur coûts variables. Les coûts qui
  dépendent du nombre de fermes, des kilomètres ou des jours de tournée sont variables ; les autres
  sont fixes.
- **Trésorerie mois par mois** : les encaissements arrivent après le délai de paiement. Les dépenses
  de démarrage et les investissements sont payés le premier mois de l'année, l'impôt en décembre,
  le prêt bancaire chaque mois. Le prêt d'honneur n'est pas remboursé par la société (c'est le
  fondateur qui le rembourse).
- **BFR** : les factures pas encore payées en fin d'année.

Le calcul est simplifié et proche du modèle Excel du cours, sans lui être identique. Les écarts sont
expliqués dans [Finance](Finance.md), section 1.

## 4. Les autres fichiers

- `outils/repeindre_prototype.py` : génère le prototype aux couleurs d'AgriTwin à partir de
  l'original.
- `outils/logo-embleme.b64.txt` : l'emblème du logo, encodé pour être intégré dans les pages.
- `docs/plan-d-affaires/` : ce dossier, avec les documents en Markdown (`md/`) et en PDF (`pdf/`).

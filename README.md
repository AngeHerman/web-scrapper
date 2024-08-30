# web-scrapper

Ce projet contient deux scrapper (pour l'instant ) qui extraient des données de sources spécifiques. Vous pouvez choisir de lancer l'un ou l'autre parser via un menu interactif dans le script `main.py`.

## Contenu

- `wiki_scrapper.starwars_sc`: Extrait les titres de la page star wars de wikipedia.
- `download_scrapper.nycbikesdata_sc`: Extrait les liens de telechargement des données des vélos de NYC. (page dynamique)

## Prérequis

- Python 3.x installé.
- Les dépendances nécessaires peuvent être installées en utilisant `pip` (si applicable).

## Utilisation

1. **Exécution avec Makefile** :
   - Pour lancer le projet, utilisez simplement la commande suivante :
     ```bash
     make
     ```
   - Vous pouvez également nettoyer les fichiers temporaires avec :
     ```bash
     make clean
     ```

2. **Exécution manuelle** :
   - Si vous préférez lancer directement le script :
     ```bash
     python3 main.py
     ```

   - Suivez les instructions à l'écran pour choisir quel parser exécuter.


## Licence

Ce projet est sous la [GNU General Public License v3.0 (GPL v3)](LICENSE). Voir le fichier `LICENSE` pour plus de détails.

# 📊 Tier-List - Architecture SQL & Python

Ce projet est une application complète de gestion de classement utilisant une base de données relationnelle SQLite.
<img width="772" height="497" alt="image" src="https://github.com/user-attachments/assets/b5fba1b2-e225-4694-9ea8-03a727f4a888" />

## 🚀 Comment l'utiliser ?
1. Exécutez `Base de donnée.py` pour initialiser le schéma SQL et les données.
2. Lancez `tierlist.py`.
3. Cliquez sur un personnage pour ouvrir sa fiche détaillée (Palmarès, Prime).
4. Attribuez-lui un rang (S, A, B, C, D) pour le voir apparaître en temps réel sur le plateau de classement.
  
## 🛠 Points Techniques Clés
- **Persistance des données** : Organisation des données via 6 tables SQL liées par des clés étrangères.
- **Interface Graphique Dynamique** : Utilisation de `Tkinter` et `Pillow` pour le rendu d'images redimensionnées à la volée.
- **Logique de filtrage** : Requêtes SQL complexes pour extraire les personnages par catégories (Sportifs, Fictifs, Rois, etc.).

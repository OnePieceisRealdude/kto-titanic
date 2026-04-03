# Partie 5 - Incident technique ydata_profiling

Lors de l'exécution de la partie 5 dans le notebook `training-titanic-exploration.ipynb`,
la dépendance `ydata_profiling` a échoué à l'import à cause de l'erreur :

`ModuleNotFoundError: No module named 'pkg_resources'`

Constat :
- `numpy`, `pandas` et `sklearn` fonctionnaient correctement
- le blocage concernait uniquement la génération du rapport de profiling HTML
- la pipeline principale d'entraînement n'était pas bloquée sur le fond

Décision prise :
- désactivation temporaire de `ydata_profiling`
- poursuite de la partie 5 avec :
  - chargement MinIO
  - split train/test
  - entraînement
  - validation
  - exécution du pipeline complet
  - report dans les scripts Python
  - tests unitaires

But :
finir la partie 5 sur les objectifs principaux du cours malgré un problème de dépendance tiers.
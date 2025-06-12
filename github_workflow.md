# 🚀 Workflow GitHub d'Équipe

## 1. Mettre à jour la branche locale principale
```bash
git checkout main
git pull origin main
```

## 2. Créer une branche de fonctionnalité
Nom convention : `feat/nom-de-la-feature`
```bash
git checkout -b feat/nom-de-la-feature
```

## 3. Développer la feature
- Faire des commits atomiques et clairs :
  ```bash
  git add .
  git commit -m "message explicite"
  ```
- Pousser régulièrement :
  ```bash
  git push -u origin feat/nom-de-la-feature
  ```

## 4. Créer une Pull Request (PR)
- Vers `main` (ou `dev` selon organisation)
- Remplir la description (ce qui a été fait, pourquoi, etc.)
- Ajouter les reviewers

## 5. Code Review par un·e autre membre
- Si changements demandés : retourner à l’étape 3

## 6. Merge après validation
- Merge via GitHub (squash ou rebase selon convention)
- Supprimer la branche distante si terminé

## 7. Rebaser régulièrement en cas de longue PR *(optionnel mais recommandé)*
```bash
git fetch origin
git rebase origin/main
```

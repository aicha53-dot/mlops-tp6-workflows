
# Orchestrateur ou integration continue ? (TP06)

| Critere | Prefect (orchestrateur) | GitHub Actions (CI) |
|---|---|---|
| Ce qui declenche l'execution | Planification CRON chaque lundi a 6 h, ou Quick run depuis l'interface | Automatiquement lors d'un git push, ou manuellement avec workflow_dispatch |
| Ou s'execute le traitement | Sur notre ordinateur Windows, via serve ou un Process Worker | Sur un runner GitHub sous Ubuntu |
| Qui surveille, et ou | Prefect, dans son interface web sur le port 4200 : Runs, Task Runs et logs | GitHub Actions, dans l'onglet Actions du depot : jobs, etapes et logs |
| Ce qui se passe en cas d'echec | La tache passe a Failed, le workflow s'arrete et la notification n'est pas executee ; le pipeline peut etre reessaye deux fois | Le job passe au rouge et le script de validation retourne le code de sortie 1 |
| Type de tache adapte | Reentrainement periodique, orchestration et controle qualite du modele | Tests automatiques et verification du pipeline a chaque modification du code |
| Ce qui est versionne dans Git | flow_mlops.py, planifier.py et prefect.yaml | .github/workflows/ci.yml, verifier_qualite.py et requirements-ci.txt |

## Conclusion (5 lignes)

Prefect permet d'orchestrer, planifier et superviser notre pipeline de detection de fraude.
Il controle la qualite du modele et interrompt le workflow si le F1 est inferieur a 0.82.
GitHub Actions verifie automatiquement le pipeline a chaque modification publiee.
Nous avons obtenu trois executions successives : Success, Failure volontaire, puis Success.
Ces deux outils sont complementaires et contribuent a la fiabilite du cycle de vie MLOps.

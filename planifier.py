
from flow_mlops import reentrainement

if __name__ == '__main__':
    # Cree le deploiement hebdomadaire
    # et attend les executions planifiees.
    reentrainement.serve(
        name='hebdomadaire',
        cron='0 6 * * 1'
    )

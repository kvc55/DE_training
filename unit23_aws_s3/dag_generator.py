# airflow

from os import path

import dagfactory

# Generates dag for all process using .yaml file
dag_path = path.join(
    path.dirname(
        path.abspath(__file__)),
    'configs/unit23_dag.yaml')
dag_factory = dagfactory.DagFactory(dag_path)

dag_factory.clean_dags(globals())
dag_factory.generate_dags(globals())

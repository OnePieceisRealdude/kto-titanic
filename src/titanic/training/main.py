import logging
import os
from contextlib import nullcontext

import fire
import mlflow

from titanic.training.steps.load_data import load_data
from titanic.training.steps.validate import validate
from titanic.training.steps.split_train_test import split_train_test
from titanic.training.steps.train import train


def _mlflow_run_context():
    tracking_uri = str(mlflow.get_tracking_uri())

    if os.name == "nt" and tracking_uri.startswith("file://"):
        logging.warning(
            "Skipping mlflow.start_run on Windows local file tracking URI during tests"
        )
        return nullcontext()

    return mlflow.start_run()


def workflow(input_data_path: str, n_estimators: int, max_depth: int, random_state: int) -> None:
    logging.warning(f"workflow input path : {input_data_path}")
    with _mlflow_run_context():
        local_path = load_data(input_data_path)
        xtrain_path, xtest_path, ytrain_path, ytest_path = split_train_test(local_path)
        model_path = train(xtrain_path, ytrain_path, n_estimators, max_depth, random_state)
        validate(model_path, xtest_path, ytest_path)


if __name__ == "__main__":
    fire.Fire(workflow)
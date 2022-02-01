import logging
import time
from pathlib import Path

from joblib import dump
from sklearn.datasets import load_diabetes
from sklearn.linear_model import ElasticNetCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

logger = logging.getLogger(__name__)
root_path = Path(__file__).parent.parent.resolve()


def train_elasticnet() -> None:
    logger.info("Training ElasticNet model")
    x, y = load_diabetes(return_X_y=True, as_frame=True)
    logger.info(f"Input, shape: {x.shape}, columns: {list(x.columns)}")
    print(x)

    start_time = time.time()
    model = make_pipeline(StandardScaler(), ElasticNetCV(cv=20)).fit(x, y)
    fit_time = time.time() - start_time

    logger.info(f"ElasticNet model training time: {fit_time:.2f}s")
    logger.info(f"ElasticNet model R2 score: {model.score(x, y):.4f}")

    logger.info("Saving ElasticNet model")
    dump(model, f"{root_path}/elasticnet_model.joblib")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    train_elasticnet()

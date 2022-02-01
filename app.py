import logging

import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request
from flask.logging import create_logger
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
logger = create_logger(app)
logger.setLevel(logging.INFO)


def scale(payload: pd.DataFrame) -> np.array:
    """Scales Payload"""

    logger.info(f"Scaling Payload: {payload}")
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict


@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home: From Pipelines (Continuous Delivery)</h3>"
    return html.format(format)


# TO DO:  Log out the prediction value
@app.route("/predict", methods=["POST"])
def predict():
    """Performs an sklearn prediction
    input looks like:
            {
    "age":{
      "0": 0.038076
    },
    "sex":{
      "0": 0.050680
    },
    "bmi":{
      "0": 0.061696
    },
    "bp":{
       "0": 0.021872
    },
    "s1":{
       "0": -0.044223
    },
    "s2":{
       "0": -0.034821
    },
    "s3":{
       "0": -0.043401
    },
    "s4":{
       "0": -0.002592
    },
    "s5":{
       "0": 0.019908
    },
    "s6":{
       "0": -0.017646
    }
    }
    result looks like:
    { "prediction": [ 152.13348416289642 ] }
    """

    model_filename = "elasticnet_model.joblib"
    try:
        clf = joblib.load(model_filename)
    except:
        logger.error(f"Impossible to load model file: {model_filename}")
        return "Model not loaded"

    json_payload = request.json
    logger.info(f"JSON payload: {json_payload}")
    inference_payload = pd.DataFrame(json_payload)
    logger.info(f"inference payload DataFrame: {inference_payload}")
    scaled_payload = scale(inference_payload)
    prediction = list(clf.predict(scaled_payload))
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)

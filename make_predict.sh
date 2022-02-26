#!/usr/bin/env bash

PORT=8000
echo "Port: $PORT"

# POST method predict
curl -d '{
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
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict
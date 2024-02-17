from fastapi import FastAPI
import uvicorn
import joblib
from pydantic_types import InputIris
from pydantic_types import OutputIris

#http://localhost:8080/predict?petal_lenght=1.5&petal_width=0.3

target_names = ['setosa', 'versicolor', 'virginica']

# with open('C:/Universidad/Python_uni/api_demo/train/iris_model.pkl', 'rb') as f:
#     pipe = joblib.load(f)

import gcsfs
gcs_client = gcsfs.GCSFileSystem()
destination_uri = 'gs://ue-models-awchacon/Iris_classification/iris_model.pkl'


with gcs_client.open(destination_uri, 'rb') as model_pkl:
    pipe = joblib.load(model_pkl)

app = FastAPI(title="IRIS", version="0.1.0")

@app.post("/predict", response_model=OutputIris)
def predict(input_iris: InputIris):
    probs = pipe.predict_proba([[input_iris.petal_lenght, input_iris.petal_width]])
    return {
            'results':[
        {name: prob for name ,prob in zip(target_names, p)}
        for p in probs
    ][0]

    }
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
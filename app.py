from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import numpy as np
from fastapi.staticfiles import StaticFiles
from mlProject.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI()

# Templates folder
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Home Page
@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# Train Route
@app.get("/train")
async def training():
    os.system("python main.py")
    return {"message": "Training Successful"}


# Prediction Route
@app.get("/predict", response_class=HTMLResponse)
async def predict_page(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    fixed_acidity: float = Form(...),
    volatile_acidity: float = Form(...),
    citric_acid: float = Form(...),
    residual_sugar: float = Form(...),
    chlorides: float = Form(...),
    free_sulfur_dioxide: float = Form(...),
    total_sulfur_dioxide: float = Form(...),
    density: float = Form(...),
    pH: float = Form(...),
    sulphates: float = Form(...),
    alcohol: float = Form(...)
):

    try:
        data = [
            fixed_acidity,
            volatile_acidity,
            citric_acid,
            residual_sugar,
            chlorides,
            free_sulfur_dioxide,
            total_sulfur_dioxide,
            density,
            pH,
            sulphates,
            alcohol
        ]

        data = np.array(data).reshape(1, 11)

        obj = PredictionPipeline()
        prediction = obj.predict(data)

        return templates.TemplateResponse(
            "results.html",
            {
                "request": request,
                "prediction": str(prediction)
            }
        )

    except Exception as e:
        print(e)
        return templates.TemplateResponse(
            "results.html",
            {
                "request": request,
                "prediction": "Something went wrong"
            }
        )


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )
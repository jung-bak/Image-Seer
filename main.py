from model import model_pipeline

from fastapi import FastAPI, UploadFile
from PIL import Image
import io

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to Jung's attempt to learn Fast API and Docker"}

@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()
    image = Image.open(io.BytesIO(content))

    result = model_pipeline(text, image)

    return {"answer": result}

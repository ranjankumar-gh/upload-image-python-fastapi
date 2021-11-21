# app.py
from fastapi import FastAPI, File, UploadFile, Form
import os

app = FastAPI()

@app.post("/upload_file/")
async def image(image: UploadFile = File(...)):
    file_name = os.getcwd()+"/images/"+image.filename.replace(" ", "-")
    with open(file_name,'wb+') as f:
        f.write(image.file.read())
        f.close()
    return {"filename": file_name}

from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
import os
import random
from PIL import Image
from ocr import dateOfBirth
import tempfile
import shutil

app = FastAPI()

# Define a route to accept the image and threshold
@app.post("/dob")
async def process_image(file: UploadFile, threshold: float = Form(...)):
    try:
        # Perform OCR using Tesseract on the saved image

        tempdir = tempfile.mkdtemp()
		
        image_path = os.path.join(tempdir, "image.png")

        # Write the image using a 'with' clause
        with open(image_path, "wb") as image_file:
             shutil.copyfileobj(file.file, image_file)
	
        date_of_birth = dateOfBirth(image_path, threshold)

        # Delete the temporary image file after processing
        shutil.rmtree(tempdir)

        return JSONResponse(content={"DoB": date_of_birth}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


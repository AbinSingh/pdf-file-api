# 1. (FastAPI entry point)

from fastapi import FastAPI, UploadFile, File, HTTPException
from pdf_processor import process_pdf
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the PDF processing API"}

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDFs are allowed.")

    try:
        word_lengths = await process_pdf(file)
        return {"word_lengths": word_lengths}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {e}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



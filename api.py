from fastapi import FastAPI, File, Form,UploadFile
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = FastAPI()

class ResponseText(BaseModel):
    response: str

def get_gemini_response(input, image_file, prompt) -> ResponseText:
    try:
        print(prompt,input)
        model = genai.GenerativeModel("gemini-pro-vision")
    
        response = model.generate_content([input, image_file[0], prompt])
        return ResponseText(response=response.text)
    except Exception as e:
        return ResponseText(response=f"Error: {str(e)}")


@app.get("/")
def home():
    return {"msg":"Welcome"}

@app.post("/gemini")
def gemini(image_file: UploadFile = File(...), prompt: str = Form(...)):
    input = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """
    image = image_file.file.read()
    image_parts = [{
            "mime_type": "image/jpeg",
            "data": image
        }]
    return get_gemini_response(input, image_parts, prompt)




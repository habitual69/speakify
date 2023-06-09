import asyncio
import edge_tts
import os
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
import random

output = "static/audio"
if not os.path.exists(output):
    os.mkdir(output)

app = FastAPI(title="Speakify")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

voices = [
    "en-AU-NatashaNeural",
    "en-AU-WilliamNeural",
    "en-CA-ClaraNeural",
    "en-CA-LiamNeural",
    "en-GB-LibbyNeural",
    "en-GB-MaisieNeural",
    "en-GB-RyanNeural",
    "en-GB-SoniaNeural",
    "en-GB-ThomasNeural",
    "en-HK-SamNeural",
    "en-HK-YanNeural",
    "en-IE-ConnorNeural",
    "en-IE-EmilyNeural",
    "en-IN-NeerjaExpressiveNeural",
    "en-IN-NeerjaNeural",
    "en-IN-PrabhatNeural",
    "en-US-AriaNeural",
    "en-US-ChristopherNeural",
    "en-US-EricNeural",
    "en-US-GuyNeural",
    "en-US-JennyNeural",
    "en-US-MichelleNeural",
    "en-US-RogerNeural",
    "en-US-SteffanNeural",
    "en-ZA-LeahNeural",
    "en-ZA-LukeNeural"
]

async def _convert_text_to_speech(text: str, voice: str) -> str:
    id=random.randint(1,1000000)
    output_file = f"{voice}{id}.mp3"
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(os.path.join(output, output_file))
        return output_file
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "voices": voices})

@app.post("/convert")
async def convert_text(request: Request, text: str = Form(...), voice: str = Form(...)):
    if voice not in voices:
        return {"error": f"Voice '{voice}' not available."}
    output_file = await _convert_text_to_speech(text, voice)
    if "error" in output_file:
        return {"error": output_file["error"]}
    return templates.TemplateResponse("index.html", {"request": request, "output_file": output_file})

@app.get("/audio/{output_file}")
async def get_audio(output_file: str):
    file_path = os.path.join(output, output_file)
    return FileResponse(file_path)

if __name__=="__main__":
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8000, log_level="info", reload=True)
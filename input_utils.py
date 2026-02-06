import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
import soundfile as sf

def extract_text_from_pdf(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text[:3000]

def extract_text_from_url(url):
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.get_text(" ")[:3000]
    except:
        return ""

def load_audio(audio_file):
    data, samplerate = sf.read(audio_file)
    return data, samplerate

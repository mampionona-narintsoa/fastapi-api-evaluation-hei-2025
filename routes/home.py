# app/routes/home.py
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/home")
def home():
    html_content = "<html><body><h1>Welcome home!</h1></body></html>"
    return HTMLResponse(content=html_content, status_code=200)
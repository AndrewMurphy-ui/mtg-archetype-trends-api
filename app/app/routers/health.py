from fastapi import APIRouter #class Apirouter

router = APIRouter() 

@router.get("/health")
def health_check():
    return {"status": "ok"}


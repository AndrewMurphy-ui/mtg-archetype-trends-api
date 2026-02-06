from fastapi import APIRouter #class Apirouter

router = APIRouter() #creates Aoi type instance ib memory 

@router.get("/health")
def health_check():
    return {"status": "ok"}


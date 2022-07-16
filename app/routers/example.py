from fastapi import APIRouter


router = APIRouter()


@router.get("/example/", tags=["example"])
async def example():
    return {"message": "Example API"}

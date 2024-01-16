from fastapi import APIRouter


router = APIRouter(tags=['app'])


# проверка соединения
@router.get("/")
async def test_conn():
    return {"success": True}

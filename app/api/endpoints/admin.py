from fastapi import APIRouter, Depends


router = APIRouter(prefix='/admin', tags=['admin'])


# проверка соединения
@router.get("/")
async def test_conn():
    return {"success": True}

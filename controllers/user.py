from fastapi import APIRouter
from services.user import UserRepository
from prisma.partials import UserRequest, UserResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import status

router = APIRouter(prefix="/users", tags=['Usuários'])
userRepository = UserRepository()

@router.get("/all")
async def list_students() -> List[UserResponse]:
    response = await userRepository.get_all()
    
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
async def insert_student(request: UserRequest) -> UserResponse:
    try:
        response = await userRepository.create(request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.put("/{id}/modify")
async def modify_student(id: str, request: UserRequest) -> UserResponse:
    try:
        response = await userRepository.change(id, request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.delete("/remove")
async def remove_student(id: str) -> UserResponse:
    response = await userRepository.remove(id)
    
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado um diário com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)
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
def list_users() -> List[UserResponse]:
    response = userRepository.get_all()
    
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
def insert_user(request: UserRequest) -> UserResponse:
    try:
        response = userRepository.create(request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.put("/{id}/modify")
def modify_user(id: str, request: UserRequest) -> UserResponse:
    try:
        response = userRepository.change(id, request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.delete("/remove")
def remove_user(id: str) -> UserResponse:
    response = userRepository.remove(id)
    
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado um diário com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from prisma.partials import UserRequest
from .test_base import TestBase
from main import app
import datetime
from prisma.models import User
from services.user import UserService

client = TestClient(app)
prefix = "/users"

userService = UserService()

class TestApp(TestBase):

    def test_get_all_users(self, setUp):
        response = userService.get_all()

        assert len(response) >= 0

    def test_create_user(self, setUp):
        user = {
            "name": "Bruna Maria",
            "registration": 20211094040009,
            "picture": "test",
            "department": "Aluno"
        }

        response = userService.create(user)

        assert response

    def test_edit_user(self, setUp):
        user = {
            "name": "Bruna Maria",
            "registration": 20211094040009,
            "picture": "test",
            "department": "Aluno"
        }

        edited_user = {
            "name": "Bruna Teste",
            "registration": 20211094040009,
            "picture": "test",
            "department": "Aluno"
        }

        response_create_user = userService.create(user)
        user_id = response_create_user.id
        
        response = userService.change(user_id,edited_user, )
        
        assert response

    def test_delete_user(self, setUp):
        user = {
            "name": "Bruna Maria",
            "registration": 20211094040009,
            "picture": "test",
            "department": "Aluno"
        }

        response_create_user = userService.create(user)
        user_id = response_create_user.id

        response = userService.remove(user_id)
        
        assert response

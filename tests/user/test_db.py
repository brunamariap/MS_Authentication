from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from prisma.partials import UserRequest
from .test_base import TestBase
from main import app
import datetime
from prisma.models import User

client = TestClient(app)
prefix = "/users"


class TestApp(TestBase):

    def test_get_all_users(self, setUp):
        response = User.prisma().find_many()

        assert len(response) >= 0

    def test_create_user(self, setUp):
        user = {
            "name": "Bruna Maria",
            "registration": 20211094040009,
            "picture": "test",
            "department": "Aluno"
        }

        response = User.prisma().create(user)

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

        response_create_user = User.prisma().create(user)
        user_id = response_create_user.id
        
        response = User.prisma().update(data=edited_user, where={"id": user_id})
        
        assert response

    def test_delete_user(self, setUp):
        user = {
            "name": "Bruna Maria",
            "registration": 20211094040009,
            "picture": "test",
            "department": "Aluno"
        }

        response_create_user = User.prisma().create(user)
        user_id = response_create_user.id

        response = User.prisma().delete(where={"id": user_id})
        
        assert response

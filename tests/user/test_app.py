from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from prisma.partials import UserRequest
from .test_base import TestBase
from main import app
import datetime

client = TestClient(app)
prefix = "/users"


class TestApp(TestBase):

    def test_get_all_users(self, setUp):
        response = client.get(f"{prefix}/all")

        assert response.status_code == 200

    def test_create_user(self, setUp):
        user = {
            "name": "Bruna Maria",
            "registration": 20211094040009,
            "picture": "test",
            "department": "Aluno"
        }
        request = UserRequest(**user)

        response = client.post(
            f"{prefix}/create", json=jsonable_encoder(request))

        assert response.status_code == 201
        # assert response.json() == user

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

        request = UserRequest(**user)
        response_create_user = client.post(
            f"{prefix}/create", json=jsonable_encoder(request))
        user_res = response_create_user.json()
        user_id = user_res["id"]
        print(user_id)

        request = UserRequest(**edited_user)
        response = client.put(
            f"{prefix}/{user_id}/modify", json=jsonable_encoder(request))
        
        assert response.status_code == 200

    def test_delete_user(self, setUp):
        user = {
            "name": "Bruna Maria",
            "registration": 20211094040009,
            "picture": "test",
            "department": "Aluno"
        }

        request = UserRequest(**user)
        response_create_user = client.post(
            f"{prefix}/create", json=jsonable_encoder(request))
        user_res = response_create_user.json()
        user_id = user_res["id"]
        print(user_id)

        response = client.delete(
            f"{prefix}/remove", params={"id": user_id})
        
        assert response.status_code == 204

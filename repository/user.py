from prisma.models import User
from prisma.partials import UserRequest


class UserRepository:

    def __init__(self):
        self.repository = User

    def create(self, request: UserRequest):
        return self.repository.prisma().create(request)

    def get_all(self):
        return self.repository.prisma().find_many()

    # def get_by_id(self):
    #     pass

    def change(self, id: str, request: UserRequest):
        return self.repository.prisma().update(data=request, where={'id': id})

    def remove(self, id: str):
        return self.repository.prisma().delete({'id': id})

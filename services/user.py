from repository.user import UserRepository
from prisma.partials import UserRequest

class UserService:
		
		def __init__(self):
				self.service = UserRepository()
				
		def create(self, request: UserRequest):
				return self.service.create(request)
		
		def get_all(self):
			return self.service.get_all()
		
		def get_by_id(self, id: str):
			return self.service.get_by_id(id)

		def change(self, id: str, request: UserRequest):
			return self.service.change(id, request)

		def remove(self, id: str):
			return self.service.remove(id)

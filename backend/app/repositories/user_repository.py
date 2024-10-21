from app.models.user import User

class UserRepository:
    def __init__(self):
        self.users = [
            User("77d2", "Gustavo", "gustavo@ig.com.br", "123456"),
            User("62ce", "João", "joao@ig.com.br", "123456")
        ]

    def get_all_users(self):
        return [user.to_dict() for user in self.users]

    def get_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user
        return None
from app.models.user import User

class UserRepository:
    def __init__(self):
        self.users = [
            User("e41a", "Andreia", "andreia@andreia.com", "1234@"),
            User("1ecc", "Karoline", "karol@karoline.com", "1234#")
        ]

    def get_all_users(self):
        return [user.to_dict() for user in self.users]

    def get_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user
        return None
class User:
    def __init__(self, user_id: str, name: str, email: str, password: str):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.name,
            "email": self.email,
            "senha": self.password,
        }
    
    def check_password(self, password: str):
        return self.password == password

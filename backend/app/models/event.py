class Event:
    def __init__(self, event_id: str, title: str, date: str, time: str, price: float, image_url: str, is_private: bool):
        self.id = event_id
        self.title = title
        self.date = date
        self.time = time
        self.price = price
        self.image_url = image_url
        self.is_private = is_private

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.title,
            "data": self.date,
            "horario": self.time,
            "preco": self.price,
            "url_da_imagem": self.image_url,
            "evento_privado": self.is_private
        }

from app.models.event import Event

class EventRepository:
    def __init__(self):
        self.events = [
            Event("1", "Baile de Carnaval", "12/02/2024", "19:00", 40, 
                "https://www.frinoticias.com.br/hf-conteudo/uploads/posts/2022/01/872_carnaval-2022-jpg.jpg", False),
            Event("2", "Baile de Debutante", "28/02/2024", "19:00", 0, 
                "https://cdnm.westwing.com.br/glossary/uploads/br/2021/05/17212845/Presente-de-15-anos.jpg", True),
            Event("3", "Bodas João Paulo & Millena", "15/03/2024", "19:00", 0, 
                "https://nossasbodas.com/wp-content/uploads/2021/03/Arte-Gratuita-Nossas-Bodas-de-Trigo-3-anos-de-casamento-1-scaled.jpg", True)
        ]

    def get_all_events(self):
        return [event.to_dict() for event in self.events]
    
    def delete_event(self, event_id):
        event_to_delete = next((event for event in self.events if event.id == event_id), None)

        if event_to_delete is None:
            return False

        self.events.remove(event_to_delete)
        return True
    
    def add_event(self, event_data):
        new_id = str(len(self.events) + 1)
        
        new_event = Event(
            new_id, 
            event_data['titulo'], 
            event_data['data'], 
            event_data['horario'], 
            event_data['preco'], 
            event_data['url_da_imagem'], 
            event_data['evento_privado']
        )
        
        self.events.append(new_event)
        return new_event.to_dict()

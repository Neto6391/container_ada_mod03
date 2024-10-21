from app.models.event import Event

class EventRepository:
    def __init__(self):
        self.events = [
            Event("1", "Formatura Colegio D. Pedro", "12/02/2024", "20:00", 0,"https://roofranklin.github.io/casa-de-eventos/img/formatura.jpeg", True),
            
            Event("2", "Concurso de Fantasias", "15/02/2024", "20:00", 40,"https://uniao.ugv.edu.br/content/uploads/2023/03/2K4A9490.jpg", False),
            
            Event("3", "Casamento Florinda e Girafales", "09/03/2024", "16:00", 0, "https://imgsapp.em.com.br/app/noticia_127983242361/2023/05/21/1496049/uma-cor-que-esta-totalmente-proibida-para-as-convidadas-de-acordo-com-a-etiqueta-de-casamento-e-o-branco-que-esta-reservado-para-as-noivas-a-nao-ser-que-o-casamento-seja-na-praia_1_55583.jpg", False)
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

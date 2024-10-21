from app.repositories.event_repository import EventRepository

class EventService:
    def __init__(self):
        self.event_repository = EventRepository()

    def get_all_events(self):
        return self.event_repository.get_all_events()
    
    def delete_event(self, event_id):
        return self.event_repository.delete_event(str(event_id))

    def add_event(self, event_data):
        return self.event_repository.add_event(event_data);
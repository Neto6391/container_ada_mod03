from app.repositories.event_repository import EventRepository

class EventService:
    def __init__(self):
        self.event_repository = EventRepository()

    def get_all_events(self):
        return self.event_repository.get_all_events()

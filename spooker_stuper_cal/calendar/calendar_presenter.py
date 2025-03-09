from .calendar_view import CalendarView

class CalendarPresenter:
    def __init__(self,view):
        self.calendar_view = view
        self.view = self.calendar_view

    @property
    def widget(self):
        return self.view
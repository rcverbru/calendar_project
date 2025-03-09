from .calendar_presenter import CalendarPresenter
from .calendar_view import CalendarView

class Calendar:
    def __init__(self):
        view = CalendarView()
        self._presenter = CalendarPresenter(view)

    @property
    def presenter(self):
        return self._presenter

    @property
    def widget(self):
        return self.presenter.widget
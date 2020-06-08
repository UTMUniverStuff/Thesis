class CronSchedule:
    def __init__(
        self,
        name: str = 'CronSchedule',

        start_date: datetime = None,
        end_date: datetime = None,

        year: str = '*',
        month: str = '*',
        day: str = '*',
        week: str = '*',
        day_of_week: str = '*',
        hour: str = '*',
        minute: str = '*',
        second: str = '*'):
    ...

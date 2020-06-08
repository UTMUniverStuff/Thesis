class ApsScheduler(Scheduler):
    def __init__(self):
        self._scheduler = BackgroundScheduler()

    def start(self):
        self._scheduler.add_jobstore(DjangoJobStore(), 'default')
        self._scheduler.start()

    def add_job(self, func, func_kwargs, cron_schedule: CronSchedule) -> str:
        job = self._scheduler.add_job(
            func=func,
            kwargs=func_kwargs,
            trigger='cron',
            start_date=cron_schedule.start_date,
            end_date=cron_schedule.end_date,
            year=cron_schedule.year,
            ...)

        return job.id

    def modify(self, cron_schedule: CronSchedule):
        ...

    def delete(self, cron_schedule_id: int):
        for job_id in self._get_all_affected_job_ids(cron_schedule_id):
            self._scheduler.remove_job(job_id)
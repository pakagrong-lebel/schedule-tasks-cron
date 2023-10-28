# Python script to schedule tasks using cron syntax
from crontab import CronTab
def schedule_task(command, schedule):
    cron = CronTab(user=True)
    job = cron.new(command=command)
    job.setall(schedule)
    cron.write()
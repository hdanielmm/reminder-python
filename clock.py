from apscheduler.schedulers.blocking import BlockingScheduler
from ao_reminder import my_job

sched = BlockingScheduler()

# Runs Wednesday and Friday at 14:30 (am) until forever
sched.add_job(my_job, 'cron', day_of_week='wed,fri', hour=14, minute=30)

sched.start()
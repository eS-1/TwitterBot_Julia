from apscheduler.schedulers.blocking import BlockingScheduler
from replyAsBot import replyAsBot

twische = BlockingScheduler()


@twische.scheduled_job('interval', seconds=30)
def timed_job():
    replyAsBot()


if __name__ == "__main__":
    twische.start()

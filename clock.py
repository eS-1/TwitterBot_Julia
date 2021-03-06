from apscheduler.schedulers.blocking import BlockingScheduler
from ReplyAsBot import replyAsBot

twische = BlockingScheduler()


@twische.scheduled_job('interval', minutes=1)
def timed_job():
    replyAsBot()


if __name__ == "__main__":
    twische.start()

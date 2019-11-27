from apscheduler.schedulers.blocking import BlockingScheduler
import ReplyAsBot

twische = BlockingScheduler()


@twische.scheduled_job('interval', minutes=1)
def timed_job():
    ReplyAsBot.ReplyAsBot()


if __name__ == "__main__":
    twische.start()

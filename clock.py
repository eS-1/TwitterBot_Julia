from apscheduler.schedulers.blocking import BlockingScheduler
import replyAsBot

twische = BlockingScheduler()


@twische.scheduled_job('interval', seconds=30)
def timed_job():
    replyAsBot.replyAsBot()


if __name__ == "__main__":
    twische.start()

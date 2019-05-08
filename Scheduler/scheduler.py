import time

import schedule


class Scheduler(object):

    def __init__(self):
        schedule.every(1).minutes.do(self.job)
        schedule.every().hour.do(self.job)
        schedule.every().day.at("17:06").do(self.job)
        schedule.every(1).to(2).minutes.do(self.job)
        schedule.every().monday.do(self.job)
        schedule.every().wednesday.at("17:06").do(self.job)
        schedule.every().minute.at(":05").do(self.job)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def job(self):
        print("I'm working...")


if __name__ == '__main__':
    sh = Scheduler()
    print(sh)

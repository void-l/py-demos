# -*- coding:utf8 -*-
import time
import sched

scheduler = sched.scheduler(time.time, time.sleep)


def func(msg):
    print "now is ", time.time(), "msg", msg
    scheduler.enter(3, 0, func, ("hello sched",))


scheduler.enter(3, 0, func, ("hello sched",))
scheduler.run()

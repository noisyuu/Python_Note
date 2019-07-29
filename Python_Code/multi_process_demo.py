from random import randint
import time
from multiprocessing import Process
from os import getpid


def download_task(filename, sleepTime):
    print("%s %s" % (filename, time.strftime("download start at: %Y-%m %d %H:%M:%S", time.localtime())))
    print("进程号 [%s] " % getpid())
    time_to_download = randint(5, 15)

    if time is None:
        time_to_download = sleepTime
    time.sleep(time_to_download)
    print("%s %s" % (filename, time.strftime("download end at: %Y-%m %d %H:%M:%S", time.localtime())))


def main():
    start = time.time()
    p1 = Process(target=download_task, args=('Filename 1',15 ,))
    p2 = Process(target=download_task, args=('Filename 2',5,))
    # download_task('Filename 2')
    p1.start()
    p2.start()
    p1.join()
    end = time.time()
    print('总共耗费了%.2f秒' % (end - start))


if __name__ == '__main__':
    main()

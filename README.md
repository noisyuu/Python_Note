# Python_Note
 Python_learning_curve

Day 01
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
1.进程和线程

- 进程之间有着自己独立的内存，因此必须通过进程间通信机制（IPC，Inter-Process Communication）来实现数据共享，具体的方式
包括管道、信号、套接字、共享内存区等.
- 一个进程可以包含多个线程，每个都可以获得CPU调度的时间。线程在一个进程里可以共享相同的上下文。
- Windows环境下没有fork()来创建进程.
- fork()函数由父进程调用，创建出子进程，子进程是父进程的拷贝，但是却拥有自己的PID(Process ID)。fork()会返回两遍，父进程会返回
子进程PID，而子进程永远返回0.
- python的os模块提供了fork()函数.
- 两个进程p1 p2，当p1和p2都call了start()函数以后，当其中一个进程p1调用join()则主进程需要等待p1完成后才可以继续下去,p2仍然可
以返回结果


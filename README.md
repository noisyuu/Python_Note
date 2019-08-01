# Python_Note
 Python_learning_curve

Day 01

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

Day2学习目标：
1.了解以及使用多线程
2. 如何消除github中的conflict
2. 如何消除github中的conxxxflict
2. 如何消除github中的conflxxict

Day3

- 任务类型分计算密集型以及I/O密集型，当处理计算密集型的任务时，这种任务全靠CPU的运算能力，则当任务越多，花在任务切换的时间越多，则CPU
的执行效率越低.
- 而对于I/O密集型的任务，使用多任务可以减少I/O的等待时间，大大增加CPU的运转效率。这类任务大多涉及网络、存储介质。

单线程 + 异步I/O

事件驱动模型:
利用系统对异步I/O的支持，用单进程单线程模型来处理多任务
多核CPU上可以运行多个进程（数量与CPU核心数量相同）
Node.js开发的服务器端程序就用了这种工作模式

在Python这种单线程模型被称为协程。
优势: 因为子程序切换不是线程切换，而是程序自身控制，因此，没有线程切换的开销。不需要多线程的锁机制，因为只有一个线程
不存在同时写变量冲突，在协程中控制共享资源不加锁，只要判断状态，所以执行效率比多线程高很多。

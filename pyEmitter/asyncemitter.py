from threading import Thread
from pyEmitter.emitter import EventEmitter
from pyEmitter.Event import Event
from pyEmitter.TSQueue import TSQueue

class AsyncEmitter(Thread,EventEmitter):
    def __init__(self,isDaemon=False):
        Thread.__init__(self);
        EventEmitter.__init__(self);
        self.setDaemon(isDaemon);
        self.queue = TSQueue();
        self.start();

    def run(self):
        self.EventLoop();

    def emit(self,event,*args):
        self.queue.enqueue(Event(name = event,value = args));

    def EventLoop(self):
        while True:
            Event = self.queue.dequeue();
            consumers = self.emitter.get(Event.name)
            if(consumers == None):
                pass
            else:
                [consumer(self.UUID,*Event.value) for consumer in consumers]

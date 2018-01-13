from threading import Thread
from pyEmitter.boundedemitter import BoundedEmitter
from pyEmitter.Event import Event
from pyEmitter.TSQueue import TSQueue
import pyEmitter.Noise import EventCannotBeEmitted

class BoundedAsyncEmitter(Thread,BoundedEmitter):
    def __init__(self,*events,noisy=False,isDaemon=False):
        Thread.__init__(self);
        BoundedEmitter.__init__(*events,noisy=noisy);
        self.setDaemon(isDaemon);
        self.queue = TSQueue();
        self.start();

    def run(self):
        self.EventLoop();

    def emit(self,event,*args):
        if(event in self.emitter):
            self.queue.enqueue(Event(name = event,value = args));
        elif(self.noisy):
            raise EventCannotBeEmitted

    def EventLoop(self):
        while True:
            Event = self.queue.dequeue();
            consumers = self.emitter.get(Event.name)
            if(consumers == None):
                pass
            else:
                [consumer(self.UUID,*Event.value) for consumer in consumers]

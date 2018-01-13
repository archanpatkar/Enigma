import uuid
import pyEmitter.Noise import EventNotListenable
import pyEmitter.Noise import EventCannotBeEmitted

class BoundedEmitter:
    def __init__(self,*events,noisy=False):
        self.UUID = uuid.uuid4();
        self.noisy = noisy;
        self.emitter = {};
        [self.addEvent(event) for event in events]

    def addEvent(self,event):
        self.emitter[event] = [];

    def on(self,event,f):
        if(event in self.emitter):
            self.emitter[event].append(f);
        elif(self.noisy):
            raise EventNotListenable

    def emit(self,event,*args):
        if(event in self.emitter):
            consumers = self.emitter.get(event);
            if(consumers == None):
                pass
            else:
                [consumer(self.UUID,*args) for consumer in consumers]
        elif(self.noisy):
            raise EventCannotBeEmitted

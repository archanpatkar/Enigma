import uuid

class EventEmitter:
    def __init__(self):
        self.UUID = uuid.uuid4();
        self.emitter = {};

    def on(self,event,f):
        if(self.emitter.get(event) == None):
            self.emitter[event] = [];
            self.emitter[event].append(f);
        else:
            self.emitter[event].append(f);

    def emit(self,event,*args):
        consumers = self.emitter.get(event);
        if(consumers == None):
            pass
        else:
            [consumer(self.UUID,*args) for consumer in consumers]

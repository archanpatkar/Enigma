import threading

class TSQueue:
    def __init__(self):
        self.q = [];
        self.monitor = threading.Condition();

    def enqueue(self,msg):
        with self.monitor:
            self.q.append(msg)
            self.monitor.notify()

    def dequeue(self):
        with self.monitor:
            if(self.isEmpty()):
                self.monitor.wait()
            msg = self.q[0]
            self.q.remove(self.q[0])
            return msg

    def isEmpty(self):
        return (len(self.q) == 0);

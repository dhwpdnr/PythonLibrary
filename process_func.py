from multiprocessing import Process


class HelloProcess(Process):
    def __init__(self):
        super(Process, self).__init__()

    def run(self):
        print("Hello process")


p1 = HelloProcess()
p1.start()

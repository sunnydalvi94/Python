class Engine:
    def start(self):
        print('started the Engine')


class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.start()

result =Car()
result.drive()

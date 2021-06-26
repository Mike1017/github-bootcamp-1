class Bootcamp:
    def __init__(self, author: str, start_at: str):
        self.author = author
        self.start_at = start_at
    
    def start(self, current_time):
        if self.start_at == current_time:
            print("Bootcamp has started!")
        else:
            print("Can't start the bootcamp right now!")   

    def finish(self):
        print("boot camp has finished")

    def dealy(self):
        print("boot camp has been delayed")

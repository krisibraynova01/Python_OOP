class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, new_quantity):
        if self.quantity + new_quantity <= self.size:
            self.quantity += new_quantity

    def status(self):
        return self.size - self.quantity
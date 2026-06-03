class Factory:
    def __init__(self,material,zip,pocket):
        self.material=material
        self.zip=zip
        self.pocket=pocket
    def show(self):
        print(f"your material is {self.material}")
reebok=Factory("Leather",2,4)
campus=Factory("nylon",4,4)
reebok.show()
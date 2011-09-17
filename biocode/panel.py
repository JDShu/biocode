class Panel:

    def __init__(self,dim):
        self.w, self.h = dim
        self.selector = selector.Selector()
        self.switcher_pos = (10,10)
        self.health = None
    
    def scan(self):
        pass

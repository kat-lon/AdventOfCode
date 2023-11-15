class Directory:

    def __init__(self, father, name):
        self.father = father
        self.name = name
        self.children = []
        self.size = 0

    def add_child(self, child):
        self.children.append(child)

    def increment_size(self, size):
        self.size += size
        if (self.father != None):
            self.father.increment_size(size)
    
    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
            
        return None

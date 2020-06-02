class owner(person):
    def __init__(self):
        self.definition = "Administrative permission"
        self.level_pass = 3

class friend(person):
    def __init__(self):
        self.definition = "Standard pemission"
        self.level_pass = 2

class neutral(person):
    def __init__(self):
        self.definition = "Unknown entity, basic permission only"
        self.level_pass = 1

class enemy(person):
    def __init__(self):
        self.definition = "Hostile threat, no permissions"
        self.level_pass = 0

class person():
    def __init__(self):
        self.definition = "A human"
        self.name = None 
        self.age = None
        self.tech_ability = None #limits difficult commands available if necessary , such as data analysis voice scripting

class secret_user():
    def __init__(self):
        self.definition = None
        self.level = 5
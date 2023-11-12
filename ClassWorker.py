class Worker:
    def __init__(self, name, s_name, departament, salary):
        self.name = name
        self.s_name = s_name
        self.departament = departament
        self.salary = salary
        self.__id = 0
        
    def __str__(self):
        return f"{self.name} {self.s_name}: {self.departament}, {self.salary}"
    
    def set_id(self, id):
        self.__id = id
        
    def get_id(self):
        return self.__id
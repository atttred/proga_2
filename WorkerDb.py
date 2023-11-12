from ClassWorker import Worker
import csv

class WorkerDB:
    def __init__(self):
        self.workers = []
        
    def add_worker(self):
        name = input("Enter name: ")
        s_name = input("Enter second name: ")
        departament = input("Enter departament: ")
        salary = input("Enter salary: ")
        
        if(len(self.workers) == 0):
            id = 0
        else:
            id = self.workers[-1].get_id()
        
        worker = Worker(name, s_name, departament, salary)
        self.workers.append(worker)
        
    def delete_by_id(self):
        id = input("Enter id to delete: ")
        self.workers.pop(id)
        
    def print_all(self):
        for w in self.workers:
            print(w)
            
    def edit_by_id(self, id, field, value):
        if(field == 1):
            self.workers[id].name = value
        elif(field == 2):
             self.workers[id].s_name = value
        elif(field == 3):
             self.workers[id].departament =value
        elif(field == 4):
             self.workers[id].salary = value
        else:
            print("Please enter a valid field.") 
from ClassWorker import Worker
import csv

def sort_dec(func):
    def inner(self, field):
        func(self, field)
    return inner

def search_dec(func):
    def inner(self, field, value):
        res = func(self, field, value)
        return res
    return inner

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
        worker.set_id(id+1)
        self.workers.append(worker)
        
    def delete_by_id(self):
        id = input("Enter id to delete: ")
        self.workers.pop(id-1)
        
    def print_all(self):
        for w in self.workers:
            print(w)
            
    def edit_by_id(self, id, field, value):
        if(field == "1"):
            self.workers[id-1].name = value
        elif(field == "2"):
             self.workers[id-1].s_name = value
        elif(field == "3"):
             self.workers[id-1].departament =value
        elif(field == "4"):
             self.workers[id-1].salary = value
        else:
            print("Please enter a valid field.") 
            
    def read_form_csv(self, filename):
        with open(filename, newline='') as file:
            reader = csv.DictReader(file, delimiter=',')
            if len(self.workers) != 0:
                id = max(1, self.workers[-1].get_id() + 1)
            else:
                id = 1
                
            for row in reader:
                self.add_from_row(row, id)
                id+=1

    def add_from_row(self, row, id):
        name = row['name']
        s_name = row['second name']
        departament = row['departament']
        salary = row['salary']
        
        worker = Worker(name, s_name, departament, salary)
        worker.set_id(id)
        self.workers.append(worker)
        
    def write_to_csv(self, filename):
        with open(filename, "a", newline='') as file:
            writer = csv.writer(file)
            for w in self.workers:
                writer.writerow([w.name, w.s_name, w.departament, w.salary])
                
    @sort_dec
    def sort(self, field):
        self.workers.sort(key=lambda x: getattr(x, field))
        
    @search_dec
    def search(self, field, value):
        res = list(filter(lambda x: getattr(x, field) == value, self.workers))
        return res
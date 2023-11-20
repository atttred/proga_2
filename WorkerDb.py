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

def id_generator():
    id = 1
    while True:
        yield id
        id += 1

class WorkerDB:
    id_gen = id_generator()
    def __init__(self):
        self.workers = []
        
    def add_worker(self):
        name = input("Enter name: ")
        s_name = input("Enter second name: ")
        departament = input("Enter departament: ")
        salary = input("Enter salary: ")
        
        """
        if(len(self.workers) == 0):
            id = 0
        else:
            id = self.workers[-1].get_id()
        """
        id = next(WorkerDB.id_gen)
        worker = Worker(name, s_name, departament, salary)
        worker.set_id(id)
        self.workers.append(worker)
        
    def delete_by_id(self, id):
        self.workers.pop(id-1)
        
    def print_all(self):
        for w in self.workers:
            print(w)
            print(w.get_id())
            
    def edit_by_id(self, id, field, value):
        if(field == "name"):
            self.workers[id].name = value
        elif(field == "second name"):
             self.workers[id].s_name = value
        elif(field == "departament"):
             self.workers[id].departament =value
        elif(field == "salary"):
             self.workers[id].salary = value
        else:
            print("Please enter a valid field.") 
            
    def read_form_csv(self, filename):
        with open(filename, newline='') as file:
            reader = csv.DictReader(file, delimiter=',')
            """
            if len(self.workers) != 0:
                id = max(1, self.workers[-1].get_id() + 1)
            else:
                id = 1
            """
            for row in reader:
                id = next(WorkerDB.id_gen)
                self.add_from_row(row, id)

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
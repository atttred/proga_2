from WorkerDb import WorkerDB
import tkinter as tk
import valdiator

@valdiator.validate_int_input
def get_int_input(x):
    pass
@valdiator.validate_string_input
def get_str_input(x):
    pass
@valdiator.validate_file
def get_file(x):
    pass

def main():
    worker_db = WorkerDB()
    while True:
        print("Menu:\n")
        print("1. Add worker.")
        print("2. Delete worker.")
        print("3. Edit worker.")
        print("4. Display all.")
        print("5. Read from CSV.")
        print("6. Write to CSV.")
        print("7. Sort by a field.")
        print("8. Search by a field and a value.")
        print("9. Diagram by departaments")
        print("10. Exit")
        
        choice = input("Enter your choice:")
        
        if(choice == "1"):
            worker_db.add_worker_by_input()
        elif(choice == "2"):
            id = get_int_input("Enter id to delete: ")
            worker_db.delete_by_id(id)
        elif(choice == "3"):
            id = get_int_input("Enter id to edit: ")
            field = get_str_input("Enter a field to edit(name, second name, dep., salary): ")
            if field == "salary":
                value = get_int_input("Enter a new value for it: ")
            else:
                value = get_str_input("Enter a new value for it: ")                
            worker_db.edit_by_id(id, field, value)
        elif(choice == "4"):
            worker_db.print_all()
        elif(choice == "5"):
            filename = get_file("Enter a filename to read from: ")
            worker_db.read_form_csv(filename)
        elif(choice == "6"):
            filename = get_file("Enter a filename to write: ")
            worker_db.write_to_csv(filename)
        elif(choice == "7"):
            field = get_str_input("Enter a field to sort(name, second name, dep., salary): ")
            worker_db.sort(field)
        elif(choice == "8"):
            field = get_str_input("Enter a field to search(name, second name, dep., salary): ")
            if field == "salary":
                value = get_int_input("Enter a value to search for: ")
            else:
                value = get_str_input("Enter a value to search for: ")   
            res = worker_db.search(field, value)
            print("Result: \n")
            for r in res:
                print(r)
        elif(choice == "9"):
            worker_db.pie_by_departament()
        elif(choice == "10"):
            break 
   
class WorkerTextApp:
    def __init__(self, root):
        self.db = WorkerDB()
        self.db.read_form_csv("Workers.csv")
        self.root = root
        self.root.title("Workers")

        self.button_pie = tk.Button(root, text="Diagram", command=self.db.pie_by_departament)
        self.button_pie.pack(fill=tk.BOTH)

        self.button_sort = tk.Button(root, text="Sort", command=self.show_sort_entry)
        self.button_sort.pack(fill=tk.BOTH)
        
        self.button_search = tk.Button(root, text="Search", command=self.show_search_entry)
        self.button_search.pack(fill=tk.BOTH)
        
        self.hide = tk.Button(self.root, text="Hide", command=self.hide_all)

        self.label = None
        self.display_db = None
        self.entry = None
        self.entry_value = None
        self.sort_button = None
        self.search_button = None
        self.label_value = None
        self.error = None
        self.success = None

    def show_sort_entry(self):
        if self.label:
            self.label.destroy()
        if self.entry:
            self.entry.destroy()
        if self.sort_button:
            self.sort_button.destroy()

        self.label = tk.Label(self.root, text="Enter a field to sort (name, second name, dep., salary): ")
        self.label.pack(side=tk.LEFT)

        self.entry = tk.Entry(self.root)
        self.entry.pack(side=tk.LEFT)

        self.sort_button = tk.Button(self.root, text="Sort", command=self.sort_db_by_field)
        self.sort_button.pack(side=tk.LEFT)
        
    def sort_db_by_field(self):
        if self.entry and isinstance(self.entry, tk.Entry):
            try:
                field = self.entry.get()
                self.db.sort(field)
                if self.error:
                    self.error.destroy()
                if not self.success and not self.display_db:
                    self.success = tk.Label(self.root, text="Sorted!")
                    self.display_db = tk.Text(self.root)
                    self.display_db.pack()
                    self.display_db.insert(tk.END, self.db.workers)
                    self.success.pack(side=tk.LEFT)
                    self.hide.pack(side=tk.LEFT)
            except AttributeError:
                if self.success:
                    self.success.destroy()
                if not self.error:
                    self.error = tk.Label(self.root, text="Please enter a valid field.")
                    self.error.pack(side=tk.LEFT)
                    
    def show_search_entry(self):
        if self.label:
            self.label.destroy()
        if self.entry:
            self.entry.destroy()
        if self.search_button:
            self.search_button.destroy()
        if self.entry_value:
            self.entry_value.destroy()
        if self.label_value:
            self.label_value.destroy()
         
        self.label = tk.Label(self.root, text="Enter a field to search (name, second name, dep., salary): ")
        self.label.pack(side=tk.LEFT)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(side=tk.LEFT)
        
        self.search_button = tk.Button(self.root, text="Search", command=self.search_db_by_field)
        self.search_button.pack(side=tk.RIGHT)
 
    def search_db_by_field(self):
        if self.entry and isinstance(self.entry, tk.Entry):
            try:
                field = self.entry.get()
                if (field == "name" or field == "secname" or field == "departament" or field == "salary") and not self.entry_value and not self.label_value:
                    self.label_value = tk.Label(self.root, text="Enter a value to search for: ")
                    self.label_value.pack(side=tk.LEFT)
                    self.entry_value = tk.Entry(self.root)
                    self.entry_value.pack(side=tk.LEFT)
                

                value = self.entry_value.get()
                
                res = self.db.search(field, value)
                if self.error:
                    self.error.destroy()
                if not self.success:
                    for r in res:
                        self.success = tk.Label(self.root, text=r)
                        self.success.pack(side=tk.LEFT)
                    self.hide.pack(side=tk.LEFT)
            except AttributeError:
                if self.success:
                    self.success.destroy()
                if not self.error:
                    self.error = tk.Label(self.root, text="Please enter a valid field.")
                    self.error.pack(side=tk.LEFT)
                    
    def hide_all(self):
        if self.label:
            self.label.destroy()
        if self.entry:
            self.entry.destroy()
        if self.error:
            self.error.destroy()
        if self.success:
            self.success.destroy()
        if self.sort_button:
            self.sort_button.destroy()   
        if self.search_button:
            self.search_button.destroy()
        if self.label_value:
            self.label_value.destroy()
        if self.entry_value:
            self.entry_value.destroy()
        if self.display_db:
            self.display_db.destroy()
        if self.hide:
            self.hide.destroy()
            
if __name__ == "__main__":
    root = tk.Tk()
    app = WorkerTextApp(root)
    root.mainloop()
    #main()
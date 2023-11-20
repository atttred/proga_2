from WorkerDb import WorkerDB
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
        print("9. Exit")
        
        choice = input("Enter your choice:")
        
        if(choice == "1"):
            worker_db.add_worker()
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
            break 
            

if __name__ == "__main__":
    main()
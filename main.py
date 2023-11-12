from WorkerDb import WorkerDB

def main():
    worker_db = WorkerDB()
    while True:
        print("Menu:\n")
        print("1. Add worker.\n")
        print("2. Delete worker.\n")
        print("3. Edit worker.\n")
        print("4. Display all.\n")
        print("7. Exit")
        
        choice = input("Enter your choice:")
        
        if(choice == "1"):
            worker_db.add_worker()
        elif(choice == "2"):
            worker_db.delete_by_id()
        elif(choice == "3"):
            id = int(input("Enter id to edit: "))
            field = input("Enter a field to edit(1-name, 2-second name, 3-dep., 4-salary): ")
            value = input("Enter a new value for it: ")
            worker_db.edit_by_id(id, field, value)
        elif(choice == "4"):
            worker_db.print_all()
        elif(choice == "7"):
            exit  
            

if __name__ == "__main__":
    main()
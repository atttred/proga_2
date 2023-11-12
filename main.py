from WorkerDb import WorkerDB

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
            worker_db.delete_by_id()
        elif(choice == "3"):
            id = int(input("Enter id to edit: "))
            field = input("Enter a field to edit(1-name, 2-second name, 3-dep., 4-salary): ")
            value = input("Enter a new value for it: ")
            worker_db.edit_by_id(id, field, value)
        elif(choice == "4"):
            worker_db.print_all()
        elif(choice == "5"):
            filename = input("Enter a filename to read from: ")
            worker_db.read_form_csv(filename)
        elif(choice == "6"):
            filename = input("Enter a filename to read from: ")
            worker_db.write_to_csv(filename)
        elif(choice == "7"):
            field = input("Enter a field to sort(1-name, 2-second name, 3-dep., 4-salary): ")
            worker_db.sort(field)
        elif(choice == "8"):
            field = input("Enter a field to search from(1-name, 2-second name, 3-dep., 4-salary): ")
            value = input("Enter a value to search for: ")
            res = worker_db.search(field, value)
            print("Result: \n")
            for r in res:
                print(r)
        elif(choice == "9"):
            break 
            

if __name__ == "__main__":
    main()
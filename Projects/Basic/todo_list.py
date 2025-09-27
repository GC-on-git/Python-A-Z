def show_menu():
    print(
        """Welcome to To-do List : 
-------------------------
    1. View tasks
    2. Add tasks
    3. Mark as done
    4. Remove tasks
    5. Quit"""
    )

def add_item(items):
    user_item = input("Enter item to add: ")
    items.append({"task": user_item, "status": "Not Done"})

def remove_item(items):
    show_all_items(items)
    if not items:
        return

    try:
        index = int(input("Enter index to remove: ")) - 1
        if 0 <= index < len(items):
            removed = items.pop(index)
            print(f"Removed: {removed['task']}")
        else:
            print("Invalid index")
    except ValueError:
        print("Please enter a valid number")

def mark_item(items):
    show_all_items(items)
    if not items:
        return

    try:
        index = int(input("Enter index to mark done: ")) - 1
        if 0 <= index < len(items):
            items[index]["status"] = "Done"
            print(f"Marked as done: {items[index]['task']}")
        else:
            print("Invalid index")
    except ValueError:
        print("Please enter a valid number")

def show_all_items(items):
    if not items:
        print("No items present")
    else:
        print("\nYour current items are as follows:")
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item['task']} : {item['status']}")
        print()

def main():
    items = []
    show_menu()

    while True:
        user_input = input("Enter an input: ")
        if user_input == "1":
            show_all_items(items)
        elif user_input == "2":
            add_item(items)
        elif user_input == "3":
            mark_item(items)
        elif user_input == "4":
            remove_item(items)
        elif user_input == "5":
            print("Exiting the list......")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()

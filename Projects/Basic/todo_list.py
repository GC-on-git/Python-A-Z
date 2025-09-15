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
    items[user_item] = "Not Done"

def remove_item(items):
    show_all_items(items)

    user_item = input("Enter item to remove: ")

    if user_item in items:
        items.pop(user_item)
    else:
        print("Item not found")

    show_all_items(items)

def mark_item(items):
    show_all_items(items)

    user_item = input("Enter item to mark done: ")

    if user_item in items:
        items[user_item] = "Done"
    else:
        print("Item not found")

    show_all_items(items)

def show_all_items(items):
    if not items:
        print("No items present")
    else:
        print("Your current items are as follows:")
        for item in items:
            print(f"{item} : {items[item]}")

def main():
    items = {}
    show_menu()

    while True:
        user_input = input("Enter an input: ")
        if user_input == "1":
            show_all_items(items)
        elif user_input == "2":
            add_item(items = items)
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


## Prettify the show items, add index
# 1. sleep
# 2. work
## Rewrite or modify the functions (mark as done, remove) to work with the specific index
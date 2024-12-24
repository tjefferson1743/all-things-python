""" user_prompt = "Enter a todo:"
todo = input(user_prompt) 
todos = [todo]
while (todo != "0"):
    todo = password(user_prompt)
    todos.append(todo)
    print(todos) """

todos = []

while True:
    user_input = input("Type add or show:")
    if (user_input.strip().lower() == "show"):
        print("You chose show")
        if (len(todos) >= 1):
            for todo in todos:
                print(str(todos.index(todo)+1) + ". " + todo)
        else:
            print("Your todo list is empty.")
            # print("Type add to create a todo list:")
    elif (user_input.strip().lower() == "add"):
        print ("You chose add")
        while True:            
            user_add = input("Enter your todo or 0 to exit:")
            if (user_add != "0"):
                todos.append(user_add)
            else:
                break
            
    else:
        print("You didn't make a valid choice. Exiting")
        exit()


user_prompt = "Enter a todo:"
todo = input(user_prompt) 
todos = [todo]
while (todo != "0"):
    todo = input(user_prompt)
    todos.append(todo)
    print(todos)


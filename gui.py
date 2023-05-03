import functions
import PySimpleGUI as sg



label = sg.Text("Type in a To-D0")
input_box = sg.InputText(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")

window = sg.Window('MY To_Do App',
                   layout = [[label], [input_box, add_button]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.add_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()

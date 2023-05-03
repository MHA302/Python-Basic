import functions
import PySimpleGUI as sg



label = sg.Text("Type in a To-D0")
input_box = sg.InputText(tooltip="Enter To-Do")
add_button = sg.Button("Add")

window = sg.Window('MY To_Do App', layout = [[label], [input_box], [add_button]])
window.read()
window.close()

import functions
import PySimpleGUI as sg
# First row
label1 = sg.Text("Enter Feet: ")
input_box_1 = sg.Input()
# second row
label2 = sg.Text("Enter inches:")
input_box_2 = sg.Input()
# compress button
convert_button = sg.Button("Convert")

window = sg.Window("Converter",
                   layout=[[label1, input_box_1],
                           [label2, input_box_2],
                           [convert_button]])
window.read()
window.close()

from feet_to_iches import convert
import PySimpleGUI as sg
# First row
feet_label = sg.Text("Enter Feet: ")
feet_input = sg.Input(key="feet")
# second row
inches_label = sg.Text("Enter inches:")
inches_input = sg.Input(key="inches")
# compress button
convert_button = sg.Button("Convert")
output_text = sg.Text(" ", key="output")

window = sg.Window("Converter",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_button, output_text]])

while True:
    event, values = window.read()
    feet = float(values['feet'])
    inches = float(values['inches'])
    result = convert(feet, inches)
    print(result)
    window["output"].update(value=f"{result}m", text_color="white")

window.close()

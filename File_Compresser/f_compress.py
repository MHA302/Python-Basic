import PySimpleGUI as sg
from zip_creator import make_archive

sg.theme("black")
# First row
label1 = sg.Text("Select files to compress: ")
input_box_1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")
# second row
label2 = sg.Text("Select destination Folder:")
input_box_2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")
# compress button
compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="white")

exit_button = sg.Button("Exit")

window = sg.Window("File Compressor ",
                   layout=[[label1, input_box_1, choose_button1],
                           [label2, input_box_2, choose_button2],
                           [compress_button, exit_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed")

window.close()

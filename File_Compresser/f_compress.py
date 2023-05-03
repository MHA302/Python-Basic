import functions
import PySimpleGUI as sg
# First row
label1 = sg.Text("Select files to compress: ")
input_box_1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")
# second row
label2 = sg.Text("Select destination Folder:")
input_box_2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")
# compress button
compress_button = sg.Button("Compress")

window = sg.Window("File Compressor ",
                   layout=[[label1, input_box_1, choose_button1],
                           [label2, input_box_2, choose_button2],
                           [compress_button]])
window.read()
window.close()


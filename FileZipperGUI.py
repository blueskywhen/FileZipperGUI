import FreeSimpleGUI as sg

label1 = sg.Text("Select files to zip")
input1 = sg.Input()
chooseButton1 = sg.FilesBrowse("Select files")

label2 = sg.Text("Select output folder")
input2 = sg.Input()
chooseButton2 = sg.FolderBrowse("Select destination")

compressButton = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout = [[label1, input1, chooseButton1],
                             [label2, input2, chooseButton2],
                             [compressButton]],)

window.read()
window.close()
import FreeSimpleGUI as sg
import FileZipper

label1 = sg.Text("Select files to zip")
input1 = sg.Input()
chooseButton1 = sg.FilesBrowse("Select files", key = "files")

label2 = sg.Text("Select output folder")
input2 = sg.Input()
chooseButton2 = sg.FolderBrowse("Select destination", key = "folder")

compressButton = sg.Button("Compress")
outputLabel = sg.Text(key = "output")

window = sg.Window("File Compressor",
                   layout = [[label1, input1, chooseButton1],
                             [label2, input2, chooseButton2],
                             [compressButton, outputLabel]],)
while True:
    event, values = window.read()
    match event:
        case "Compress":
            filepaths = values["files"].split(";")
            folder = values["folder"]
            FileZipper.ZipFiles(filepaths, folder)
            window["output"].update(value = "zip completed")
        case sg.WIN_CLOSED:
            break
window.close()
 import PySimpleGUI as sg

layout = [[sg.Text("Hello World!")], [sg.Button("OK")]]
#create the window
window = sg.Window("Demo", layout)

#create loop for the Window
while True:
    event, values = window.read()
    #end if user closes window or presses ok Button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()

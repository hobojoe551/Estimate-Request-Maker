import PySimpleGUI as sg


cost_input = [
    [
        sg.Text("Part Cost"),
        sg.In(size=(25,1), enable_events=True, key = "-PCOST-"),


    ]
]

cost_output = [
    [
        sg.Text(size=(6,1), key='-OUTPUT-')
    ],
]
layout = [
    [
    sg.Column(cost_input),
    sg.VSeperator(),
    sg.Column(cost_output),
    ]
]

window = sg.Window("Estimate Requests", layout)

while True:
    event, values = window.read()
    if event == "-PCOST-":
        def part_cost():
            try:
                pcost = float(values["-PCOST-"])

                if pcost<=15:
                    pcost = str(round(pcost+55, 2))
                    window['-OUTPUT-'].update(str(pcost))
                elif pcost<=20 and pcost>15:
                     pcost = str(round(pcost*5,0)+.99)
                     window['-OUTPUT-'].update(str(pcost))
                elif pcost<30:
                    pcost = str(round(pcost*4.6,0)+.99)
                    window['-OUTPUT-'].update(str(pcost))
                elif pcost<50:
                    pcost = str(round(pcost*3.8,0)+.99)
                    window['-OUTPUT-'].update(str(pcost))
                elif pcost<70:
                    pcost = str(round(pcost*3.3,0)+.99)
                    window['-OUTPUT-'].update(str(pcost))
                elif pcost<100:
                    pcost = str(round(pcost*2.9,0)+.99)
                    window['-OUTPUT-'].update(str(pcost))
                elif pcost<150:
                    pcost = str(round(pcost*2.6,0)+.99)
                    window['-OUTPUT-'].update(str(pcost))
                elif pcost<200:
                    pcost = str(round(pcost*2.3,0)+.99)
                    window['-OUTPUT-'].update(str(pcost))
                elif pcost<250:
                    pcost = str(round(pcost*2.1,0)+.99)
                    window['-OUTPUT-'].update(str(pcost))
                elif pcost<300:
                    pcost = str(round(pcost*2.0,0)+.99)
                    window['-OUTPUT-'].update(str(pcost))
                else:
                    pcost = str(round(pcost*1.9,0)+.99)
                    window['-OUTPUT-'].update(str(pcost))
            except ValueError:
                window['-OUTPUT-'].update('')
                pass



        part_cost()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

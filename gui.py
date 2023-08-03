#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-01 17:24:50

import begin
import PySimpleGUI as sg

def run():
    sg.theme('DarkAmber')
    sg.set_options(font='Default 18', keep_on_top=True)
    layout = [ 
        [sg.Text('Sime text on row 1')],
        [sg.Text('Some text on Row 2'), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
      ]

    window = sg.Window('Window Ttitle', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        print('you entered ', values[0])

    window.close()

@begin.start
def main(arg1 = None):
    run()

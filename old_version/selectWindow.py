from tkinter import Tk, StringVar, ttk
from tkinter import *
from PIL import ImageTk, Image
from FunctionsDescription import *
import pickle


def selectCommands(appName, button):

    button.config(state = DISABLED)
    
    selectWindow = Toplevel(appName)
    selectWindow.geometry('700x380')
    

    selection1 = 'Vehicle Speed'
    selectionbox_1 = ttk.Combobox(selectWindow, state = 'readonly')
    selectionbox_1['values'] = obdCommandDescription
    selectionbox_1.grid(column = 10, row = 10)

    selectionbox_2 = ttk.Combobox(selectWindow, state = 'readonly')
    selectionbox_2['values'] = obdCommandDescription
    selectionbox_2.grid(column = 100, row = 10)

    selectionbox_3 = ttk.Combobox(selectWindow, state = 'readonly')
    selectionbox_3['values'] = obdCommandDescription
    selectionbox_3.grid(column = 200, row = 10)

    # do if function to handle error where election1 is nothin textvariable = selection1
    #selection_1_command = obdCommand[obdCommandDescription.index(selection1)]


    saveButton = Button(selectWindow, text = 'Save',
                        command = lambda: saveCommand(selectionbox_1,
                                                      selectionbox_2,
                                                      selectionbox_3,
                                                      button,
                                                      appName,
                                                      selectWindow)).grid(row = 300, column = 620)
    selectWindow.protocol('WM_DELETE_WINDOW', lambda: saveCommand(selectionbox_1,
                                                          selectionbox_2,
                                                          selectionbox_3,
                                                          button,
                                                          appName,
                                                          selectWindow))
    
def saveCommand(selectionbox_1, selectionbox_2, selectionbox_3, button, appName, window):
    selection = [None]*3
    selection[0] = selectionbox_1.get()
    selection[1] = selectionbox_2.get()
    selection[2] = selectionbox_3.get()
    
    if selection[0]=='' or selection[1]=='' or selection [2]=='':
        print('Select Command!')
    else:
        appName.after(10, putLabels)
        f = open('obdDescriptions.pckl', 'wb')
        pickle.dump(selection, f)
        f.close()
        window.destroy()
        button.config(state = NORMAL)
        return


    #have boolean or something so button cant be pressed more than once
    #and is reset after all variables are saved

    
    

    
    

    


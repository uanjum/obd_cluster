from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from FunctionsDescription import *
import pickle
import obd


def connectOBD():
    ports = obd.scan_serial()
    print(ports)
    connection = obd.OBD(ports[2])
    connection_status = connection.is_connected()

    if connection_status:
        print('connected succesfully!')

    else:
        print('connection failed...')

    # returns physical connection that is used to query the car for commands and boolean status of connection
    return connection, connection_status


def sendCommand(connection, status, mainCanvas, arc1, arc2, arc3, arc4, arc5, arc6,
                val1, val2, val3, val4, val5, val6, index,
                maximumValue, minimumValue, buttonstate):

    global nwerty

    if status and buttonstate.cget('state') == 'normal':
        comVal = [1]*6
        convert = [1]*6

        for x in range(0, 5):
            # asks the car for the value
            comVal[x] = connection.query(obd.commands[obdCommand[index[x]]])
            if comVal[x].value is not None:
                convert[x] = -(((comVal[x].value.magnitude-minimumValue[index[x]]) /
                               (maximumValue[index[x]]-minimumValue[index[x]])*180))
                mainCanvas.itemconfig(eval("arc"+str(x+1)), extent=convert[x])
                mainCanvas.itemconfig(
                    eval("val"+str(x+1)), text=int(comVal[x].value.magnitude))

    mainCanvas.after(10, lambda: sendCommand(connection, status, mainCanvas, arc1, arc2, arc3, arc4, arc5, arc6,
                                             val1, val2, val3, val4, val5, val6, index,
                                             maximumValue, minimumValue, buttonstate))


def selectCommands(appName, button, connection):
    button.config(state=DISABLED)

    selectWindow = Toplevel(appName)
    selectWindow.geometry('700x380')

    selection1 = 'Vehicle Speed'
    selectionbox_1 = ttk.Combobox(selectWindow, state='readonly')
    selectionbox_1['values'] = obdCommandDescription
    selectionbox_1.grid(row=1, column=1, padx=10, pady=10)

    selectionbox_2 = ttk.Combobox(selectWindow, state='readonly')
    selectionbox_2['values'] = obdCommandDescription
    selectionbox_2.grid(row=1, column=2, padx=10, pady=10)

    selectionbox_3 = ttk.Combobox(selectWindow, state='readonly')
    selectionbox_3['values'] = obdCommandDescription
    selectionbox_3.grid(row=1, column=3, padx=10, pady=10)

    selectionbox_4 = ttk.Combobox(selectWindow, state='readonly')
    selectionbox_4['values'] = obdCommandDescription
    selectionbox_4.grid(row=2, column=1, padx=10, pady=10)

    selectionbox_5 = ttk.Combobox(selectWindow, state='readonly')
    selectionbox_5['values'] = obdCommandDescription
    selectionbox_5.grid(row=2, column=2, padx=10, pady=10)

    selectionbox_6 = ttk.Combobox(selectWindow, state='readonly')
    selectionbox_6['values'] = obdCommandDescription
    selectionbox_6.grid(row=2, column=3, padx=10, pady=10)

    saveButton = Button(selectWindow, text='Save',
                        command=lambda: saveCommand(selectionbox_1,
                                                    selectionbox_2,
                                                    selectionbox_3,
                                                    selectionbox_4,
                                                    selectionbox_5,
                                                    selectionbox_6,
                                                    button,
                                                    selectWindow)).grid(row=3, column=3, pady=40)
    selectWindow.protocol('WM_DELETE_WINDOW', lambda: saveCommand(selectionbox_1,
                                                                  selectionbox_2,
                                                                  selectionbox_3,
                                                                  selectionbox_4,
                                                                  selectionbox_5,
                                                                  selectionbox_6,
                                                                  button,
                                                                  selectWindow))


def saveCommand(selectionbox_1, selectionbox_2, selectionbox_3,
                selectionbox_4, selectionbox_5, selectionbox_6, button, window):
    selection = [None]*6

    for x in range(0, 6):
        selection[x] = eval('selectionbox_' + str(x+1)).get()

    if selection[0] == '' or selection[1] == '' or selection[2] == '' or selection[3] == '' or selection[4] == '' or selection[5] == '':
        print('Select Command!')
    else:

        for z in range(0, 5):
            index[z] = obdCommandDescription.index(selection[z])
            master.itemconfig(eval('label_'+str(z+1)), text=selection[z])
            master.itemconfig(eval('minVal_'+str(z+1)), text=minVal[index[z]])
            master.itemconfig(eval('maxVal_'+str(z+1)), text=maxVal[index[z]])
            master.itemconfig(eval('inc'+str(z+1)+'_1'),
                              text=Increment1[index[z]])
            master.itemconfig(eval('inc'+str(z+1)+'_2'),
                              text=Increment2[index[z]])
            master.itemconfig(eval('inc'+str(z+1)+'_3'),
                              text=Increment3[index[z]])

        command1 = obd.commands[obdCommand[index[0]]]
        command2 = obd.commands[obdCommand[index[1]]]
        command3 = obd.commands[obdCommand[index[2]]]
        command4 = obd.commands[obdCommand[index[3]]]
        command5 = obd.commands[obdCommand[index[4]]]
        command6 = obd.commands[obdCommand[index[5]]]

        f = open('obdDescriptions.pckl', 'wb')
        pickle.dump(selection, f)
        f.close()
        window.destroy()
        button.config(state=NORMAL)
        global nwerty
        nwerty = 1

        return


[connection, status] = connectOBD()

app = Tk()
app.title("AccordOBD")
app.geometry('800x480')


master = Canvas(app, width=800, height=480)
master.grid(row=0, column=0)
index = [None]*6
nwerty = 1

backimg = "A:/Projects/obd_cluster/blueback.gif"
filename = PhotoImage(file=backimg)
background = master.create_image(0, 0, image=filename, anchor=NW)

im = "A:/Projects/obd_cluster/dial2.gif"
photo = PhotoImage(file=im)
radar1 = master.create_image(35, 60, image=photo, anchor=NW)
radar2 = master.create_image(310, 60, image=photo, anchor=NW)
radar3 = master.create_image(560, 60, image=photo, anchor=NW)

radar4 = master.create_image(35, 300, image=photo, anchor=NW)
radar5 = master.create_image(310, 300, image=photo, anchor=NW)
radar6 = master.create_image(560, 300, image=photo, anchor=NW)


f = open('A:/Projects/obd_cluster/obdDescriptions.pckl', 'rb')
labels = pickle.load(f)
f.close()

index[0] = obdCommandDescription.index(labels[0])
index[1] = obdCommandDescription.index(labels[1])
index[2] = obdCommandDescription.index(labels[2])
index[3] = obdCommandDescription.index(labels[3])
index[4] = obdCommandDescription.index(labels[4])
index[5] = obdCommandDescription.index(labels[5])

print(index)

TextFont = 'Arial 12'
MainFont = 'MSSansSerif 35 bold'
IncFont = 'Arial 12'  # numbers
MainColor = 'gray75'

label_1 = master.create_text(
    140, 210, text=labels[0], fill='White', font=TextFont)
value_1 = 0
value1_MAIN = master.create_text(
    140, 150, text=value_1, fill=MainColor, font=MainFont)
minVal_1 = master.create_text(
    50, 180, text=minVal[index[0]], fill=MainColor, font=IncFont)
maxVal_1 = master.create_text(
    232, 180, text=maxVal[index[0]], fill=MainColor, font=IncFont)
inc1_1 = master.create_text(
    50, 80, text=Increment1[index[0]], fill=MainColor, font=IncFont)
inc1_2 = master.create_text(
    140, 50, text=Increment2[index[0]], fill=MainColor, font=IncFont)
inc1_3 = master.create_text(
    232, 80, text=Increment3[index[0]], fill=MainColor, font=IncFont)
arc_1 = master.create_arc(60, 85, 215, 245, outline=MainColor,
                          style=ARC, start=180, extent=-135, width=20)

label_2 = master.create_text(
    420, 210, text=labels[1], fill='White', font=TextFont)
value_2 = 0
value2_MAIN = master.create_text(
    420, 150, text=value_2, fill=MainColor, font=MainFont)
minVal_2 = master.create_text(
    335, 180, text=minVal[index[1]], fill=MainColor, font=IncFont)
maxVal_2 = master.create_text(
    500, 180, text=maxVal[index[1]], fill=MainColor, font=IncFont)
inc2_1 = master.create_text(
    335, 80, text=Increment1[index[1]], fill=MainColor, font=IncFont)
inc2_2 = master.create_text(
    410, 50, text=Increment2[index[1]], fill=MainColor, font=IncFont)
inc2_3 = master.create_text(
    490, 80, text=Increment3[index[1]], fill=MainColor, font=IncFont)
arc_2 = master.create_arc(335, 85, 490, 245, outline=MainColor,
                          style=ARC, start=180, extent=-180, width=20)


label_3 = master.create_text(
    670, 210, text=labels[2], fill='White', font=TextFont)
value_3 = 0
value3_MAIN = master.create_text(
    670, 150, text=value_3, fill=MainColor, font=MainFont)
minVal_3 = master.create_text(
    587, 180, text=minVal[index[2]], fill=MainColor, font=IncFont)
maxVal_3 = master.create_text(
    750, 180, text=maxVal[index[2]], fill=MainColor, font=IncFont)
inc3_1 = master.create_text(
    580, 80, text=Increment1[index[2]], fill=MainColor, font=IncFont)
inc3_2 = master.create_text(
    660, 50, text=Increment2[index[2]], fill=MainColor, font=IncFont)
inc3_3 = master.create_text(
    750, 80, text=Increment3[index[2]], fill=MainColor, font=IncFont)
arc_3 = master.create_arc(587, 85, 740, 245, outline=MainColor,
                          style=ARC, start=180, extent=-180, width=20)


label_4 = master.create_text(
    140, 450, text=labels[3], fill='White', font=TextFont)
value_4 = 0
value4_MAIN = master.create_text(
    140, 390, text=value_4, fill=MainColor, font=MainFont)
minVal_4 = master.create_text(
    50, 420, text=minVal[index[3]], fill=MainColor, font=IncFont)
maxVal_4 = master.create_text(
    232, 420, text=maxVal[index[3]], fill=MainColor, font=IncFont)
inc4_1 = master.create_text(
    50, 320, text=Increment1[index[3]], fill=MainColor, font=IncFont)
inc4_2 = master.create_text(
    140, 290, text=Increment2[index[3]], fill=MainColor, font=IncFont)
inc4_3 = master.create_text(
    232, 320, text=Increment3[index[3]], fill=MainColor, font=IncFont)
arc_4 = master.create_arc(60, 327, 215, 483, outline=MainColor, style=ARC,
                          start=180, extent=-180, width=20)


label_5 = master.create_text(
    420, 450, text=labels[4], fill='White', font=TextFont)
value_5 = 0
value5_MAIN = master.create_text(
    420, 390, text=value_5, fill=MainColor, font=MainFont)
minVal_5 = master.create_text(
    335, 420, text=minVal[index[4]], fill=MainColor, font=IncFont)
maxVal_5 = master.create_text(
    500, 420, text=maxVal[index[4]], fill=MainColor, font=IncFont)
inc5_1 = master.create_text(
    335, 320, text=Increment1[index[4]], fill=MainColor, font=IncFont)
inc5_2 = master.create_text(
    410, 290, text=Increment2[index[4]], fill=MainColor, font=IncFont)
inc5_3 = master.create_text(
    490, 320, text=Increment3[index[4]], fill=MainColor, font=IncFont)
arc_5 = master.create_arc(335, 327, 490, 483, outline=MainColor, style=ARC,
                          start=180, extent=-180, width=20)

label_6 = master.create_text(
    670, 450, text=labels[5], fill='White', font=TextFont)
value_6 = 0
value6_MAIN = master.create_text(
    670, 390, text=value_6, fill=MainColor, font=MainFont)
minVal_6 = master.create_text(
    587, 420, text=minVal[index[5]], fill=MainColor, font=IncFont)
maxVal_6 = master.create_text(
    750, 420, text=maxVal[index[5]], fill=MainColor, font=IncFont)
inc6_1 = master.create_text(
    580, 320, text=Increment1[index[5]], fill=MainColor, font=IncFont)
inc6_2 = master.create_text(
    660, 290, text=Increment2[index[5]], fill=MainColor, font=IncFont)
inc6_3 = master.create_text(
    750, 320, text=Increment3[index[5]], fill=MainColor, font=IncFont)
arc_6 = master.create_arc(587, 327, 740, 483, outline=MainColor, style=ARC,
                          start=180, extent=-180, width=20)

selectButton = Button(master, text='Commands', background='Black',
                      anchor=CENTER, command=lambda: selectCommands(app, selectButton, connection))
selectButton.config(width=10, relief=FLAT)
button1_window = master.create_window(10, 10, anchor=NW, window=selectButton)


sendCommand(connection, status, master, arc_1, arc_2, arc_3, arc_4, arc_5, arc_6,
            value1_MAIN, value2_MAIN, value3_MAIN, value4_MAIN, value5_MAIN, value6_MAIN, index,
            maxVal, minVal, selectButton)


app.mainloop()

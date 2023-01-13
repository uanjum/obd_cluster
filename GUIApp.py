from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pickle
from FunctionsDescription import *
from OBDConnection import OBDConnection

class GUIApp:

    def __init__(self):
        self.app = Tk()


    def build_gui(self):
        self.app.title("OBD Cluster")
        self.app.geometry('800x480')

        y_top_margin = 40
        x_pad = 20
        x_inc = 800/3
        y_inc = 480/2

        self.master = Canvas(self.app, width=800, height=480)
        self.master.grid(row=0, column=0)

        index = [None]*6
        #self.background_img = PhotoImage(file="/Users/MB/SoftwareMEng/projects/obd_cluster/blueback.gif")
        self.background_img = PhotoImage(file="blueback.gif")

        self.dial_img = PhotoImage(file="dial2.gif")

        self.master.create_image(0, 0, image=self.background_img, anchor=NW)

        self.master.create_image(140, 200, image=self.dial_img, anchor=S)
        self.master.create_image(400, 200, image=self.dial_img, anchor=S)
        self.master.create_image(660, 200, image=self.dial_img, anchor=S)

        self.master.create_image(140, 400, image=self.dial_img, anchor=S)
        self.master.create_image(400, 400, image=self.dial_img, anchor=S)
        self.master.create_image(660, 400, image=self.dial_img, anchor=S)

        f = open('obdDescriptions.pckl', 'rb')
        self.labels = pickle.load(f)
        f.close()
        print(self.labels)

        index = []

        for i in range(0,6):
            index.append(obdCommandDescription.index(self.labels[i]))

        TextFont = 'Arial 12'
        MainFont = 'MSSansSerif 35 bold'
        IncFont = 'Arial 12'  # numbers
        MainColor = 'gray75'

        self.value_list = []
        self.arc_list = []

        counter = 0
        for j in range(0,2):
            for i in range(0,3):
                self.master.create_text(140+i*260, 260+j*200, text = self.labels[counter], fill = 'White', font = TextFont, anchor=S)
                self.value_list.append(self.master.create_text(140+i*260, 200+j*200, text = 0, fill = 'White', font = MainFont, anchor=S))
                self.master.create_text(40+i*260, 230+j*200, text=minVal[obdCommandDescription.index(self.labels[counter])], fill=MainColor, font=IncFont, anchor=S)
                self.master.create_text(230+i*260, 230+j*200, text=maxVal[obdCommandDescription.index(self.labels[counter])], fill=MainColor, font=IncFont, anchor=S)
                self.master.create_text(50+i*260, 120+j*200, text=Increment1[obdCommandDescription.index(self.labels[counter])], fill=MainColor, font=IncFont, anchor=S)
                self.master.create_text(140+i*260, 90+j*200, text=Increment2[obdCommandDescription.index(self.labels[counter])], fill=MainColor, font=IncFont, anchor=S)
                self.master.create_text(220+i*260, 120+j*200, text=Increment3[obdCommandDescription.index(self.labels[counter])], fill=MainColor, font=IncFont, anchor=S)
                self.arc_list.append(self.master.create_arc(55+i*260, 113+j*200, 220+i*260, 280+j*200, outline=MainColor, style=ARC, start=180, extent=-180, width=20))
                counter +=1
        
        self.select_button = Button(self.app, text='Commands', anchor=CENTER, command = self.select_commands, borderwidth=0, pady=0)
        #selectButton.config(width=10, relief=FLAT)
        self.select_button.place(x = 10, y = 10)
        print("Finished building GUI")



    

    def select_commands(self):
        self.select_button.config(state = DISABLED)
        print("Hello")
        self.select_window = Toplevel(self.app)
        self.select_window.geometry('700x380')

        self.combo_boxes = []
        counter_box = 0
        for i in range(0,2):
            for j in range(0,3):
                self.combo_boxes.append(ttk.Combobox(self.select_window, state = 'readonly'))
                self.combo_boxes[counter_box]['values'] = obdCommandDescription
                self.combo_boxes[counter_box].grid(row = i, column = j, padx = 10, pady = 10)
                self.combo_boxes[counter_box].current(obdCommandDescription.index(self.labels[counter_box]))
                counter_box += 1
        
        saveButton = Button(self.select_window, text = 'Save', command = self.save_new_commands)
        saveButton.place(x = 100, y = 100)
    
    def save_new_commands(self):
        new_selection = []
        for combo_box in self.combo_boxes:
            new_selection.append(combo_box.get())
        f = open('obdDescriptions.pckl', 'wb')  
        pickle.dump(new_selection, f)
        f.close()
        self.select_window.destroy()   
        self.build_gui()


    def update_values(self):
        if (str(self.select_button['state']) == "normal"):
            for i in range(0,6):
                list_index = obdCommandDescription.index(self.labels[i])
                res = self.connection.send_command(obdCommand[list_index])
                if res.value != None:
                    arc_degree = -(((res.value.magnitude-minVal[list_index]) / (maxVal[list_index]-minVal[list_index])*180))
                    raw_val = int(res.value.magnitude)
                else:
                    arc_degree = 0
                    raw_val = "N/S"

                self.master.itemconfig(self.arc_list[i], extent = arc_degree)
                self.master.itemconfig(self.value_list[i], text = raw_val)
        
        self.master.after(5000, self.update_values)



    def run_app(self):
        print("Setting up Connection")
        self.connection = OBDConnection()
        print(self.connection.look_for_connections())

        self.connection.connect_to_port(1)

        if self.connection.check_connection_status():
            self.update_values()

        self.app.mainloop()
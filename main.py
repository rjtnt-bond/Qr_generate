
# Name: Rezwanul Islam Bondhon
# Email: bondhonbondhon342@gmail.com
# Begum rokeya univarsity Rangpur

from tkinter import *
import  tkinter as tk
from tkinter import messagebox,Toplevel
import pyqrcode
import png
import speech_recognition as sr
import os
import pyttsx3
import time
import pyautogui
import  datetime
from  pynput.keyboard import  Controller as key_controller
#Scan Module list Here

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import winsound

pyautogui.FAILSAFE = False
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

voice =sr.Recognizer()
kebroad=key_controller()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('good morning boss ')

    if hour > 12 and hour < 18:
        speak('good afternoon boss')

    elif hour > 18 and hour <= 24:
        speak('good evening boss')

    speak('i am alexa your artificial assistant. how can i help you ')

#Tkinter start


# # function work
# def S_scan():
#     cap = cv2.VideoCapture(0)
#     font = cv2.FONT_HERSHEY_DUPLEX
#     with open('record.txt') as f:
#         myDataList = f.read().splitlines()
#         # print(myDataList)
#
#     named_tuple = time.localtime()  # get struct_time
#     time_string = time.strftime(" %m/%d/%Y, %H:%M:%S ", named_tuple)
#     # print(time_string)
#     while True:
#         # time.sleep(1)
#         _, frame = cap.read()
#         decodeObj = pyzbar.decode(frame)
#         for obj in decodeObj:
#             print(" ", obj.data)
#             myData = obj.data.decode('utf-8')
#             print(myData)
#
#             if myData in myDataList:
#                 pts = np.array([obj.polygon], np.int32)
#                 pts = pts.reshape((-1, 1, 2))
#                 cv2.polylines(frame, [pts], True, (255, 0, 255), 3)
#                 pts2 = obj.rect
#                 cv2.putText(frame, str('Entry'), (pts2[0], pts2[1]), font, 0.9,
#                             (255, 0, 0), 2)
#                 cv2.putText(frame, str('Welcome Our world'), (150, 350), font, 0.9,
#                             (255, 0, 0), 2)
#             else:
#                 pts = np.array([obj.polygon], np.int32)
#                 pts = pts.reshape((-1, 1, 2))
#                 cv2.polylines(frame, [pts], True, (255, 0, 255), 3)
#                 pts2 = obj.rect
#                 cv2.putText(frame, str('No entry'), (pts2[0], pts2[1]), font, 0.6,
#                             (0, 0, 255), 2)
#
#                 cv2.putText(frame, str('Sorry,Unknown Person'), (50, 350), font, 0.9,
#                             (0, 0, 255), 2)
#                 winsound.Beep(500, 400)
#
#         cv2.imshow("security scanner", frame)
#         key = cv2.waitKey(1)
#         if key == 27:
#             break
#
# def written():
#     with sr.Microphone() as sourch:
#         data =  voice.listen(sourch)
#         data_final=voice.recognize_google(data)
#         print(data_final)
#         for x in data_final:
#             kebroad.type(x)
#
# def Make_Qr():
#     # wishme()
#     Qr_Name = Qr_Name_Entry.get()
#     # query2 = takecommand().lower()
#     # Qr_Id=Qr_Id_Entry.insert((END,query2))
#     Qr_Id = Qr_Id_Entry.get()
#
#     Qr_Message = Qr_Message_Entry.get()
#     Data = 'Name: ' + Qr_Name + ' Id: ' + Qr_Id + '  Message: ' + 'Qr_Message'
#     named_tuple = time.localtime()  # get struct_time
#     time_string = time.strftime(" %m/%d/%Y, %H:%M:%S ", named_tuple)
#
#     print(time_string)
#
#     # write our data in txt file also save date and time
#     with open('record.txt', 'a') as f:
#         f.write(
#             f'{Data}'  +  f' Data entry time: {time_string}'+'\n')
#     # Empty data Qr code
#     if Data==' ':
#             res=messagebox.askyesno('Notification','Are you create empty QR?')
#             if (res==True):
#                     Qr_code = pyqrcode.create(Data)
#                     path=r'C:\Users\Lenovo\Desktop\qrfile' #Desktop file must creat it in your deasktop
#                     save_path='{}\{}{}.png'.format(path,Qr_Id,Qr_Name)
#                     list_dir=os.listdir(path)
#                     if('{}{}.png'.format(Qr_Id,Qr_Name) in list_dir):
#                             messagebox.showinfo('Notification','Sorry,This Name and Id are repeat!')
#
#                     else:
#                         Qr_code.png(save_path, scale=8)  # if you change qr color use color module(rgb)
#                         notification_ms = 'Save as: ' + Qr_Id + Qr_Name + '.png'
#                         Qr_Notification_Message_label.configure(text=notification_ms)
#                         result = messagebox.askyesno('Notification', 'Qr File is generate now click Yes Button')
#                         if (result == True):
#                             top = Toplevel()
#                             top.geometry('400x400')
#                             top.configure(bg='white')
#                             top.wm_iconbitmap('qr2.ico')
#                             img = PhotoImage(file=save_path)
#                             lebel = Label(top, image=img, bg='white')
#                             lebel.place(x=10, y=10)
#                             top.mainloop()
#             else:
#                 pass
#     # Qr_data file start
#     else:
#                Qr_code = pyqrcode.create(Data)
#                path = r'F:\qr.scen\qr_file'
#                save_path = '{}\{}{}.png'.format(path, Qr_Id, Qr_Name)
#                list_dir = os.listdir(path)
#                if ('{}{}.png'.format(Qr_Id, Qr_Name) in list_dir):
#                    messagebox.showinfo('Notification', 'Sorry,This Name and Id are repeat!')
#
#                else:
#                   Qr_code.png(save_path, scale=8) #if you change qr color use color module(rgb)
#                   notification_ms='Save as: '+Qr_Id+Qr_Name+ '.png'
#                   Qr_Notification_Message_label.configure(text=notification_ms)
#                   result = messagebox.askyesno('Notification','Qr File is generate now click Yes Button')
#                   if(result==True):
#                       top = Toplevel()
#                       top.geometry('400x400')
#                       top.configure(bg='white')
#                       top.wm_iconbitmap('qr1.ico')
#                       img=PhotoImage(file=save_path)
#                       lebel = Label(top, image=img,bg='white')
#                       lebel.place(x=10,y=10)
#                       top.mainloop()




# Label area
class Mainwindow:
     def __init__(self,master):
         self.master = master
         master.geometry('580x460')
         master.maxsize(580, 460)
         master.minsize(580, 460)
         font = ('times', 12, 'italic bold')
         master.title('QR_Generator')
         master.configure(bg='grey')
         master.wm_iconbitmap('qr1.ico')

         # self.frame=tk.Frame(self.master,width=580,hegiht=300)
         # self.frame.title('QR_Generator')
         # self.frame.configure(bg='grey')

         #
         # self.frame.pack()
         def Quit_root(self):
             res = messagebox.askokcancel('Notification', 'Are you want to Exit Qr_Generator?')
             if (res == True):
                 self.root.destroy()
             else:
                 pass
         self.Qr_Id_label = Label(self.master, text="Enter Your Id:", bg="powder blue", fg='black', width=15, height=2,
                            font=('times', 12, 'italic bold'))
         self.Qr_Id_label.place(x=10, y=20)

         self.Qr_Name_label = Label(self.master, text="Enter Your Name:", bg="powder blue", fg='black', width=15, height=2,
                              font=('times', 12, 'italic bold'))
         self.Qr_Name_label.place(x=10, y=80)

         self.Qr_Message_label = Label(self.master, text="Enter Qr Message:", bg="powder blue", fg='black', width=15, height=2,
                                  font=('times', 12, 'italic bold'))
         self.Qr_Message_label.place(x=10, y=140)

         self.Qr_Notification_label = Label(self.master, text="Notification:", bg="powder blue", fg='black', width=10, height=2,
                                      font=('times', 15, 'bold underline'))
         self.Qr_Notification_label.place(x=10, y=400)

         self.Qr_Notification_Message_label = Label(self.master, text="", bg="powder blue", fg='black', width=30, height=2,
                                              font=('times', 15, 'bold'))
         self.Qr_Notification_Message_label.place(x=200, y=400)

        # Entry box area start

         self.Qr_Id_Entry = tk.Entry(self.master,width=30, bg='Beige',relief=SOLID, bd=1, font=('Arial', 15, 'bold'))
         self.Qr_Id_Entry.place(x=230, y=20)

         self.Qr_Name_Entry = tk.Entry(self.master, width=30, bg='Beige',relief=SOLID, bd=1, font=('Arial', 15, ' bold'))
         self.Qr_Name_Entry.place(x=230, y=80)

         self.Qr_Message_Entry = tk.Entry(self.master, width=30, bg='Beige',relief=SOLID, bd=1, font=('Arial', 15, ' bold'))
         self.Qr_Message_Entry.place(x=230, y=140)


         self.Make_Qr_image = tk.Button(self.master, text='Generate', width=15, font=('times', 11, 'bold'), bd=10,
                               bg='tan')
         self.Make_Qr_image.place(x=10, y=250)

         self.Clear_Button = Button(self.master, text='Clear', width=15,font=('times', 11, 'bold'), bd=10,
                              bg='tan')
         self.Clear_Button.place(x=210, y=250)
         self.Clear_Button.bind('<Button-1>', Quit_root)##it's not working if we select button from my keybord.Function Quit_root not working.

         self.Quit_Button = tk.Button(self.master, text='Exit', width=15, font=('times', 11, 'bold'), bd=10,
                             bg='tan')
         self.Quit_Button.place(x=410, y=250)


         self.S_Scan_Button = Button(self.master, text='S_scan', width=15,font=('times', 11, 'bold'), bd=10,
                             bg='olive')
         self.S_Scan_Button.place(x=210, y=320)

         self.speak_Button = Button(self.master, text='S_scan', width=5,font=('times', 7, 'bold'), bd=10,
                             bg='olive')
         self.speak_Button.place(x=100, y=320)

         # self.bindings()

         # self.Clear()
         # self.Quit_root()

     def Clear(self):
         cl = messagebox.askokcancel('Notification', 'Are you want to Clear?')
         if (cl == True):
             self.Qr_Id_Entry.delete(0, 'end')
             self.Qr_Name_Entry.delete(0, 'end')
             self.Qr_Message_Entry.delete(0, 'end')
             self.Qr_Notification_Message_label.config(text='')



     def Quit_root(self):
        res = messagebox.askokcancel('Notification', 'Are you want to Exit Qr_Generator?')
        if (res == True):
            self.root.destroy()
        else:
               pass
     # def bindin/gs(self):
     #     self.Clear_Button.bind('<Enter>', lambda event:self.Clear(self.Clear_Button))


# Buttons hover Effect && Functions but this area  is not  working my project it's optional
# def Make_Qr_imageEnter(e):
#     Make_Qr_image["bg"] = 'purple2'
#
# def Make_Qr_imageLeave(e):
#     Make_Qr_image['bg'] = 'powder blue'
#
# def Clear_ButtonEnter(e):
#     Clear_Button['bg'] = 'purple2'
#
# def Clear_ButtonLeave(e):
#     Clear_Button['bg'] = 'powder blue'
#
# def Quit_ButtonEnter(e):
#     Quit_Button['bg'] = 'purple2'
#
# def Quit_ButtonLeave(e):
#     Quit_Button['bg'] = 'powder blue'



# Make_Qr_image.bind = ('<Enter>', Make_Qr_imageEnter)
# Make_Qr_image.bind = ('<Leave>', Make_Qr_imageLeave)
#
# Clear_Button.bind = ('< Enter >', Clear_ButtonEnter)
# Clear_Button.bind = ('< Leave >', Clear_ButtonLeave)
#
# Quit_Button.bind = ('< Enter >', Quit_ButtonEnter)
# Quit_Button.bind = ('< Leave >', Quit_ButtonLeave)

root=tk.Tk()
window=Mainwindow(root)
root.mainloop()
# if __name__ == '__main__':
#     written()

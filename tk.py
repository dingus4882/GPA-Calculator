import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('GPA Calculator')
win.geometry('900x750+0+0')

#--------------Labels and Textboxes------------
trans_lbl = ttk.Label(win, text='Transcript GPA') #lbl
trans_lbl.pack()

trans_textbox = ttk.Entry(win) #txt
trans_textbox.pack()

core_lbl = ttk.Label(win, text='Core GPA') #lbl
core_lbl.pack()

core_textbox = ttk.Entry(win)#txt
core_textbox.pack()

cur_lbl = ttk.Label(win, text='Current GPA') #lbl
cur_lbl.pack()

cur_textbox = ttk.entry(win)
cur_textbox.pack()

cur_cor_lbl = ttk.Label(win, text='Current Core GPA') #lbl
cur_cor_lbl.pack()

cur_cor_textbox = ttk.entry(win)
cur_cor_textbox.pack()

predict_lbl = ttk.Label(win, text='Predicted GPA') #lbl
predict_lbl.pack()

predict_textbox = ttk.entry(win)


predict_cor_lbl = ttk.Label(win, text='Predicted Core GPA') #lbl
predict_cor_lbl.pack()
#-------------Input--------------



global trans_gpa
global core_gpa
global cur_gpa
global cur_cor_gpa
global predicted_gpa
global predicted_cor_gpa
classes = []
trans_gpa = 0.0
core_gpa = 0.0
cur_gpa = 0.0
cur_cor_gpa = 0.0
predicted_gpa = 0.0
predicted_cor_gpa = 0.0



def display_gpa():
  print("Transcript GPA: " + str(trans_gpa))
  print("Core GPA: " + str(core_gpa))
  print("Current GPA: " + str(cur_gpa))
  print("Current core GPA: " + str(cur_cor_gpa))
  print("Predicted GPA: " + str(predicted_gpa))
  options()

def gpa_data():
  global trans_gpa
  global core_gpa
  global cur_gpa
  global cur_cor_gpa
  global predicted_gpa
  global predicted_cor_gpa
  cur_gpa = 0.0
  print("Enter your transcript GPA:")
  trans_gpa = float(input(""))
  print("Enter your core GPA:")
  core_gpa = float(input(""))
  if cur_gpa != 0.0:
    print("N/A")
  else:
    print("Enter your current GPA:")
    cur_gpa = float(input(""))
  print("Enter your current core GPA:")
  cur_cor_gpa = float(input(""))
  print("Data added successfully!")
  options()

def calc_cur_gpa():
  my_sum = 0.0
  print("Enter number of courses")
  num_classes = int(input(""))
  print("Note: Enter core classes FIRST")
  for i in range(num_classes):
    print("GPA for class " + str(i+1) + ":")
    class_gpa = float(input(""))
    classes.append(class_gpa)
  for gpa in classes:
    my_sum = my_sum + gpa
  cur_gpa = my_sum/num_classes
  print("Current GPA: " + str(cur_gpa))
  cur_cor_gpa = (classes[0]+classes[1]+classes[2]+classes[3])/4
  print("Core GPA: " + str(cur_cor_gpa))
  options()

def gpa_prediction():
  print("Have you entered your GPA data?")
  print("1) Yes")
  print("2) No")
  choice = int(input(""))
  if choice == 1:
    predicted_gpa = (trans_gpa + cur_gpa)/2
    print("Predicted GPA: " + str(predicted_gpa))
    predicted_cor_gpa = (core_gpa + cur_cor_gpa)/2
    print("Predicted Core GPA: " + str(predicted_cor_gpa))
  elif choice == 2:
    gpa_data()
  options()

def options():
  print("Select One")
  print("1) Enter GPA data")
  print("2) Calculate current GPA")
  print("3) Predict GPA")
  print("4) Display GPA Data")
  option = int(input(""))
  if option == 1:
    gpa_data()
  elif option == 2:
    calc_cur_gpa()
  elif option == 3:
    gpa_prediction()
  elif option == 4:
    display_gpa()


    #------------Button--------------
submit_btn = ttk.Button(win, text='Submit',command=lambda:print("hai"))
submit_btn.pack()


#options()
#https://www.pythontutorial.net/tkinter/tkinter-label/
win.mainloop()
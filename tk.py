import tkinter as tk
from tkinter import ttk
#from win_one import display_win

#-------------GPA Functions--------------
global trans_gpa
global core_gpa
global cur_gpa
global cur_cor_gpa
global predicted_gpa
global predicted_cor_gpa
classes = []
"""trans_gpa = tk.StringVar()
core_gpa = tk.StringVar()
cur_gpa = tk.StringVar()
cur_cor_gpa = tk.StringVar()
predicted_gpa = tk.StringVar()
predicted_cor_gpa = tk.StringVar()
"""

def display_gpa():
  lbl1 = ttk.Label(dis_win, 'Transcript GPA' + str(trans_gpa))
  lbl1.pack()
  print("Transcript GPA: " + str(trans_gpa))
  print("Core GPA: " + str(core_gpa))
  print("Current GPA: " + str(cur_gpa))
  print("Current core GPA: " + str(cur_cor_gpa))
  print("Predicted GPA: " + str(predicted_gpa))

  """
def gpa_data():
  global trans_gpa
  global core_gpa
  global cur_gpa
  global cur_cor_gpa
  global predicted_gpa
  global predicted_cor_gpa
  cur_gpa = cur_textbox.get()
  trans_gpa = trans_textbox.get()
  core_gpa = core_textbox.get()
  cur_gpa = cur_textbox.get()
  cur_cor_gpa = cur_cor_textbox.get()
  #print("Data added successfully!")
"""

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


#--------------------Display Window--------------------------
def display_win():
  
  #gpa_data()
  dis_win = tk.Tk()
  dis_win.title('Display GPA')
  dis_win.geometry('900x750+0+0')
  
  #-------------GPA Labels-------------

  lbl1 = ttk.Label(dis_win, text='Transcript GPA: ' + trans_gpa.get())
  lbl1.pack()
  
  lbl2 = ttk.Label(dis_win, text='Core GPA: ' + core_gpa.get())
  lbl2.pack()

  lbl3 = ttk.Label(dis_win, text='Current GPA: ' + cur_gpa.get())
  lbl3.pack()

  lbl4 = ttk.Label(dis_win, text='Current Core GPA: ' + cur_cor_gpa.get())
  lbl4.pack()

  lbl5 = ttk.Label(dis_win, text='Predicted GPA: ' + predicted_gpa.get())
  lbl5.pack()

  lbl6 = ttk.Label(dis_win, text='Predicted Core GPA: ' + predicted_cor_gpa.get())
  lbl6.pack()

  main_btn = ttk.Button(dis_win, text='Main Menu', command=main_win)
  main_btn.pack()

  dis_win.mainloop()
#------------------Function Merge-----------------
def display():
  display_win()

#------------------Input Window--------------------
def input_win():
  global trans_gpa
  global core_gpa
  global cur_gpa
  global cur_cor_gpa
  global predicted_gpa
  global predicted_cor_gpa
  win = tk.Tk()
  win.title('GPA Input')
  win.geometry('900x750+0+0')

  trans_gpa = tk.StringVar()
  core_gpa = tk.StringVar()
  cur_gpa = tk.StringVar()
  cur_cor_gpa = tk.StringVar()
  predicted_gpa = tk.StringVar()
  predicted_cor_gpa = tk.StringVar()

  trans_lbl = ttk.Label(win, text='Transcript GPA') #lbl
  trans_lbl.pack()

  trans_textbox = ttk.Entry(win, textvariable = trans_gpa) #txt
  trans_textbox.pack()

  core_lbl = ttk.Label(win, text='Core GPA') #lbl
  core_lbl.pack()

  core_textbox = ttk.Entry(win, textvariable = core_gpa)#txt
  core_textbox.pack()

  cur_lbl = ttk.Label(win, text='Current GPA') #lbl
  cur_lbl.pack()

  cur_textbox = ttk.Entry(win, textvariable = cur_gpa)
  cur_textbox.pack()

  cur_cor_lbl = ttk.Label(win, text='Current Core GPA') #lbl
  cur_cor_lbl.pack()

  cur_cor_textbox = ttk.Entry(win, textvariable = cur_cor_gpa)
  cur_cor_textbox.pack()

  predict_lbl = ttk.Label(win, text='Predicted GPA') #lbl
  predict_lbl.pack()

  predict_textbox = ttk.Entry(win, textvariable = predicted_gpa)
  predict_textbox.pack()

  predict_cor_lbl = ttk.Label(win, text='Predicted Core GPA') #lbl
  predict_cor_lbl.pack()

  predict_cor_txtbox = ttk.Entry(win, textvariable = predicted_cor_gpa)
  predict_cor_txtbox.pack()

  #submit_btn = ttk.Button(win, text='Submit', command=gpa_data)
  #submit_btn.pack()

  continue_btn = ttk.Button(win, text='Continue', command=display_win)
  continue_btn.pack()

  main_btn = ttk.Button(win, text='Main Menu', command=main_win)
  main_btn.pack()

  win.mainloop()


def main_win():
  main = tk.Tk()
  main.title('GPA Calculator')
  main.geometry('900x750+0+0')

  #-------------Buttons-------------
  input_btn = ttk.Button(main, text='Input GPA Data', command=input_win)
  input_btn.pack(side=tk.TOP)

  display_btn = ttk.Button(main, text='Display GPA Data', command=display_win)
  display_btn.pack()

  main.mainloop()
  

#input_win()
main_win()


#options()
#https://www.pythontutorial.net/tkinter/tkinter-label/
import tkinter as tk
from tkinter import ttk
#from win_one import display_win
win = tk.Tk()
win.title('GPA Calculator')
win.geometry('900x750+0+0')
#-------------GPA Functions--------------
global trans_gpa
global core_gpa
global cur_gpa
global cur_cor_gpa
global predicted_gpa
global predicted_cor_gpa
global mainF

global classes
global GPA_sum
global num_classes

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

#---------------------Predict Frame--------------------------
def predict_win():
    predF = tk.Frame(win, bg='green')
    predF.place(relwidth=1, relheight=1)

#---------------------Calculate Frame-----------------------

def calculate_win():
    global classes
    global GPA_sum
    global num_classes

    classes=[]
    GPA_sum = tk.StringVar()
    num_classes = tk.StringVar()


    calcF = tk.Frame(win, bg='green')
    calcF.place(relwidth=1, relheight=1)
    calcF.columnconfigure(0, weight=1)
    calcF.rowconfigure(0, weight=1)
    calcF.rowconfigure(1, weight=1)
    calcF.rowconfigure(2, weight=1)



    frameL = ttk.Label(win, text='Enter Number of Classes')
    frameL.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

    txt1 = ttk.Entry(win, textvariable=num_classes)
    txt1.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

    cont_btn = ttk.Button(win, text='Continue', command=display)
    cont_btn.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)



#--------------------Display Window--------------------------
def display_win():
  
  #gpa_data()
  disF = tk.Frame(win, bg='gray')
  disF.columnconfigure(0, weight=1)
  disF.columnconfigure(1, weight=1)
  disF.rowconfigure(0, weight=1)
  disF.rowconfigure(1, weight=1)
  disF.rowconfigure(2, weight=1)
  disF.rowconfigure(3, weight=1)
  disF.rowconfigure(4, weight=1)
  disF.rowconfigure(5, weight=1)
  disF.rowconfigure(6, weight=1)
  disF.place(relwidth=1, relheight=1)
  
  disF.tkraise()
  
  #-------------GPA Labels-------------

  lbl1 = ttk.Label(win, text='Transcript GPA: ' + trans_gpa.get())
  lbl1.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)
  
  lbl2 = ttk.Label(win, text='Core GPA: ' + core_gpa.get())
  lbl2.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

  lbl3 = ttk.Label(win, text='Current GPA: ' + cur_gpa.get())
  lbl3.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)

  lbl4 = ttk.Label(win, text='Current Core GPA: ' + cur_cor_gpa.get())
  lbl4.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5)

  lbl5 = ttk.Label(win, text='Predicted GPA: ' + predicted_gpa.get())
  lbl5.grid(column=0, row=4, sticky=tk.EW, padx=5, pady=5)

  lbl6 = ttk.Label(win, text='Predicted Core GPA: ' + predicted_cor_gpa.get())
  lbl6.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=5)

  main_btn = ttk.Button(win, text='Main Menu', command=main_win)
  main_btn.grid(column=0, row=6, sticky=tk.EW, padx=5, pady=5)

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

  trans_gpa = tk.StringVar()
  core_gpa = tk.StringVar()
  cur_gpa = tk.StringVar()
  cur_cor_gpa = tk.StringVar()
  predicted_gpa = tk.StringVar()
  predicted_cor_gpa = tk.StringVar()

  inputF = tk.Frame(win, bg='gray')
  inputF.columnconfigure(0, weight=1)
  inputF.columnconfigure(1, weight=1)
  inputF.columnconfigure(2, weight=1)
  inputF.rowconfigure(0, weight=1)
  inputF.rowconfigure(1, weight=1)
  inputF.rowconfigure(2, weight=1)
  inputF.rowconfigure(3, weight=1)
  inputF.rowconfigure(4, weight=1)
  inputF.rowconfigure(5, weight=1)
  inputF.rowconfigure(6, weight=1)
  inputF.place(relwidth=1, relheight=1)
  
  inputF.tkraise()

  trans_lbl = ttk.Label(win, text='Transcript GPA') #lbl
  trans_lbl.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

  trans_textbox = ttk.Entry(win, textvariable = trans_gpa) #txt
  trans_textbox.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

  core_lbl = ttk.Label(win, text='Core GPA') #lbl
  core_lbl.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

  core_textbox = ttk.Entry(win, textvariable = core_gpa)#txt
  core_textbox.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

  cur_lbl = ttk.Label(win, text='Current GPA') #lbl
  cur_lbl.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)

  cur_textbox = ttk.Entry(win, textvariable = cur_gpa)
  cur_textbox.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

  cur_cor_lbl = ttk.Label(win, text='Current Core GPA') #lbl
  cur_cor_lbl.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5)

  cur_cor_textbox = ttk.Entry(win, textvariable = cur_cor_gpa)
  cur_cor_textbox.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

  predict_lbl = ttk.Label(win, text='Predicted GPA') #lbl
  predict_lbl.grid(column=0, row=4, sticky=tk.EW, padx=5, pady=5)

  predict_textbox = ttk.Entry(win, textvariable = predicted_gpa)
  predict_textbox.grid(column=1, row=4, sticky=tk.EW, padx=5, pady=5)

  predict_cor_lbl = ttk.Label(win, text='Predicted Core GPA') #lbl
  predict_cor_lbl.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=5)

  predict_cor_txtbox = ttk.Entry(win, textvariable = predicted_cor_gpa)
  predict_cor_txtbox.grid(column=1, row=5, sticky=tk.EW, padx=5, pady=5)

  continue_btn = ttk.Button(win, text='Continue', command=display_win)
  continue_btn.grid(column=0, row=6, sticky=tk.EW, padx=5, pady=5)

  main_btn = ttk.Button(win, text='Main Menu', command=main_win)
  main_btn.grid(column=1, row=6, sticky=tk.EW, padx=5, pady=5)

  predict_btn = ttk.Button(win, text='Predict GPA', command=predict_win)
  predict_btn.grid(column=2, row=6, sticky=tk.EW, padx=5, pady=5)




def main_win():
  global mainF
  mainF = tk.Frame(win, bg='gray')
  mainF.columnconfigure(0, weight=5)
  mainF.rowconfigure(0, weight=1)
  mainF.rowconfigure(1, weight=1)
  mainF.rowconfigure(2, weight=1)
  mainF.place(relwidth=1, relheight=1)

  mainF.tkraise()

  #-------------Buttons-------------
  input_btn = ttk.Button(win, text='Input GPA Data', command=input_win)
  input_btn.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

  display_btn = ttk.Button(win, text='Display GPA Data', command=display_win)
  display_btn.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

  calc_btn = ttk.Button(win, text='Calculate Current GPA', command=calculate_win)
  calc_btn.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)


  


  

#input_win()
main_win()
win.mainloop()

#options()
#https://www.pythontutorial.net/tkinter/tkinter-label/


import os
from tkinter import *
from pandastable import Table
from implementation import *
from reader import reader_fun, get_ssuspect, df_faz1

#global df
#df = pandas.DataFrame()

win = Tk()
this_graph = Graph_Abstract()
reader_fun(this_graph)

# برای فریم فاز یک از تابع dffaz1 و برای بقیه فاز ها getsuspect دیتا فریم می دهد
# برای فاز یک رویداد فقط نمایش دیتا فریم فاز یک و برای بقیه رویداد هایthis_graph.Faze2() مثل این استفاده می کنیم

win.title("project")
win.geometry("600x570")
win.configure(bg='#78849E')
win.resizable(False, False)

# filelist = Listbox(bg = 'black', fg = 'white', highlightcolor = 'lime', borderwidth = 2, highlightthickness = 3, selectbackground = 'red')
# filelist.configure(font=("Courier", 9, "bold"))

# def load():
#    path = ask()
#    os.chdir(path)
#    mylist = os.listdir(path)
#    for items in mylist:
#        if items.endswith('.mp3'):
#            i = 0
#            filelist.insert(i, items)
#            i = i + 1

frame = Frame(win)

def change_df1():
    #if faz == 1:
    df = df_faz1(this_graph)
    pt = Table(frame, dataframe=df)
    pt.show()

def change_df2():
    #elif faz == 2:
    this_graph.Faze2()
    df = get_ssuspect(this_graph)
    pt = Table(frame, dataframe=df)
    pt.show()

def change_df3():
    #elif faz == 3:
    this_graph.Faze3()
    df = get_ssuspect(this_graph)
    pt = Table(frame, dataframe=df)
    pt.show()

def change_df4():
    #else:
    this_graph.Faze4()
    df = get_ssuspect(this_graph)
    pt = Table(frame, dataframe=df)
    pt.show()


# btnload = Button(win, width = 3, height = 3, text = "انتخاب مسیر", bg='blue', fg='white', command = load)
btn1 = Button(win, width=3, height=3, text="فاز 1", bg='#51AADF', fg='black', command=change_df1)
btn2 = Button(win, width=3, height=3, text="فاز 2", bg='#62B9CE', fg='black', command=change_df2)
btn3 = Button(win, width=3, height=3, text="فاز 3", bg='#73C8BD', fg='black', command=change_df3)
btn4 = Button(win, width=3, height=3, text="فاز 4", bg='#84D7AC', fg='black', command=change_df4)

# btnload.pack(fill = "x")
# filelist.pack(fill = "x")
btn1.pack(fill="x")
btn2.pack(fill="x")
btn3.pack(fill="x")
btn4.pack(fill="x")
frame.pack()
win.mainloop()
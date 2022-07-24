import tkinter
from tkinter import *
from tkinter import filedialog as fd
import pandas as pd
from tkinter import messagebox
import tkinter.scrolledtext as ScrolledText


# Se instala openpyxl


def callback():
    st.delete("1.0", "end")
    name = fd.askopenfilename()
    strfilename.set(name)
    st.configure(state='normal')
    st.insert(tkinter.INSERT,'1-Proceso1\n')
    st.configure(state='disabled')


def read_excel():
    resultdlg = messagebox.askokcancel("Confirm", "Esta seguro de ejecutar el proceso?")

    print(resultdlg)
    if resultdlg:
        df = pd.read_excel(strfilename.get(), sheet_name='Hoja1')
        json_excel = df.to_json(orient='records')
        # print( json_excel )
        print(df.describe())


def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


root = Tk()
root.title("Legalización masiva de bonos")
root.attributes('-toolwindow', True)
# Log

# Add text widget to display logging info
st = ScrolledText.ScrolledText(root)
st.configure(font='TkFixedFont')
st.grid(column=0, row=2,  columnspan=4)


# set the configuration of GUI window
# root.geometry("700x300")
center_window(700, 430)
# root.eval('tk::PlaceWindow . center')
errmsg = 'Error!'

filename = Label(root, text="Archivo: ")
filename.grid(row=1, column=0)

strfilename = StringVar()
filename_field = Entry(root, textvariable=strfilename)

filename_field.grid(row=1, column=1, padx=5, pady=10, ipadx=130)

btn = Button(root, text="Cargar archivo...", command=callback, width=15)
btn.grid(row=1, column=2)

btn2 = Button(root, text="Procesar", width=15, command=read_excel)
btn2.grid(row=1, column=3, padx=10)
root.mainloop()

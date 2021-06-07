import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
#
import os, shutil
from os import listdir
from os.path import isfile, join
import k_nn
import k_means
from PIL import ImageTk,Image


def remove_content(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


directory = 'imgs'
remove_content(directory)
idx = 0

root = tk.Tk()
root.title("Data mining")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='K-NN')
tabControl.add(tab2, text='K-means')
tabControl.pack(fill='both')

ttk.Label(tab1, text="Thuật toán K láng giềng gần nhất (K-NN)").grid(column=0, row=0, padx=30, pady=30)
label1 = ttk.Label(tab1, text="Kết quả")
label1.grid(column=1, row=1, padx=30, pady=30)

canvas = tk.Canvas(tab2, width=640, height=480)
canvas.grid(column=0, row=1, padx=30, pady=30, columnspan=2)


def choose_file():
    global entry1
    k = entry1.get()
    k = int(k)
    file_path = askopenfilename()
    print(file_path)
    ratio, rows = k_nn.test(file_path, k)
    for idx, row in enumerate(rows):
        list_box.insert(idx, row)
    label1['text'] = "Độ chính xác: {} %".format(ratio * 100)

def view():
    global img, idx
    only_files = [f for f in listdir(directory) if isfile(join(directory, f))]
    if len(only_files) > 0:
        if idx >= len(only_files):
            idx = 0
        if idx < 0:
            idx = len(only_files) - 1
        img = ImageTk.PhotoImage(Image.open("{}/{}".format(directory, only_files[idx])))
        canvas.create_image(20, 20, anchor='nw', image=img)


def random_test_k_means():
    global entry
    k = entry.get()
    k = int(k)
    print({k})
    remove_content(directory)
    k_means.test(k)
    view()


def handle_next():
    global idx
    idx += 1
    view()


def handle_prev():
    global idx
    idx -= 1
    view()


ttk.Button(tab1, text="Chọn file excel", command=choose_file).grid(column=2, row=0, padx=30, pady=30)

ttk.Label(tab2, text="Thuật toán K-Means").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(tab2, text="K = ").grid(column=1, row=0, sticky='w')
ttk.Label(tab1, text="K = ").grid(column=1, row=0, sticky='w')
entry = tk.Entry(tab2)
entry1 = tk.Entry(tab1)
entry.grid(column=1, row=0, sticky="w",  padx=30)
entry1.grid(column=1, row=0, sticky="w",  padx=30)
ttk.Button(tab2, text="Random dữ liệu + test", command=random_test_k_means)\
    .grid(column=2, row=0, padx=30, pady=30)
ttk.Button(tab2, text="Prev", command=handle_prev).grid(column=0, row=2, padx=30, pady=30)
ttk.Button(tab2, text="Next", command=handle_next).grid(column=1, row=2, padx=30, pady=30)

onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
if len(onlyfiles) > 0:
    print(onlyfiles)
    img = ImageTk.PhotoImage(Image.open("{}/{}".format(directory, onlyfiles[idx])))
    print(img)
    canvas.create_image(20, 20, anchor='nw', image=img)


list_box = tk.Listbox(tab1, width=80, height=20)
list_box.grid(column=0, row=1, sticky='news')
scrollbar = tk.Scrollbar(tab1, orient="vertical")
scrollbar.config(command=list_box.yview)
scrollbar.grid(column=0, row=1, sticky="nse")


# K-NN

root.mainloop()



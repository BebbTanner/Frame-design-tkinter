# https://blog.teclado.com/side-values-in-tkinters-pack-geometry-manager/

#https://www.youtube.com/watch?v=lH1y7kiDeyg

import tkinter as tk

'''
root = tk.Tk()
root.geometry("600x400")

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.pack(ipadx=10, ipady=10)

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(ipadx=10, ipady=10)

root.mainloop()
'''



root = tk.Tk()
root.geometry("600x400")

frame1 = tk.Frame(root, bg="green")
frame1.pack(ipadx=10, ipady=10, expand=True, side="left", fill="both")

#rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
#rectangle_1.pack(ipadx=10, ipady=10, expand=True, side="left", fill="both")

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(ipadx=10, ipady=10, expand=True, fill="both")

rectangle_3 = tk.Label(root, text="Rectangle 3", bg="blue", fg="white")
rectangle_3.pack(ipadx=10, ipady=10, expand=True, side="left", fill="both")

rectangle_4 = tk.Label(root, text="Rectangle 4", bg="yellow", fg="black")
rectangle_4.pack(ipadx=10, ipady=10, expand=True, fill="both")

rectangle_5 = tk.Label(root, text="Rectangle 5", bg="orange", fg="white")
rectangle_5.pack(ipadx=10, ipady=10, expand=True, side="left", fill="both")

root.mainloop()
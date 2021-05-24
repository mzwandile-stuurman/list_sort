from tkinter import *

root=Tk()
root.title("new form")
root.config(bg = "yellow")
root.geometry("500x500")

list = StringVar


def instertion_sort(arr):

    for i in range (1,len(arr)):
        j=i
        while arr[j-1] > arr[j] and j>0:
            arr[j-1], arr[j]=arr[j],arr[j-1]
            j-=1

    arr =[4,7,2,8,25,3,9]
    instertion_sort(arr)




display_label = Label(root, text= sorted , textvariable=list)
display_label.place(x=10, y=50)



root.mainloop()

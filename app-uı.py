from sqlite3.dbapi2 import Row
from tkinter import *
from tkinter import messagebox
import datacontrolservices as datactrl

#create top level a window object.
window=Tk()
window.title("A basic GUI App With Python")
window.geometry("1000x300")
window.children

#create some variable for entry etc.
nameVar=StringVar()
lastNameVar=StringVar()
studentNoVar=StringVar()
departmentNameVar=StringVar()
searchStudentVar=StringVar()
nameUpdateVar=StringVar()
lastNameUpdateVar=StringVar()
studentNoUpdateVar=StringVar()
departmentUpdateNameVar=StringVar()
studentNoDeleteVar=StringVar()

def clearInput():
    nameVar.set("")
    lastNameVar.set("")
    studentNoVar.set("")
    departmentNameVar.set("")
    searchStudentVar.set("")

def clearInputUpdated():
    nameUpdateVar.set("")
    lastNameUpdateVar.set("")
    studentNoUpdateVar.set("")
    departmentUpdateNameVar.set("")

def sendControlGetRecord():
    name=nameVar.get()
    lastName=lastNameVar.get()
    studentNo=studentNoVar.get()
    department=departmentNameVar.get()
    if(datactrl.dataControl(name,lastName,studentNo,department)):
        messagebox.showinfo("RECOR SUCCESS.","RECORD WRİTE SUCCESSFUL.")
        clearInput()
    else:
        messagebox.showinfo("İNVALİD RECORD","PLEASE WRİTE CORRECT İNPUT.")
        clearInput()

def sendSearchRecord():
    searchVal=searchStudentVar.get()
    if(datactrl.searchRecordControl(searchVal)):
        res=[]
        res=datactrl.searchRecordControl(searchVal)
        showStudentFrame(res)
        messagebox.showinfo("RECORD SUCCESS","RECORD İS BROUGHT")
        clearInput()
    else:
        messagebox.showinfo("İNVALİD SEARCH","PLEASE CHECK QUERY.")
        clearInput()

def updateRecord():
    for widget in window.winfo_children():
        if(str(type(widget)))=="<class 'tkinter.Toplevel'>":
            widget.destroy()
    showUpdateWidget()
    clearInputUpdated()

def sendControlUpdateRecord():
    name=nameUpdateVar.get()
    lastName=lastNameUpdateVar.get()
    studentNo=studentNoUpdateVar.get()
    department=departmentUpdateNameVar.get()
    if(datactrl.updateRecordControl(name,lastName,studentNo,department)):
        messagebox.showinfo("RECORD İNFO","UPDATE İS SUCCESS.")
        clearInputUpdated()
        for widget in window.winfo_children():
            if(str(type(widget)))=="<class 'tkinter.Toplevel'>":
                widget.destroy()
    else:
        messagebox.showinfo("RECORD İNFO","RECORD İS UNSUCCESS.")
        clearInputUpdated()

def sendControlDeleteRecord():
    #searching that record studentNo in this widget.
    for widget in window.winfo_children():
        if(str(type(widget)))=="<class 'tkinter.Toplevel'>":
            for child in widget.winfo_children():
                if(child.winfo_name())=="!label7":
                    res=child.cget('text')
                    #control request and destroy query widget.
                    if(datactrl.deleteRecordControl(res)):
                        messagebox.showinfo("RECORD İNFO","DELETE İS SUCCESS.")
                        for widget in window.winfo_children():
                            if(str(type(widget)))=="<class 'tkinter.Toplevel'>":
                                widget.destroy()
                    else:
                        messagebox.showinfo("RECORD İNFO","DELETE İS UNSUCCESS.")

def showUpdateWidget():
    #show Update Widget and send control layer  info.
    frame=Toplevel(bd=10)
    frame.geometry("350x200")
    frame.title("UPDATE")
    lblNameTitle=Label(frame,fg="black",text="NAME : ")
    lblNameTitle.grid(row=0,column=0)
    lblLstNameTitle=Label(frame,fg="black",text="LAST NAME : ")
    lblLstNameTitle.grid(row=1,column=0)
    lblStdntNoTitle=Label(frame,fg="black",text="STUDENT NO : ")
    lblStdntNoTitle.grid(row=2,column=0)
    lblDepartmntTitle=Label(frame,fg="black",text="DEPARTMENT : ")
    lblDepartmntTitle.grid(row=3,column=0)
    lblName=Entry(frame,justify="center",textvariable=nameUpdateVar)
    lblName.grid(row=0,column=1)
    lblLastName=Entry(frame,justify="center",textvariable=lastNameUpdateVar)
    lblLastName.grid(row=1,column=1)
    lblStudentNo=Entry(frame,justify="center",textvariable=studentNoUpdateVar)
    lblStudentNo.grid(row=2,column=1)
    lblDepartment=Entry(frame,justify="center",textvariable=departmentUpdateNameVar)
    lblDepartment.grid(row=3,column=1)
    btnUpdate=Button(frame,bd=10,text="Submit",fg="white",bg="black",activebackground="white",activeforeground="black",command=sendControlUpdateRecord).grid(row=4,column=1)
    

def showStudentFrame(res):
    #show Search Result in frame this section
    frame=Toplevel(bd=10)
    frame.geometry("250x200")
    frame.title("Kayıt No:"+str(res[2]))
    lblNameTitle=Label(frame,fg="black",text="NAME : ")
    lblNameTitle.grid(row=0,column=0)
    lblLstNameTitle=Label(frame,fg="black",text="LAST NAME : ")
    lblLstNameTitle.grid(row=1,column=0)
    lblStdntNoTitle=Label(frame,fg="black",text="STUDENT NO : ")
    lblStdntNoTitle.grid(row=2,column=0)
    lblDepartmntTitle=Label(frame,fg="black",text="DEPARTMENT : ")
    lblDepartmntTitle.grid(row=3,column=0)
    lblName=Label(frame,text=res[0])
    lblName.grid(row=0,column=1)
    lblLastName=Label(frame,text=res[1])
    lblLastName.grid(row=1,column=1)
    lblStudentNo=Label(frame,text=res[2])
    lblStudentNo.grid(row=2,column=1)
    lblDepartment=Label(frame,text=res[3])
    lblDepartment.grid(row=3,column=1)
    btnUpdate=Button(frame,bd=10,text="Update",fg="white",bg="black",activebackground="white",activeforeground="black",command=updateRecord).grid(row=4,column=0)
    btnDelete=Button(frame,bd=10,text="Delete",fg="white",bg="black",activebackground="white",activeforeground="black",command=sendControlDeleteRecord).grid(row=4,column=1)


#components for main window.
#label for input
name=Label(text="NAME:",fg="black").place(x=25,y=60)
lastName=Label(text="LAST NAME:",fg="black").place(x=25,y=100)
studentNo=Label(text="STUDENT NO:",fg="black").place(x=25,y=140)
bookName=Label(text="DEPARTMENT NAME :",fg="black").place(x=25,y=180)

#label for info
info=Label(text="PLEASE DONT LEAVE BLANK.",fg="black").place(x=25, y=20)

#input entries.
nameEntry=Entry(window,justify="center",textvariable=nameVar).place(x=165,y=60)
lastNameEntry=Entry(window,justify="center",textvariable=lastNameVar).place(x=165,y=100)
studentNoEntry=Entry(window,justify="center",textvariable=studentNoVar).place(x=165,y=140)
bookNameEntry=Entry(window,justify="center",textvariable=departmentNameVar).place(x=165,y=180)

#button for submit
bntSubmit=Button(text="Submit",fg="white",bg="black",activebackground="white",activeforeground="black",command=sendControlGetRecord).place(x=200,y=220)

#label for search
lblSearch=Label(text="Student No:").place(x=525,y=100)

#button for search record
btnSearch=Button(text="Search",fg="white",bg="black",activebackground="white",activeforeground="black",command=sendSearchRecord).place(x=810,y=100)

#entry for search student
studentSearchBtn=Entry(window,textvariable=searchStudentVar).place(x=630,y=100)



window.mainloop()
"""import Tkinter
import ttk


def main():

  root = Tkinter.Tk()

  ft = ttk.Frame()
  fb = ttk.Frame()

  ft.pack(expand=True, side=Tkinter.TOP)
  fb.pack(expand=True, side=Tkinter.TOP)

  pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='determinate')
  pb_hD = ttk.Progressbar(ft, orient='horizontal', mode='indeterminate')
  pb_vd = ttk.Progressbar(fb, orient='vertical', mode='determinate')
  pb_vD = ttk.Progressbar(fb, orient='vertical', mode='indeterminate')

  pb_hd.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
  pb_hD.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
  pb_vd.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.LEFT)
  pb_vD.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.LEFT)

  pb_hd.start(50)
  pb_hD.start(50)
  pb_vd.start(50)
  pb_vD.start(50)

  root.mainloop()
import Tkinter as tk

def populate(frame):
    '''Put in some fake data'''
    for row in range(100):
        tk.Label(frame, text="%s" % row, width=3, borderwidth="1", 
                 relief="solid").grid(row=row, column=0)
        t="this is the second column for row %s" %row
        tk.Label(frame, text=t).grid(row=row, column=1)

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, background="#ffffff")
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

root.mainloop()"""

"""import Tkinter as T
root=T.Tk()
frame=T.Frame(root,width=600,height=600,bg="white")
#frame.grid(row=0,column=0)
scrollcanvas = T.Canvas(frame,bg='white',width=300,height=300,scrollregion=(0,0,500,500))
hbar=T.Scrollbar(frame,orient=T.HORIZONTAL)
hbar.pack(side=T.BOTTOM,fill=T.X)
hbar.config(command=scrollcanvas.xview)
vbar=T.Scrollbar(frame,orient=T.VERTICAL)
vbar.pack(side=T.RIGHT,fill=T.Y)
vbar.config(command=scrollcanvas.yview)
scrollcanvas.config(width=300,height=300)
scrollcanvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
scrollcanvas.pack(side=T.LEFT,expand=True,fill=T.BOTH)

#frame1=T.Frame(scrollcanvas)
#frame1.place(x=0,y=0,anchor=T.NW)
#frame2=T.Frame(frame)
#frame2.place(relx=0.5,rely=0.1,anchor=T.S)
#label1=T.Label(frame2,text="DATANODE  TASKTRACKER SNO.  IP   RAM   HARDDISK",font="8",fg="white",bg="red",anchor=T.CENTER)
#label1.pack(fill=T.X,expand="yes")

root.mainloop()"""
import Tkinter as T
root=T.Tk()
root.geometry("600x600+100+200")  
root.update()
frame=T.Frame(root,width=600,height=600)
frame.grid(row=0,column=0)
scrollcanvas=T.Canvas(frame,bg='#FFFFFF',width=300,height=300)
hbar=T.Scrollbar(frame,orient=T.HORIZONTAL)
hbar.pack(side=T.BOTTOM,fill=T.X)
hbar.config(command=scrollcanvas.xview)
vbar=T.Scrollbar(frame,orient=T.VERTICAL)
vbar.pack(side=T.RIGHT,fill=T.Y)
vbar.config(command=scrollcanvas.yview)
scrollcanvas.config(width=300,height=300)
scrollcanvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
scrollcanvas.pack(side=T.LEFT,expand=True,fill=T.BOTH)

#frame1=T.Frame(scrollcanvas)
#frame1.place(x=0,y=0,anchor=T.NW)
frame1 = T.Frame(scrollcanvas)
scrollcanvas.create_window((0,0), window=frame1, anchor=T.NW)
frame1.bind('<Configure>', self.set_scrollregion)
frame2=T.Frame(frame)
frame2.place(relx=0.5,rely=0.1,anchor=T.S)
label1=T.Label(frame2,text="DATANODE  TASKTRACKER SNO.  IP   RAM   HARDDISK",font="8",fg="white",bg="red",anchor=T.CENTER)
label1.pack(fill=T.X,expand="yes")

var1=[]
var2=[]
checkbuttons=[]
string=[]
for i in range(1,100):
	string.append(str(i)+" "+str(i)+"."+str(i)+"."+str(i*i))
for i in string:
		j=i.split()
		j=int(j[0].strip())
		#print(j,manual.sequence[manual.seq[j]])
		#print(manual.seq[j],j,manual.status[manual.seq[j]])
		#v=T.IntVar()
		var1.append(T.IntVar())
		var2.append(T.IntVar())
		#print(var1[len(var1)-1].get())
		checkbuttons=T.Checkbutton(frame1, variable=var1[len(var1)-1],bg="dark green",fg="light green")
		checkbuttons.grid(row=j,column=0,sticky=T.W+T.E)
		checkbuttons=T.Checkbutton(frame1, text=i, variable=var2[len(var2)-1],bg="dark green",fg="light green")
		checkbuttons.grid(row=j,column=1,sticky=T.W+T.E)
scrollcanvas.config(scrollregion=(0, 0, 200, len(string)))

root.mainloop()



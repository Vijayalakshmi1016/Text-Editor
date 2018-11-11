import tkinter as tk 
import tkinter.scrolledtext as sc
from tkinter import filedialog
#3import tkinter.filedialog
#tkinter used for providing GUI
#scrolled text for providing scrolling in text editor
#window variable represents a blank screen
window=tk.Tk()

#adding title to the window
window.title("Text Editor")

#defining size o f the window
window.geometry("500x500")

#add text area for editor app 
text_field=sc.ScrolledText(window,width=400,height=400)
#specicfy its position in window(by default at top)
text_field.pack()

#adding menu bar to window
menu_bar=tk.Menu(window)


#adding functionalities of file open,save,and exit
#to open file
def open_file():
 window.filename =  tk.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
 print (window.filename)
 return;

def to_save():
 f = tk.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
 if f is None: 
  return
 text2save = str(text.get(1.0, END))
 f.write(text2save)
 f.close()

        
def to_exit():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        window.destroy()

def about():
    label = tkMessageBox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")
      

# add fle_menu to the menu bar
file_menu = tk.Menu(menu_bar,tearoff=0)

#add cascading to file menu
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open..",command=open_file)
file_menu.add_command(label="Save",command=to_save)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=to_exit)

#edit menu
edit_menu = tk.Menu(master=menu_bar,tearoff=0)

#add cascading to edit menu
menu_bar.add_cascade(label="Edit",menu=edit_menu)#, menu=edit_menu)

edit_menu.add_command(label="Undo")#,command=open_file)
edit_menu.add_command(label="Redo",)#command=to_save)
edit_menu.add_separator()
edit_menu.add_command(label="Cut")#,command=to_exit)
edit_menu.add_command(label="Copy")#,ommand=to_exit)
edit_menu.add_command(label="Paste")#,command=to_exit)

#help menu
help_menu =tk.Menu(master=menu_bar,tearoff=0)

menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About..",command=about)

# display the menu
window.config(menu=menu_bar)

window.mainloop()

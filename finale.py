import tkinter as tk 
import tkinter.scrolledtext as sc
from tkinter import filedialog
from tkinter import messagebox
#import tkinter.filedialog
#tkinter used for providing GUI
#scrolled text for providing scrolling in text editor
#window variable represents a blank screen
window=tk.Tk()

#adding title to the window
window.title("My Notebook")

#defining size o f the window
window.geometry("500x500")

#add text area for editor app 
text_field=sc.ScrolledText(window,width=400,height=400)
#specicfy its position in window(by default at top)
text_field.pack()

#adding menu bar to window
menu_bar=tk.Menu(window)


#adding functionalities of file menu : open,save,and exit
file_open="no_file"
def open_file():
 open_return = tk.filedialog.askopenfile(parent=window,initialdir="c:",title='Select file to open:',filetypes=(("text files","*.txt"),("all files","*.*")))
 if open_return!= None:
  text_field.delete(1.0,"end")   
  for line in open_return:
   text_field.insert("end",line)
  file_open=open_return.name
  open_return.close()  
 
  
def save_as_file():
 f = tk.filedialog.asksaveasfile(mode='w',defaultextension=".txt",title='Save file as')
 if f != None:
 # slice off the last character from get, as an extra return is added
  data = text_field.get('1.0', 'end')
  file_open=f.name
  f.write(data)
  f.close()
 if f is None:
  return

def save_file():
 if file_open=="no_file":
  save_as_file()
 else:
  f=open(file_open,"w+")
  f.write(text_field.get(1.0,"end"))
  f.close()

def to_exit():
 if tk.messagebox.askokcancel("Quit", "Do you really want to quit?"):
  window.destroy()


#adding functionalities of Edit menu : cut, copy, paste 

def copy_text():
 text_field.clipboard_clear()
 text_field.clipboard_append(text_field.selection_get())

def cut_text():
 copy_text()
 text_field.delete("sel.first","sel.last")

def paste_text():
 text_field.insert(INSERT,text_field.clipboard_get())
 
def about():
 label = tk.messagebox.showinfo("About", "A Mini-Project on Text Editor using tkinter module\n\n\tALL COPYRIGHTS RESERVED © ")
      
# add fle_menu to the menu bar
file_menu = tk.Menu(menu_bar,tearoff=0)

#add cascading to file menu
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open..",command=open_file)
file_menu.add_command(label="Save As",command=save_as_file)
file_menu.add_command(label="Save ",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=to_exit)

#edit menu
edit_menu = tk.Menu(master=menu_bar,tearoff=0)

#add cascading to edit menu
menu_bar.add_cascade(label="Edit",menu=edit_menu)


edit_menu.add_command(label="Cut                Ctrl+X",command=cut_text)
edit_menu.add_command(label="Copy             Ctrl+C",command=copy_text)
edit_menu.add_command(label="Paste             Ctrl+V",command=paste_text)

#help menu
help_menu =tk.Menu(master=menu_bar,tearoff=0)

menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About..",command=about)

# display the menu
window.config(menu=menu_bar)

#an infinite loop for the program to stay
window.mainloop()

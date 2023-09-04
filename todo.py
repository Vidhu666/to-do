import tkinter
import tkinter.messagebox
import pickle

window = tkinter.Tk()
window.title("TO-DO LIST")
window.configure(background="black")
window.geometry("500x450+500+200")




def task_adding():
    todo = task_add.get()
    if todo != "":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention !!", message="T0 add a task, please enter a task")

def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)
    except:
        tkinter.messagebox.showwarning(title="Attention !!",message="To delete a task, you must select a task")


def task_save():
    todo_list = todo_box.get(0, todo_box.size())
    pickle.dump(todo_list, open("todo_list.dat", "wb"))



list_frame = tkinter.Frame(window)
list_frame.pack(pady=20)

todo_box = tkinter.Listbox(list_frame,height=10, width=25, font=("Cascadia code",18), bd=0, background="blue", highlightthickness=0, selectbackground="lightgreen", activestyle="none")
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill="both")

#todo_box.config(yscrollcommand=scroller.set)
#scroller.config(command=todo_box.yview)

task_add = tkinter.Entry(window, width=70)
task_add.pack(pady=40)

add_task_button = tkinter.Button(window, text="ADD TASK", font=("stencil",20,"bold"),width=20,  background="grey",  command=task_adding)
add_task_button.pack(pady=6)

remove_task_button = tkinter.Button(window, text="DELETE TASK", font=("stencil",20,"bold"),  width=20,background="grey",  command=task_removing)
remove_task_button.pack(pady=6)

save_task_button = tkinter.Button(window, text="SAVE TASk",font=("stencil",20,"bold"),  width=20,background="grey",  command=task_save)
save_task_button.pack(pady=6)

window.mainloop()
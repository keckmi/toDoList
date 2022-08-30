import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x450')
window.title('toDoList')
window.config(bg='#111111')


def add_task():
    task = taskInput.get()

    if task != '':
        if task == 'Taks Input':
            messagebox.showwarning('Error', 'Task Input Please')
        else:
            taskList.insert(tk.END, task)
            taskInput.delete(0, 'end')
    else:
        messagebox.showwarning('Error', 'Task Input Please')


def delete_task():
    taskList.delete(tk.ANCHOR)


def input_delete(event, input):
    input.delete(0, tk.END)


frame = tk.Frame(window)
frame.pack(pady=10)

taskList = tk.Listbox(frame, width=25, height=8, font=('Times', 18),
                      fg='#464646', selectbackground='#333333', activestyle='none')
taskList.pack(side=tk.LEFT, fill=tk.BOTH)

scrollBar = tk.Scrollbar(frame)
scrollBar.pack(side=tk.RIGHT, fill=tk.BOTH)

taskList.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=taskList.yview)

taskInput = tk.Entry(window, font=('Times', 24))
taskInput.insert(0, 'Task Input')
taskInput.bind('<Button-1>', lambda event: input_delete(event, taskInput))
taskInput.pack(pady=20)

buttonFrame = tk.Frame(window)
buttonFrame.pack(pady=20)

buttonAddTask = tk.Button(buttonFrame, text='Add Task', font=('Times', 14),
                          bg='green', fg='white', padx=20, pady=10, command=add_task)
buttonAddTask.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

buttonDeleteTask = tk.Button(buttonFrame, text='Delete Task', font=('Times', 14),
                             bg='red', fg='white', padx=20, pady=10, command=delete_task)
buttonDeleteTask.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

window.mainloop()

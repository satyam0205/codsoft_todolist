import tkinter as tk

class ToDoListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.tasks = []
        

        self.create_gui_components()

    def create_gui_components(self):
        self.task_list = tk.Listbox(self.master, width=40)
        self.task_list.pack(padx=10, pady=10)
        
        self.entry = tk.Entry(self.master, width=40)
        self.entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.update_button = tk.Button(self.master, text="Update Task", command=self.update_task)
        self.update_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.entry.get()
        if task:  # validate non-empty task
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def update_task(self):
        try:
            index = self.task_list.curselection()[0]
            new_task = self.entry.get()
            self.tasks[index] = new_task
            self.task_list.delete(index)
            self.task_list.insert(index, new_task)
            self.entry.delete(0, tk.END)
        except IndexError:
            print("Select a task to update!")

    def delete_task(self):
        try:
            index = self.task_list.curselection()[0]
            del self.tasks[index]
            self.task_list.delete(index)
        except IndexError:
            print("Select a task to delete!")

root = tk.Tk()
my_gui = ToDoListGUI(root)
root.mainloop()
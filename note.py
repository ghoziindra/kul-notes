import tkinter as tk

class KulNotes:
    def __init__(self, master):
        self.master = master
        self.master.title('Kulnotes')
        self.notes = []

    #membuat input dan button
        self.note_input = tk.Entry(self.master, width=40)
        self.note_input.grid(row=0, column=0, padx=5, pady=5)
        self.add_button = tk.Button(self.master, text="Add Note", command=self.add_note)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

    def add_note(self):
        note_text = self.note_input.get()
        if note_text:
            note_label = tk.Label(self.master, text=note_text, bg='orange', padx=5, pady=5)
            note_label.grid(row=len(self.notes)+1, column=0, padx=5, pady=5, sticky='we')
            self.notes.append(note_label)
            self.note_input.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    KulNotes(root)
    root.mainloop()
                            
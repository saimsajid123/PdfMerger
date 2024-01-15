import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")

        self.file_list = []

        self.create_widgets()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add PDFs", command=self.add_pdfs)
        self.add_button.pack(pady=5)

        self.merge_button = tk.Button(self.root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(pady=5)

    def add_pdfs(self):
        files = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF files", "*.pdf")])
        if files:
            for file in files:
                self.listbox.insert(tk.END, file)
            self.file_list.extend(files)

    def merge_pdfs(self):
        if not self.file_list:
            tk.messagebox.showwarning("Warning", "No PDFs selected.")
            return

        merger = PdfMerger()
        for pdf_file in self.file_list:
            merger.append(pdf_file)

        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_file:
            merger.write(output_file)
            tk.messagebox.showinfo("Success", "PDFs merged successfully.")

            self.file_list = []
            self.listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()

# Import needed modules
from PyPDF2 import PdfReader
import pyttsx3
import tkinter
from tkinter import filedialog, messagebox


# Function to read in PDF into text
def extract_pdf_text(pdf_path):
    """
    Takes in the path of a PDF and extracts text from it as an output
    """
    try:
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            return text
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"


# Function to turn extracted text into audio
def text_to_audio(text_input, save_path):
    """
    Converts text to audio and saves to file.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.save_to_file(text_input, save_path)
    engine.runAndWait()


# Define application class
class PDFAudioConverter:
    # Initialize the app's layout and starting state
    def __init__(self, master):
        self.master = master
        self.master.title("PDF to audio converter")
        self.master.minsize(width=400, height=200)
        self.master.resizable(False, False)
        self.pdf_path = ''
        self.text_input = ''
        self.audio_info = ''

        # Introduction text
        self.intro_label = tkinter.Label(text="PDF to audio converter", font=('Arial', 16, 'bold'))
        self.intro_label.pack(pady=(20, 5))

        self.instruction_label = tkinter.Label(text="Select a PDF to convert into a playable audio file.",
                                               font=('Arial', 12), wraplength=600)
        self.instruction_label.pack(pady=(5, 20))

        # Label that mentions selected file
        self.file_selected_label = tkinter.Label(text="No file selected", wraplength=350, justify='left')
        self.file_selected_label.pack(pady=5)

        # Buttons frame
        self.btn_frame = tkinter.Frame(self.master)
        self.btn_frame.pack(pady=10)

        # Upload button
        self.upload_btn = tkinter.Button(self.btn_frame, text="Select PDF", command=self.select_pdf)
        self.upload_btn.pack(side=tkinter.LEFT, padx=10)

        # Save audio button
        self.save_btn = tkinter.Button(self.btn_frame, text="Save audio", command=self.save_audio,
                                       state=tkinter.DISABLED)
        self.save_btn.pack(side=tkinter.LEFT)

    def select_pdf(self):
        """
        Function to select PDF files only, store them into a file path and update the text label accordingly.
        """
        file_path = tkinter.filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_path = file_path
            self.file_selected_label.config(text=f"Selected: {file_path.split('/')[-1]}")
            self.save_btn.config(state=tkinter.NORMAL)
        else:
            self.file_selected_label.config(text="No file selected")

    def load_pdf_text(self):
        """
        Loads and validates PDF text. Returns True if successful, False otherwise.
        """
        if not self.pdf_path:
            self.file_selected_label.config(text="Please select a PDF file first.")
            return False

        self.text_input = extract_pdf_text(self.pdf_path)
        if self.text_input.startswith("Error"):
            messagebox.showerror("Error", self.text_input)
            return False

        return True

    def save_audio(self):
        """
        Saves audio generated
        """
        if self.load_pdf_text():
            save_path = filedialog.asksaveasfilename(
                defaultextension=".mp3",
                filetypes=[("MP3 files", "*.mp3"), ("WAV files", "*.wav")]
            )
            if save_path:
                text_to_audio(self.text_input, save_path)
                self.file_selected_label.config(text="Audio saved successfully!")
                tkinter.messagebox.showinfo("Success", "Audio saved successfully!")


# Run app
if __name__ == "__main__":
    root = tkinter.Tk()
    app = PDFAudioConverter(root)
    root.mainloop()

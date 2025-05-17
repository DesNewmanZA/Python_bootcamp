# Import needed modules
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image, ImageDraw, ImageFont


# Define the application
class Watermarker:
    def __init__(self, app_window):
        # Define main app views
        self.window = app_window
        self.window.title("Image watermarker")
        self.window.minsize(width=800, height=600)
        self.window.config(padx=10, pady=10)

        # Define a frame to contain the GUI
        self.frame = Frame(self.window)
        self.frame.pack(expand=True)

        # Define starting state variables
        self.img_path = None
        self.user_img = None
        self.watermarked_img = None
        self.watermarking_txt = "Watermark text"

        # Define app heading
        self.label = Label(self.frame, text="Watermarking Tool", font=('Arial', 20, 'bold'))
        self.label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Define load image button
        self.open_img_btn = Button(self.frame, text="Select image", command=self.load_image)
        self.open_img_btn.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Define image loading panel
        self.img_panel = Canvas(self.frame, width=600, height=450, bg="lightgray")
        self.img_panel.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Define watermark input form
        self.watermark = Entry(self.frame, width=60)
        self.watermark.insert(END, string="Watermark text")
        self.watermark.grid(row=3, column=0, pady=10)

        # Define watermark placing button
        self.watermark_button = Button(self.frame, text="Add watermark", command=self.watermark_image)
        self.watermark_button.grid(row=3, column=1)

        # Define save image button
        self.save_button = Button(self.frame, text="Save image", command=self.save_image)
        self.save_button.grid(row=3, column=2, columnspan=2)

    # Define function to load image
    def load_image(self):
        img_path = filedialog.askopenfilename(filetypes=[("Valid image formats", "*.jpg; *.png;")])
        if img_path:
            self.img_path = img_path
            self.user_img = Image.open(self.img_path)
            self.user_img = self.user_img.resize((600, 450), Image.Resampling.LANCZOS)
            self.watermarked_img = self.user_img
            self.user_img = ImageTk.PhotoImage(self.user_img)
            self.img_panel.delete("all")
            self.img_panel.create_image(0, 0, anchor='nw', image=self.user_img)

    # Watermark image
    def watermark_image(self):
        # Error handle for if no image loaded yet
        if self.user_img is None:
            messagebox.showwarning("No image loaded!", "Please load an image to watermark")
            return

        # Watermark if an image is loaded
        self.watermarking_txt = self.watermark.get()
        watermarked_img = self.watermarked_img.copy().convert("RGBA")
        wm_text = Image.new("RGBA", watermarked_img.size, (255, 255, 255, 0))

        draw_watermark = ImageDraw.Draw(wm_text)
        draw_watermark.text((150, 200), self.watermarking_txt, font=ImageFont.truetype("arial.ttf", size=40),
                            fill=(255, 255, 255, 120))
        self.watermarked_img = Image.alpha_composite(watermarked_img, wm_text)
        self.user_img = ImageTk.PhotoImage(self.watermarked_img.convert("RGB"))
        self.img_panel.delete("all")
        self.img_panel.create_image(0, 0, anchor='nw', image=self.user_img)

    # Save watermarked image
    def save_image(self):
        if self.watermarked_img is None:
            messagebox.showwarning("No watermarked image!", "Please add a watermark before saving")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG file", "*.jpg")])
        if not save_path:
            return
        else:
            img_to_save = self.watermarked_img.convert("RGB")
            img_to_save.save(save_path)


if __name__ == "__main__":
    window = Tk()
    app = Watermarker(window)
    window.mainloop()
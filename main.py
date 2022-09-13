from PIL import Image, ImageTk
# im = Image.open("photo.jpg")

from tkinter import Tk, Button, Label, filedialog, Text


# WORKING WITH [GUI]

# function in order to open file explorer window and get filename
def openfile():
    filename = filedialog.askopenfilename(initialdir='/',
                                          title='Select an image',
                                          filetypes=(('jpg images', '*.jpg'),
                                                     ('png_images', '*.png'),
                                                     ('jpeg files', '*.jpeg')))
    return filename


# open an image using filename
def open_img():
    img_name = openfile()
    img = Image.open(img_name)
    img = img.resize((400, 400))
    img = ImageTk.PhotoImage(img)

    panel = Label(window, image=img)
    panel.image = img
    panel.grid(row=4)
    get_input.grid(row=6)
    input_label.grid(row=5)


# put watermark on the image
def watermark():
    pass


# setting up the window
window = Tk()
window.title('Image Watermarking')
window.minsize(500, 600)
window.geometry('500x500')


label_top = Label(window,
                  text="Open an image to put your watermark!",
                  width=40,
                  font=('Arial', 20, 'bold'))


button_open = Button(window, text="Open an image", command=open_img)
button_exit = Button(window, text='Exit', command=exit)

label_top.grid(row=1)
button_open.grid(row=2)
button_exit.grid(row=3)

# working with watermark text input
input_label = Label(window,
                    text='Enter your watermark text: ')

get_input = Text(window,
                 height=1,
                 width=30)

button_watermark = Button(window, text='Watermark', command=watermark)


window.mainloop()

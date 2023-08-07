from tkinter import *
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO
import main



# Define the function to display book results
def show_book_results():
    # Get book name from the Entry widget
    book_name = book_entry.get()
    
    details = main.recom(book_name)
    names = details[0]
    links = details[1]
    
    # Create a new window for the book results
    book_window = Toplevel(root)
    book_window.title("Book Results")
    book_window.geometry("800x400")
    book_window.resizable(True,True)
    book_window.configure(bg='black')

    # Load and resize background image
    # bg_image = Image.open("bg.png")
    # bg_image = bg_image.resize((800, 600), Image.ANTIALIAS)
    # bg_photo = ImageTk.PhotoImage(bg_image)
    # bg_label = Label(book_window, image=bg_photo)
    # bg_label.place(x=0, y=0)

    # Create image and text labels for book results
    for i in range(4):
        # Get image from URL and create PhotoImage object
        image_url = links[i]
        with urllib.request.urlopen(image_url) as url:
            image_data = url.read()
        image = Image.open(BytesIO(image_data))
        image = image.resize((150, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        # Create image label and place it on the window
        image_label = Label(book_window, image=photo)
        image_label.image = photo
        image_label.place(relx=0.2+i*0.2, rely=0.3, anchor=CENTER)

    text = Label(book_window, text="It is Highly recommended for you to read these books too!", font=("Helvetica", 16), bg="white")
    text.place(relx=0.5, rely=0.7, anchor=CENTER)
# Create the main window
root = Tk()
root.title("Book Search")
root.geometry("600x600")
root.resizable(False, False)

# Load and resize background image
bg_image = Image.open("bg.png")
bg_image = bg_image.resize((600, 600), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0)

# Create label and entry widget for book search
book_label = Label(root, text="Enter book name:", font=("Helvetica", 16), bg="white")
book_label.place(relx=0.5, rely=0.4, anchor=CENTER)
book_entry = Entry(root, width=30, font=("Helvetica", 12))
book_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

# Create curved button for book search
search_button = Button(root, text="Search", font=("Helvetica", 12), bg="white", bd=0, command=show_book_results)
search_button.place(relx=0.5, rely=0.6, anchor=CENTER)

# Run the main loop
root.mainloop()

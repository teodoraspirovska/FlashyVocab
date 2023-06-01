from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Here we create a function, when the buttons are pressed tish function get triggerd
# For that we must use Pandas, to create a DataFrame, so we can read from our data
# Next thing we create a dictionary from our data, for that we need to orient our table
# To format the dictionary in the right way we must use orient set to records with key and value
# Next we need to pick some data from our formatted dictionary with help of random module
# When we hold the random choice from the data in current_card, we can use [] to specify to exact word like in our data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# We need to create a variable for the canvas card_title, word_title, so we can use them in the function
# Next we need to config the canvas to change the title with the French and word with the proper word
# We also call this next_card() func in the end of code, so it can change the title when we run the code
# And we put this next_card for command in the buttons
# Also we need time mechanism here every time when we press new card
# Fix the bug when we press new card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# Change the font for the English
# We need to hold of the canvas and item config the text and word
# For that we need to create the global current_card like and empty dictionary and use that in two functions
# Next thing is to change the image, because the English card is with different background
# We create the new card with variable
# We config the canvas with new bg and we change the color
# Next thing here is when wi press the button, new card new word, that is happening in the next_card() function
# In the next_card() we config the window with -
# canvas.item config(card_background, image=card_background) and we change the color fill="black"
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    if "English" in current_card:
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    else:
        pass
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# First we create window with title end we add pady and padx and bg=color
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# We need to use window.after method - so we can flip the card after some time
# Than we add 3 seconds and we add function flip_card - which we need to create
flip_timer = window.after(3000, func=flip_card)

# We create a Canvas Widget width and height, when we can put our image
# Next we create a image from our image class, than we can hold our canvas and create image inside
# and type x and y values in the center and after all that we can use grid method
# Than we config the canvas end we change bg=color and highlight-thickness=0
# In the canvas we also have text and add x and y coordinates
# we can create that text (text="Title", font=("Ariel", 40, "italic"))


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 236, text="", font=("Ariel", 50, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons and we add image in the Widget or Calss we set up grid, and we change also:
# canvas.grid(row=0, column=0, columnspan=2) because must be indented 2 columns

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, borderwidth=0, command=next_card)
unknown_button.grid(column=0, row=1)
check_image = PhotoImage(file="images/right.png")
unknown_button = Button(image=check_image, borderwidth=0, command=is_known)
unknown_button.grid(column=1, row=1)

next_card()

window.mainloop()

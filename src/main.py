# imports
from tkinter import *
import webbrowser
import keyboard


expression = ""


#region - functions
# function to update expression in the text entry box
def press(num):

    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)

# function to evaluate the final expression
def equalpress():
    # Try and except statement is used for handling the errors like zero division error etc.
 
    # Put that code inside the try block which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression and str function convert the result into string
        total = str(eval(expression))
 
        equation.set(total)
 
        # initialize the expression variable by empty string
        expression = ""
 
    # if error is generate then handle by the except block
    except:
 
        equation.set(" error ")
        expression = ""

# function to clear the contents of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# function to delete only 1 digit of the text entry box
def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# function to open in a browser a github profile
def github():
    webbrowser.open('https://github.com/afonsocortereal15')

# function to open in a browser a github repo
def github_repo():
    webbrowser.open('https://github.com/afonsocortereal15/the-calculator')

# function to open in a browser a github issues page
def github_issues():
    webbrowser.open('https://github.com/afonsocortereal15/the-calculator/issues')

#endregion


#region - gui configs
# create a GUI window
gui = Tk()
 
#window configs
# set the background colour of GUI window
gui.configure(background='#333333')
 
# set the title of the window
gui.title("The Calculator")
 
# set the configuration of window
gui.geometry("400x400")

# StringVar() is the variable class we create an instance of this class
equation = StringVar()

# create the text entry box for showing the expression
expression_field = Entry(gui, textvariable=equation, bg='#333333', font='Arial 30 bold', bd=0, fg='white', justify='right')
 
# set grid method
expression_field.grid(columnspan=4, ipadx=154)

#endregion
    

#region - buttons
# dynamically resize buttons when resizing the window
Grid.rowconfigure(gui,(0, 1, 2, 3, 4, 5),weight=1)
Grid.columnconfigure(gui,(0, 1, 2, 3),weight=1)

# clear button
button_clear = Button(gui, text='Clear', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=clear, height=2, width=14)
button_clear.grid(row=1, column=1, sticky='NSEW')

# delete button
button_delete = Button(gui, text='<-', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=delete, height=2, width=14)
button_delete.grid(row=1, column=2, sticky='NSEW')

# divide button
button_divide = Button(gui, text='÷', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press("/"), height=2, width=14)
button_divide.grid(row=1, column=3, sticky='NSEW')

# button 7
button7 = Button(gui, text='7', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press(7), height=2, width=14)
button7.grid(row=2, column=0, sticky='NSEW')

# button 8
button8 = Button(gui, text='8', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press(8), height=2, width=14)
button8.grid(row=2, column=1, sticky='NSEW')

# button 9
button9 = Button(gui, text='9', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press(9), height=2, width=14)
button9.grid(row=2, column=2, sticky='NSEW')

# multiply button
button_multiply = Button(gui, text='x', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press('*'), height=2, width=14)
button_multiply.grid(row=2, column=3, sticky='NSEW')

# button 4
button4 = Button(gui, text='4', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press(4), height=2, width=14)
button4.grid(row=3, column=0, sticky='NSEW')

# button 5
button5 = Button(gui, text='5', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press(5), height=2, width=14)
button5.grid(row=3, column=1, sticky='NSEW')

# button 6
button6 = Button(gui, text='6', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press(6), height=2, width=14)
button6.grid(row=3, column=2, sticky='NSEW')

# subtract button
button_subtract = Button(gui, text='-', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press('-'), height=2, width=14)
button_subtract.grid(row=3, column=3, sticky='NSEW')

# button 1
button1 = Button(gui, text='1', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press(1), height=2, width=14)
button1.grid(row=4, column=0, sticky='NSEW')

# button 2
button2 = Button(gui, text='2', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press(2), height=2, width=14)
button2.grid(row=4, column=1, sticky='NSEW')

# button 3
button3 = Button(gui, text='3', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press(3), height=2, width=14)
button3.grid(row=4, column=2, sticky='NSEW')

# sum button
button_sum = Button(gui, text='+', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press('+'), height=2, width=14)
button_sum.grid(row=4, column=3, sticky='NSEW')

# button 0
button0 = Button(gui, text='0', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press(0), height=2, width=14)
button0.grid(row=5, column=1, sticky='NSEW')

# comma button
button_comma = Button(gui, text=',', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=lambda: press('.'), height=2, width=14)
button_comma.grid(row=5, column=2, sticky='NSEW')

# equal button
button_equal = Button(gui, text='=', fg='white', bg='#454545', font='Arial 20', relief=RIDGE,
                command=equalpress, height=2, width=14)
button_equal.grid(row=5, column=3, sticky='NSEW')
#endregion


#region - physical keyboard
def pressed_key(key):
    if key.name == '1':
        press(1)

    elif key.name == '2':
        press(2)

    elif key.name == '3':
        press(3)

    elif key.name == '4':
        press(4)

    elif key.name == '5':
        press(5)

    elif key.name == '6':
        press(6)

    elif key.name == '7':
        press(7)

    elif key.name == '8':
        press(8)

    elif key.name == '9':
        press(9)

    elif key.name == '0':
        press(0)

    elif key.name == '/':
        press('/')

    elif key.name == '*':
        press('*')

    elif key.name == '-':
        press('-')

    elif key.name == '+':
        press('+')

    elif key.name == 'enter':
        equalpress()
    
    elif key.name == 'backspace':
        delete()

    else:
        ''

        
keyboard.on_press(pressed_key)
#endregion


#region - menus
# create main menu
menubar = Menu(gui)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="☰", menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=gui.quit)

# create help menu
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=github_repo)
helpmenu.add_command(label='Help', command=github_issues)
helpmenu.add_separator()
helpmenu.add_command(label='Made with ♡ by Afonso', command=github)
    
gui.config(menu=menubar)
#endregion


# start the GUI
gui.mainloop()

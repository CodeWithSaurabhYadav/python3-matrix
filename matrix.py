#!/use/bin/python3

#This multicolur matrix program is written by TechMyth
#instagram - www.instagram.com/this.is.saurabh.official
#youtube - https://www.youtube.com/channel/UCafj9WZVz0hYCZhk882oLLQ
#twitter - https://twitter.com/T3CHMYTH

#importing modules
import random as rd
from colored import fg, bg , attr #pip install colored or pip3 install colored
import string as st
import time
import os

#defining terms
reset = attr("reset")

#defining colors
green = fg(47) + bg(232)
pink = fg(165) + bg(232)
red = fg(9) + bg(232)
blue = fg(4) + bg(232)
yellow = fg(3) + bg(232)
white = fg(255) + bg(232)
once = fg(22) + bg(232)

#main matrix program

#types of matrix
def matrixes():
    dash = "-"
    print ( once + "You Have Two Types Of Matrix Available" + reset )
    print ( green + "1. Character Matrix" + reset )
    print ( green + "2. Binary Matrix" + reset )
    print ( dash*55 )
#color_options for matrix
def color_options():
    dash = "-"
    print ( once + "You Have Available Matrix Colors Avaible" + reset )
    print ( green + "1. Green (default)" + reset )
    print ( pink + "2. Pink" + reset )
    print ( red + "3. Red" + reset )
    print ( blue + "4. Blue" + reset )
    print ( yellow + "5. Yellow" + reset )
    print ( white + "6. White" + reset )
    print ( dash*55 )
    print ( red + "Note : " + reset + "\n" + blue + "You must only input above coluor number." + reset )
    print ( red + "If you enter any other number default color will be used." + reset )
    print ( dash*55 )

#choosing matrix color here
def matrix_color():
    dash = "-"
    color_options()

    while True:
        try:
            try:
                mat = int(input( "Your colour choice : " ))
                print ( dash*55 )
                break
            except ValueError:
                print ( red + "Only number from 1-6 are allowed" + reset )
        except KeyboardInterrupt:
            print ( red + "Only number from 1-6 are allowed" + reset )
    matrixes()
    def matrix_prog():
        while True:
            try:
                try:
                    mat_option = int(input( blue + "Enter the Option : " + reset ))
                    break
                except ValueError:
                    print ( red + "Enter a valid otion." + reset )
            except KeyboardInterrupt:
                print ( red + "Enter a valid option." + reset )
        if mat_option == 1 :
            s1 = st.ascii_letters*2
            s2 = st.digits*2
            s3 = st.punctuation*3
            lst = []
            lst.extend(s1)
            lst.extend(s2)
            lst.extend(s3)
            lst =  lst * 50
        elif mat_option == 2:
            s1 = "01"*50
            lst = []
            lst.extend(s1)
            lst = lst*50
        else :
            print ( red + "Wrong Input" + reset )
            matrix_prog()
        def default():
            while 1 < 2 :
                #terminal size
                row, column = os.popen('stty size','r').read().split()
                rows = int(row) 
                columns = int(column)
                #green matrix
                rd.shuffle(lst)
                matrix = ("".join(lst[:columns]))
                print ( green + matrix + reset )
        if mat == 1 :
            default()
        elif mat == 2 :
            while 1 < 2 :
                #terminal size
                row,column = os.popen('stty size','r').read().split()
                rows = int(row)
                columns = int(column)
                #pink matrix
                rd.shuffle(lst)
                matrix = ("".join(lst[:columns]))
                print ( pink + matrix + reset )
        elif mat == 3 :
            while 1 < 2 :
                #terminal size
                row, column = os.popen('stty size','r').read().split()
                rows = int(row)
                columns = int(column)
                #red matrix
                rd.shuffle(lst)
                matrix = ("".join(lst[:columns]))
                print ( red  + matrix + reset )        
        elif mat == 4 :
            while 1 < 2 :
                #terminal size
                row, column = os.popen('stty size','r').read().split()
                rows = int(row)
                columns = int(column)
                #blue matrix
                rd.shuffle(lst)
                matrix = ("".join(lst[:columns]))
                print ( blue + matrix + reset )
        elif mat == 5 :
            while 1 < 2 :
                row, column = os.popen('stty size','r').read().split()
                rows = int(row)
                columns = int(column)
                #yellow matrix
                rd.shuffle(lst)
                matrix = ("".join(lst[:columns]))
                print ( yellow + matrix + reset )
        elif mat == 6 :
            while 1 < 2 :
                #terminal size
                row, column = os.popen('stty size','r').read().split()
                rows = int(row)
                columns = int(column)
                #white matrix
                rd.shuffle(lst)
                matrix = ("".join(lst[:columns]))
                print ( white + matrix + reset )
        else :
            print ( red + "No colour found on you choosen option" + reset )
            print ( green +  "Default Color Green Is Used" + reset )
            print ( green + "Matrix starting in 5 seconds" + reset  )
            time.sleep(5)
            default()
    matrix_prog()

#welcome as start up
def welcome():
    while True:
        try:
            try:
                name = str(input( blue + "\tEnter your name : " + reset ))
                break
            except ValueError:
                print ( red + "Enter valid Name" + reset )
        except KeyboardInterrupt:
            print ( red + "Enter valid Name." + reset )
    print ( green + "\tWELCOME TO MATRIX WORLD " + name + reset )
    print(red + "\t\tHAA! HAA! HAA!" + reset)
    while True:
        try:
            start = input( yellow + "Press any key or enter to satrt the Matrix" + reset + "\n" )
            break
        except KeyboardInterrupt:
            matrix_color()
    matrix_color()

if __name__ == "__main__":
    print ( red + "Author" + reset + '' +  red + '-' + reset + '' + red + "T3CHMYTH" + reset + '\n' )
    while True:
        try:
            welcome()
        except KeyboardInterrupt:
            pass
        finally:
            print ("\n")
            os.system("clear")
            exit()


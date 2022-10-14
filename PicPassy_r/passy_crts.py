import enum
from tracemalloc import start
from PicPassy_r.passy import regsz_passer, srt_wrt, rd_that
import os


def usr_get():
    print("-" * 32)
    get_input_name = input("enter your name with numbers : ")
    get_input = input("enter your password \nto store as a pic : ")
    if len(get_input) < 99:
        regsz_passer(get_input_name,get_input)
        print("-" * 32)
        print('succesfully created your PicPassy...look for the filename ' + get_input_name+'.jpg')
        print('Note: dont every share this picture to anyone')
    else:
        print("Error: Picpassy can hold up to  98 characters only !!..")

def usr():
    print("welcome to PicPassy")
    print("copyright @ Suresh P | All Rights Reserved")
    print(" ")

    runner = True

    while runner:
        str_lk = ["create a PicPassy picture", "decrypt your PicPassy to show your password","quit"]  

        for y, x in enumerate(str_lk, start=0):
            print(str(y + 1)+ "." + x)
        opt = int(input("choose the option: "))

        if opt == 1:
            usr_get()
            print(" ")
        if opt == 2:
            print("---------------------------------------------------")
            filename = str(input("please enter your filename with extension: "))
            try:
                print("Your stored picpassy: ")
                print(rd_that(filename))
            except Exception as err:
                print('oops! you are incorrectly enter the filename')
                print(" ")
        if opt == 3:
            runner = False

usr()

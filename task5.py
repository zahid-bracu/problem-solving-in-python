# -*- coding: utf-8 -*-
"""Task5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GGus3nYAUoOE-09kPrThhjX62vfAWd2N
"""

'''
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
'''
print("Please Enter the file name")
file_name=input()
files=file_name.split(".")
print("File extension name : "+files[1])
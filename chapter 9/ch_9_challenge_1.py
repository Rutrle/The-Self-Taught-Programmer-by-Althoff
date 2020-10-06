import os


path = r"C:\Users\rutrl\OneDrive\Plocha\Python_MAIN\The-Self-Taught-Programmer-by-Althoff\chapter 9\file_for_reading.txt"
with open(path, "r") as f:
    reader = f.read()
    print(reader)

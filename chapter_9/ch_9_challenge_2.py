import os


path = r"C:\Users\rutrl\OneDrive\Plocha\Python_MAIN\The-Self-Taught-Programmer-by-Althoff\chapter 9\answers.txt"

answer = input(
    "Mirror mirror on the wall, who is the prettiest of them all? : ")

with open(path, "w") as f:
    f.write(answer)

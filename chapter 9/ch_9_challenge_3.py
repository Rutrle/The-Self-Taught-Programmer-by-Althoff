import os
import csv


path = r"C:\Users\rutrl\OneDrive\Plocha\Python_MAIN\The-Self-Taught-Programmer-by-Althoff\chapter 9\list_csv.csv"

list_overall = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic",
                                                                   "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

directory = os.getcwd()

with open(os.path.join(directory, "chapter 9", "list_csv.csv"), "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for i in range(3):
        w.writerow(list_overall[i])
        print(list_overall[i])

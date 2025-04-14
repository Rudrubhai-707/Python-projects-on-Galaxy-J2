import datetime as dt
import csv
import os
import random

print("Welcome to the ultimate expense tracker!")
def AddExpenses():
    filename = input("Enter the name of your expense file: ")
    if os.path.exists(f"{filename}.csv"):
        newopt = int(input("The file already exists!\n1. Enter a new name \n2. Replace the file\n: "))
        if newopt == 1:
            filename = input("Enter new name for the file: ")
            os.system(f"touch {filename}.csv")
        elif newopt == 2:
            os.system(f"rm -rf {filename}.csv")
            os.system(f"touch {filename}.csv") 
        else:
            filename = filename + str(random.randint(100, 9999))            
            print(f"A random file named {filename} is being generated!")            
    exp = ""
    with open(f"{filename}.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
    while exp.lower() != "done":
        exp = input("Enter done if 'done' else press Enter to skip:")
        if exp.lower() == "done":
            print("Records Saved ✓ !!")    
            break 
        categories = ["Food", "Entertainment", "Travel/Transport", "Health",  "Others"]
        print("Select category:-")
        for ind, category in enumerate(categories):
            print(f"{ind+1}. {category}")
        catnum = ""
        while not catnum.isdigit():
            catnum = input("Enter the number of category: ")
            if catnum.isdigit():
                break
        categnum = int(catnum)                
        categ = categories[categnum - 1]
        desc = input("Describe this expense: ")
        amount = int(input("Enter amount in dollars: "))
        date = dt.datetime.now().strftime('%Y-%m-%d')
        with open(f"{filename}.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, categ, f"${amount}", desc])
            
def ViewExpenses():
    filename = ""
    while not os.path.exists(filename):
        file = input("Enter the name of csv file with expense records: ")
        filename = f"{file}.csv"
        if os.path.exists(filename):
            break
    with open(filename, "r") as file:
        data = csv.DictReader(file)
        l = [sets for sets in data]  
         
    for rec in l:
        print(f"""
---------------------------------        
Date: {rec["Date"]}
Category: {rec["Category"]}
Amount: {rec["Amount"]}
Description: {rec["Description"]}
---------------------------------""")        

def ViewTotalExpense():
    filename = ""
    while not os.path.exists(filename):
        file = input("Enter the name of csv file with expense records: ")
        filename = f"{file}.csv"
        if os.path.exists(filename):
            break
    with open(filename, "r") as file:
        data = csv.DictReader(file)
        l = [sets for sets in data]
        total = int(0)
        for rec in l:
            spent = int(rec["Amount"][1:])
            total += spent
            print(f"""
{rec["Date"]}: ${spent}""")
    print(f"\nTotal: ${total}")
    
def CatDisplay(listname, category):
        if listname:
            print(f"""
*********************************      
{category} expenditure:-
*********************************         """)
            for rec in listname:
                print(f"""
Date: {rec["Date"]}
Amount: {rec["Amount"]}
Description: {rec["Description"]}
---------------------------------""")     
def ViewExpenseByCat():
    filename = ""
    while not os.path.exists(filename):
        file = input("Enter the name of csv file with expense records: ")
        filename = f"{file}.csv"
        if os.path.exists(filename):
            break
    with open(filename, "r") as file:
        data = csv.DictReader(file)
        l = [sets for sets in data]
        foodexp = [sets for sets in l if sets["Category"] == "Food"]
        entexp = [sets for sets in l if sets["Category"] == "Entertainment"]
        ttexp = [sets for sets in l if sets["Category"] == "Travel/Transport"]
        hltexp = [sets for sets in l if sets["Category"] == "Health"]
        othexp = [sets for sets in l if sets["Category"] == "Others"]
        CatDisplay(foodexp, "Food")
        CatDisplay(entexp, "Entertainment")
        CatDisplay(ttexp, "Travel/Transport")
        CatDisplay(hltexp, "Health")
        CatDisplay(othexp, "Others")
        
if __name__ == "__main__":
    while True:
        try:
            choice = int(input(
                "\nWhat would you like to do?\n"
                "1. Add expense\n"
                "2. View all expenses\n"
                "3. View total spent\n"
                "4. View expense by category\n"
                "5. Exit\n"
                "Enter your choice: "
            ))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            AddExpenses()
        elif choice == 2:
            ViewExpenses()
        elif choice == 3:
            ViewTotalExpense()
        elif choice == 4:
            ViewExpenseByCat()
        elif choice == 5:
            print("Thanks for using THE ULTIMATE EXPENSE TRACKER!")
            break
        else:
            print("Invalid Choice. Try again.")
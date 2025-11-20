
schedule = {} #Empty dictionary to hold schedule
import time


#parameter: temp_sched is schedule dictionary, draft before classes are added
def build_mod(temp_sched, num): 
    print (f"Enter Mod {num} Classes")

    #colect input
    classA = input("A Block class: ")
    teachA = input("Teacher: ")
    classB = input("B Block class: ")
    teachB = input("Teacher: ")
    classC = input("C Block class: ")
    teachC = input("Teacher: ")

    #save classes in dictionary and what to print
    temp_sched[f"Mod {num}"] = {
                "A Block": classA + " with " + teachA,  
                "B Block": classB + " with " + teachB,
                "C Block": classC + " with " + teachC  
            }
    return temp_sched

#temp dblock sched
def build_dblock(temp_sched): 
    print(f"Enter D Block Classes")

    #input
    fall = input("Fall: ")
    winter = input("Winter: ")
    spring = input("Spring: ")

    #add dblock to dictionary
    temp_sched["D Block"] = {
        "Fall Aug 20/25 - Oct 31  ": fall,
        "Winter Nov 3/4 - Feb 20  ": winter,
        "Spring Feb 23/24 - May 29  ": spring
    }
    return temp_sched

def main ():
    print ("welcome")
    time.sleep(1)

    global schedule #makes schedule editiable so i can add them together and it doesn't restart everytime
    modnum = None #create variable

    mod_dates = {
        "Mod 1": "Aug 27 - Oct 2",
        "Mod 2": "Oct 6 - November 6",
        "Mod 3": "November 10 - December 19",
        "Mod 4": "January 5 - February 6",
        "Mod 5": "February 10 - March 13",
        "Mod 6": "March 30 - April 30",
        "Mod 7": "May 4 - June 5"
    }

    choice = ""
    while choice != "4": #keep working until chooses 4
        print("What would you like to do?")
        time.sleep(1)
        print("1. Add/Edit a mod")
        print("2. Add/Edit a Dblock")
        print("3. View schedule")
        print("4. Quit")
        time.sleep(1)
        choice = input("Please Enter (1, 2, 3, 4)\n>")

        if choice == "1":

            modnum = ""
            modopt = ["1", "2", "3", "4", "5", "6", "7"]
            
            while modnum not in modopt:    
                modnum = input("Which Mod would you like to work on? (1-7)\n>")

                if modnum not in modopt:
                    print("Please enter a number 1-7")
            
            schedule = build_mod(schedule, modnum) #adds info to dictionary


        elif choice == "2":
            schedule = build_dblock(schedule)

        elif choice == "3": 
            print(f"Current Schedule:")
            time.sleep(1)

            for mod in schedule:
                if mod in mod_dates:
                    print (f" {mod}, {mod_dates[mod]}") #print final sched
                    for blocks in schedule[mod]:
                        
                        print (f" {blocks}, {schedule[mod][blocks]} ") #adds Mod Dates
                else:
                    for season in schedule["D Block"]:
                        print(f" {season}: {schedule['D Block'][season]}") #includes dblock in print
                    time.sleep(1)

            correct = input("does this look correct? (y/n)\n>").lower()
            
            if correct == ("y"):
                    print("Great! You can quit or add more.")
                    continue

            elif correct == ("n"):
                print ("Ok, you can edit the Mod by re-entering the # and info.")
                time.sleep(1)
                modnum = None
                continue

            else:print("Please enter y/n")

        elif choice == "4": 
            print ("bye")

        else: 
            print("Please type 1, 2, 3, or 4")

main()
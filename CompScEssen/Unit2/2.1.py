#BROWNTOWN BURGER JOINT POINT OF SALE SOFTWARE
#VERSION 1.21 LAST REVISION DATE 3/11/2024


#VARIABLES
orderComplete = False
totalCost = 0
tax = 0.06

#WELCOME THE USER TO THE POINT OF SALE(POS)
print()
print()
print("Welcome to the Browntown Burger Joint, voted 2nd best Burger in Browntown")
print()

#ASK THEM FOR THEIR NAME AND STORE IT IN name
name = input("Can I have your name please?  ")
print()
print("Thanks " + name)
print()
print()


#POINT OF SALE LOOP
while orderComplete == False:
    #STAY IN THIS LOOP UNTIL THEY SELECT "COMPLETE ORDER"
    print()
    print ("What would you like to order: Burgers, Sides, Drinks, Complete Order.")
    menu = input("-> ")
    
    
    if menu == "Burgers":
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following burgers:")
        print("1: Hamburger $5.50")
        print("2: Cheesebuger $6.00")
        print("3: Western burger (Cheese, onion, western sauce) $6.75")
        print()
        burgerChoice = input("What would you like (input a number 1-3): ")
        #BURGER 1: HAMBURGER
        if burgerChoice == "1":
            totalCost = totalCost + 5.50
            print("You added Hamburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 2: CHEESEBURGER
        elif burgerChoice == "2":
            totalCost = totalCost + 6.00
            print("You added Cheeseburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 3: WESTERN BURGER
        elif burgerChoice == "3":
            totalCost = totalCost+ 6.75
            print("You added Western Burger to your order")
            print("Your total cost so far: $", totalCost)
        
        #BURGER 4: ADD ONE HERE
            #ADD A NEW BURGER OPTION AND UPDATE ALL CODE ABOVE TO MAKE IT WORK


            
        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("please make a valid choice")
        
    elif menu == "Sides":
        print("We offer the following sides:")
        print("1: Fries $1.50")
        print("2: Onion Rings $3.00")
        print("3: Mozzarella Sticks $3.00")
        sideChoice = input("What would you like (input a number 1-3): ")
        if sideChoice == "1":
            totalCost = totalCost + 1.50
            print("You added Fries to your order")
            print("Your total cost so far: $", totalCost)
        elif sideChoice == "2":
            totalCost = totalCost + 3.00
            print("You added Onion Rings to your order")
            print("Your total cost so far: $", totalCost)
        elif sideChoice == "3":
            totalCost = totalCost + 3.00
            print("You added Mozzarella Sticks to your order")
            print("Your total cost so far: $", totalCost)
        else:
            print("please make a valid choice")
        #Add your Code/Comments Here for sides
        #Add at least three sides
        
    elif menu == "Drinks":
        print("We offer the following Drinks:")
        print("1: Small Liquid $2.75")
        print("2: Medium Liquid $3.50")
        print("3: Large Liquid $4.25")
        drinkChoice = input("What would you like (input a number 1-3): ")
        if drinkChoice == "1":
            totalCost = totalCost + 2.75
            print("You added Small Liquid to your order")
            print("Your total cost so far: $", totalCost)
        elif drinkChoice == "2":
            totalCost = totalCost + 3.50
            print("You added Medium Liquid to your order")
            print("Your total cost so far: $", totalCost)
        elif drinkChoice == "3":
            totalCost = totalCost + 4.25
            print("You added Large Liquid to your order")
            print("Your total cost so far: $", totalCost)
        else:
            print("please make a valid choice")
        #Add Your code/Comments here for Drinks
        #Add at least three drinks
    
    elif menu == "Complete Order":
        #IF THEY SELECT COMPLETE ORDER, SET THE ORDERCOMPLETE TO TRUE
        orderComplete = True
        print()

        #GIVE THEM THEIR TOTALS
        #Finish this section to give you a grand total as well as print your complete order
        print("order finished")
        print("You have ordered")
        print("Subtotal: $", totalCost)
        totalTax = float(totalCost) * tax
        print("Total Tax: $", totalTax)
        grandTotal = float(totalCost) + (totalTax)
        print("Grand Total: $", grandTotal)
        
 
        
    else:
        print("Sorry, not a valid choice, please start over...")

#THE USER ONLY GETS HERE IF THEY FINISH THEIR ORDER
print("Thank you for eating with us!")
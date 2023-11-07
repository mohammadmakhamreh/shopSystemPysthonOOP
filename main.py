import random
import sys
import json


# Mahmoud Hamdan - 1201134
# Mohammad Makhamreh - 1200227

class Product:
    def __init__(self, Product_id, Product_name, Product_category, Price, Inventory, Supplier, Has_an_offer,Offer_price, Valid_until):
        self.Product_id = int(Product_id)
        self.Product_name = Product_name
        self.Product_category = Product_category
        self.Price = float(Price)
        self.Inventory = int(Inventory)
        self.Supplier = Supplier
        self.Has_an_offer = int(Has_an_offer)
        self.Offer_price = float(Offer_price)
        self.Valid_until = Valid_until

    def __str__(self):
        print(f"Product ID : {self.Product_id}")
        print(f"Product Name : {self.Product_name}")
        print(f"Product category : {self.Product_category}")
        print(f"Price of product : {self.Price}")
        print(f"Inventory : {self.Inventory}")
        print(f"Supplier of the product : {self.Supplier}")
        if self.Has_an_offer == 1:
            print(f"Product {self.Product_id} has an offer ")
            print(f"Offer price is {self.Offer_price}")
            print(f"The offer is valid until : {self.Valid_until}")
        else:
            print(f"Product {self.Product_id} is not on offer")
        print()





class User:
    def __init__(self, User_id, User_name, User_DoB, Role, Active):
        self.User_id = int(User_id)
        self.User_name = User_name
        self.User_DoB = User_DoB
        self.Role = Role
        self.Active = int(Active)
        self.Basket = Basket
        self.Order = int(Order)

    def __str__(self):
        print(f"User ID : {self.User_id}")
        print(f"User name : {self.User_name}")
        print(f"User Date Of Birth : {self.User_DoB}")
        print(f"User role : {self.Role}")
        if self.Active == 1:
            print(f"User {self.User_id} is active ")
        else:
            print(f"User {self.User_id} is not active ")
        print(f"Basket of {self.User_id} : {self.Basket}")
        if self.Order == 1:
            print(f"User {self.User_id} finished adding items to the basket")
        else:
            print(f"User {self.User_id} still adding items to the basket")
        print()







class Shopper(User):
    def __init__(self, User_id, User_name, User_DoB, Role, Active, Basket, Order):
        self.User_id = int(User_id)
        self.User_name = User_name
        self.User_DoB = User_DoB
        self.Role = Role
        self.Active = int(Active)
        self.Basket = Basket
        self.Order = int(Order)

    def __str__(self):
        print(f"User ID : {self.User_id}")
        print(f"User name : {self.User_name}")
        print(f"User Date Of Birth : {self.User_DoB}")
        print(f"User role : {self.Role}")
        if self.Active == 1:
            print(f"User {self.User_id} is active ")
        else:
            print(f"User {self.User_id} is not active ")
        print(f"Basket of {self.User_id} : {self.Basket}")
        if self.Order == 1:
            print(f"User {self.User_id} finished adding items to the basket")
        else:
            print(f"User {self.User_id} still adding items to the basket")
        print()

class Admin(User):
    def __init__(self, User_id, User_name, User_DoB, Role, Active):
        self.User_id = int(User_id)
        self.User_name = User_name
        self.User_DoB = User_DoB
        self.Role = Role
        self.Active = int(Active)


    def __str__(self):
        print(f"User ID : {self.User_id}")
        print(f"User name : {self.User_name}")
        print(f"User Date Of Birth : {self.User_DoB}")
        print(f"User role : {self.Role}")
        if self.Active == 1:
            print(f"User {self.User_id} is active ")
        else:
            print(f"User {self.User_id} is not active ")

        print()



currentUserID = 0
currentUserRole = ""


def printAdminMenu():
    adminMenu = """
    Select a choice from the following menu please
    *************************************************************
    1. Add product 
    2. Place an item on sale 
    3. Update product 
    4. Add a new user 
    5. Update user 
    6. Display all users 
    7. List products 
    8. List shoppers 
    9. Execute order 
    10. Save products to a file 
    11. Save users to a text file 
    12. Exit
    *************************************************************
    """
    print(adminMenu)


def printShopperMenu():
    ShopperMenu = """
    *************************************************************
    1. List products 
    2. Add product to the basket 
    3. Display basket 
    4. Update basket 
    5. Place order
    6. Exit 
    ************************************************************
    """
    print(ShopperMenu)


############### main ###################

products = []
users = []
with open('products.txt', 'r') as productsFile:
    for line in productsFile:
        data = line.strip().split(';')
        product1 = Product(*data)
        products.append(product1)

print("products file loaded successfully\n")
# for p in products:
# print(p.__str__())

with open('users.txt', 'r') as usersFile:
    for line1 in usersFile:
        userInfo = line1.strip().split(';')

        if len(userInfo)==7:
            User_id, User_name, User_DoB, Role, Active, BasketString, Order = userInfo
            Basket = eval(BasketString)
            user1 = Shopper(User_id, User_name, User_DoB, Role, Active, Basket, Order)
            users.append(user1)
        elif len(userInfo)==5:
            User_id, User_name, User_DoB, Role, Active = userInfo
            user1 = Admin(User_id, User_name, User_DoB, Role, Active)
            users.append(user1)
print("Users File loaded successfully")

# check the role of the user if Admin or Shopper:
flag3 = 0
userId = input("Welcome To M2Linux Shop, Please Enter your ID please : ")
if str(userId).isdigit():
    userId = int(userId)
    for user in users:

        if user.User_id == userId:
            flag3 = 1
            print("user found. \n ")
            user.__str__()
            currentUserID = userId
            currentUserRole = user.Role;

        if flag3 == 0:
            print("user not Found, Access Denied.")
else:
    print("invalid, user ID must be number.")
print(currentUserRole)

if currentUserRole == "admin":
    printAdminMenu()
    choice = int(input("Enter your choice please : "))
    while choice != 0:
        if choice == 1:
            # Add product (admin-only) code here
            Product_id = int(input("Enter the product ID: "))
            Product_name = input("Enter the product name: ")
            Product_category = input("Enter the Category: ")
            Price = float(input("Enter the product price: "))
            Inventory = int(input("Enter the product inventory: "))
            Supplier = input("Enter the product supplier: ")
            Has_an_offer = int(input("Enter if the product offer 0 for no 1 for yes. : "))
            if (Has_an_offer == 1):
                Offer_price = input("Enter the offer price: ")
            else:
                Offer_price = 0
            Valid_until = input("Enter the valid date dd/mm/yy : ")
            newProduct = Product(Product_id, Product_name, Product_category, Price, Inventory, Supplier, Has_an_offer,
                                 Offer_price, Valid_until)
            products.append(newProduct)
            # for productt in products:
            # productt.__str__()
            print("Adding a product has been done successfully")
        elif choice == 2:
            flag8 = 0
            productID = int(input("Enter the Product Id to place it on sale : "))
            # Place an item on sale (admin-only) code here
            for pro in products:
                if (pro.Product_id == productID):
                    flag8 = 1
                    print("Product founded. \n ")
                    pro.__str__()
                    if pro.Has_an_offer == 0:
                        ans = int(input("Still want to place it on sale? 0 for no / one for yes. "))
                        if (ans == 1):
                            pro.Has_an_offer = 1
                            print("The Product placed on sale successfully.")
                            offerPrice = float(input("Enter the offer Price please: "))
                            validUntil = input("Enter the valid until date: dd/mm/yy : ")
                            pro.Offer_pSSrice = offerPrice
                            pro.Valid_until = validUntil
                            print("Product on Sale now. May god Bless you sir")
                        else:
                            print("Process Cancelled Successfully")
                    else:
                        print("Product is already on sale")

            if flag8 == 0:
                print("Product is not found, try again.")
        # placing an item on sale method done.
        elif choice == 3:

            # Update product (admin-only)
            productID = int(input("Enter the product ID to update its info."))
            for pro in products:
                if pro.Product_id == productID:
                    x = -1
                    while (x != 9):
                        print("Product found, what do you want to update? ")
                        updateChoice = int(input("""
                                 1.Product_name,
                                 2.Product_category
                                 3.Price
                                 4.Inventory
                                 5.Supplier
                                 6.Has_an_offer
                                 7.Offer_price (if the product has an offer)
                                 8.Valid_until (if the product has an offer)
                                 9.Quit Editing
                        """))
                        x = updateChoice
                        match updateChoice:
                            case 1:
                                newName = input("Enter the updated name of the product: ")
                                pro.Product_name = newName
                                print("Updating the Product Name done successfully ")
                            case 2:
                                newCategory = input("Enter the updated Category of the product: ")
                                pro.Product_category = newCategory
                                print("Updating the Product Name done successfully ")
                            case 3:
                                newPrice = float(input("Enter the updated Price of the product: "))
                                pro.Offer_price = newPrice
                                print("Updating the Product Price done successfully ")
                            case 4:
                                newInventory = int(input("Enter the updated inventory of the product: "))
                                pro.Inventory = newInventory
                                print("Updating the Product Inventory done successfully ")
                            case 5:
                                newSupplier = input("Enter the updated Supplier of the product: ")
                                pro.Supplier = newSupplier
                                print("Updating the Product Supplier done successfully ")
                            case 6:
                                newOfferState = input("Enter the updated Offer State of the product: ")
                                pro.Has_an_offer = newOfferState
                                if (newOfferState == 1):
                                    newOfferPrice = float(input("Enter the offer Price"))
                                    pro.Offer_price = newOfferPrice
                                print("Updating the Product Offer State done successfully ")
                            case 7:
                                if (pro.Has_an_offer == 1):
                                    newOfferPrice = float(input("Enter the offer Price"))
                                    pro.Offer_price = newOfferPrice
                                    print("Updating the Product Offer Price done successfully")
                                else:
                                    print("Product is not on sale to update its sale's price.")
                            case 8:
                                if (pro.Has_an_offer == 1):
                                    newOfferDate = input("Enter the until date of the offer sale: ")
                                    pro.Valid_until = newOfferDate
                                    print("Updating the Product Offer valid date done successfully")
                                else:
                                    print("Product is not on sale to update its sale's valid until date.")
                            case 9:
                                print("Updating Process done.")



        elif choice == 4:
            # Add a new user (admin-only)

            # function to suggest a random variable of 6 digits unique for the new User ID
            def suggestUserID():

                x = random.randint(100000, 999999)
                for y in users:
                    if (y.User_id == x):
                        x = random.randint(100000, 999999)
                return x


            newUserId = int(input("Please Enter the User ID: "))
            for user1 in users:
                if (user1.User_id == newUserId):
                    print("User Id already exist try again please")
                    print("Suggested available userID: ", suggestUserID())
                    newUserId = int(input("Please Enter the User ID: "))

            newUserName = input("Please Enter the User Name: ")
            userDoB = input("Please Enter the user's Date of Birth")
            newRole = input("Please Enter the Role of the user (admin/shopper) : ")
            newActive = int(input("Enter 1 if the user active, 0 if not: "))
            newBasket = {}
            newOrder = 0
            if newRole=="shopper":
                user2 = Shopper(newUserId, newUserName, userDoB, newRole, newActive, newBasket, newOrder)
                users.append(user2)
            else:
                user2 = Admin(newUserId, newUserName, userDoB, newRole, newActive)
                users.append(user2)
            print("Adding a new user done successfully.")

        elif choice == 5:
            # Update user (admin-only)
            print("Updating a user...")
            updateUserID = int(input("Enter the user ID to update its info."))
            for userU in users:
                if userU.User_id == updateUserID:
                    x = -1
                    while (x != 5):
                        print(
                            "User found, what do you want to update? ")  ################################################
                        User_id, User_name, User_DoB, Role, Active, Basket, Order
                        updateChoice = int(input("""

                                             1.User name
                                             2.User Date of Birth
                                             3.Role
                                             4.Active
                                             5.Quit Editing

                                    """))
                        x = updateChoice
                        match updateChoice:
                            case 1:
                                userU.User_name = input("Enter the updated name of the User: ")
                                print("Updating the User Name done successfully ")
                            case 2:
                                userU.User_DoB = input("Enter the new Date of Birth of the User: ")
                                print("Updating the Date of birth done successfully ")
                            case 3:
                                userU.Role = input("Enter the updated Role of the User: ")
                                print("Updating the Role of the User done successfully ")
                            case 4:
                                userU.Active = int(input("Enter the updated active status: "))
                                print("Updating the active status done successfully ")
                            case 5:
                                print("Updating Process done.")




        elif choice == 6:
            dispSel = int(input("""
                        This is how you can display the information
                        1. All users
                        2. Only shoppers
                        3. Only admins

                        Enter your choice please : """))
            match dispSel:
                case 1:
                    for u in users:
                        u.__str__()
                        print(
                            "--------------------------------------------------------------------------------------------")

                case 2:
                    for u in users:
                        if u.Role == "shopper":
                            u.__str__()
                            print(
                                "--------------------------------------------------------------------------------------------")

                case 3:
                    for u in users:
                        if u.Role == "admin":
                            u.__str__()
                            print(
                                "--------------------------------------------------------------------------------------------")

                case _:
                    print("Invalid input, you should chose 1,2 or 3 only")
            # print("All users and their info: ")
            # for u in users:
            #    u.__str__()
            # print("Displaying all users done successfully.")

        elif choice == 7:
            # List products (admin and shopper)
            print("""
                1.All: all products
                2. Offers: products that have offers/discount
                3.Category: products belonging to a specific category. The user must input the name of the
                category.
                4. Name: products with the name entered by the user. It's important to note that a single product
                might be present in the system but offered by various suppliers""")
            listpr = int(input("Enter your Option of listing  please : "))
            if listpr == 1:
                for p in products:
                    print(p.__str__())

            elif listpr == 2:
                for p in products:
                    if p.Has_an_offer == 1:
                        p.__str__()

            elif listpr == 3:
                cat = input("Enter the category please : ")
                for p in products:
                    if p.Product_category == cat:
                        p.__str__()
                        flag1 = 1
                        if flag1 != 1:
                            print("Category is not found")
            elif listpr == 4:
                name = input("Enter the name of the product : ")
                for p in products:
                    if p.Product_name == name:
                        p.__str__()
                        flag2 = 1
                        if flag2 != 1:
                            print("No such product")
            else:
                print("Invalid input")

        elif choice == 8:
            criteria = int(input("""
                        SPECIFY how to list the shoppers by inserting a number of the following :
                        1. All Shoppers
                        2. All shoppers that have added products for purchase to the basket.
                        3. All shoppers that have made an order and the order is still not processed by the admin.  """))
            match criteria:
                case 1:
                    print("All Shopers: ")
                    for shopper in users:
                        if (shopper.Role == "shopper"):
                            shopper.__str__()
                case 2:
                    print("Shoppers with items in the basket:")
                    for shopper in users:
                        if (shopper.Role == "shopper" and len(shopper.Basket) > 0):
                            shopper.__str__()
                case 3:
                    print("Shoppers has unprocessed orders:")
                    for shopper in users:
                        if (
                                shopper.Role == "shopper" and shopper.Order == 1):  # when excute the order the (order will back to zero)
                            shopper.__str__()
            # List shoppers (admin) done
            print("Listing shoppers done successfully...")


        elif choice == 9:
            # Execute order (admin-only)
            print("The shoppers that are ready to execute their order are : ")
            for shopper in users:
                if (
                        shopper.Role == "shopper" and shopper.Order == 1):  # when excute the order the (order will back to zero)
                    shopper.__str__()

            id1 = int(input("Which shopper ID do you need to serve first : "))
            flag10 = 0
            for shopper in users:
                if int(shopper.Order) == 1 and shopper.User_id == id1:
                    for key, value in shopper.Basket.items():
                        for pr in products:
                            if pr.Product_id == int(key):
                                pr.Inventory = pr.Inventory - int(value)
                                print("Sucessfully minused ")
                                flag10 = 1

                    shopper.Basket.clear()
                    shopper.Order = 0
                    print(
                        f"Order has been executed successfully, and the basket for {shopper.User_name} is : {shopper.Basket}")
                    with open('products.txt', 'w') as pfile:
                        for p in products:
                            pfile.write(
                                f"{p.Product_id};{p.Product_name};{p.Product_category};{p.Price};{p.Inventory};{p.Supplier};{p.Has_an_offer};{p.Offer_price};{p.Valid_until}\n")

                    with open('users.txt', 'w') as ufile:
                        for u in users:
                            ufile.write(
                                f"{u.User_id};{u.User_name};{u.User_DoB};{u.Role};{u.Active};{u.Basket};{u.Order}\n")

            if flag10 == 0:
                print("Invalid input, shopper is not found or the shopper is not ready to execute his order ")

        elif choice == 10:
            # Save products to a file (admin-only) code here
            in2 = input("Enter the name of the file to save the products on it : ")
            with open(in2, 'w') as file:
                for p in products:
                    file.write(
                        f"{p.Product_id};{p.Product_name};{p.Product_category};{p.Price};{p.Inventory};{p.Supplier};{p.Has_an_offer};{p.Offer_price};{p.Valid_until}\n")

            print(f"Products saved to {in2} file...")
        elif choice == 11:
            # Save users to a text file (admin-only) code here
            in3 = input("Enter the name of the file to save the users on it : ")
            with open(in3, 'w') as file2:
                for u1 in users:
                    if u1.Role =="shopper":
                        file2.write(
                            f"{u1.User_id};{u1.User_name};{u1.User_DoB};{u1.Role};{u1.Active};{u1.Basket};{u1.Order}\n")
                    else:
                        file2.write(
                            f"{u1.User_id};{u1.User_name};{u1.User_DoB};{u1.Role};{u1.Active}\n")


            print(f"Users saved to {in3} file...")
        elif choice == 12:
            with open('products.txt', 'w') as file4:
                for p in products:
                    file4.write(
                        f"{p.Product_id};{p.Product_name};{p.Product_category};{p.Price};{p.Inventory};{p.Supplier};{p.Has_an_offer};{p.Offer_price};{p.Valid_until}\n")

            with open('users.txt', 'w') as file5:
                for u in users:
                    file5.write(f"{u.User_id};{u.User_name};{u.User_DoB};{u.Role};{u.Active};{u.Basket};{u.Order}\n")
            print("Exiting the program.")
            sys.exit(1)


        else:
            print("Invalid choice. Please select a valid choice.")
            choice = int(input("Enter your choice please : "))
        choice = int(input("Enter your choice please : "))

if currentUserRole == "shopper":
    printShopperMenu()
    choice = int(input("Enter your choice please : "))
    while choice != 0:
        if choice == 1:
            # List products (admin and shopper)
            print("""
                           1.All: all products
                           2. Offers: products that have offers/discount
                           3.Category: products belonging to a specific category. The user must input the name of the
                           category.
                           4. Name: products with the name entered by the user. It's important to note that a single product
                           might be present in the system but offered by various suppliers""")
            listpr = int(input("nter your Option of listing  please : "))
            if listpr == 1:
                for p in products:
                    print(p.__str__())

            elif listpr == 2:
                for p in products:
                    if p.Has_an_offer == 1:
                        p.__str__()

            elif listpr == 3:
                cat = input("Enter the category please : ")
                for p in products:
                    if p.Product_category == cat:
                        p.__str__()
                        flag1 = 1
                        if flag1 != 1:
                            print("Category is not found")
            elif listpr == 4:
                name = input("Enter the name of the product : ")
                for p in products:
                    if p.Product_name == name:
                        p.__str__()
                        flag2 = 1
                        if flag2 != 1:
                            print("No such product")
            else:
                print("Invalid input")

            print("Listing products...")
        elif choice == 2:
            flag00 = 0
            productId = int(input("Enter the Product Id that you want to add to the Basket: "))
            for productI in products:
                if (productI.Product_id == productId):
                    print("Product Found.")
                    productI.__str__()
                    quantity = int(input("Enter the number of items that you want: "))
                    if (quantity > productI.Inventory):
                        print("Sorry, this quntity is not available there is just : ", productI.Inventory)
 #                       quantity = int(input("Enter the number of items that you want: "))
                    else:
                        flag00 = 1
                        for shopper1 in users:
                            if (shopper1.User_id == currentUserID):
                                shopper1.Basket[productId] = quantity
                                print("Adding to the Basket done successfully.")
                                shopper1.__str__()
                                # Add product to the basket done.
                            # if value not in shopper1.Basket:
                            #   print("Invalid product !! ")

            if flag00 == 1:
                print("Adding a product to the basket Done Successfully.")
            else:
                print("Invalid process !!")



        elif choice == 3:
            # Display basket (shopper-only)
            print("Displaying the detailed basket")
            basketCost = 0
            for shopper in users:
                if (shopper.User_id == currentUserID):
                    for key, value in shopper.Basket.items():
                        print(f"{key}, {value}")
                        for item in products:
                            if (item.Product_id == int(key)):
                                item.__str__()
                                print("Number of items: ", value)
                                if (item.Has_an_offer == 1):
                                    itemCost = value * item.Offer_price
                                    basketCost = basketCost + itemCost
                                else:
                                    itemCost = value * item.Price
                                    basketCost = basketCost + itemCost
                                print("Cost of purchase of the product: ", itemCost)
                    print("-------------------------------------------")
                    print("Basket Cost = ", basketCost)
            print("Displaying the basket Done")


        elif choice == 4:
            # Update basket (shopper-only)
            updateOption = int(input("""
                        Please insert the number of the option
                        1. Clear (Remove all products from the basket
                        2. Remove (Remove a specific product from the basket based on product id)
                        3. Update (Change the number of items of a particular product in the basket based on product id)
                        """))
            match updateOption:
                case 1:
                    for shopper in users:
                        if (shopper.User_id == currentUserID):
                            shopper.Basket.clear()
                            print("Clearing the Basket done successfully")
                            shopper.__str__()
                case 2:
                    Pid = input("Enter the Product ID that you want to remove from your Basket : ")
                    for shopper in users:
                        if (shopper.User_id == currentUserID):
                            intPid = int(Pid)
                            if (Pid in shopper.Basket):
                                shopper.Basket.pop(Pid)
                                print("Item removed successfully")
                                shopper.__str__()
                            elif intPid in shopper.Basket:
                                shopper.Basket.pop(intPid)
                                print("Item removed successfully")
                                shopper.__str__()
                            else:
                                print("Product is not in the basket ")

                case 3:
                    Pid = input("Enter the Product ID that you want to update the number of items from your Basket : ")
                    newNumber = int(input("Enter the new number of items you want"))
                    for shopper in users:

                        if (shopper.User_id == currentUserID):
                            intPid = int(Pid)
                            if (Pid in shopper.Basket):
                                shopper.Basket[Pid] = newNumber
                                print("Number of items has been updated successfully")
                                shopper.__str__()
                            elif intPid in shopper.Basket:
                                shopper.Basket[intPid] = newNumber
                                print("Number of items has been updated successfully")
                                shopper.__str__()
                    print("Updating the basket...")




        elif choice == 5:
            # Place order (shopper-only)
            for shopper in users:
                if (shopper.User_id == currentUserID):
                    shopper.Order = 1
                    print("Order Placed to one successfully, waiting the admin to execute the order..")
                    shopper.__str__()

            print("Placing an order...")
        elif choice == 6:

            with open('users.txt', 'w') as file1:
                for u in users:
                    if u.Role == "shopper":
                        file1.write(
                            f"{u.User_id};{u.User_name};{u.User_DoB};{u.Role};{u.Active};{u.Basket};{u.Order}\n")
                    else:
                        file1.write(
                            f"{u.User_id};{u.User_name};{u.User_DoB};{u.Role};{u.Active}\n")

            print("Exiting the program.")
            currentUserRole = ""
            currentUserID = 0
            sys.exit(1)

        else:
            print("Invalid choice. Please select a valid choice.")
            choice = int(input("Enter your choice please : "))
        choice = int(input("Enter your choice please : "))

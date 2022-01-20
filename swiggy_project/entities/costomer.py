from random import choice, choices
from entities.resturant import Resturant
from entities.payment import Payment

class Customer:
    
    def order(self,ch):
        
        resto = Resturant()
       # self.show_restaurant(self)
        # dish = input("Enter the dish required:")
        # print(dish)
        # #dish search in menu of each restaurant
        #if dish is there show it, otherwise ask again for the dish
        choice = "Y"
        ord1 = {}
        while choice =="Y" or choice == 'y':
            

            dish = input("Enter the dish required:")
            ord1[dish]= resto.reg_dic[ch][0][dish]
            print()
            self.choice = input("Do you wish to add more food . Press Y for YES & N for NO: ")
                
            print()
            if self.choice == 'Y' or self.choice == 'y':
                    continue
            elif self.choice == 'N' or self.choice == 'n':
                    break
        print(ord1)
        print("***********************************************************************")
        self.py_choice = input("Do you wish to continue for payment.Press 'Y' for YES & 'N' for NO: ") 
        print()

        if self.py_choice == 'Y' or self.py_choice == 'y':
            Payment.order_payment(ord1)
            

        elif self.py_choice == 'N' or self.py_choice == 'n':
            return



    def show_resturant(self):

        resto = Resturant()
       
        for i in resto.reg_dic.keys():
            print(i)
        ch = input("Select a restaurant(type it's name):")

        if ch == "Archana Grand" or ch == "Tharavadu" or ch== "Gun Powder":
           
            print("Menu:")
            print({k: v for k, v in sorted(resto.reg_dic[ch][0].items(), key=lambda item: item[1])})
            self.order(ch)

        elif choice=="D":

            print({key:value for key,value in resto.reg_dic[0]})
            

        
                
           
        else:
            print("give correct option")

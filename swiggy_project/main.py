from entities.resturant import Resturant
from entities.customer import Customer


def run():
    
        print("Welcome:")
        print()
        user_type = input("Are you a restaurant(R) registering or a customer buying food(C): ")

        if user_type == "R":
            rest = Resturant()
            rest.resto()


        elif user_type == "C":
            cust = Customer()

            cust.show_resturant()

        else:
            print("Please provide valid option")


    
    


if __name__=="__main__":
    run()

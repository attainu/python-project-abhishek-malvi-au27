


class Resturant:
    def __init__(self) -> None:

        self.reg_dic ={"Sarkar":[{"Biryani":300,"Matonsoup":150,"Roti":20,"Chikansoup":100,"Raita":80},3],
                        "Icon":[{"Veg-Biryani":300,"Mix-Veg":100,"Roti":20,"Kaju_kari":150,"DalFry":100},3],
                        "Sayaji":[{"Biryani":300,"Raita":100,"Roti":20,"Rice":90,"Chikansoup":120},3]
                       }

        
    def resto(self):

        ch= input("Do you want to Register(R) or Update(U):")

        if ch == "R":
            self.regist() 
            
        elif ch =="U":
            self.Update()
            
    def regist(self):

            self.reg_dic2={}

            wish = True

            while True:

                if wish == False:

                    break
                print()
                name = input("Enter The resutarant Name: ")
                proc_capacity = int(input("Enter capacity: "))
                menu = self.menu_list()

                self.reg_dic2[name]=[menu,proc_capacity]

                choice = input("do you want to register resturant(T/F):")

                if choice == "T":
                    continue
                else:
                    wish = False

            print(self.reg_dic2)


    def menu_list(self):
        menu = {}
        more = True

        while True:
            if more == False:
                break
            item = input("Enter item name:")
            price = int(input("Enter the price:"))
            menu[item] = price

            choice = input("do you want to add another menu (T/F):")

            if choice == "T":
                continue
            else:
                more = False
        print(menu)
        return menu

    def Update(self):
            menu = {}
            
            for i in self.reg_dic.keys():

                print(i)

            rname =input("Select from above Resturant:")
           

            print({k: v for k, v in sorted(self.reg_dic[rname][0].items(), key=lambda item: item[1])})

            ch = input("do you want to 1.Add,2.Delete,3.modify:")

            if ch == "1":
                item = input("Enter item name:")
                price = int(input("Enter the price:"))
                self.reg_dic[rname][0][item]= price
                print(self.reg_dic[rname][0])

            elif ch =="2":
                item = input("Enter item name:")
                self.reg_dic[rname][0].pop(item)
                #del self.r[item]
                print(self.reg_dic[rname])

            elif ch =="3":

                item = input("Enter item name:")
                price = int(input("Enter price:"))

                self.reg_dic[rname][0][item] = price
                print(self.reg_dic[rname][0])



    
            

   

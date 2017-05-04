#expense passbook

class expense :

    import os
    
    def __init__(self):
        self.nam  = ""
        self.id   = 0
        self.exp  = 0.0
        self.rsn  = ""
        self.dat  = ""
        self.tim  = ""
        
    def entry(self,name):
        
        stop = False
        try:
            while not stop:
            
                print()
                print('\t\t\t\t\t\t\t DATE : \t',date)
                print('\t\t\t\t\t\t\t TIME : \t',tim)
                print()
            
                opt2 = input("Enter e to exit             : \t")
                print()
            
                if opt2 == "E" or opt2 == "e":
                    stop = True
                    main()
                
                else:
                    import os
                    if not os.path.exists('hexpn.txt') :
                        opn = open('hexpn.txt','w')
                        n = 1
                    else:
                        rfi = open('hexpn.txt','r')
                        n=0
                        for lin in rfi:
                            n=n+1
                        n=n+1
                        rfi.close()
                        opn = open('hexpn.txt','a')

                    self.tim = tim
                    self.dat = date
                    self.id  = n
                    self.nam = name
                    self.rsn = input("Enter the reason of expense : \t")
                    self.exp = float(input("Enter the ammount spend     : \t"))
                    opn.write(str(self.id)+"-----"+self.nam+"-----"+self.rsn+"-----"+str(self.exp)+"-----"+str(self.dat)+"-----"+str(self.tim)+"-----"+"\n")
                    opn.close()
                    exp.disply()
        except:
            opn.close()
            print()
            print("Please Enter a valid option")

    def disply(self):

        import os
        if not(os.path.exists('hexpn.txt')) :
            print("Nothing to display")
            main()
        else:
            rf = open('hexpn.txt','r')
            print()
            print()
            info1 = '{0:8s}{1:13s}{2:32s}{3:10s}{4:17s}{5:17s}'.\
                    format("NO.","NAME","REASON","EXPENSE","DATE","TIME")
            print(info1)
            print()
            
            ms=ns=os=us=fs=0.0
            for lin in rf:
                lin = lin.split('-----')
                info = '{0:8s}{1:13s}{2:32s}{3:10s}{4:17s}{5:17s}'.\
                       format(lin[0],lin[1],lin[2],lin[3],lin[4],lin[5])
                print(info)
                if lin[1] == 'User 1':
                    ms = ms + float(lin[3])
                elif lin[1] == 'User 2':
                    ns = ns + float(lin[3])
                elif lin[1] == 'User 3':
                    os = os + float(lin[3])
                elif lin[1] == 'User 4':
                    us = us + float(lin[3])
                elif lin[1] == 'common':
                    fs = fs + float(lin[3])
                else:
                    continue
            print()
            print()
            print("User 1     expense           : \t",ms)
            print("User 2     expense           : \t",ns)
            print("User 3     expense           : \t",os)
            print("User 4     expense           : \t",us)
            print("Common     expense           : \t",fs)
            print()
            print("Total     expense           : \t",ms+ns+os+us+fs)
            print()
            print()
            rf.close()

    def tdsply(self):
        print(""""1. User 1
2. User 2
3. User 3
4. User 4
5. Common
press anything other then (1-5) to exit""")
        print()
        opt1 = input("Enter the option (1-6)      : \t")
        if opt1 == '1':
            nam = "User 1"
        elif opt1 == '2':
            nam = "User 2"
        elif opt1 == '3':
            nam = "User 3"
        elif opt1 == '4':
            nam = "User 4"
        elif opt1 == '5':
            nam = "Common"
        else :
            main()
            
        rf = open('hexpn.txt','r')
        print()
        print()
        info1 = '{0:8s}{1:13s}{2:32s}{3:10s}{4:17s}{5:17s}'.\
                format("NO.","NAME","REASON","EXPENSE","DATE","TIME")
        print(info1)
        print()

        sm=n= 0    
        for lin in rf:
            lin = lin.split('-----')
            if lin[1] == nam:
                n=n+1
                sm = sm + float(lin[3])
                info = '{0:8s}{1:13s}{2:32s}{3:10s}{4:17s}{5:17s}'.\
                       format(lin[0],lin[1],lin[2],lin[3],lin[4],lin[5])
                print(info)
        if n == 0:
            info = '{0:8s}{1:13s}{2:32s}{3:10s}{4:17s}{5:17s}'.\
                   format("-","-","-","-","-","-")
            print(info)
            
        print()
        print(nam,'Total expns       : \t',sm)
        print()
        print()
        
def main():
    print("Expense passbook of Four users")
    ext = False
    try:
        while not ext:
            print()
            print('\t\t\t\t\t\t\t DATE : \t',date)
            print('\t\t\t\t\t\t\t TIME : \t',tim)
            print()
            print("""1.Entry
2.Display
3.Exit""")
            print()
            opt = int(input("Enter the option (1-3)      : \t"))
            print()

            if opt == 1:
                print("""1. User 1
2. User 2
3. User 3
4. User 4
5. Common""")
                print()
                opt1 = input("Enter the option (1-4)      : \t")
                print()
                if opt1 == '1':
                    nam = "User 1"
                elif opt1 == '2':
                    nam = "User 2"
                elif opt1 == '3':
                    nam = "User 3"
                elif opt1 == '4':
                    nam = "User 4"
                elif opt1 == '5':
                    nam = 'Common'
                else :
                    break
                exp.entry(nam)

            elif opt == 2:
                exp.disply()
                exp.tdsply()

            elif opt == 3:
                ext = True

            else:
                print("Invalid input")
            
    except :
            print()
            print("Invalid input plz try again")

import time
global date 
global tim
tm   = list(time.localtime(time.time()))
mon  = {1:'JAN' , 2:'FEB' , 3:'Mar' , 4:'Apr' , 5:'MAY' , 6:'JUN' , 7:'JUL' , 8:'AUG' , 9:'SEP' , 10:'OCT' , 11:'NOV' , 12:'DEC'}
date = str(tm[2])+'  '+mon[tm[1]]+'  '+str(tm[0])
tim  = str(tm[3])+'  '+str(tm[4])+'   '+str(tm[5])

exp = expense()
main()


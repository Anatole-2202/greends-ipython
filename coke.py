#Set the object (integer) money which is equal to 0 at the begining
money=0
#loop that repeats itself until user have put 50 or more in the machine
#asking the type of coin, verifying if its accepted. If it is, added to the object money
while money<50:
    coin=int(input("please insert a coin:"))
    if coin==10 or coin==25 or coin==5:
        money+=coin
        if money<50:
            print(f"Amount Due: {50-money}")
    else:
        print(f"Amount Due: {50-money}")

#once money is equal or superior to 50, informing the user of the change he owes by substracting
#50 from money
print(f"Change Owed: {money-50}" )

# to verify : check50 cs50/problems/2022/python/coke

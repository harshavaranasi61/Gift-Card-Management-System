import os
members=[["Harsha","IbstIbnbo",1,11011,20000],["Manu","NbopsbNb",2,22022,100000],["Doggy","EpcfsNbo",3,33033,10000]]
gift_cards=[[] for i in range(3)]
gift_card_transactions=[[] for i in range(3)]
gift_card_sl_num=[0 for i in range(3)]
gift_card_transact_personal=[[] for i in range(10000)]
reward_points=[0 for i in range(3)]
def account_details(username,i):
    print('Acc number:',members[i-1][3])
    print('Serial number:',members[i-1][2])
    print('Username: '+username)
    print('Balance:',members[i-1][4])
    return
def new_gift_card(username,n):
    present=[]
    global gift_card_num
    global gift_card_pass
    gift_card_num+=1
    gift_card_pass+=1
    gift_card_sl_num[n-1]+=1
    present.append(gift_card_sl_num[n-1])
    present.append(gift_card_num)
    present.append(gift_card_pass)
    present.append(0)
    flag=0
    present.append(flag)
    gift_cards[n-1].append(present)
    print('Gift Card Serial number:',gift_card_sl_num[n-1])
    print('Gift Card number:',gift_card_num)
    print('Gift Card Balance:',0)
    return
def show_gift_cards(n):
    global gift_cards
    req=gift_cards[n-1]
    for i in range(len(req)):
        print("----Gift card:"+str(i+1)+"----")
        print("Gift card number:"+str(req[i][1]))
        print("Gift card Balance:"+str(req[i][3]))
    return
def topup_gift_card(inp):
    global gift_cards
    global reward_points
    n=int(input("Enter the gift card serial to be top-up:"))
    req=gift_cards[inp-1]
    c=0
    present=[]
    for i in range(len(req)):
        if(req[i][0]==n):
            amount=int(input("Enter amount to be credited:"))
            if(amount>members[n-1][4]):
                print("Insufficient Balance!!!")
                break
            else:
                if(req[i][4]!=1):
                    req[i][3]+=amount
                    members[n-1][4]-=amount
                    print("!!Amount credited into Gift card!!")
                    present.append(req[i][0])
                    present.append(req[i][1])
                    present.append(amount)
                    present.append("Credited")
                    reward_points[inp-1]+=(amount/100)
                    gift_card_transactions[n-1].append(present)
                    break
                else:
                    print("Gift card is blocked..Can't topup money")
        else:
            c+=1
    if(c==len(req)):
        print("Invalid gift card number!!!!")
        return
    else:
        gift_cards[n-1]=req
    return
def transaction_history(n):
    global gift_card_transactions
    req=gift_card_transactions[n-1]
    c=0
    for i in range(len(req)):
        print("Transaction Number:"+str(i+1))
        print("Gift Card Number:"+str(req[i][1])+" ---> Amount:"+str(req[i][2])+" Status:"+str(req[i][3]))
    return
def block_gift_card(n):
    global gift_cards
    present=[]
    req=gift_cards[n-1]
    inp=int(input("Enter the serial number of gift card to be blocked:"))
    if(inp>len(req)):
        print("Invalid Gift Card number!!!")
    else:
        if(req[inp-1][4]):
            print("Gift Card is already blocked!!")
        else:
            present.append(req[inp-1][0])
            present.append(req[inp-1][1])
            present.append("----")
            present.append("BLOCKED")
            print("Gift Card is Blocked!!!")
            members[n-1][4]+=req[inp-1][3]
            req[inp-1][3]=0
            req[inp-1][4]=1
            gift_card_transactions[n-1].append(present)
    return
def unblock_gift_card(n):
    global gift_cards
    present=[]
    req=gift_cards[n-1]
    inp=int(input("Enter the serial number of gift card to be unblocked:"))
    if(inp>len(req)):
        print("Invalid Gift Card number!!!")
    else:
        if(req[inp-1][4]==0):
            print("Gift Card is not yet blocked!!")
        else:
            present.append(req[inp-1][0])
            present.append(req[inp-1][1])
            present.append("----")
            present.append("UNBLOCKED")
            print("Gift Card is Unblocked!!!")
            print("Charge the gift card as the balance is low")
            req[inp-1][4]=0
            gift_card_transactions[n-1].append(present)
    return
def redeem(n):
    global reward_points
    global members
    members[n-1][4]+=reward_points[n-1]
    print('Reward points have been redeemed!!!')
    return
def userlogin(username,n):
    while(1):
        print("---------------")
        print(username+"  Login Page")
        print('1.Account details')
        print('2.create a new gift card')
        print('3.Show gift cards')
        print('4.topup the existing card')
        print('5.gift card transcation history')
        print('6.block the existing card')
        print('7.unblock the gift card')
        print('8.redeem reward points')
        print('9.Logout')
        inp=int(input("Enter any value:"))
        if(inp==1):
            os.system('cls')
            account_details(username,n)
        elif(inp==2):
            os.system('cls')
            new_gift_card(username,n)
        elif(inp==3):
            os.system('cls')
            show_gift_cards(n)
        elif(inp==4):
            os.system('cls')
            topup_gift_card(n)
        elif(inp==5):
            os.system('cls')
            transaction_history(n)
        elif(inp==6):
            os.system('cls')
            block_gift_card(n)
        elif(inp==7):
            os.system('cls')
            unblock_gift_card(n)
        elif(inp==8):
            os.system('cls')
            redeem(n)
        elif(inp==9):
            os.system('cls')
            main()
        else:
            break
def decryption(password):
    res=""
    for i in range(len(password)):
        if(password[i]=='Z'):
            res+='A'
        elif(password[i]=='z'):
            res+='a'
        elif(password[i]=='9'):
            res='0'
        else:
            res+=chr(ord(password[i])+1)
    return res
def users(username,password):
    os.system('cls')
    c=0
    for i in range(3):
        if(members[i][0]==username and members[i][1]==password):
            userlogin(username,i+1)
            break
        else:
            c+=1
    if(c==3):
        os.system('cls')
        print("Invalid Login Id/Password!!!!")
        login()
            
def login():
    username=input("Enter username:")
    password=input("Enter Password:")
    decrypt_password=decryption(password)
    users(username,decrypt_password)
def debit_from_gc(n,x):
    global gift_cards
    global gift_card_transact_personal
    c=0
    amount=int(input("Enter amount to be debited:"))
    for i in range(3):
        req=gift_cards[i]
        for j in range(len(req)):
            c+=1
            if(c==n):
                if(amount<=req[j][3]):
                    print("Amount is debited from the gift card!!")
                    req[j][3]-=amount
                    gift_card_transact_personal[n-1].append([req[j][2],amount,"DEBITED"])
                else:
                    print("Insufficient balance in the gift card")
                    gift_card_login(n,x)
    return
def gift_card_trans(n,x):
    global gift_card_transact_personal
    req=gift_card_transact_personal[n-1]
    for i in range(len(req)):
        print("Gift card ID"+str(req[i][0])+" --->amount:"+str(req[i][1])+" Status:"+str(req[i][2]))
    return
def gift_card_login(transcount,x):
    print("----Gift card Login page----")
    print("1.Debit from gift card")
    print("2.Gift card transactions")
    print("3.Logout")
    n=int(input("Enter any value:"))
    if(n==1):
        os.system('cls')
        debit_from_gc(transcount,x)
    elif(n==2):
        os.system('cls')
        gift_card_trans(transcount,x)
    else:
        os.system('cls')
        purchase()
    return
def check(num,pin):
    global gift_card_sl_num
    global gift_cards
    no_of_cards=sum(gift_card_sl_num)
    transcount=0
    c=0
    for i in range(3):
        for j in range(len(gift_cards[i])):
            transcount+=1
            if(gift_cards[i][j][1]==num and gift_cards[i][j][2]==pin):
                gift_card_login(transcount,gift_cards[i][j][1])
            else:
                c+=1
    if(c==no_of_cards):
        print("Invalid card!!!!")
        purchase()
def purchase():
    gift_card_purchase=int(input("Enter the Gift card number to be purchased:"))
    gift_card_pin=int(input("Enter the Pin of above gift card:"))
    check(gift_card_purchase,gift_card_pin)
def main():
    while(1):
        print("--------LOGIN PAGE-----------")
        print("1.Login:")
        print("2.Purchase:")
        print("3.Exit")
        n=int(input("Enter a value:"))
        if(n==1):
            os.system('cls')
            login()
        elif(n==2):
            os.system('cls')
            purchase()
        else:
            return
gift_card_num=90000
gift_card_pass=9000
main()

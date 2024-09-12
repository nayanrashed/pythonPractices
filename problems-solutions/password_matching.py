password_bank = {'Rifat':1234,'Sifat':'2345','Mahir':3456,'Sam':1111}
matched= False
x=0 #loop control variable
print('Enter Your Name: ')
while x<5:
    name=input()
    if name in password_bank:
        for i in range(0,3):
            print('Enter Your Password: ')
            password=input()
            if int(password) in password_bank.values():
                matched= True
                print('Access GRANTED')
                break
            else:
                print('Wrong Password. Enter Again. You Have '+str(2-i)+' tries left')
    else:
        print('There is no such Name in the IDs')
    x=x+1
    if matched:
        break
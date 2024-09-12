#letter counting
'''import pprint as pp
text = 'i love my country'
letters = {}
for i in text:
    letters.setdefault(i,0)
    letters[i]=letters[i]+1
pp.pprint(letters)'''

#Password checking/controlling
'''password_bank = {'Rifat':1234,'Sifat':'2345','Mahir':3456,'Sam':1111}
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
                print('Wrong Password. Enter Again. You Have '+str(2-i)+'tries left')
    else:
        print('There is no such ID')
    x=x+1
    if matched:
        break'''
    
#Phone Book
contact_no={'Sam':17232616, 'Smith':125486569, 'Ran':145856}
x=0
while x<5:
    print('Enter your name(press ENTER to Exit): ')
    name=input()
    if name =='':
        break
    if name in contact_no:
        print('The contact number of '+name+' is '+str(contact_no[name]))
    else:
        print('Not Found.Do you want to add it?')
        desc=input()
        if desc == 'yes':
            print('Enter the number: ')
            num =input()
            contact_no[name]=num
            print('Phonebook Updated')
        elif desc=='no':
            print('Do you want to quit?')
            desc=input()
            if desc== 'yes':
                break
            else:
                print('Keep searching')
x=x+1
                
                
                
                   
    
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
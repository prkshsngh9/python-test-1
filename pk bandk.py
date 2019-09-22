##ask for new account or existing
####if exist enter id and password using file handling
##   if enters wrong id more than 3 break and exit
##   if correct allow to check balance and add or withdraw money
##if doesnt exist allow to create an account


class bank:
        
    username = input("Please input the username ")
    password = input("Please input your desired password ")
    file = open("accountfile.txt","w")
    l=[username,password]
    file.writelines(l)
    file.close()

    username = input("Please input the username ")
    password = input("Please input your desired password ")
    file = open("accountfile.txt","r")
    data=file.readlines()
    l=data.split(',')
    print(data)
    print(l[0])
    file.close()
    

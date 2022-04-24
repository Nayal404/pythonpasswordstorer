n = input('Enter the number of password to save \n')
n = int(n)
i = 0
for i in range(n):
    userPass = input("Enter your Password \n")
    savePass = open('YourPasswords.txt', 'a+')
    savePass.write(f'{userPass} \n')
    savePass.close()
def bintodec():
    n=int(input("enter no."))
    if 
    p=0
    r=0
    while n>0:
        r+= (n%10)*(2**p)
        p+=1
        n= int(n/10)
    print("decimal no.",r)

def octtodec():
    n=int(input("enter no."))
    p=0
    r=0   
    while n>0:
        r+= (n%10)*(8**p)
        p+=1
        n= int(n/10)
    print("decimal no.",r)
    
def hextodec():
    
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hexadecimal = input("Enter the hexadecimal number: ").strip().upper()
    decimal = 0
    power = len(hexadecimal) -1
    for digit in hexadecimal:
        decimal += conversion_table[digit]*16**power
        power -= 1
    print(decimal)
        
def main():
    print("\nMenu\n(2)base 2\n(8)base 8\n(16)base 16\n(Q)uit")
    choose=input("Enter your choice>>> ")
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    choice=choose.lower()
    while choice!="q":
        if choice=="2":
            bintodec()
            main()
        elif choice=="8":
            octtodec()
            main()
        elif choice=="16":
            
            hextodec()
            main()
        else:
            print("Invalid choice, please choose again")
            print("\n")
#print("Do you wish to continue(Y/N)") #
main()



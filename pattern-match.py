tal= int(input("Indtast:    "))

match tal: 
    case 1:
        print(f" du valgte mulighed 1")
    case 2:
        print(f" du valgte mulighed 2")
    case 3:
        print(f" du valgte mulighed 3")
    case _:
        print(f"ukendt mulighed {tal}")

if tal == 1: 
    print(f" du valgte mulighed 1")
elif tal == 2:
    print(f" du valgte mulighed 2")
elif tal == 3:
    print(f" du valgte mulighed 3")
else:
    print(f"ukendt mulighed {tal}")

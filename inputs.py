def message(name):
    while 1:
        try:
            temp = input(f"Enter {name} Signal: ")
            lens = len(temp)
            temp = int(temp,2)
            return bin(temp)[2:].rjust(lens,"0")
        except:
            print("Enter valid value")

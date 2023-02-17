def getTicket():
    speedLimit = 60
    bigTicketOffset = 20
    speed = int(input("How fast were they going?: "))
    birthday = input("Is it their birthday (y/n): ")
    if(birthday.upper()=="Y"):
        speedLimit += 5
    if(speed>speedLimit+bigTicketOffset):
        print("big ticket")
    elif (speed>speedLimit):
         print("small ticket")
    else:     
        print("no ticket")
getTicket()
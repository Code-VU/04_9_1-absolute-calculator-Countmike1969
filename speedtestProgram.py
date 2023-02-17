def getTicket():
    getSingleTicket()
    print("---")
    def getSingleticke():
    speedLimit = 60
    bigticketoffSet = 20 
    speed = int(input("How fast were they going?: "))
    birthday = input("Is it their birthday (y/n): ")
    if(birthday.upper()=="Y"):
        speedLimit += 5
    if(speed>speedLimit+bigticketoffSet):
        print("big ticket")
    elif(speed>speedLimit):
        print("small ticket")
    else:
        print("no ticket")

getTicket()

    
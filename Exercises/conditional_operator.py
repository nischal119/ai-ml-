isMagician = input("Are you a magician")
isExpert = input("Are you a expert")

if isMagician == "yes" and isExpert == "yes":
    print("You are an expert magician")

elif isMagician == "yes" and isExpert == "no":
    print("At least you're getting there")

else:
    print("You're not magician and you need a magic powers")

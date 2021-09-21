exitcode = ""
aantalherhalingen = 0
print("welcome sir")
while exitcode != "quit":
    aantalherhalingen = aantalherhalingen + 1
    exitcode = input("type 'quit' to exit the program. ")
    print("")
    if exitcode != "quit":
        print("Try again, ", aantalherhalingen, "failed attempts")
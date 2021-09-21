dag = input("Welke dag? (ma,di,wo,do,vr,za,zo): ").lower()
daglist = ["ma","di","wo","do","vr","za","zo"]
printed_day = "None"
dagnummer = 0

while dag != printed_day:
    if dag in daglist:
        print("")
    else:
        print("Choose an existing day please.")
        break
    printed_day = daglist[dagnummer]
    print(printed_day)
    dagnummer = dagnummer + 1
    
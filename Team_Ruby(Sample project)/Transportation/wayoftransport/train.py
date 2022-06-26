def booktrainticket(v):
    need = ["speed", "cost", "luxury"]
    print(need)
    sel = input("select ur convienet category from list:")
    if sel == "speed":
        L1 = ["=200", ">200<=800", ">800<=1000"]
        print(L1)

        cost = int(input("enter between what range of cost:"))
        if cost == 200:
            print("ur available trains are")
            L2 = ["rajadhani", "padhmavathi", "navajivana"]
            for i in L2:
                print(i)

            print("please book ur ticket")
            h = int(input("Enter 1.rajadhani , 2. padhmavathi , 3.navajivana"))
            if h == 1:
                print("Rajadhani train ticket booked")
            if h == 2:
                print("padhmavathi train ticket booked")
            if h == 3:
                print("navajivana train ticket booked")

        elif cost > 200 and cost < 800:
            print("ur available trains are")
            L2 = ["garib_rath_express", "teja_express ", "Gatimaan_express"]
            for i in L2:
                print(i)

            print("please book ur ticket")
            h = int(input("Enter 1.garib_rath_express , 2. teja_express, 3.Gatimaan_express"))
            if h == 1:
                print("garib_rath_express train ticket booked")
            if h == 2:
                print("teja_express train ticket booked")
            if h == 3:
                print("navajivana train ticket booked")
        elif cost > 800 and cost <= 1000:
            print("ur available trains are")
            L2 = ["telangana_ex", "Shantabdi_express", "Golconda express AC"]
            for i in L2:
                print(i)

            print("please book ur ticket")
            h = int(input("Enter 1.telangana_ex , 2. Shantabdi_express, 3.Golconda express AC"))
            if h == 1:
                print("telangana_ex train ticket booked")
            if h == 2:
                print("Shantabdi_express train ticket booked")
            if h == 3:
                print("Golconda express AC ticket booked")
    elif sel == "cost":
        L1 = ["=100", ">100<=600", ">600<=800"]
        print(L1)
        cost = int(input("enter between what range of cost:"))
        if cost == 100:
            print("ur available trains are")
            L2 = ["samparak", "padhmavathi", "navajivana"]
            for i in L2:
                print(i)

            print("please book ur ticket")
            h = int(input("Enter 1.samparak, 2.padhmavathi_express, 3.navajivana express AC"))
            if h == 1:
                print("samparak train ticket booked")
            if h == 2:
                print("padhmavathi_express train ticket booked")
            if h == 3:
                print("navajivana express AC ticket booked")
        elif cost > 100 and cost < 600:
            print("ur available trains are")
            L2 = ["dakshith_express", "teja_express ", "Gatimaan_express"]
            for i in L2:
                print(i)

            print("please book ur ticket")
            h = int(input("Enter 1.dakshith_express, 2.teja_express, 3.Gatimaan_ express AC"))
            if h == 1:
                print("dakshith_express train ticket booked")
            if h == 2:
                print("teja_express train ticket booked")
            if h == 3:
                print("Gatimaan express AC ticket booked")
        elif cost > 600 and cost <= 800:
            print("ur available trains are")
            L2 = ["Duronto_express", "Shantabdi_express", "Golconda AC"]
            for i in L2:
                print(i)

            print("please book ur ticket")
            h = int(input("Enter 1.Duronto_express, 2.Shantabdi_express, 3.Gatimaan_ express AC"))
            if h == 1:
                print("Duronto_express train ticket booked")
            if h == 2:
                print("Shantabdi_express train ticket booked")
            if h == 3:
                print("Gatimaan express AC ticket booked")

    elif sel == "luxury":
        L2 = {'gandhi': 600, 'AJAC': 500, 'nakaiyak': 800}
        for i in L2:
            print(i)
            print("please book ur ticket")

        h = int(input("Enter 1.gandhi, 2.AJAC, 3.nakaiyak"))
        if h == 1:
            print("gandhi train ticket booked")
        if h == 2:
            print("AJAC train ticket booked")
        if h == 3:
            print("nakaiyak ticket booked")

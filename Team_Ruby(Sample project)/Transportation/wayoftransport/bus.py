def bookbusticket(v):
    travellerneed = ["speed", "cost", "luxury", "nothing"]
    print(travellerneed)
    select = input("select ur convinient from list:")
    if select == "speed":
        List1 = ["=400", ">400<=900", ">900<=1500"]
        print(List1)
        cost = int(input("enter between what range of cost:"))
        if cost == 100:
            print("available buses are")
            List2 = ["RTC", "ordinary", "vantare platinum plus"]
            for i in List2:
                print(i)
            print("please book ur ticket")
            h = int(input("Enter 1.RTC , 2. ordinary , 3.vantare platinum plus"))
            if h == 1:
                print("RTC bus ticket booked")
            if h == 2:
                print("ordinary bus ticket booked")
            if h == 3:
                print("vantare platinum plus ticket booked")
        elif cost >= 500 and cost < 1000:
            print("available buses are")
            List2 = ["superbus", "rhythm travel"]
            for i in List2:
                print(i)
            print("please book ur ticket")
            h = int(input("Enter 1.superbus  , 2.rhythm travel "))
            if h == 1:
                print(" superbus Bus ticket booked")
            if h == 2:
                print("  rhythm travel Bus ticket booked")
        elif cost >= 1000 and cost <= 2500:
            print(" available buses are")
            List2 = ["globe Trotter", "explorania"]
            for i in List2:
                print(i)
            print("please book ur ticket")
            h = int(input("Enter 1.globe Trotter , 2.explorania  "))
            if h == 1:
                print("globe Trotter  Bus ticket booked")
            if h == 2:
                print("explorania Bus ticket booked")
    elif select == "cost":
        List1 = ["=400", ">400<=900", ">900<=1500"]
        print(List1)
        cost = int(input("enter  cost:"))
        if cost == 100:
            print(" available buses are")
            List2 = ["conquest", "garuda", "ordinary"]
            for i in List2:
                print(i)
            print("please book ur ticket")
            h = int(input("Enter 1.conquest , 2.garuda  , 3.ordinary"))
            if h == 1:
                print("conquest  Bus ticket booked")
            if h == 2:
                print("garuda Bus ticket booked")
            if h == 3:
                print("ordinary Bus ticket booked")
        elif cost >= 500 and cost < 1000:
            print(" available buses are")
            List2 = ["safari", "galaxy travels "]
            for i in List2:
                print(i)
                print("please book ur ticket")
            h = int(input("Enter 1.safari , 2.galaxy travels"))
            if h == 1:
                print("safari  Bus ticket booked")
            if h == 2:
                print("galaxy travels Bus ticket booked")
        elif cost >= 1000 and cost <= 2500:
            print(" available buses are")
            List2 = ["ac travels", "sunrise"]
            for i in List2:
                print(i)
                print("please book ur ticket")
                h = int(input("Enter 1.ac travels , 2. sunrise"))
                if h == 1:
                    print("ac travels  Bus ticket booked")
                if h == 2:
                    print("sunrise Bus ticket booked")
    elif select == "luxury":
        List2 = {'sunrise': 900, 'Ac': 1000}
        for i in List2:
            print(i)
        print("please book ur ticket")
        h = int(input("Enter 1. , 2.Ac "))
        if h == 1:
            print("sunrise Bus ticket booked")
        if h == 2:
            print("Ac Bus ticket booked")

    elif select == "nothing":
        request = input("Enter the transport type:")
        vehicle = input("Enter the vehicle type")
        rate = int(input("Enter the kilometers of your destination:"))
        a = 'roadway'
        d = 'railway'
        b = 'buses'
        c = 'taxi'
        e = 'metro'
        f = 'general'
        buses = [
            {
                "name": "ordinary",
                "units": rate,
                "price": rate * 15
            },
            {
                "name": "express",
                "units": rate,
                "price": rate * 20
            },
            {
                "name": "super luxury",
                "units": rate,
                "price": rate * 25
            },
            {
                "name": "garuda express",
                "units": rate,
                "price": rate * 30
            },

        ]
        taxi = [
            {
                "name": "ordinary cab",
                "units": rate,
                "price": rate * 10
            },
            {
                "name": "2 seaters",
                "units": rate,
                "price": rate * 15
            },
            {
                "name": "4 seaters",
                "units": rate,
                "price": rate * 20
            },
            {
                "name": "ac cab",
                "units": rate,
                "price": rate * 25
            },

        ]
        metro = [
            {
                "name": "metro train",
                "units": rate,
                "price": rate * 20
            },
        ]
        ordinary = [
            {
                "name": "ordinary train",
                "units": rate,
                "price": rate * 10
            },
        ]
        if request == a:
            if vehicle == b:
                print(buses)
            elif vehicle == c:
                print(taxi)
        elif request == d:
            if vehicle == f:
                print(metro)
            elif vehicle == e:
                print(ordinary)

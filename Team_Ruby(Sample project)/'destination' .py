import Transportation
import Transportation.wayoftransport as wt
from Transportation import way_of_tranport as wt
from Transportation.wayoftransport import bus as bs
#from Transportation.wayoftransport import Car as cr
from Transportation.wayoftransport import train as tr
#from Transportation.wayoftransport import nothing as no
print('''Enter Origin And Destination''')
f=input("From :")
t=input("To:")
print("Available Transport")
if f!=t:
    wt.ways(f,t)
else:
    print("Try again")
if f!=t:
    wt.waysb(f,t)
else:
    print("Try again")
if f!=t:
    wt.wayst(f,t)
else:
    print("Try again")

v=int(input('''Enter to continue
1.Roadways
2.Railways'''))
if v==1:
    bs.bookbusticket(v)
elif v==2:
    tr.booktrainticket(v)

#wt.tm(v)
#y=int(input(" :"))
#bs.choosebus(y)


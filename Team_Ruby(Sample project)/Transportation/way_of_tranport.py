'''import wayoftransport
from wayoftransport import Bus as bs
from wayoftransport import Trains as tr
from wayoftransport import Car as cr'''


initialall=['warangal','hyderabad','karimnagar','vizag','dornakal']
finalall=['waranagl','hyderabad','dornakal','karimnagar','vizag']
def ways(f,t):
    for i in initialall:
        for j in finalall:
             if f in i:
                 if t in j:
                     print("Railway(Train) , Roadway(Bus)")

initialcar=['warangal','kazipet','hanamkonda','hasanparthy']
finalcar=['warangal','kazipet','hanamkonda','hasanparthy']
def waysb(f,t):
    for i in initialcar:
        for j in finalcar:
             if f in i:
                 if t in j:
                     print("Roadway(Bus,Car)")

initialtrain=['waranagl','delhi','tirupathi','mumbai','hyderabad','chennai']
finaltrain=['waranagl','delhi','tirupathi','mumbai','hyderabad','chennai']
def wayst(f,t):
    for i in initialtrain:
        for j in finaltrain:
             if f in i:
                 if t in j:
                     print("Railway(Train)")












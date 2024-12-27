import win32evtlog as wlog # type: ignore
import datetime
POWERONID = 30
SHUTDOWNID = 50104
MAXSESSIONS = 10


validIds = [SHUTDOWNID, POWERONID]
sessions = []
ultimoInicio = None
powerEvents = []
#POWERONID = inicio
#SHUTDOWNID = apagado

handle = wlog.OpenEventLog("localhost", "System")
flags = wlog.EVENTLOG_BACKWARDS_READ | wlog.EVENTLOG_SEQUENTIAL_READ
#print("Flags: {:b}\n".format(flags))

i = 0
while i <= MAXSESSIONS*2:
    events = wlog.ReadEventLog(handle, flags, 0)
    events = list(filter(lambda x : (
        x.EventID in validIds), events))
    for e in events:
        powerEvents.append(e)
        i+=1


if powerEvents[len(powerEvents)-1].EventID == SHUTDOWNID:
    powerEvents = powerEvents[:len(powerEvents)-1]
if powerEvents[0].EventID == POWERONID:
    ultimoInicio = powerEvents[0]
    powerEvents = powerEvents[1:]

if len(powerEvents) % 2 != 0:
    quit()

class Session:
    def __init__(self, start, finish, time):
        self.start = start
        self.finish = finish
        self.time = time


while powerEvents != []:
    j = powerEvents.pop(0)
    e = powerEvents.pop(0)
    timeStart = e.TimeGenerated
    timeFinish = j.TimeGenerated
    sessions.append(Session(start = timeStart, finish = timeFinish, time = timeFinish-timeStart))


print("La PC se encuentra encendida desde: {}".format(ultimoInicio.TimeGenerated))
print("Ultimas sesiones (Desde que se prende hasta que se apaga): \n")



for s in sessions:
    print("\nInicio: {} - Fin: {}\nDuracion: {}".format(s.start, s.finish, s.time))


#for e in powerEvents:
#    print ("{}/{}/{}   -   {:02}:{:02}:{:02}   -   ID: {}".format(e.TimeGenerated.day, e.TimeGenerated.month, e.TimeGenerated.year, e.TimeGenerated.hour, e.TimeGenerated.minute, e.TimeGenerated.second, e.EventID))

input()
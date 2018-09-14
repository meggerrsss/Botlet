# http://tpcg.io/IeUZWG
 


now=1754

def todm(time): # converting time in 4 digits to nth minute of the day (direct minute time)
    minute = time % 100
    hour = (time - minute)/100
    newtime = hour*60 + minute
    return newtime
    
def fromdm(newtime): # converting time minutes of the day back to a readable time format
    minute = newtime % 60
    hour = (newtime-minute)/60
    actualtime = hour*100+minute
    return actualtime

def tiermoji(bird): # just for kanto birds!!!	
	if lower(bird) == "articuno":
		return ❄️
	if lower(bird) == "zapdos":
		return ⚡
	if lower(bird) == "moltres":
		return 🔥
	
def report(tier,place,pokemon="egg",reporttime=now,timeleft=45,starttime=None,endtime=None,raidlength=45):
	# converting to minute of day
	reporttime = todm(reporttime) 
	if not starttime == None: starttime = todm(starttime)
	if not endtime == None: endtime = todm(endtime)
	
	# print pokemon name at the end if present
	mon = " - "+pokemon
	if pokemon == "egg":
		mon = ""
	
	# kanto birds emoji!!!
	if lower(pokemon) in ['articuno','moltres','zapdos']:
		tier = tiermoji(pokemon)
	
	# given starttime and assumed length	
	if not starttime == None: 
		endtime = starttime + raidlength
		
	# given endtime and assumed length
	if not endtime == None: 
		starttime = endtime - raidlength
		
	# given reporttime and timeleft 	
	if endtime == None and starttime == None: 
		endtime = reporttime + timeleft
		starttime = endtime - raidlength
		
	# converting back to readable time	
	starttime = fromdm(starttime)
	endtime = fromdm(endtime)
	
	#nicely prant
	times = str(starttime)+"-"+str(endtime)
	print str(tier)+"* "+times+" "+str(place)+str(mon)
	
report(3,"here","moltres")
report(2,"there",starttime=1512)
report(5,"boy meets girl","articuno",endtime = 1904)
report(4,"rotary bridge" ,'lapras',timeleft = 50)

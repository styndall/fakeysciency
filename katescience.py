import string, random, time




def graphs(graphtype):
	#select distinct graph types
	if graphtype == 1:
		#plain bar graph
		start_char = "|"
		graph_char = "-"
		end_char = "O"
	elif graphtype == 2:
		#moving asterisks
		start_char = "*"
		graph_char = " "
		end_char = "*"
	elif graphtype == 3:
		#arrows
		start_char = "|"
		graph_char = "-"
		end_char = ">"
	else:
		#dicks
		start_char = "8"
		graph_char = "="
		end_char = "D"

	print "RESULTS OF DATA ANALYSIS "+"".join(random.sample(string.ascii_uppercase,3))+str(random.randint(400,123124))
	time.sleep(2)
	for x in range(64):
        	print start_char+ graph_char*random.randint(3,18)+end_char+"\n"
        	time.sleep(.1)
	#keep final dick in dick graph
	if graphtype == 4:
		print "8====D<<"
	print "DATA VISUALIZATION COMPLETE"
	time.sleep(1)
	return

def checks():
    y = random.randint(1,24)
    for l in range(y):
        print "RUNNING CHECK "+ str(random.randint(23423,220000))+random.sample(string.ascii_uppercase,1)[0]+"..."
        time.sleep(random.random())
    print "CHECKS COMPLETE"
    time.sleep(.3)
    return



def rand_ip():
	ip = ""
	for x in range(3):
		ip = ip + str(random.randint(35, 899)) + "."
	ip = ip + str(random.randint(35,999))
	return ip


def hackit():
	attacker_ip = rand_ip()
	print "WARNING: your science is being hacked by: " + attacker_ip
	print "Hack back? Y/N"
	answer = raw_input().lower()	
	if answer == "y":
		counter_hack()
	elif answer == "n":
		print "CEDING SCIENCE TO ATTACKER"
		time.sleep(3)
	else:
		print "LOSING HACKING BATTLE"
		time.sleep(3)
		print "HACKING BATTLE LOST"	

def counter_hack():
	print "BEGINNING COUNTERHACK\n"
	print "GENERATING SPOOFED IPS:\n"
	for x in range(10):
		print str(x) + "::" + rand_ip()
		time.sleep(.2)
	print "\n\nFLOODING HOSTILE UDP PORTS"
	for x in range(10):
		print "CLOSING IP LABEL: " + str(x)
		time.sleep(.1)
	print "COUNTERHACK SUCCESSFUL\n\n"
	time.sleep(2)
	
def publish_results():
	print "SCIENCE COMPLETE"	
        
def do_science():
	b = list(string.printable)*40000
	g = ""
	x = 0
	while g!= "end":
	    if x%3589==1:
		g=raw_input("enter science parameters ")
		#with raw_input, try/except no longer necessary
		#except: g=raw_input("invalid parameters; enter science parameters ")
		x+=1
	    elif x%2332 ==1:
		graphtype = random.randint(1,4)
		graphs(graphtype)
	        x+=1
	    elif x%2351 ==1:
	    	checks()
	        x+=1
	    elif x%3111 ==1:
		hackit()
		x+=1
	    else:
	        c = "".join(random.sample(b, 1232))+"\n"
	        x+=c.count("k")
	        print c
    


import string, random, time

#define misc science functions below

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

def rand_ip():
	ip = ""
	for x in range(3):
		ip = ip + str(random.randint(35, 899)) + "."
	ip = ip + str(random.randint(35,999))
	return ip

def hackit():
	attacker_ip = rand_ip()
	print "WARNING: Your science is being hacked by: " + attacker_ip
	print "Hack back? Y/N"
	answer = raw_input().lower()
	if answer == "y":
		counter_hack()
		time.sleep(3)
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
	time.sleep(3)
	
def checks():
	y = random.randint(1,24)
	for l in range(y):
		print "RUNNING CHECK "+ str(random.randint(23423,220000))+random.sample(string.ascii_uppercase,1)[0]+"..."
		time.sleep(random.random())
	print "CHECKS COMPLETE"
	time.sleep(.3)
	
def print_cat():
	cat=[]
	cat.append('         /\\`-.-`/\\')
	cat.append('         )` _ _ `(')
	cat.append('     (`\\ |=  Y  =|')
	cat.append('      ) )_\\  ^  /_')
	cat.append('     ( (/ ;`-u-`; \\')
	cat.append('      \\| /       \\ |')
	cat.append('       \\ \\_ \\ / _/ /')
	cat.append('       (,(,,)~(,,),)')
	for catline in cat: 
		print catline
		time.sleep(1)
		
# waiting animation for use wherever
def waiting(seconds):
	for n in range(0,seconds):
		time.sleep(1)
		print "."

def publish_results():
	print "YOU HAVE PROVEN SCIENCE"
	print "Publish results? Y/N"
	answer = raw_input().lower()
	while answer!="y":
		print "PUBLISH OR PERISH" 
		print "Publish results? Y/N"
		answer = raw_input().lower()
	print "CHOOSE JOURNAL: Nature, Tumblr, or Lingua?" 
	gotitright = False
	while not gotitright:
		journal = raw_input().lower()
		if journal=="nature":
			gotitright = True
			print "YOU HAVE SUBMITTED SCIENCE TO NATURE"
			time.sleep(1)
			print "WAITING FOR REVIEW"
			waiting(10)
			yes_no = random.randint(1,3)
			if yes_no == 1:
				print "SUBMISSION ACCEPTED"
			if yes_no == 2: 
				print "COMPUTATIONAL MODEL INSUFFICIENTLY INAPPROPRIATE"
				time.sleep(1)
				print "SUBMISSION REJECTED"
			if yes_no == 3:
				print "HAVE YOU CONSIDERED ADDING A MALE AUTHOR"
				time.sleep(1)
				print "SUBMISSION REJECTED"
		elif journal=="tumblr":
			gotitright = True
			print "YOU HAVE SUBMITTED SCIENCE TO TUMBLR"
			time.sleep(1)
			print_cat()
			time.sleep(2)
		elif journal=="lingua":
			gotitright = True
			print "YOU HAVE SUBMITTED SCIENCE TO LINGUA"
			time.sleep(1)
			print "YOU SHOULD BE ASHAMED"
			time.sleep(1)
			print "WAITING FOR REVIEW"
			waiting(10)
			print "SUBMISSION REJECTED"
		else:
			print "ENTER JOURNAL NAME"
	print "DOING MORE SCIENCE"
	time.sleep(2)
			
#define main science function below
def do_science():
	b = list(string.printable)*40000
	g = ""
	x = 0
	while g!= "end":
		if x%3589==1:
			g=raw_input("Enter science parameters ")
			#with raw_input, try/except no longer necessary
			#except: g=raw_input("invalid parameters; enter science parameters ")
			x+=1
		elif x%2332 ==1:
			graphtype = random.randint(1,4)
			graphs(graphtype)
			x+=1
		elif x%2017 ==1:
			checks()
			x+=1
		elif x%3111==1:
			hackit()
			x+=1
		elif x%4337==1:
			publish_results()
			x+=1
		else:
			c = "".join(random.sample(b, 1232))+"\n"
			x+=c.count("k")
			print c


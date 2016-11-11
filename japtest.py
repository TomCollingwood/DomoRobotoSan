#!/usr/bin/python
import random

from optparse import OptionParser


parser = OptionParser()
parser.add_option("-s", "--sentencetype", dest="_s", default=0,
                  help="which type of sentence", metavar="SENTENCE")
#parser.add_option("-q", "--quiet",
#                  action="store_false", dest="verbose", default=True,
#                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()


endwords = ["",", doomo"]
startwords = ["","sumimasen, ","hai, ","aa,","hajimemashite, ","konnichiwa, ","ohayoo gozaimasu, ","konbanwa, ", "oyasumi nasai", "kochira e"]
phrases = ["so desu ne" , "so desu"]
nounA = ["inu","neko","sore","baka","Amerikajin","kyoo","denwa"]
nounB = ["dore","are","kore","kochira"]
nounC = ["koko","doko","soko","asoko"]
nounLocations = ["Tookyoo"]
verbstoLocations = ["yookoso","ikimasu"]
adjectives = ["ookii"]
ownverb = ["desu"]
actionverb = [""]
question = ["","ka"]
names = ["Tom san", "Chereen san", "Kao san", "Yoko sensei", "Tito san"]

nouns = nounA + nounB + names
verbs=ownverb

def pickone( _list ):
	return _list[random.randint(0,len(_list)-1)];


def generatedescribednoun():
	described = random.randint(0,1)
	if(described):
		return pickone(nouns)+" no "+pickone(nounA)
	else:
		return pickone(nouns)



def generatesentence( _sentencetype ):

	if(_sentencetype==0):
		return pickone(startwords)+pickone(nouns)+" "+pickone(ownverb)+" "+pickone(question)+pickone(endwords)

	elif(_sentencetype==1):
		return pickone(startwords)+generatedescribednoun()+" "+pickone(ownverb);

	elif(_sentencetype==3):
		return pickone(nouns)+" wa "+pickone(nounC)+" ni arimasu"

	elif(_sentencetype==4):
		return pickone(nouns)+" wa "+pickone(adjectives)+" "+pickone(nouns)+pickone(endwords)

	elif(_sentencetype==5):
		return pickone(nounLocations)+" e "+pickone(verbstoLocations)

	elif(_sentencetype==6):
		return 

	elif(_sentencetype==7):
		return generatesentence(random.randint(0,2))+" ga, "+generatesentence(random.randint(0,2))

print "\n"
for i in range(10):
	print generatesentence(_s)
print "\n"



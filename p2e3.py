import random
import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x))
import pprint

def generate_dicc(n):
	'''genera un diccionario de usuarios con sus campos hasta 200'''
	raw_usernames='''syntaxisunfreeze
kneebang
verifypacified
ninettasextans
montagutone
atrophyimpotent
paringphilip
computerrelativity
smokeyjagger
updatesvagabond
fustilarianpriority
orbitexit
flapwhitendale
viruspolicies
lousedan
junkiecups
boringnebraska
scaredradio
expendcasper
dipstickethanoate
micedcamel
porousteeming
foggyparts
glasgowflagman
treatgangrene
sectdecode
conapicalo
chapterscientist
wottledbulb
chucksterstewarts
baptistsoak
lurksaxophone
haberbutler
terrineopulently
potatopython
frailbank
dillonvigorous
jellybymirror
sidfit
greatpowdering
pungentoccupy
agefletal
yellowknifeottawa
fooddelicious
messageupscale
visualningers
maplemetrics
craniachatch
driftunrobed
bramblespotify
pruneritzy
possibilityoral
direnessdeliver
trippingruin
paddyprude
chowseronion
offalcorpuscle
tweakvan
sufferingcoca
afraidschematic
venuebobolink
scornbonny
openingemit
mincecategory
winteddemocracy
meridianinform
strainermagnesium
midriffjoops
overratednoted
processeswreckage
tisherarethusa
dismissparp
chivalryhug
backedchasma
swordsexorcist
crinklyensemble
lohnsparents
claytyson
batteryculture
niagaradiagram
pierrehypertext
comejulian
careergrudie
melonfocus
swilledenzyme
bedacquire
premiumcylinder
paroleunsmoked
mencersplatform
andromedabrilly
chocolatywolden
descentshaft
stubbeduncured
thousandlupus
setsdaves
sandlotmicawber
dotflowery
baldyworrisome
speakcaring
dentistgrandy
demotionbucket
ramboearthen
appealpresley
tedexpose
nephewsheffield
reversionare
ebenezerstreak
cordialboned
fripperyfarrah
lizardhusband
wantedpiglet
junkyardtricky
parmesanreprimand
parrotmealy
sculpturevixen
lankinessannabelle
biddymolt
cacklechirm
favorrebel
nickertirry
jugglingobsessed
quickennewspaper
kinswomanjersey
malcontentkanaird
uprootstuffy
muffleddense
vincentloperty
watermelonmeasures
harleyonstage
tallahasseegillie
logmutton
impactsuperbowl
moodthor
undresschromate
sanitaryhope
buffalofair
maturingcharlie
estuarybangin
cettifags
bookhudeshope
royalaboard
troddenshelf
patronagecornelia
cuillinroundworm
assertivetrifocals
twinnasturtium
railcarerratic
pascalsposer
daylongbullseye
backmiss
luggrange
gaseousflop
scallopsrotting
floppysilicon
ethicallymeitnerium
roomduke
salsahatchling
meerkatmayonnaise
flakynorthern
scroogeunusual
washerroom
bipingmorse
sobspider
mouldyshastic
objectsdeceiving
minuteelevator
hardcoreapache
chicarejoicing
slammingcripples
snoolhigher
woodchatrepose
hackneyart
ejectrepeat
shuffledelightful
letsunwanted
generousoverreach
jijimoving
damagemicky
occiputcustomary
sagablackhazel
obtainduo
drearyvelocity
relianceonboard
ferrymisguided
scudbladnoch
everybodysnushy
cheakyscoat
saviknee
blockblue
minoucepheid
agonizeditch
pulledtwite
huntsmangland
sandwormheader
lariganimagination
lonelavender
calliechevrolet
hydroxidecopyright
fluffquartile
degreasecredit'''
	usernames = raw_usernames.split('\n')
	#print(len(usernames))
	usernames = set(usernames)
	usernames = list(usernames)  #por si se repiten, igual no
	#print(len(usernames))
	dicc={}
	for i in range(n):
		dicc[usernames[i]]={}
		dicc[usernames[i]]['nivel']=random.randrange(1,99)
		dicc[usernames[i]]['puntaje']=random.randrange(1,999999999)
		dicc[usernames[i]]['tiempo']=round(random.uniform(0,999), 2)
	return dicc

def impr_dicc(dicc):
	for key in dicc:
		print('{:>10}:'.format(key))
		sub=''
		for L in key:
			sub+='^'
		print(sub)
		for e in dicc[key]:
			print('  {:>10}: {}'.format(e,dicc[key][e]))
		print()

def impr_lis(lis):
	c=0
	for i in lis:
		c+=1
		print('{}) {}:'.format(c,i[0]))
		sub=''
		for L in i[0]+str(c)+') ':
			sub+='^'
		print(sub)
		for e in i[1]:
			print('  {:>10}: {}'.format(e,i[1][e]))
		print()	
	
def primerosN(usuarios,n):
	#impr_dicc(usuarios) # este imprime todos no se puede contar
	#impr_lis(list(usuarios)) #error porque convierte solo las claves no como .items()
	#debug(list(usuarios))
	lis=list(usuarios.items())
	#debug(lis) #list lo convierte bien y le saca ese dict pedorro
	impr_lis(lis[:n])
	print()	

def impr_ord(usuarios,orden):
	if orden=='nombre':
		w=0
		orden=0
		desc=False
	else:
		w=1
		desc=True
	Sort = sorted(usuarios.items(), key=lambda t: t[w][orden],reverse=desc)
	                        #el 0 es porque nombre es el primer elemto de la tupla de la lista que generó .items()
	#pprint.pprint(Sort, indent=3, width=1) #imprime pero con todos los simbolos de listas y dicc
	#print()
	impr_lis(Sort)
	print()

def impr_lvl(usuarios):  #queda obsoleto
	Sort = sorted(usuarios.items(), key=lambda punt: punt[1]['nivel'],reverse=True)
	                       #el 1 es porque es el segundo elemto de la tupla de la lista que generó .items
	#pprint.pprint(Sort, indent=3, width=1)
	#print()
	impr_lis(Sort)
	print()

usuarios = generate_dicc(15)


print('PRIMEROS 10:')
print()
primerosN(usuarios,10)
print()
print('SORT x NOMBRE : ')
print()
impr_ord(usuarios,'nombre')
print('SORT x NIVEL: ') 
print()
impr_ord(usuarios,'nivel')

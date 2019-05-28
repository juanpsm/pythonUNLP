import sys  
if sys.version_info[0] >= 3:  
    import PySimpleGUI as sg  
else:  
    import PySimpleGUI27 as sg  
import collections
import random
import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x))
	print()

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
		dicc[usernames[i]]['puntaje']=random.randrange(1,999999)
		dicc[usernames[i]]['tiempo']=round(random.uniform(0,999), 2)
	return dicc

def cadena(lis):
	col = [20,8,10,10]
	formato_col = '{:<'+str(col[0])+'}|{:^'+str(col[1])+'}|{:>'+str(col[2])+'}|{:^'+str(col[3])+'}|'
	txt = ''
	w = sum(col)+len(col)  #ancho columnas + separadores
	txt += ('-'*w)+'\n'
	txt += formato_col.format('Nombre','LVL','PTS','TIME')+'\n'
	txt += ('^'*w)+'\n'
	for x in lis:
		txt += formato_col.format(x[0],x[1]['nivel'],x[1]['puntaje'],x[1]['tiempo'])+'\n'
	return txt
def ordenar(dicc,orden,desc=False):
	'''recibe diccionario de cierto formato y devuelve una lista de tuplas (nombre, diccionario de campos)'''
	if orden=='nombre':
		w=0
		orden=0
		#desc=False #de cuando no tenia toogle
	else:
		w=1
		#desc=True
		desc=not(desc)
	return sorted(dicc.items(), key=lambda t: t[w][orden],reverse=desc)

p=generate_dicc(80)
debug(p)

o=ordenar(p,'puntaje',True)
debug(o)

t=cadena(o)
print(t)

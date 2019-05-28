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
def rand_key(dicc):
	return random.choice(list(dicc.keys()))
def rand_tema():
	raw_temas=  '''GreenTan      
LightGreen      
BluePurple      
Purple      
BlueMono      
GreenMono      
BrownBlue      
BrightColors      
NeutralBlue      
Kayak      
SandyBeach      
TealMono'''
	temas = raw_temas.replace(' ','').split('\n')
	return random.choice(temas)
#print = sg.Print #todo lo que imprimo va a una ventana debug

def to_string(dicc):
	col = [20,8,10,10]
	formato_col = '{:<'+str(col[0])+'}|{:^'+str(col[1])+'}|{:>'+str(col[2])+'}|{:^'+str(col[3])+'}|'
	txt = ''
	w = sum(col)+len(col)  #ancho columnas + separadores
	txt += ('-'*w)+'\n'
	txt += formato_col.format('Nombre','LVL','PTS','TIME')+'\n'
	txt += ('^'*w)+'\n'
	for x in dicc:
		txt += formato_col.format(x,dicc[x]['nivel'],dicc[x]['puntaje'],dicc[x]['tiempo'])+'\n'
	return txt
		
default_dicc=generate_dicc(30)
r = rand_key(default_dicc)
tema=rand_tema()
sg.ChangeLookAndFeel(tema)
usuarios={}

layout = [      
		  [sg.Text('Please enter your Name, Address, Phone'),sg.Button('tema'),sg.Text(tema, size=(15, 1), key='_THEME_')],      
		  [sg.Text('Username', size=(15, 1)), sg.InputText(r, key='_NAME_')],      
		  [sg.Text('Nivel alcanzado', size=(15, 1)), sg.InputText(default_dicc[r]['nivel'], key='_LVL_')],      
		  [sg.Text('Puntaje', size=(15, 1)), sg.InputText(default_dicc[r]['puntaje'], key='_PTS_')],      
		  [sg.Text('Tiempo', size=(15, 1)), sg.InputText(default_dicc[r]['tiempo'], key='_TIME_')],
		  [sg.Button('Agregar'), sg.Button('Cerrar')],
		  [sg.Multiline(default_text='', size=(60,10),font=("Courier"), key='_LISTA_')],
		  [sg.Text('Cantidad de jugadores: ', size=(20, 1)), sg.Text(len(usuarios.keys()), key='_COUNT_')]
		 ]      

window = sg.Window('Jugadores GUI').Layout(layout)  

while True:                 # Event Loop  
	event, values = window.Read()  
	#print(event, values)
	if event is None or event == 'Cerrar':  
		break  
	if event == 'Agregar':
		usuarios[values['_NAME_']]={}
		usuarios[values['_NAME_']]['nivel']=values['_LVL_']
		usuarios[values['_NAME_']]['puntaje']=values['_PTS_']
		usuarios[values['_NAME_']]['tiempo']=values['_TIME_']
		
		#print(formato.format(values['_NAME_'],values['_LVL_'],values['_PTS_'],values['_TIME_']))
		#UPDATE
		
		r = rand_key(default_dicc) #saco otro random key para actualizar los default input
		#while r in usuarios.keys():  #si quiero que no se repitan
		#	print(r," ++++ YA ESTABA ++++")
		#	r = rand_key(default_dicc) #saco otro random key para actualizar los default input
		#		window.FindElement('_NAME_').Update(r)
		#		break #si no cuando se le acaban los default hace loop infinito
		window.FindElement('_NAME_').Update(r)
		window.FindElement('_LVL_').Update(default_dicc[r]['nivel'])
		window.FindElement('_PTS_').Update(default_dicc[r]['puntaje'])
		window.FindElement('_TIME_').Update(default_dicc[r]['tiempo'])
		
		window.FindElement('_COUNT_').Update(len(usuarios.keys()))
		window.FindElement('_LISTA_').Update(to_string(usuarios))
	if event == 'tema':
		tema=rand_tema()
		sg.ChangeLookAndFeel(tema)
		window.FindElement('_THEME_').Update(tema)
		
window.Close()

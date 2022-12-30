from tkinter import *
from random import randint
import tkinter as tk  # importing tkinter for our graphical interface
from tkinter.ttk import Combobox

root = tk.Tk()

root.title("Learn Luganda With Erick.W.    0752629514    erickwaiswa7@gmail.com")
root.geometry("600x600")
#root.iconbitmap("C:/Users/Waiswa/Desktop/Lugandaproject/Dick/log.png")
root.config(bg="#68BBE3")
root.resizable(FALSE, FALSE)

#For the dictionary comand to open
def dic_open():

   def update(data):
      # clear the list box
      my_list.delete(0, END)

      # adding nouns to alist box
      for item in data:
         my_list.insert(END, item)


   # update the entry box with listbox clicked
   def fillout(event):
      # delete what ever is in the enry boc
      my_entry.delete(0, END)

      my_entry.insert(0, my_list.get(ACTIVE))


   # function that checks our entry Vs or list box
   def check(event):
      # get everything we type
      typed = my_entry.get()
      if typed == '':
         data = nouns
      else:
         data = []
         for item in nouns:
            if typed.upper() in item.upper():
               data.append(item)
      # update the list box with what we are typing
      update(data)


   # create a label
   my_label = Label(root, text="Translate any English or Luganda Word here!!!", font=("times new roman", 20),bg="#68BBE3", fg="#EEEEEE")
   my_label.pack(pady=20)

   # Create an entry box
   my_entry = Entry(root, font=("times new roman", 12))
   my_entry.pack()

   # create alist box
   my_list = Listbox(root, width=50,height=10, font=("times new roman", 15),bg="#68BBE3")
   my_list.pack(pady=20)

   # creating alist of Luganda words
   nouns = [
      "omusajja  ----------> man ",  "omugenyi ----------> guest",     "omuyimbi ----------> singer","omukazi ------------> woman", "munnabyabufuzi ----> Politican", "omusubuuzi --------> business person","omuwala ------------> girl",  "omuntu ------------> person",    "omukozi -----------> worker", "muganda-------------> sibling","omusomesa-----------> teacher)", "omugagga --------> rich person", "omwana ----------> child)", "omuyizi  -----------> student",  "omusawo ---------> doctor", "omulenzi -----------> boy)",     "omufumbi --------> cook",         "omujaasi -------> soldier)","mukyaala ----------> wife, madam", "omufumbo -------> spouse","omusambi -----------> player)", "omwami ---------> husband, man", "omuzadde ------> parent", "omulirwana -----> neighbor","omulogo ------------> witch/ witchdoctor)", "omuwanguzi -------> winner", " omuwuulu-------> bachelor","omuvubuk ----------> youth","nnabbi -------> prophet","omukuumi -------> protector","omukuumi ------> goal keeper","abakungu aba waggulu -----	high officials","abakungu ------> officials","omutwalo	ten thousand shillings","emirundi ebiri	----> two times / twice","omunwe gwa lumonde ---->	a single potatoe","omuluka	---> administrative division", "omuvule------> african hard wood tree","omukka ---->	air","omwenge ----> alcohol", "omukago----> allies", "omukono -----> arm", "omugongo ----> back","omupiira -----> ball", "omutuba ---> bark cloth tree", "omumwa --->beak/Mouth","omwenge ----->beer","omugaso ------> benefit", "omukisa ---> blessing /Luck","omusaayi ----> blood","omukago ------> blood brother hood", "omubiri ----> body", "omutego ------>bow","omugaati ----> bread","omugugu ----> bundle (of clothes / blankets)","omuganda	-----> bundle (of sticks / firewood)","omugugu ----> burden","omukebe -----> tin/can","omusubbaawa----> candle","omuwogo ----> cassava","omuvule ----->cedar tree","omulambo -------> corpse","omusango ----.>court case", "omusango ---->crime","omusalaba ----> cross","omusiri ----> cultivated plot", "omutto ---> cushion","omusana ----> daylight","omusulo ----> dew","omunyolo ---> door handle","omulyango ---->doorway","omufulejje ----> drain","omuzannyo ----->drama","omusu  -----> eddible rat","omusango ----> fault","omusujja----> fever","omutango-----> fine","omuliro-----> fire","omulongooti ---> flagstaff/ telecom mast","omuseetwe ---- >flat land","omulere----> flute","omusingi ---->foundation","omukwano -----> friend/love/friendship","omuzannyo ---> game","omuddo---->grass","omusu ----> guinea pig", "omufulejje ---->gutter","omutwe --->head","omutwe --->headship","omutima----->heart","omuyini----> hoe handle","omubisi ----> honey/banana juice","omulimu ----> job","omwalo -----> landing place","omumwa ---> lip","omunya ----->	lizard","omugugu ----> load","omusujja -----> malaria","omuyembe ----> mango/mango tree","omukeeka -----> mat (made of palm leaves)","omufaliso =-----> attress","omwezi =---->Month/ moon","omuzigiti ----> mosque","omusumaali ---->nail",
      "omuwendo---->number","omucungwa	--->orange/orange tree","omusaala ---->pay","omutto ----> pillow","omuseetwe ----> plain","omuzannyo---> play","omusingo ---->pledge","omwalo ----->port/ landing site","omuwendo ---->price","omuceere----->rice","omugga	--->river","omuguwa---->	rope","omusittali (e)--->	ruled line","omunnyo---->	salt","omusenyu---->sand","omusumeeno--->	saw","omugabo	--->share","omutala---->	side of hill","omukka ---->	smoke","omusota ---->	snake","omwoyo---->	spirit","omuzimu ---->spirit of the dead","omuggo--->	stick","omuswaki ---->	stick for cleaning teeth","omugga --->	stream","omutwe--->	sub-heading","omusana --->sun/ sunlight","Ekisenyi--->	swamp","omukira --->tail","omusolo--->	tax","omutwe--->theme","omulundi--->	time","emirundi  ----->	times","omukebe	tin","omupiira --->	tire","omutwe	--->title","omuswaki	--->tooth brush","omumuli--->	torch (made of reeds)","omuziro--->	totem","omunaala---->tower","omutego--->trap","omuti--->tree","omukono--->	trunk of elephant","omunwe	--->unit (single)","omusulo--->urine","omugaso--->use","omukka	--->vapour","omusaala--->wage","omufulejje--->water pipe","omuddo---->weeds","omuzimu----->spirits","omusege--->wild dog","omusege----->	wolf","omulimu	---->work","omukono	-----> hand writing","omwaka --->	year","ekitiibwa---->glory","ekitiibwa --->Respect/title","amagezi --->advice","eggye	--->army","evvu---->	ashes","ebbega---->sholder"," amabega	--->back","eryenvu--->banana (small sweet variety)","ebbavu--->blister","eryato--->boat","eggumba--->bone","ettabi(amatabi)	------>branch(s)","ettabi / amatabi	 --->branch office","ebbeere / amabeere--->breast","ettoffaali	---->brick","essasi--->	bullet","eppeesa / amapeesa---->button","eryato---->canoe","effumbe --->cat (civet)","eryanda---->drycell/ charcoal","ejjembe	--->charm","ettama--->cheek (of face)","ebbumba--->clay (of potter)","amagezi	--->cleverness","eryanda--->coal","ettwale--->colony","essiga--->cooking stone","essaza--->country","amaddu	--->craving (for food)","eggigi----->curtain","ettwale--->deanery","ebbanja-->debt","eddungu--->desert","eddiiro / amaliiro--->dining room","ettwale--->	district","ejjiba--->dove","eddagala / amalagala	--->medicene / drugs","eggi / amagi----->	egg","ebbugumu	--->heat/ warmth/ enthusiasm","eriiso / amaaso--->	eye","amaaso----->	face","ekkolero / amakolero---->factory","essavu / amasavu--->fat","eddembe--->freedom","eddibu / amalibu	-----> gap","essubi---> grass","ettale --->	grass land (dry)","amagombe---->grave","amalaalo---->grave","amakungula---->	harvest","ettima --->hatred","maka ---->home","essuubi---->hope","ejjembe----->horn","eddwaliro / amalwaliro----->hospital","amaddu ---->	intense desire","essanga----->ivory","essanyu----->joy","evviivi / amaviivi---->knee","ebbula---->scarcity/ lack","amadaala	---->ladder","ettaka---->land","etteeka / amateeka	----->law","amalagala/ ebikoola----> leaves","egguggwe	---->lung","eriwuggwe--->lung","eddalu -----> madness","ettooke / amatooke	matooke ----->banana","amakulu-------> meaning","eddagala / amalagala------> medicine","ettuntu --->midday","ettumbi	 ---> midnight","amata---->milk","eggwanika----> mortuary","ettosi----->mud","ettemu----->murder","eggwanga / amawanga----->nation","amawulire----->news","eggulire / amawulire	-----> news/newspaper","ezadde-----> offspring","amafuta	-----> oil (not for cooking)","ebbanga / amabanga---->opportunity","ebbanga / amabanga	---->outer space","amagenda------> outward journey","eppaapaali / amapaapaali	---->pawpaw/ papaya","ettale---->pasture ground","ekkubo / amakubo-----> path","amafuta----->fuil / oil / petrol","amaanyi	----->power",
      "ekkomera /amakomera --->prison","amagoba	 ---->rofit","amasira --->pus","eddaala / amadaala ---->rank/step ladders/ stairs","amadda --->return journey","ekkubo / amakubo --->road","ejjinja / amayinja --->Stone/rock","amalusu --->saliva","essomero / amasomero---->school","ezadde ---->own children","amagombe	---->grave","edduka / amaduka--->	shop","ebbali / amabbali --->side (of a thing)","eddiba	--->animal skin","eggulu --->heaven/sky","ettaka---->	soil","ebbwa --->wound/sore","ebbanga / amabanga --->	space","effumu / amafumu--->spear","ettima--->spite","amaanyi	----> power/ strength","ezziga / amaziga--->	tear (from crying)","eriggwa--->thorn","ettegula --->	tile","eddebe --->	tin (four gallon size)","amalaalo --->tomb/ grave yard","erinnyo---->	tooth","eggwanga / amawanga --->	tribe/ nationality","amazima	--->truth","erinnyo -----> tusk/ tooth","essanga-----> tusk","ebbwa -----> ulcer","ettale ------>	veldt","ettemu	------> violence","eddoboozi / amaloboozi ------>	voice","ebbugumu -------> warmth","amazzi ------>water","ejjengo -----> wave","ekkubo / amakubo	way/road/ ways","eddenge ------> whistle","eddungu----> wilderness","amagezi	wisdom","amagezi----> wits","ebbwa --->wound","essaza / amasaza -----> parish","essaza / amasaza -----> district","obuyinza -----> authority","obuyinza ---> power","obwakatikkiro -------> mayor","obwakatikkiro ------> prime minister","obuwaŋŋanguse -----> exile","taata ---->father"," caayi ---->tea","balansi --->balance","maama ----> mother","ffenne ----->jackfruit","ovakeddo ---->avocado","jjaja ----> grandparent","sabuuni ----> soap","kaawa --->coffee","ssebo ---> sir","kawo ---->peas","kamulali---->chilli","nnyabo ---->madam","ssukaali ----> sugar","ssentebe ---->chairperson","katonda --->god","kabaka ----> king","ssalongo ---> father of twins","wakabi --->superstar","nannyini ---> owner","nnabagereka ----> queen","Lumonde ---> sweet potato","gundi--->so and so","nnaalongo -----> mother of twins","nnamwandu -----> widow","ssemwandu ------> widower","ssemaka ----> head of the family","omusuwo ---->muscle","- omukolo----> function","omuzizo----> taboo","omuzira ---> alam of joy/ a hero/ snow","engatto ----> shoe","ensobi -----> mistake","ensiri -----> mosquito","ensawo----> bag","ennyindo ---->nose","emundu -----> gun","emmere ----> food","ennyumba ----> house","entamu ----> sauce pan", "embuzi ---->goat", "ensenene ------> grasshopper","entungo-----> sesame","embizi ---->pig","etangawuuzi ----> ginger","essowani---->plate","ente----->cow","ennyaanya ---->tomato","enswa----->ant","enkoko----->chicken","embwa----->dog","enswaswa----->alligator","entugga ---->giraffe","enjovu ----> elephant","entebe------>chair / bench","enkima------->monkey","ensi----->Earth/ world/ planet/ country","ensujju ---->pumpkin","ennyama ----->meat","ensalo -------> border/ boundary","empuliziganya----->communication",
      "ssente ----> money","kkapa----> cat","gomesi------>traditional wear for women","palamenti------>parliament","nnamba------->number","poliisi ----->police","kaloti-----> carrot","ssaati ---->shirt","ekintu------> thing","ekisenge----->room","ekitanda -----> bed","ekizimbe -----> building","ekisolo -----> animal","ekinusu ----> coin","ekikopo -----> cup","ekibuuzo -----> question","ekirabo----->Gift/present","ekifaananyi ------>picture", "ekyama (secret)","ekibiina (class room)","ekitabo (book)","ekigambo (word)","ekibina (butt)","ekinyonyi (bird) ","ekiwuka (insect)","ekiteeteeyi (dress) ","ekirowoozo (opinion)/(thoubht)"," ekirooto (dream)","ekikajjo (sugar cane)","ekibira (forest) ","ekiro (night) ","ekisaawe (field) ","ekyalo (village)","ekifuba (chest/ caugh) ","ekitiibwa (respect) ","ekiseera (moment/ period of time)","ekisuubizo (promise) "," ekisumuluzo (key)","ettooke (banana)"," ettaka (land, soil)"," eryenvu (sweet banana) ","ebbaluwa (letter)","eddwaaliro (hospital)"," amakoloni (pasta)","amagye (army) ","amaserengeta (south)","amaalo (backwardness)","amaka (family, home)","amasanyalaze (electricity) ","amazaalibwa (birthday)","amambuka (north)","akatungulu (onion)"," akatunda (passion fruit)","akalevu (chin) ","katungulucumu (garlic)","akambe (knife) ","akagere (toe)","ekigere (foot) "," akaveera (plastic bag)","akabenje (accident) ","akabonero (sign, label)","akajanja (drama queen)","akakiiko (commission)","kabuvubuka (adolescence)","obulamu (life)","obuzibu (issue(s)/problems/ deficulty) ","obugagga (wealth) ","obudde (time) ","obulwadde (disease)","obuwanguzi (success) ","obulungi (goodness)","obuto (childhood) ","obukenuzi (corruption)","obukulu (age)","obutwa (poison) ","obwenzi (adultery)","obunene (size)","obufumbo (marriage)","obusobozi (ability)","obusungu (anger)","obubaka (message)","obuyambi (assistance) ","obwannanyini (private ownership) ","obwegassi (union/ unity)","obunyiivu (anger)","olulimi (language, tongue) ","olusu (smell)","olweyo (broom) "," olusozi (mountain)","oluyimba (song)","olugambo (rumour)","olubuto (stomach/ pregancy)","olunaku (day)","oludda (direction/ side)","oluganda (Luganda/ brother hood)","olutalo (battle/ war)","oluwummula (vacation)","oluzungu (English)","olugoye (clothes)","olususu (skin)","oluviiri (hair)","oluguudo (road) ","olujji (door)","olugero (proverb/ story)","olugendo (trip, hike)","olupapula (page, paper)","olukunŋŋaana (meeting)","olugalo (finger)","olukiiko (meeting)",
      "Okugulu (leg)","okubala (mathematics)","okulambula (adventure)","okutu (ear)","okulonda (election / voting)","okubaka (netball)","otulo (sleep)","otuzzi (small drop of water)","otuta (small drop of milk)","Otuzi (small droops of feaces )","otunyira (.....)","Otufuta(.....)"

   ]

   # adding words to our list
   update(nouns)

   # create a binding
   my_list.bind("<<ListboxSelect>>", fillout)

   # Create a binding when we thy out somthing in the entry box
   my_entry.bind("<KeyRelease>", check)
def donate():
   my_donation = Toplevel()
   my_donation.title("Your Contribution")
   my_donation.iconbitmap("C:/Users/Waiswa/Desktop/Lugandaproject/images/icon.png")
   dona = tk.StringVar()
   donar = tk.Label(my_donation, textvariable=dona)
   donar.grid(row=2, column=1, padx=20, pady=20)
   dona.set("Contribute :- \n (1) Money \n (2) A thought \n to make the system much better\n\nYou can Call for help on how to make your contribution: \n \n __Whats App --> +256752629514__\n __Tell ----------> +256752629514__")

def contact():
    my_contact =Toplevel()
    my_contact.title("Contact Me")
    detailes = tk.StringVar()









my_menu = Menu(root)
root.config(menu=my_menu)


file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Files", menu=file_menu)
file_menu.add_command(label="Dictionary", command=lambda: dic_open())
file_menu.add_separator() # this is to add line separator between the menus
file_menu.add_command(label="Contribution", command=lambda: donate())
file_menu.add_separator() # this is to add line separator between the menus
file_menu.add_command( label="Close", command=root.quit) # we dont need to create the functio for Quie becoause its in built.

Help_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Help", menu=Help_menu)

Help_menu.add_command(label="Contact Admin", command=lambda: contact())




flash = [
    (("ekintu"),("thing")), (("ekiwuka"),("insect")), (("ekiteeteeyi"), ("dress")), (("ekirowoozo"), ("opinion")), (("ekirooto"), ("dream")), (("ekisenge"),("room")),(("ekitanda"),("bed")),(("ekizimbe"),("building")),(("ekisolo"),("animal")),(("ekinusu"),("coin")),(("ekikopo"),("cup")),(("ekibuuzo"),("question")),(("ekirabo"),("gift")),(("ekifaananyi"), ("picture")),(("ekyama"),("secret")),(("ekibiina"),("class room")),(("ekitabo"),("book")),(("ekigambo"),("word")),(("ekibina"),("butt")),(("ekinyonyi"),("bird")),(("ekikajjo"),("sugar cane")), (("ekibira"),("forest")),(("ekiro"),("night")),(("ekisaawe"),("field")), (("ekyaalo"),("village")),(("ekifuba"),("chest")),(("ekitiibwa"),("respect")), (("ekiseera"),("moment")), (("ekisuubizo"), ("promise")),(("ekisumuluzo"),("key")),
    (("omsomesa"), ("teacher")), (("omuggaga"), ("rich person")), (("omuwala"), ("girl")), (("omuyizi"), ("student")), (("omwana"), ("child")), (("omusawo"),("doctor")),(("omulenzi"),("boy")),(("omufumbi"),("cook")),(("omujaasi"),("solier")),(("mukyala"),("wife")),(("omufumbo"),("married Person")),(("omzanyi"),("player")),(("mwami"),("husband")),(("mulirwana"),("neighbor")), (("omulogo"),("wizard")),(("omuzadde"),("parent")),(("omuwanguzi"),("winner")),(("omuwuulu"),("abachelor")),(("polofes"),("profesor")),(("taata"),("father")),(("maama"),("mather")),(("jjaja"),("grand parent")),(("ssebo"),("sir")),(("nnyabo"),("madam")),(("katonda"),("god")),(("owaakabi"),("supestar")),(("caayi"),("tea")),(("ffene"),("jackfruit")),(("sabuuni"),("soap")),(("kawo"),("peas")),(("sukaali"),("sugar")),(("kabaka"),("king")),(("nannyini"),("owner")),(("baalansi"),("balance")),(("ovakeddo"),("avocado")),(("kamulari"),("chilli")),(("ssentebe"),("chairperson")),(("ssalongo"),("father of twins")),(("nnabakyala"),("chair lady")),(("nabagereka"),("queen")),(("lumonde"),("sweet potato")),(("nnaalongo"),("mother of twins")),(("ssemwandu"),("widower")),(("nnamwandu"),("widow")),(("ssemaka"),("family head")),
    (("omkwano"), ("friendship")),(("omukono"), ("arm")),(("omukisa"), ("luck")),(("omubiri"),("body")),(("omuti"), ("tree")),(("omulimu"),("job")),(("omwaka"),("year")),(("omupila"),("ball")),(("omusolo"),("tax")),(("Okugulu"), ("leg")),(("okubala"), ("mathematics")),(("okulambula"), ("adventure")),(("okutu"),("ear")),(("okulonda"),("election ")),(("okubaka"),("netball")),(("otulo"),("sleep")),(("otuzzi"),("small drop of water")),(("otuta"), ("small drop of milk")),
    (("Otuzi"),("small droops of feaces")),(("ekyama"),("secret")),(("ekibiina"), ("class room")),(("ekitabo"), ("book")),(("ekigambo"),("word")),(("ekibina"), ("butt")),(("ekinyonyi"), ("bird")),(("ekiwuka"), ("insect")),(("ekiteeteeyi"), ("dress")),(("ekirowoozo"), ("thought")),(("ekirooto"), ("dream")),(("ekikajjo"), ("sugar cane")),(("ekibira"), ("forest")),(("ekiro"),("night")),(("ekisaawe"), ("field")),(("ekyalo"), ("village")),(("ekifuba"), ("chest")),
    (("ekitiibwa"), ("respect")),(("ekiseera"), ("moment")),(("ekisuubizo"), ("promise")),(("ekisumuluzo"), ("key")),(("ettooke"), ("banana")),(("ettaka"),("land")),(("eryenvu"), ("sweet banana")),(("ebbaluwa"), ("letter")),(("eddwaaliro"),("hospital")),(("amagye"), ("army")), (("amaserengeta"), ("south")),(("amaalo"),("backwardness")),(("amaka"),("home")),(("amasanyalaze"), ("electricity")),(("amazaalibwa"), ("birthday")),(("amambuka"), ("north")),(("akatungulu"), ("onion")),(("akatunda"), ("passion fruit")),(("akalevu"), ("chin")),(("katungulucumu"), ("garlic")),(("akambe"), ("knife")),(("akagere"), ("toe")),(("ekigere"), ("foot")),(("akabenje"), ("accident")),(("akabonero"), ("sign")),(("akajanja"), ("drama queen")),
    (("akakiiko"), ("commission")),(("kabuvubuka"), ("adolescence")),(("obulamu"), ("life")),(("oludda"), ("direction")),(("oluganda"), ("brother hood")),(("olutalo"), ("battle/ war")),(("olupapula"), ("paper")),(("olukunŋŋaana"), ("meeting")),(("olugalo"),("finger")),(("olukiiko"), ("meeting"))
     
     ]

# get count of our words
Count = len(flash)


def answer():
    if my_entry.get().lower() == flash[random_word][1]:
        answer_label.config(text=f"Correct! {flash[random_word][0]} is {flash[random_word][1]}", fg="#00ff00",font=("times new roman",20))
    else:
        answer_label.config(text=f"Wrong ! {flash[random_word][0]}  is not {my_entry.get().lower()} try again",fg="red",font=("times new roman",20,))


def next():
    global hit_count
    global hinter
    # clear screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hit_label.config(text="")
    hinter = ""
    global random_word
    # creating random Selection
    random_word = randint(0, Count - 1)
    # update label with luganda word
    Luganda_word.config(text=flash[random_word][0])
    hit_count = 0


# keeping track of the hints
hinter = ""
hit_count = 0


def hint():
    global hinter
    global hit_count

    if hit_count < len(flash[random_word][1]):
        hinter = hinter + flash[random_word][1][hit_count]
        hit_label.config(text=hinter)
        hit_count += 1


Luganda_word = Label(root, text="", font=("Times new romans ", 20),bg="#68BBE3")
Luganda_word.pack()

answer_label = Label(root, text="",bg="#68BBE3")
answer_label.pack()

my_entry = Entry(root, font=("times new roman ", 12))
my_entry.pack()

# creating buttons
button_frame = Frame(root, bg="#68BBE3")
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Translate", command=answer,bg="#a0aadf")
answer_button.grid(row=0, column=0, padx=20, pady=20)

answer_button = Button(button_frame, text="Next", command=next, bg="#5c6dc9")
answer_button.grid(row=0, column=1, padx=20, )

answer_button = Button(button_frame, text="Hint", command=hint, bg="#83dfe9")
answer_button.grid(row=0, column=2, padx=20, pady=20)

# Creating a hint Label
hit_label = Label(root, text="", bg="#68BBE3")
hit_label.pack(pady=20)

next()
root.mainloop()
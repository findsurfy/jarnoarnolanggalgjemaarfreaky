#!/usr/bin/env python3
import os
import random
import sys
import time

MAX_WRONG = 7

MAKKELIJK = """
kaas fiets brood huis kat hond boom water melk tafel stoel deur raam boek
pen zon maan vis koek soep hand voet neus mond oor oog haar been arm buik
kop koppie kip ei ham worst kaasje appel peer banaan druif wijn bier koffie
thee suiker zout peper rijst pasta pizza friet saus kipfilet visstick
auto bus trein boot vliegtuig fietsbel bel tram metro taxi vrachtwagen
school klas leraar leerling stoep straat plein park bos meer rivier zee
zand steen gras bloem tulp roos boomstam blad tak wortel ui prei kool
sla tomaat komkommer paprika aardappel wortelkoek drop dropje hagelslag
pindakaas hagelslagmes mes vork lepel bord kopje glas fles pan oven
koelkast tv radio telefoon laptop muis toets lamp kast bed kussen deken
douche wc bad zeep handdoek spiegel kam tandenborstel tandpasta
jas broek shirt sok schoen muts sjaal handschoen riem tas portemonnee
geld munt brief kaart briefje postzegel krant tijdschrift
voetbal tennis golf zwemmen lopen rennen springen vallen lachen huilen
slapen waken eten drinken koken bakken braden snijden smeren
papa mama opa oma broer zus kind baby tiener man vrouw
vriend vriendin buur baas collega
maandag dinsdag woensdag donderdag vrijdag zaterdag zondag
lente zomer herfst winter regen sneeuw hagel wind storm zonnestraal
wolk lucht ster planeet aarde vuur ijs rook stoom
rood blauw groen geel oranje paars roze wit zwart grijs bruin
groot klein lang kort dik dun hoog laag
hard zacht nat droog vies schoon mooi lelijk
ja nee misschien misschieniet
galg strop touw ladder emmer hout nagel hamer zaag
lul piemel pik bal eikel kont reet poep pis plas kut
neuken wippen vingeren zuigen likken klaarkomen spuiten
hoer slet sletje geil geilerd geilerds
""".split()

GEMIDDELD = """
windmolen klompen stroopwafel fietspad bibliotheek chocolade paraplu
vriendschap verjaardag slaapkamer woonkamer keuken badkamer
treinstation luchthaven supermarkt apotheek brandweer politieauto
ziekenhuis voetbalveld basketbal zwembad speeltuin boswandeling
regenjas winterjas zonnebril horloge sleutelhanger
computerprogramma wachtwoord toetsenbord beeldscherm
telefoonnummer postcode huisnummer straatnaam
boodschappenlijst koffiezetapparaat magnetron ovenwant
wasmachine droger strijkijzer stofzuiger
burenruzie filespits fileleed files
voetbalschoen scheidsrechter doelpunt corner
zwemles zwembroek bikini zonnebrand
vakantiehuis campingtent caravan
kerstdiner oliebollen nieuwjaar
sinterklaas pepernoten chocoladeletter
koningsdag oranjefeest vrijmarkt
haringhappen jenever borrel nootjes
patatjeoorlog patatjemayo patatjespeciaal
kroket bitterbal kaassouffle
pannenkoek poffertje tompouce boschebol
dropveter zoutjes chips pinda
buurvrouw schoonmoeder schoonvader
zwager schoonzus neef nicht
collega kantoortuin koffiepauze
vergadering presentatie deadline
huiswerk tentamen diploma
jarnovanvuur
bushalte tramhalte treinkaartje
ovchipkaart inchecken uitchecken
regenbui onweersbui hagelbui
sneeuwpop sneeuwbal ijsbaan
schaatsen sleeen langlaufen
voetbalpoule poulepoule
biertje wijntje shotje
kater hoofdpijn misselijk
verkouden griep koorts
pleister zalf pilletje
tandarts huisarts specialist
wachtkamer recept apothekersassistent
kapper kapperzaak knipbeurt
tattoo piercing baard
snor sik sikje
onderbroek bh sokkenmand
wasrek wasknijper wasmiddel
afwas afwasmiddel vaatwasser
prullenbak vuilniszak kliko
glasbak kledingbak batterijenbak
fietsenhok fietsslot kettingslot
autostoel gordel airbag
benzine diesel laadpaal
filevorming spitsuur
snelweg afrit oprit
rotonde zebrapad stoplicht
parkeerplek parkeerboete
flitspaal drempel
politieagent boa
ambulance sirene
brandweerwagen ladderwagen
gemeentehuis stembureau
verkiezing stempas
belastingdienst toeslag
huurtoeslag zorgtoeslag
studiefinanciering
studentenkamer
huisgenoot
feestje afterparty
hangover ontbijt
uitslapen brunch
tinder date afspraakje
zoenen tongzoen
handjob pijpen
voorplay naakt
condooms glijmiddel
one night stand
""".split()

MOEILIJK = """
verzekeringsmaatschappij gezondheidszorg onderwijsministerie
waterleidingbedrijf rijksoverheid gemeentebestuur
arbeidsomstandigheden milieubescherming verkeersongeval
openbaarvervoer wetenschappelijk taalkundige
rechtsbijstand belastingaangifte kasteelgracht
scheurkalender polderlandschap dijkbewaking
haringkar karnemelk erwtensoep boerenkool stamppot
oliebollen nieuwjaarsdag sinterklaasavond koningsdag
bevrijdingsdag prinsjesdag
werkloosheidsuitkering arbeidsongeschiktheid
ziektewet zwangerschapsverlof ouderschapsverlof
huwelijksvoltrekking echtscheidingsakte
geboorteakte overlijdensakte
identiteitsbewijs rijbewijsnummer
burgerservicenummer sofinummer
kamervragen ministerraad
tweede kamerstuk
gemeenteraadsverkiezingen
waterschapsverkiezingen
provinciale staten
wateroverlast dijkdoorbraak
hoogwaterperiode
stormvloedkering
afsluitdijk markerwaard
zuiderzeewerken
deltawerken
poldergemaal
boezemwater
kwelwater
veenweidegebied
natuurreservaat
waddengebied
zeehondenopvang
vogeltrek
ganzenoverlast
meeuwenpoep
duivenoverlast
rattenplaag
wespensteek
tekenbeet
ziekenhuisopname
wachtlijstproblematiek
huisartsenpost
spoedeisendehulp
ambulancevervoer
brandweerkazerne
politiebureau
gevangenisstraf
taakstraf
jorishectorvannunen
rechtszaak
getuigenverklaring
advocatenkantoor
notariskantoor
hypotheekakte
koopovereenkomst
huurcontract
arbeidscontract
caoafspraak
salarisstrook
pensioenfonds
vakantiegeld
dertiendemaand
eindejaarsuitkering
studievoorschot
collegegeld
scriptiebegeleiding
afstudeeronderzoek
promotieonderzoek
universiteitsbibliotheek
collegezaal
werkgroepbijeenkomst
herkansingstentamen
cumlaude
propedeuse
bacheloropleiding
masteropleiding
stagebegeleider
bijbaantje
vakkenvuller
postbezorger
bezorgerdienst
maaltijdbezorger
thuisbezorgd
boodschappenservice
supermarktketen
kortingsactie
klantenkaart
spaarpunten
cadeaubon
waardebon
loterijticket
staatsloterij
postcodeloterij
kraslot
jackpot
miljoenenjacht
realitysoap
datingprogramma
songfestival
eurovisiesongfestival
voetbalelftal
eredivisie
kampioenswedstrijd
degradatiewedstrijd
bekerfinale
wkkwalificatie
oranjefan
sjaaltje
toeter
rookbom
stadionverbod
hooligan
scheldkanonnade
fluitconcert
blessuretijd
penaltyreeks
doelpuntenmaker
aanvoerder
bondscoach
selectieprocedure
jarnoarnovanvuur
spelersgroep
kleedkamer
blessureleed
spierenpijn
fysiotherapie
revalidatietraject
""".split()


def schoon(lijst):
    uit = []
    gezien = set()
    for w in lijst:
        w = "".join(c for c in w.upper() if "A" <= c <= "Z")
        if len(w) >= 3 and w not in gezien:
            gezien.add(w)
            uit.append(w)
    return uit


WORDS = {
    "makkelijk": schoon(MAKKELIJK),
    "gemiddeld": schoon(GEMIDDELD),
    "moeilijk": schoon(MOEILIJK),
}

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def wacht(sec):
    try:
        time.sleep(sec)
    except KeyboardInterrupt:
        raise


def vraag(txt):
    try:
        return input(txt)
    except (KeyboardInterrupt, EOFError):
        print("\nja doei dan")
        sys.exit(0)


def tekening(fout, geil=False, spuit=0):
    kop = "   "
    midden = "   "
    benen = "   "
    if fout >= 1:
        kop = " O "
    if fout >= 2:
        midden = " | "
    if fout >= 3:
        midden = "/| "
    if fout >= 4:
        midden = "/|\\"
    if fout >= 5:
        benen = "/  "
    if fout >= 6:
        benen = "/ \\"
    if geil:
        kop = "\\O/"
        midden = "/|\\"
        benen = "/ \\"

    print("  +---+")
    print("  |   |")
    print("  |  " + kop)
    print("  |  " + midden)
    print("  |  " + benen)
    if geil:
        straal = [
            "  |    8==D",
            "  |    8==D~",
            "  |    8==D~~",
            "  |    8==D~~~ ~",
            "  |    8==D~~~~ ~~",
            "  |    8==D~~~~~ ~ *",
            "  |    8==D~~~~~~ ~~ * drip",
        ][min(spuit, 6)]
        print(straal)
    elif fout >= 6:
        print("  |    8==D")
    print("  |")
    print(" =========")


PRAAT_FOUT = [
    "fout. hij wordt er hard van. kut.",
    "mis. hij grijnst naar zn kruis.",
    "nee gast. hij vindt dit lekker.",
    "verkeerde letter. zn broek zit krap.",
    "hahaha nee. hij zucht geil.",
    "kut. hij mompelt doe nog een fout",
    "dat was em niet. hij wiebelt.",
    "nope. zn oogjes gaan half dicht",
    "au. niet voor hem. hij is blij.",
    "broer dat was geen letter van het woord",
]

PRAAT_GOED = [
    "kut ja die zit erin. hij is pissed.",
    "goed. hij zucht teleurgesteld.",
    "ja die. fucking spoilersport.",
    "raak. hij wou dat je miste.",
    "oke die telt. hij wordt slapper. zielig.",
    "yes. hij vloekt zachtjes.",
]

PRAAT_DOM = [
    "dat is geen letter sukkel",
    "gewoon a tot z man",
    "leeg. type iets",
    "die had je al. let op",
    "cijfers? serieus?",
]


def status(woord, geraden):
    return " ".join(c if c in geraden else "_" for c in woord)


def kies_level():
    while True:
        print("hoe moeilijk")
        print("1 makkelijk")
        print("2 beetje")
        print("3 kutmoeilijk")
        k = vraag("> ").strip().lower()
        if k in ("1", "makkelijk"):
            return "makkelijk"
        if k in ("2", "beetje", "gemiddeld"):
            return "gemiddeld"
        if k in ("3", "kutmoeilijk", "moeilijk"):
            return "moeilijk"
        print("1 2 of 3. niet zo moeilijk doen\n")


def lees_gok(raw, geraden):
    t = raw.strip().upper()
    if not t:
        return None, random.choice(PRAAT_DOM)
    if len(t) > 1:
        if not t.isalpha():
            return None, "alleen letters. geen rare tekens"
        return t, None
    if t not in ABC:
        return None, random.choice(PRAAT_DOM)
    if t in geraden:
        return None, "die had je al gast"
    return t, None


def scherm(woord, geraden, fout, level, praat, geil=False, spuit=0):
    cls()
    print("GALGJE maar dan vies")
    print()
    tekening(fout, geil=geil, spuit=spuit)
    print()
    print("level:", level)
    print("woord:", status(woord, geraden))
    print("nog", MAX_WRONG - fout, "fouten over")
    used = " ".join(sorted(geraden)) if geraden else "-"
    miss = " ".join(sorted(c for c in geraden if c not in woord)) or "-"
    print("al gehad:", used)
    print("fouten:", miss)
    if praat:
        print()
        print(praat)
    print()


def spuit_animatie(woord, geraden, level):
    zinnen = [
        "laatste fout. hij is er klaar voor",
        "hij perst",
        "oh fuck",
        "daar komt ie",
        "en ie blijft komen",
        "jesus christ",
    ]
    for i, zin in enumerate(zinnen):
        scherm(woord, geraden, MAX_WRONG, level, zin, geil=True, spuit=i)
        wacht(0.45)
    scherm(
        woord,
        geraden,
        MAX_WRONG,
        level,
        "hij is klaargekomen. overal. je hebt verloren. dikke pech.",
        geil=True,
        spuit=6,
    )
    print("woord was", woord)
    print("volgende keer beter raden of niet. whatever")


def speel():
    level = kies_level()
    woord = random.choice(WORDS[level])
    geraden = set()
    fout = 0
    praat = "raad het woord. als je faalt spuit hij. letterlijk."

    while True:
        if all(c in geraden for c in woord):
            scherm(woord, geraden, fout, level, praat)
            print("je hebt het. hij is dry. teleurgesteld. jammer voor hem.")
            print("woord was", woord)
            return
        if fout >= MAX_WRONG:
            spuit_animatie(woord, geraden, level)
            return

        scherm(woord, geraden, fout, level, praat)
        raw = vraag("letter of heel het woord: ")
        gok, err = lees_gok(raw, geraden)
        if err:
            praat = err
            continue

        if len(gok) > 1:
            if gok == woord:
                geraden.update(woord)
                praat = "kut je had em meteen. saai."
            else:
                fout += 1
                praat = gok.lower() + "? lol nee. " + random.choice(PRAAT_FOUT)
            continue

        geraden.add(gok)
        if gok in woord:
            n = woord.count(gok)
            extra = " (zit er " + str(n) + "x in)" if n > 1 else ""
            praat = random.choice(PRAAT_GOED) + extra
        else:
            fout += 1
            praat = random.choice(PRAAT_FOUT)


def nogeen():
    while True:
        a = vraag("nog een keer? j/n: ").strip().lower()
        if a in ("j", "ja", "y"):
            return True
        if a in ("n", "nee", "no"):
            return False
        print("j of n")


def main():
    random.seed()
    cls()
    print("GALGJE")
    print("nederlands woord raden")
    print("fout raden = hij wordt geiler")
    print("7x fout = hij spuit")
    print()
    print(len(WORDS["makkelijk"]), "makkelijke woorden /",
          len(WORDS["gemiddeld"]), "gemiddeld /",
          len(WORDS["moeilijk"]), "moeilijk")
    print()
    vraag("enter en gaan ")

    while True:
        speel()
        print()
        if not nogeen():
            print("oke doei")
            break
        cls()


if __name__ == "__main__":
    main()
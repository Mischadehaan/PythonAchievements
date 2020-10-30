# Dagelijkse keuzes maken

print('De bel gaat. Wat doe je? je doet de deur OPEN, of je doet NIKS')

choice = input()
if choice == 'OPEN':
    print('Je doet de deur open en het is de postbode')

elif choice == 'NIKS':
    print('Je doet niks en staat nu bekend als de man die nooit open doet.')

# keuze twee
print('Je bent aan het lopen naar school')
print('Het lijkt alsof iemand je aandacht zoekt maar je hebt oortjes in')
print('doe je je oortjes in om te LUISTEREN? of NEGEER je hem?')

choice2 = input()
if choice2 == 'LUISTEREN':
    print('Je luistert naar hem en hij zegt dat je je portemonnee hebt laten vallen')

elif choice2 == 'NEGEER':
    print('Je negeert hem en je dag gaat verder alsof er niks is gebeurt.')
    print('Je merkt wel dat je portemonnee kwijt is. hmm wat gek.')

# keuze 3
print('Je wil wat eten maar er is keuze tussen een BROODJE of een KOEKJE')
print('Wat kies je?')

choice3 = input()
if choice3 == 'BROODJE':
    print('Je koopt een broodje. hij is erg lekker')

elif choice3 == 'KOEKJE':
    print('Je koopt een koekje, hij is erg lekker')

# keuze 4
print('je ligt te slapen. ineens hoor je een knal. wat doe je?')
print('KIJKEN? of NIKS?')

choice4 = input()
if choice4 == 'KIJKEN':
    print('je kijkt waar het geluid vandaan komt. er is gewoon iets omgevallen in je kamer.')
    print('niks om je zorgen over te maken')
elif choice4 == 'NIKS':
    print('Je blijft liggen en maakt je er nog de hele nacht zorgen over')

# keuze 5
print('Je moet daily choices verzinnen voor een school opdracht')
print('Wat doe je? BEDENKEN? of NIKS?')

choice5 = input()
if choice5 == 'BEDENKEN':
    print('je krijgt genoeg studiepunten')
elif choice5 == 'NIKS':
    print('Je komt in de problemen met de leerplicht')

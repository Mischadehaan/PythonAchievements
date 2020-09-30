import time

print("Hello You!, ik ben Mischa")
time.sleep(2)
print("Wie ben jij?")

username = input("Jouw naam:")

print("Hello " + username)
print(" ")
time.sleep(2)

print("Ik ben een nieuwkomer op het Mediacollege Amsterdam")
print("dit is mijn verhaal over hoe ik hier ben gekomen.")
print(" ")
time.sleep(3)

print("Ik ben geboren in syrië waar toen ik 12 was een oorlog gaande was.")
print("Mijn moeder, zus en ik moesten vluchten terwijl onze vader achterbleef in ons thuisland.")
print("Op een dag hoorden we een raar geluid, het leek een beetje op een vliegtuig")
print("en een raar fluitend geluid volgde. Wat ga ik doen?")
print(" ")
time.sleep(3)

print("A: Schuilen")
print("B: Zoeken waar het geluid vandaan komt")
print("C: Rennen")

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

while True:
	choice = input(">>> ")
	if choice in answer_A:
		print('Ik vind een plek om te schuilen en overleef de bombardering,')
		print('maar een meneer met een geweer vind me. Wat moet ik doen?')
		print(' ')

		print('A: Pak het geweer uit zijn handen en schiet hem neer')
		print('B: Doe je handen omhoog.')
		print(' ')

		choice = input('>>> ')
		if choice in answer_A:
			print('Je probeert het wapen te pakken maar hij schiet je neer.')
			break

		elif choice in answer_B:
			print('Je doet je handen omhoog maar hij schiet je nogsteeds neer.')
			break

	elif choice in answer_B:
		print('Ik zoek waar het geluid vandaan komt, maar voor ik het weet komt er een explosie')
		print('alles word zwart en ik denk dat het over is voor mij.')
		break

	elif choice in answer_C:
		print('Ik ren zo hard als ik kan en de bommen weten mij niet te raken,')
		print('ik ren zo lang door dat ik bij een splitsing kom. Rechts zijn meer explosies, maar links is een zee')

		print('Welke weg neem ik?')
		print(' ')

		print('A: Links')
		print('B: Rechts')
		print(' ')
		
		choice = input('>>> ')
		if choice in answer_A:
			print('Je vind een grote boot met 100 mensen en een paar uur later ben je in een veilig land.')
			print('Einde verhaal je leeft nog lang en gelukkig.')
			break
		elif choice in answer_B:
			print('Je gaat naar rechts en heb nog een lang avontuur in het oorlogs land voordat je tragisch overlijd')
			print('aan een grote bombardering.')
			break

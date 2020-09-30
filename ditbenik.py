from time import sleep

print("Hello You!, ik ben Mischa")
sleep(2)
print("Wie ben jij?")

username = input("Jouw naam:")

print("Hello " + username)
print(" ")
sleep(2)

print("Ik ben een nieuwkomer op het Mediacollege Amsterdam")
print("door een aantal vragen over mij te beantwoorden leer je mij beter kennen")
print(" ")
sleep(3)

print("Waar woon ik?")
print(" ")
sleep(3)

print("A: Amsterdam")
print("B: Hoorn")
print("C: Purmerend")

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

while True:
	choice = input(">>> ")
	if choice in answer_A:
		print('Fout antwoord, probeer het opnieuw')
		continue
	elif choice in answer_B:
		print('Goed antwoord')
		break
	elif choice in answer_C:
		print('Fout antwoord, probeer het opnieuw')
		continue

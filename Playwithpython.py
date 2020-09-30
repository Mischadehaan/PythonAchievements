Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Mischa')
Mijn naam is Mischa
>>> naam = 'Mischa'
>>> print(naam)
Mischa
>>> Print(naam.upper())
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    Print(naam.upper())
NameError: name 'Print' is not defined
>>> print(naam.upper())
MISCHA
>>> pritn(naam[0:2])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    pritn(naam[0:2])
NameError: name 'pritn' is not defined
>>> print(naam[0:2])
Mi
>>> print(naam[::-1])
ahcsiM
>>> leeftijd = 16
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Mischa ben je al 16 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Over 2 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)
763
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
311
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 311
>>> from datetime import datetime
>>> datum = datetime.now()
>>> prit(datum)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    prit(datum)
NameError: name 'prit' is not defined
>>> print(datum)
2020-09-10 15:11:11.188038
>>> datum.strftime('%A %d %B %Y')
'Thursday 10 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'donderdag 10 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'giovedì 10 settembre 2020'
>>> 
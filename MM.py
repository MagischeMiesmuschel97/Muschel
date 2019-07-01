

import os
import time
import numpy
import random

def clear():
	try:
		os.system("clear")
	except:
		os.system("cls")
def schnur(n,t):
	if(n==0):
		n = 12
	if(t==0):
		t = 0.2
	i = n
	while i >= 0:
		print"            _______"
		print"       ____/*/*****\___"
		print"   ___/***| |       ***\_"
		print" _/**/ /  / \____      **\ "
		print"\*| | |  |  /++++\___    *\_"
		print" \|/ /  / /++++++++++\_____*\ "
		print"   \/  /  \++++++++/  _____\|"
		print"    \__\__   \++/  __/      V"
		print"          \___ ___/"
		print"             \O/"
		for j in range(0,i):
			print"	      |"
		print "	      O"
		time.sleep(t)
		clear()
		i = i-1
def posans():
	pos = ["Ja.","Ja!","Definitiv!","Die Chancen stehen gut.","Kann gut sein.","Das kann ich bestaetigen.","Unbedingt!","Klar.","Warum nicht?","Auf jeden Fall!","Wenn du willst."]
	return pick(pos)
def negans():
	neg = ["Nein.","Nein!","Lieber nicht.","Absolut nicht.","Wohl kaum.","Heute nicht.","Die Antwort lautet nein.","Sieht schlecht fuer dich aus.","Auf keinen Fall!","Negativ.","Unwahrscheinlich.","Erst morgen wieder.","Bei Neptuns Bart! Nein!","Nur am Gegenteiltag."]
	return pick(neg)
def neutans():
	neut = ["Versuch's doch einfach spaeter nochmal.","Vielleicht morgen.","Keine Ahnung.","Nur mit ner Menge Fantasie!","Ich weiss nicht.","Da bin ich mir unsicher.","Frag doch einfach nochmal.","Woher soll ich das wissen? Frag jemand anders!","Womoeglich.","Wenn du Glueck hast.","Eines Tages vielleicht."]
	return pick(neut)
def pick (a):
	return a[int(numpy.floor(random.randrange(0,len(a))))]
def quit(a):
	s = ""
	if a=="quit" or a=="Quit" or a=="close" or a=="Close" or a=="end" or a=="End" or a=="exit" or a=="Exit":
		quit()
	return s	

#Main program

clear()
a = ""
while 1 == 1:
	a = raw_input("Ich bin die magische Miesmuschel! Stelle mir eine Frage!\n\n")
	clear()
	schnur(0,0)
	clear()
	if quit(a)=="":
		r = random.randrange(0,3)
		if r == 0:		
			print posans()
		if r == 1:		
			print negans()
		if r == 2:		
			print neutans()
	time.sleep(3)
	clear()

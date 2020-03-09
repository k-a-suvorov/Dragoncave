try:

	from random import randint
	from time import sleep
	import os
	import sys
	import colorama
	from colorama import Fore, Style
	colorama.init()

	def animationLoad():
		start = ['T', 'U', 'R', 'N', ' ', 'O', 'N', '.', '.', '.']
		print(Fore.RED + ' ')
		sleep(0.1)
		for i in range(0, len(start)):
			sleep(0.1)
			print(Fore.GREEN, Style.BRIGHT + " ", start[i], end="")
			

	def animationShut():
		start = ['T', 'U', 'R', 'N', ' ', 'O', 'F', 'F', '.', '.', '.']
		print(Fore.RED + ' ')
		sleep(0.1)
		for i in range(0, len(start)):
			sleep(0.1)
			print(Fore.RED, Style.BRIGHT + " ", start[i], end="") 
				
	def clearScreen():
		if (os.name == 'nt'):
			sleep(2)
			os.system('cls')
		elif (os.name == 'posix'):
			sleep(2)
			os.system('clear')
		else:
			print(Fore.YELLLOW, Back.RED + 'Другие операционные системы не поддерживаются!')
			clearScreen()
			sys.exit()

	def displayIntro():
		animationLoad()
		print(Fore.YELLOW, Style.BRIGHT + '')
		print('''Вы находитесь в землях заселенных драконами
		Перед собой Вы видите две пещеры, в которых спрятаны сокровища.
		В одной пещере добрый дракон, в другой злой... ''')
		print()

	def choiceCave():
		cave = ' '
		while (cave != '1' and cave != '2'):
			print(Fore.CYAN, Style.BRIGHT + ' ')
			print('В какую пещеру вы хотите заглянуть? Нажмите 1 или 2')
			cave = input('>>> ')
		return cave

	def checkCave(chosenCave):
		print(Fore.RED, Style.BRIGHT + ' ')
		print('Вы приближаетесь к пещере...')
		sleep(2)
		print('Которая вас сильно пугает...')
		sleep(2)
		print('Но так хочется золота...')
		sleep(2)
		print('Большой дракон медленно появляется перед вами... и...')
		sleep(2)
		friendyCave = randint(1, 2)
		if chosenCave == str(friendyCave):
			print(Fore.GREEN, Style.BRIGHT + '')
			print('Дракон лапой указывает на гору золота позади себя и вы понимаете, что вам лучше поторопиться')
		else: 
			print(Fore.RED, Style.BRIGHT + ' ')
			print('Дракон нападает и съедает вас полностью!')
			animationShut()

	playAgain = '1'

	while (playAgain == '1'):
		displayIntro()
		caveNumber = choiceCave()
		checkCave(caveNumber)
		clearScreen()
		print(Fore.CYAN, Style.BRIGHT + ' ')
		print('Испытаете удачу? (нажмите \"1\" на клавиатуре) или любую клавишу, что бы выйти из программы')
		playAgain = input('>>> ')

except ValueError:
    print("You have some mistake of userinput Value!")
except TypeError:
    print("You have some mistake of type Value!")
except SystemError:
    print("This is system mistake! Please don't panic! Relax!")
except ImportError:
    print("Some modules not loaded, please check your source code!")

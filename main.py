# Change version at 13th Line and 'info' at 25th line

from json_manager import *
import random
import colorama
from colorama import Fore

colorama.init(autoreset=True)

class Program:
	def __init__(self):
		self.diff = 1
		print(f"{Fore.YELLOW}Welcome to WordGuess! [v1 BETA]")
		self.entry()

	def entry(self):
		user_inp = input("> ")
		if user_inp.lower() == "new":
			self.new_word()
		if user_inp.lower() == "exit":
			print(f"{Fore.YELLOW}Thanks For Playing!")
			quit()
		if user_inp.lower() == "info":
			print(f"{Fore.CYAN}Developer: Jaazim")
			print(f"{Fore.CYAN}Version: v1 BETA")
			print("")
			print(f"{Fore.CYAN}This Program is Solo Developed and Purely Written in Python (and JSON for Data).")
		if user_inp.lower() == "change diff" or user_inp.lower() == "change difficulty" or user_inp.lower() == "diff":
			self.change_diff()
		self.entry()

	def new_word(self):
		jsn_word = Json_Manager("word.json", False)
		jsn_hint = Json_Manager("hint.json", False)
		random_no = random.randint(0, int(jsn_word.get_data("total")))
		x_list = list(jsn_word.get_data(str(random_no)))
		str1 = ""
		for ele in x_list:
			str1 += ele
		self.orginal_word = str1
		#print(f"orginal word -> {orginal_word}")
		#print(f"random word -> {x}")
		random.shuffle(x_list)
		self.x_list = x_list
		#print(f"random word after shuffling -> {x}")
		def ask():
			global x_list, orginal_word
			str2 = ""
			for ele in self.x_list:
				str2 += ele
			if self.diff == 1:
				print(f"Scrambled Word -> {Fore.CYAN}{str2}")
				print(f"Hint -> {Fore.CYAN}{jsn_hint.get_data(str(random_no))}")
				print("")
				user_guess = input(f"Enter Your Guess (Don't Leave Whitespace) > ")
				if str(user_guess.lower()) == self.orginal_word:
					print(f"{Fore.GREEN}Yay You Got It Correct!")
					self.entry()
				elif str(user_guess.lower()) == "skip":
					print(f"{Fore.YELLOW}You Skipped The Question")
					print("")
					print("")
					self.entry()
				else:
					print(f"{Fore.RED}Wrong Guess, Try Again!")
					print("")
					print("")
					ask()
		ask()



	def change_diff(self):
		print("Change Difficulty: 1 -> Easy (Hints Allowed), 2 -> Hard (No Hints)")
		print(f"Current Difficulty -> {self.diff}")
		new_diff_value = input("Enter a Value for New Difficulty (1/2)> ")
		if new_diff_value == "1" or new_diff_value == "2":
			self.diff = int(new_diff_value)
			print(f"Changed Difficulty to")
			if self.diff == 1:
				print(f"{Fore.YELLOW}Easy!")
			elif self.diff == 2:
				print(f"{Fore.YELLOW}Hard")
			else:
				print(f"{Fore.RED}Inccorect self.diff value! code Error")
		else:
			print(f"{Fore.RED}Inccorect Value Provided! (Value Options : 1 or 2)")
			self.entry()

if __name__ == '__main__':
	prg = Program()
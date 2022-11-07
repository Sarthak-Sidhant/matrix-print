#credit for this code goes to @Pythonica on Youtube
#https://www.youtube.com/watch?v=30N9Qr25u28
#the program is called matrix print or the most complicated hello world program ever


import random
from colorama import Fore
from time import sleep

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{};':,./<>?`~"


def random_str(string):
    return "".join([random.choice(alphabet) if i != " " else " " for i in string])


word = input("Add Text Here: ")
word_list = list(word)

shuffled_indices = [i for i in range(len(word))]
random.shuffle(shuffled_indices)

jumbled_word_list = list(random_str(word))
sleep(1)

for i in range(len(word)):
	word_list[shuffled_indices[i]] = (Fore.GREEN + word_list[shuffled_indices[i]]+ Fore.RESET)
	jumbled_word_list[shuffled_indices[i]] = word_list[shuffled_indices[i]]
	output = "".join(jumbled_word_list)
	print(output, end="\r")
	sleep(0.05)

print()

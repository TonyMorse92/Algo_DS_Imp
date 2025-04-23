######################################################
# Making a simulation of the famous Monty Hall problem:
# url: https://en.wikipedia.org/wiki/Monty_Hall_problem
# Hopefully, this helps with my intuition
######################################################

import random

num_iterations = int(input("\nHow many trials: "))
num_doors = 3


def simulate_problem(switch, num_iterations):
	wins = 0
	count = 0
	prize_door = True

	while (count < num_iterations):
		# Put the "car" behind a random door
		car_door = random.randint(0,num_doors - 1)

		# Choose a door
		door_choice = random.randint(0,num_doors - 1)

		 
		if switch:
			if car_door == door_choice:
				wins += 0 # You are switching into a loser
			else:
				wins +=1 # We win, because we are shown the door that doesn't have the car

		else:
			if car_door == door_choice:
				wins += 1
		
		count += 1

	return wins


print(f"For {num_doors} doors")

num_wins_on_switch = simulate_problem(True, num_iterations)
print("Over",num_iterations,"iterations, you win",num_wins_on_switch,"if you switch")

num_wins_on_stay = simulate_problem(False, num_iterations)
print("Over",num_iterations,"iterations, you win",num_wins_on_stay,"if you don't switch")

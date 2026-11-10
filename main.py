
print("Sawhney's Life: The Lost Key")
print("Sawhney is a brave ranger.")
print("A lost key is hidden somewhere in the nearby forest.")
print("Find it before nightfall!")

name = "Sawhney"
character_class = "Ranger"
health = 10
gold = 0
story_step = 1
playing = True

while playing:
	if story_step == 1:
		print("\nYou are at home. Your backpack is ready.")
		print("1. Leave for the forest")
		print("2. Rest")
		print("3. Quit")
		choice = input("Choose 1, 2, or 3: ")

		if choice == "1":
			story_step = 2
			print("You leave home and enter the forest.")
		elif choice == "2":
			health = 10
			print("You rest before starting your adventure.")
		elif choice == "3":
			playing = False
		else:
			print("Please choose 1, 2, or 3.")

	elif story_step == 2:
		print("\nYou find two paths in the forest.")
		print("1. Follow the path with footprints")
		print("2. Go back home")
		choice = input("Choose 1 or 2: ")

		if choice == "1":
			story_step = 3
			print("You follow the footprints and reach an old bridge.")
		elif choice == "2":
			story_step = 1
			print("You walk back home to think about your choice.")
		else:
			print("Please choose 1 or 2.")

	elif story_step == 3:
		print("\nThe bridge is old, but it looks safe enough.")
		print("1. Cross the bridge")
		print("2. Rest by the river")
		choice = input("Choose 1 or 2: ")

		if choice == "1":
			story_step = 4
			print("You cross the bridge and discover a small cave.")
		elif choice == "2":
			health = 10
			print("You rest by the river and feel ready to continue.")
		else:
			print("Please choose 1 or 2.")

	elif story_step == 4:
		print("\nThe cave is dark and quiet.")
		print("1. Search the cave")
		print("2. Leave the cave")
		choice = input("Choose 1 or 2: ")

		if choice == "1":
			gold = gold + 1
			print(name, "found the lost key under a rock!")
			print("You return home safely with", gold, "gold.")
			print("You completed the adventure!")
			playing = False
		elif choice == "2":
			story_step = 3
			print("You leave the cave and return to the bridge.")
		else:
			print("Please choose 1 or 2.")


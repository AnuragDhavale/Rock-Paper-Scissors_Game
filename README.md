Brief Explanation:
1.	Imports:
o	random: Used to generate random choices for the computer.

2.	Choices List:
o	choices = ["Rock", "Scissors", "Paper"]: Defines the possible choices for the game.

3.	Function get_user_choice:
o	This function prompts the user to choose Rock, Scissors, or Paper.
o	It validates the input to ensure the user enters a valid choice (1, 2, or 3).
o	It returns the corresponding choice from the choices list.

4.	Main Game Loop:
o	The game runs in a loop, allowing for multiple rounds of 5 games each until the user decides to exit.
o	It initializes user_score and computer_score to zero for each round of 5 games.
o	Prompts the user to start the game or exit.
	If the user chooses to start (1), it plays 5 rounds:
	For each round, it gets the user's choice and randomly selects the computer's choice.
	It compares the choices and updates the scores based on who wins or if it's a draw.
	After 5 rounds, it displays the final scores and the overall winner.
	If the user chooses to exit (2), it exits the loop and ends the game.
	If the input is invalid, it prompts the user again.

5.	Game Logic:
o	If the choices are the same, it's a draw.
o	The user wins if their choice beats the computer's choice according to the game rules.
o	Otherwise, the computer wins.
This structure ensures a clear and user-friendly game flow, with proper input validation and clear separation of different parts of the game logic

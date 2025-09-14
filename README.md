# 🎲 Guess the Number Game

A fun, interactive Python terminal game where you try to guess the number the computer is thinking of!
Each correct guess advances you to the next round with a larger number range.
Can you keep winning as the difficulty increases?

# 🚀 Features

Random number generation 🎯

Colorful feedback messages using ANSI escape codes 🌈

Increasing difficulty with each round 🔼

Limited tries (10 per round) ⏳

Option to replay after losing or winning 🔁

# 🛠️ How to Play

1. Run the script:

python guess_number.py

2. The game will display:

* Round number

* Available tries

* Range of numbers to guess from

3. Type a number to make your guess.

4. The game will respond with:

✅ Correct guess → advance to the next round

📉 Too low → guess higher

📈 Too high → guess lower

❌ No tries left → option to play again

# 📖 Rules

You start with Round 1 and 10 tries.

The range begins at 1–100.

Each new round:

Range increases by +100

Tries reset to 10

Lose all tries? → You can restart from Round 1.

# 📦 Requirements

Python 3.x

No external libraries needed (only random is used).

# ▶️ Example Gameplay
Round 1! You have 10 tries!
Guess the number (1-100): 50
 Too Low!
Guess the number (1-100): 75
 Too High!
Guess the number (1-100): 62
 You guessed right!
Type [yes] if you want to go to the NEXT ROUND. Else type [no].

# 🏆 Challenge Yourself

How many rounds can you clear?
Try to beat your personal best score and keep leveling up! 🎉

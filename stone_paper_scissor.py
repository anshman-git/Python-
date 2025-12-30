import random

guess = random.randint(1, 3)
choice_names = {1: "Stone", 2: "Paper", 3: "Scissor"}
a = int(input("Enter 1.For Stone 2.For Paper 3.For Scissor : "))

results = {
    1: ["Lose", "Tie", "Win"],
    2: ["Win", "Tie", "Lose"],
    3: ["Lose", "Win", "Tie"]
}

print(f"Your choice: {choice_names[a]}")
print(f"Computer choice: {choice_names[guess]}")
print(results[a][guess - 1])
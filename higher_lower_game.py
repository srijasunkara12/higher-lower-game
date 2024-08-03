import random

import game_art
import game_database

print(game_art.game_logo)
score=0
def display_accountinfo(acount):
    name=account_1["name"]
    description=account_1["description"]
    college=account_1["college"]
    return f"{name} is a {description} and studied in {college}"
def check_answer(guess,age_1,age_2):
    if age_1< age_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False
account_1=random.choice(game_database.data)
account_2=random.choice(game_database.data)

print(f"Compare 1: {display_accountinfo(account_1)}")
print("VS")
print(f"Compare 2: {display_accountinfo(account_2)}")
guess=int(input("Who has more age?? Type 1 or 2:"))
age_count_1=account_1["age"]
age_count_2=account_2["age"]
print(age_count_1)
print(age_count_2)

is_correct= check_answer(guess,age_1,age_2)
if is_correct:
    score +=1
    print(f"You are right.Your score is: {score}")
else:
    print(f"Your wrong. Your score is: {score}")
display_accountinfo(account_1)
display_accountinfo(account_2)
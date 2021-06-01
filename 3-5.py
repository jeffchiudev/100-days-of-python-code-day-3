# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

total_T = lower_case_name1.count("t") + lower_case_name2.count("t")
total_R = lower_case_name1.count("r") + lower_case_name2.count("r")
total_U = lower_case_name1.count("u") + lower_case_name2.count("u")
total_E = lower_case_name1.count("e") + lower_case_name2.count("e")
total_L = lower_case_name1.count("l") + lower_case_name2.count("l")
total_O = lower_case_name1.count("o") + lower_case_name2.count("o")
total_V = lower_case_name1.count("v") + lower_case_name2.count("v")

total_true = total_T + total_R + total_U + total_E
total_love = total_L + total_O + total_V + total_E

score = str(total_true) + str(total_love)

score_int = int(score)

if score_int < 10 or score_int > 90:
  print(f"Your score is {score_int}, you go together like coke and mentos.")
elif score_int > 40 and score_int < 50:
  print(f"Your score is {score_int}, you are alright together")
else:
  print(f"Your score is {score_int}")
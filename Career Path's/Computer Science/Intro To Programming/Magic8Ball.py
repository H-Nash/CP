#Magic 8-Ball Project
import random

#Var Declaration
name = "Nathan"
question = "Will I wake up on time?"
answer = ""
random_number = random.randint(1,10)

#Logic
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Im not Magic.... Sorry kid"
else:
  print("Error, out of bounds")

if not question == "":
  if not name == "":
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer : {answer}")
  else:
    print(f"Question: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
else:
  print("If you do not have a question I cannot answer. Reality hangs in the balance!")

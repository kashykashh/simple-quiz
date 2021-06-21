print('Welcome to my quiz')

play = input('Do you want to play? ').lower()
if play.lower() != 'yes':
    quit()

print("let's start playing!")
score = 0
answer = input("What does GPU stand for? ").lower()
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPU stand for? ").lower()
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does NAT stand for? ").lower()
if answer.lower() == "Network address translation":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f'Your total score is {score}')
print("You have obtained" + str((score /4) * 100) + "%")
score = int(input("What is your score?: "))
has_moderation = input("Is this year has moderation?[y/n]: ").lower() == "y"

is_passed = True
got_distinction = False
got_honors = False

if score < 40:
    is_passed = False
    print("FAILED")
elif score >= 40 and score < 75:
    print("PASSED")
elif score >= 75 and score < 90:
    got_distinction = True
    print("DISTINCTION")
elif score >= 90 and score <= 100:
    got_honors = True
    print("HORNORS")
else:
    print("INVALID SCORE")

print()
print("[ SYSTEM RESULT ]")

if(is_passed and not(got_distinction or got_honors)):
    print("Good try")
elif(not is_passed and has_moderation):
    print("You just lucky")
elif(got_distinction or got_honors):
    print("You did it well")
else:
    print("Try next year")
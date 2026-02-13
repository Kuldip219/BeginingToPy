import random

def game():
    print("You are now playing the game...")
    score = random.randint(0, 100)
    with open("File_Io/hiscore.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    with open("File_Io/hiscore.txt", "w") as f:
        if score > hiscore:
            f.write(str(score))
            print("Congratulations! You have the new high score:", score)
        else:
            f.write(str(hiscore))
            print("Your score:", score)
            print("The current high score is:", hiscore)
    
    return score

game()
from nim import train, play

while True:
    timeText = input('Use time? (y/N)')

    if timeText.lower() == "n":
        time = False
        break
    elif timeText.lower() == "y":
        time = True
        break

if time == False:
    while True:
        inNum = input('How many games would you like the AI to play?')
        try:
            int(inNum)
            break
        except:
            pass

if time == True:
    while True:
        inNum = input('How many seconds of games would you like the AI to play?')
        try:
            float(inNum)
            break
        except:
            pass

ai = train(float(inNum), time)
play(ai)

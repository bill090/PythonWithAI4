from nim import train, play

while True:
    timeText = input('Use time? (y/N)  ')

    if timeText.lower() == "n":
        time = False
        break
    elif timeText.lower() == "y":
        time = True
        break

if time == False:
    while True:
        inNum = input('How many games would you like the AI to play?  ')
        try:
            inNum = int(inNum)
            break
        except:
            pass

if time == True:
    while True:
        inNum = input('How many seconds of games would you like the AI to play?  ')
        try:
            inNum = float(inNum)
            break
        except:
            pass

ai = train(inNum, time)

while True:
    while True:
        choice = input('Keep Training, Play (Again), or Quit? (k/p/Q)').lower()
        if choice in ['k', 'p', 'q']:
            break
    if choice == 'q':
        break

    if choice == 'k':
        while True:
            timeText = input('Use time? (y/N)  ')

            if timeText.lower() == "n":
                time = False
                break
            elif timeText.lower() == "y":
                time = True
                break
        
        if time == False:
            while True:
                inNum = input('How many games would you like the AI to play?  ')
                try:
                    inNum = int(inNum)
                    break
                except:
                    pass

        if time == True:
            while True:
                inNum = input('How many seconds of games would you like the AI to play?  ')
                try:
                    inNum = float(inNum)
                    break
                except:
                    pass

        ai = train(inNum, time, ai)
    
    if choice == 'p':
        play(ai)

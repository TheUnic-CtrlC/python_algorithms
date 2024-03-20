voted = {}
def check_vote(name):
    if voted.get(name):
        print('voted! go back')
    else: 
        voted[name] = True
        print('dont voted! come on')

check_vote('mike')
check_vote('tom')
check_vote('mike')
#1 priveli gakvze gavaketed

def greet(name):
    return f"Hello, {name} how are you doing today?" #2

#3 mesamec gakvze gavaketed

def digitize(n):
    return [int(i) for i in str(n)][::-1] #4

def paperwork(n, m):
    if m < 0 or n < 0:
        return 0
    else:
        return n  * m #6

def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo" #7
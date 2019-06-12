from time import sleep


def parser( s):
    a = 0
    count = 0
    i = 1
    n = len(s[0])
    if s[0][0] == '<':
        a += 1
    elif s[0][0] == '>':
        a -= 1
    while a > 0 and i < n:
        if s[0][i] == '<':
            a += 1
            i +=1
        elif s[0][i] == '>':
            a -= 1
            count += 2
            i +=1
    return count

        
if __name__ == "__main__":
    n = int(raw_input("Type then number of strigs"))
    for i in range(n):
        s = raw_input("type ur string").rstrip().split()
        count = parser ( s)
        print count
        print " "
    sleep(15)

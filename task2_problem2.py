from time import sleep


def find_max(s, L, R, v):
    for i in range(L-1, R):
        s[i] +=v


if __name__ == "__main__":
    size = int(raw_input("type the number of elements in the array:"))
    n = int(raw_input("type the number of queries:"))
    s = []
    for i in range(size):
        s.append(i+1)
    for i in range(n):
         s1 = raw_input("your query here:").rstrip().split()
         L, R, v = s1
         find_max(s, int(L), int(R), int(v))
    print max(s)
    sleep(10)

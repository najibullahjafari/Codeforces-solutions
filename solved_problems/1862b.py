import sys
input = sys.stdin.read

data = input().split()
index = 0

t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    extracted = list(map(int, data[index:index + n]))
    index += n

    original = []
    original.append(extracted[0])

    for i in range(1, len(extracted)):
        if extracted[i] >= extracted[i-1]:
            original.append(extracted[i])
        else:
            if extracted[i] == 1:
                original.append(extracted[i])
                original.append(extracted[i])
            else:
                original.append(extracted[i]-1)
                original.append(extracted[i])

    print(len(original))
    print(" ".join(map(str, original)))

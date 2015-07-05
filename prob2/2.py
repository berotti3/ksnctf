import sys
input_lines = raw_input().split()
alf = "abcdefghijklmnopqrstuvwxyz"
alf2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num = alf.find("n")-alf.find("a")

for word in input_lines:
    for ch in word:
        if ch in alf:
            sys.stdout.write( alf[(alf.find(ch)+num)%26])
            continue
        if ch in alf2:
            sys.stdout.write( alf2[(alf2.find(ch)+num)%26])
            continue
        if ch == "," or ch == ".":
            sys.stdout.write(ch)
            continue
    print " ",

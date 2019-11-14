fh = open("OIFileHandling/example2.txt", "r")
kt = open("OIFileHandling/test.txt", "w")

kt.write(fh.readline())
kt.close()

# print(fh.read(5))
print("\n")
# print(fh.read(15))
# print(fh.readline())
# print(fh.readlines()[1])
for line in fh:
    # print(line)
    print(len(line.split(" ")))


length = len(fh.readlines()[0])
print(f"Length: {length}")

fh.close()

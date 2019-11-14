fh = open("OIFileHandling/example2.txt", "w")

for i in range(1, 11):
    fh.write("Line: %d \n" % i)  # need to be string

fh.close()

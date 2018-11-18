lines_per_file = 1000
smallfile = None
count = 0
with open('tweets_tech.csv') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                count += 1
                smallfile.close()
            small_filename = 'tweets_{}.csv'.format(count)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()

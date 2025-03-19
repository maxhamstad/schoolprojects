from ICPCScore import ICPCScore
filename = 'icpcsscore main.py' 
infile = open(filename, 'r')
names = infile.readline()
for line in infile:
    name, points, minutes, last_accepted  = line.split(',')
    points = int(points)
    minutes = int(minutes)
    last_accepted = int(last_accepted)
    name = str(name)
    score = ICPCScore(name, points, minutes, last_accepted)
    print(score)



    
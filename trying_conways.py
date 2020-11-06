import random, copy ,time



width = 60
height = 20

nextturn = []

for w in range(width):
    new = []
    for h in range(height):
        if random.randint(0,1) == 0:
            new.append('#')
            
        else:
            new.append('')
            
    nextturn.append(new)
    
boolean_logic = True

while boolean_logic: # print the game
	print('\n\n\n')
	turn = copy.deepcopy(nextturn)

	for w in range(width):
		for h in range(height):
			print(turn[w][h], end='')
		print()

	for w in range(width):
		for h in range(height):
			leftcoordinate = (w - 1) % width 
			rightcoordinate = (w + 1) % width
			downcoordinate = (h - 1) % height
			upcoordinate = (h + 1) % height

		numneighbours = 0	
		if turn[leftcoordinate][upcoordinate] == '#':
			numneighbours = numneighbours + 1
		elif turn[w][upcoordinate] == '#':
			numneighbours = numneighbours + 1
		elif turn[rightcoordinate][upcoordinate] == '#':
			numneighbours = numneighbours + 1
		elif turn[leftcoordinate][h] == '#':
			numneighbours = numneighbours + 1
		elif turn[rightcoordinate][h] == '#':
			numneighbours = numneighbours + 1
		elif turn[leftcoordinate][downcoordinate] == '#':
			numneighbours = numneighbours + 1
		elif turn[w][downcoordinate] == '#':
			numneighbours = numneighbours + 1
		elif turn[rightcoordinate][downcoordinate] == '#':
			numneighbours = numneighbours + 1

		if turn[w][h] == '#' and(numneighbours == 2 or numneighbours ==3):
			nextturn[w][h] = '#'
		elif turn[w][h] ==  '' and numneighbours == 3:
			nextturn[w][h] == '#'
		else:
			nextturn[w][h] = ''
	time.sleep(1)





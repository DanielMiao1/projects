def basicPattern(n: int) -> str:
	"""
	If n = 4, returns:
	1
	2 2
	3 3 3
	4 4 4 4
	"""
	def yieldPattern():
		for x in range(1, n + 1): yield " ".join([str(y) for y in range(1, x + 1)])
	
	return "\n".join([i for i in yieldPattern()])

def centeredBasicPattern(n: int) -> str:
	"""
	If n = 4, returns:
		 1
		2 2
	 3 3 3
	4 4 4 4
	"""
	def yieldPattern():
		for i in range(1, n + 1): yield " ".join([str(i) for _ in range(1, i + 1)]).center(
			len(" ".join([" " for _ in range(1, n + 1)]))).rstrip()
	
	return "\n".join([i for i in yieldPattern()])

def pascalsTriangle(n):
	"""
	If n = 7, prints:
	        1
         1 1
        1 2 1
       1 3 3 1
      1 4 6 4 1
    1 5 10 10 5 1
   1 6 15 20 15 6 1
	"""
	
	previous_characters = ""
	
	def getPairSum(characters) -> list:
		sums = []
		for x in range(0, len(characters) - 1): sums.append(characters[x] + characters[x + 1])
		return sums
	
	def getCharacters(number):
		if number == 1:
			return "1"
		if number == 2:
			return "1 1"
		return "1 " + " ".join(str(i) for i in getPairSum(previous_characters)) + " 1"
	
	rows = []
	
	for i in range(1, n + 1):
		_characters = getCharacters(i)
		rows.append(_characters)
		previous_characters = [int(i) for i in _characters.split()]
	
	for i in rows:
		print(i.center(len(rows[-1])))


pascalsTriangle(9)

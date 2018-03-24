def answer(x):
	uniqueCodes = set()
	for code in x:
		if code not in uniqueCodes and code[::-1] not in uniqueCodes:
			uniqueCodes.add(code)
	return len(uniqueCodes)

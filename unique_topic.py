#! /usr/bin/python

def get_unique_topics(file):
	result = []
	
	with open(file, 'r') as f:
		lines = f.readlines()
		
	for line in lines:
		for topic in line.strip().split(', '):
			if topic and topic not in result:
				result.append(topic)
				
	return result


if __name__ == "__main__":
    file = '/home/khalid/Programs/khalid/python/SE_expectation_python/file.txt'
    result = get_unique_topics(file)
    for r in result:
    	print(r)


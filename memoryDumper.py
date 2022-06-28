
import sys

import re


if len(sys.argv) != 2:

	print("Usage: " + str(sys.argv[0]) + " <process PID>")

	exit(0)


pID = sys.argv[1]

mapFile = "/proc/" + str(pID) + "/maps"

memFile = "/proc/" + str(pID) + "/mem"

outputFile = str(pID) + ".dump"

   
try:

	with open(mapFile, 'r') as mapF:

		with open(memFile, 'rb', 0) as memF:
	
			with open(outputFile, 'wb') as outputF:

				for line in mapF.readlines():

					m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
					
					if(m.group(3) == 'r'):
	
						start = int(m.group(1), 16)

						end = int(m.group(2), 16)
					
						memF.seek(start)
					
						try:

							chunk = memF.read(end - start)

							outputF.write(chunk)
						
						except OSError:

							continue

				print("Memory Dump Saved To " + outputFile)
					

except Exception as e:

	print("Error Encountered: " + str(e))

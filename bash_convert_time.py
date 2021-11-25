from datetime import datetime
import sys

def time_con(time):
	timea=time.replace("#","")
	aaa=datetime.fromtimestamp(int(timea))
	#print(aaa)
	return str(aaa)

f = open(sys.argv[1], "r")
arr=[]
for x in f:
  arr.append(x.replace("\n", ""))

start=0
thennum=1

def convertTuple(tup):
    str = ''.join(tup)
    return str

for i in arr:
	if(thennum<len(arr)):
		output=(arr[start],",",time_con(arr[start]),",",arr[thennum])
		output=convertTuple(output)+str("\n")
		print(output)
		start=start+2
		thennum=thennum+2
		
		file1 = open('bash_time_processed.csv', 'a')
		file1.write(output)
		file1.close()

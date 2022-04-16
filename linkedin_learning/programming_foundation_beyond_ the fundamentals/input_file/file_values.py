infile = open('values.txt','rt')
outfile = open('output.txt','wt')
 
sum = 0
for line in infile:
    sum+=int(line)
print('the total is = '+ str(sum),file=outfile)
outfile.close()
print('completed')
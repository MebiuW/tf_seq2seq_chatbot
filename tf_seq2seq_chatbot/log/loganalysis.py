logfile = open('log.txt')
output = open('data.csv','w+')
lines = logfile.readlines()
data = []
for i in range(0,len(lines),5):
    line = lines[i]
    tokens = line.strip('\n').split(' ')
    step = tokens[2]
    perplexity = tokens[-1]
    perplexity1 = lines[i+1].strip('\n').split(' ')[-1]
    perplexity2 = lines[i+2].strip('\n').split(' ')[-1]
    perplexity3 = lines[i+3].strip('\n').split(' ')[-1]
    perplexity4 = lines[i+4].strip('\n').split(' ')[-1]
    print step + '    ' + perplexity +' '+perplexity1+' '+perplexity2+' '+perplexity3+' '+perplexity4
    output.write(step+'\t'+perplexity+'\t'+perplexity1+'\t'+perplexity2+'\t'+perplexity3+'\t'+perplexity4+'\n')
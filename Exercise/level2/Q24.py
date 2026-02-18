'''Read a log file and count how many lines contain 'ERROR', 'WARNING', and 'INFO'. Print a
summary report with counts for each.'''

err = 0
warn = 0
info = 0 

with open("log.txt",'r') as f:
    for line in f.readlines():
        if line.startswith('ERROR'):
            err += 1
        elif line.startswith('WARNING'):
            warn += 1
        elif line.startswith('INFO'):
            info += 1

f.close()

print(f"ERROR : {err} lines  \t WARNING : {warn} lines \t INFO : {info} lines")


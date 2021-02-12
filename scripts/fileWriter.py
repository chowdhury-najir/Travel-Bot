#write to csv file
import csv

def writeFile(filename,columnName):
    file= open(filename,'w')
    writer=csv.writer(file)
    writer.writerow(columnName)
    return writer,file
    
        

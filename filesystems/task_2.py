from task_1 import getdictPurchaseLog

dictLog = getdictPurchaseLog()

with open('filesystems//visit_log.csv', 'r', encoding='UTF8') as f:
    
    with open('filesystems//funnel.csv', 'w', encoding='UTF8') as g:
    
       for line in f:
        
          lineList = line.strip().split(',')
        
          if lineList[0] in dictLog:
             lineList.append(dictLog[lineList[0]]) 
             lineString = ','.join(lineList) + '\n'
             g.write(lineString)
           
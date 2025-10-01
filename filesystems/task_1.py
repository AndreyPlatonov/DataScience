import json

def getdictPurchaseLog(): 
   
    
   with open('filesystems//purchase_log.txt', 'r', encoding='UTF8') as f:
     dictPurchaseLog = {}

     for line in f:
    
       lineJson = json.loads(line)
       
       dictPurchaseLog[lineJson['user_id']] = lineJson['category']
      
     dictPurchaseLog.pop('user_id')  
     return dictPurchaseLog    

getdictPurchaseLog()


   

 





documents = [
{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
{'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]


directories = {
'1': ['2207 876234', '11-2'],
'2': ['10006'],
'3': []
}


def getOwnerDocumentByNumber(numer):
   """
    функция возвращает владельца документа по номеру документа.
     
   """
    
   names = [] 
   
   [ names.append(doc['name']) for doc in documents   if doc['number'] == numer]
   
   if names == []:
      return ''
   else:       
      return names[0] 

def getShelfByDocumentNumber(numer):
    
    """
    функция возвращает номер полки документа по номеру документа.
    
    """
    
    keys = [key for key, value in directories.items() if numer in value]
    if keys == []:
       return ''
    else:
       return keys[0]

def listAllDocumentsInfo():
    
    """
    функция возвращает список атрибутов всех документов
    
    """
    
    alldocuments = documents
    for all in alldocuments:
        all['shelf'] =  getShelfByDocumentNumber(all['number'])
    return alldocuments 

def listAllShelf():
    
    """
     функция возвращает список всех полок
           
    """
    
    return ', '.join(map(str, list(directories.keys())))
 
def addShelfByNumber(numer):
    
    """
     функция добавляет полку по номеру полки. возвращает Истина, иначе Ложь

    """
    
    if numer in directories:
       return False
    else:  
       directories.setdefault(numer, [])
       return True  
 
 
def removeShelfByNumber(numer):
    
    """
      функция удаляет полку по номеру полки. возвращает статус . 

    """
    
    if numer in directories:
    
       if directories.get(numer) == []:
         
           directories.pop(numer)
           return 0
           
       else:
           
         return 1      
        
    else:
                             
       return 2
     
   

commandLine = ''

while commandLine != 'q':
  commandLine = input ('Введите команду: ')
 
  if commandLine == 'p':
     
     numer = str(input ('Введите номер документа: '))
     owner=getOwnerDocumentByNumber(numer)
          
     if len(owner) == 0:
        print('Документ не найден в базе')
     else: 
        print(f'Владелец документа: {owner}')  
     
          
  elif commandLine == 's':
     numer = str(input ('Введите номер документа: '))
     shelf = getShelfByDocumentNumber(numer)
     
     if len(shelf) == 0:
        print('Документ не найден в базе')
     else: 
        print(f'Документ хранится на полке: {shelf}')    
     
     
  elif commandLine == 'l':
      
     alldoc =  listAllDocumentsInfo()
     for all in alldoc:
         print(f'№: {all['number']}, тип: {all['type']}, владелец: {all['name']}, полка хранения: {all['shelf']}')
     
  elif commandLine == 'ads':
     
     shelf = str(input ('Введите номер полки: '))
     shelfStatus = addShelfByNumber(shelf)
     
     if not shelfStatus:
        print(f'Такая полка уже существует. Текущий перечень полок: {listAllShelf()}')
     else: 
        print(f'Полка добавлена. Текущий перечень полок:  {listAllShelf()}') 
      
     
  elif commandLine == 'ds':
     
      shelf = str(input ('Введите номер полки: '))
      shelfRemoveStatus = removeShelfByNumber(shelf)
      
      if shelfRemoveStatus == 2:
          print(f'Такой полки не существует. Текущий перечень полок: {listAllShelf()}')
      elif shelfRemoveStatus == 1:
          print(f'На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {listAllShelf()}')
      elif shelfRemoveStatus == 0:
          print(f'Полка удалена. Текущий перечень полок: {listAllShelf()}')
              
     
  elif commandLine == 'q':
     print('Программа завершена')
     break    
  else: 
     print('Команда введена некорректно')
        
         
                  
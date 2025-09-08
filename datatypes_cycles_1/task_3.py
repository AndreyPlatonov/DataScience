boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls) :
    print ('Внимание, кто-то может остаться без пары!')
else:
    dating=zip(sorted(boys), sorted(girls))
    print ('Идеальные пары:  ')
    for Element in dating:
      print(f' {Element[0]} и {Element[1]}') 
        
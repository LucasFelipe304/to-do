general_list = []
while True:
  def allOptions():
    print('1 | Add item ')
    print('2 | Change list')
    print('3 | Delete item')

  allOptions()


  print('Your list is empty.')
  userAddItem = str(input('Enter what you want to add: '))
  general_list.append(userAddItem)
  
  for item in general_list:
    print('-', item)



  




def allOptions():
  print('1 | Add item ')
  print('2 | Change list')
  print('3 | Delete item')

allOptions()
general_list = []

user = str(input('What do you want to-do: '))
print('--->', user)

if user == '1':
  addItem = str(input('Add item: '))
  general_list.append(addItem)
  print(general_list)
  



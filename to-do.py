general_list = []
def space():
  print()
space()


def allOptions():
  stringChangeYourOption = ('Change your option:')
  print(stringChangeYourOption)
  space()
  print('1 | Add item ')
  print('2 | Delete item')
  print('3 | View list')

while True:
  userAddItem = str(input('Firstly, enter what you want to add: '))
  if len(userAddItem) > 0:
    general_list.append(userAddItem)
    print('--- > Added item!')
    break

space()


allOptions()


variableChangeYourOption = str(input('Change your option: '))

if variableChangeYourOption == '2' and len(general_list) > 0:
  def userDeleteItem():
    for item in enumerate(general_list):
      print(item)
    getListIndex = int(input('Enter the index of the item you want to change: ')) 
    print(f'--- > Item [{general_list[getListIndex]}] removed.!')
    general_list.pop(getListIndex)
    return general_list
  userDeleteItem()
elif variableChangeYourOption == '2' and len(general_list) <= 0:
  print("""You can't remove items because your list it's empty.""")

if variableChangeYourOption == '3':
  def userViewList():
    i = 0
    for item in general_list:
      print(f'{i} -', item)
      i += 1
    return general_list
  userViewList()


 





  


 
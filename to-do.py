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
  print('3 | Change list')
  print('4 | View list')


userAddItem = str(input('Firstly, enter what you want to add: '))
general_list.append(userAddItem)
print('--- > Added item!')
space()

allOptions()

variableChangeYourOption = str(input('Change your option: '))
if variableChangeYourOption == '2':
  for item in enumerate(general_list):
    print(item)
  getListIndex = int(input('Enter the index of the item you want to change: ')) 
  print(f'--- > Item [{general_list[getListIndex]}] removed.!')
  general_list.pop(getListIndex)
  





  


 
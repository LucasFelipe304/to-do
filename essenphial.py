general_list = []
def space():
  print()
space()

def sep():
  print(end='  ')

def lines():
  print('_' * 20)

def allOptions():
  lines()
  space()
  print('1 | Add item ')
  print('2 | Delete item')
  print('3 | View list')
  print('4 | Exit')
  lines()

while True:
  def AddItem():
    userAddItem = str(input('Enter what you want to add: '))
    general_list.append(userAddItem)
    print(f'-- > Added item! [{userAddItem}]')
    return general_list
  break

allOptions()


while True:
  choiceUserOption = str(input('Change your option: '))
  if choiceUserOption == '1':
    space()
    space()
    print('| Add item')
    sep()
    AddItem()
    space()
    space()

  if choiceUserOption == '2' and len(general_list) > 0:
    def userDeleteItem():
      space()
      space()
      print('| Delete item')
      for item in enumerate(general_list):
        sep()
        print(item)
      space()
      sep()
      getListIndex = int(input('Enter the index of the item you want to change: ')) 
      print(f'-- > Item [{general_list[getListIndex]}] removed.!')
      general_list.pop(getListIndex)
      return general_list
    userDeleteItem()
    space()
    space()


  elif choiceUserOption == '2' and len(general_list) <= 0:
    print("You can't remove items because your list it's empty.")

  if choiceUserOption == '3' and len(general_list) > 0:
    def userViewList():
      i = 0
      for item in general_list:
        print(f'{i} -', item)
        i += 1
      return general_list
    userViewList()

  elif choiceUserOption == '3' and len(general_list) <= 0:
    print("You can't to see items because your list it's empty.")
    space()

  if choiceUserOption == '4':
    space()
    exit('Developed by Lucas Felipe - github.com/LucasFelipe304')
 





  


 
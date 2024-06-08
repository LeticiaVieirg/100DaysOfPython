def repeating_numbers(list1, list2):
  set_numbers1=set(list1)
  set_numbers2=set(list2)
  repeating_numbers=set_numbers1.intersection(set_number2)

  return list(repeating_numbers)

def main():
  list1=input('Enter the numbers in the first list separeted by a comma: ').split(',')
  list2=input('Enter the numbers in the second list separeted by a comma: ').split(',')

  list1=[int(num) for num in list1]
  list2=[int(num) for num in list2]

  repeating_list_numbers=repeating_numbers(list1, list2)

  print('Repeated list numbers: ', repeated_list_numbers)

if __name__=='__main__':
  main()

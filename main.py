while True:
  # 1- input first number
  while True: 
    try: 
      first_number = float(input( 'Enter the first number: '))
      break
    except ValueError:
      print('Invalid input. Please enter a numeric value')
  # 2- input operation type
  while True:
    try:
      operation = input( 'Enter the operation type: ')
      if operation in ('+', '-' , '*', '/'):
        break
      else:
        raise ValueError
    except ValueError:
      print('Invalid operator, Please enter +, -, *, / ')
        
  # 3- input second number
  while True:
   try:
    second_number = float(input( 'Enter the second number: '))
    if second_number == 0 and operation == '/':
      raise ZeroDivisionError
    break
   except ZeroDivisionError:
      print('Cannot devide by zero.')
   except ValueError:
      print('Invalid input. Please enter a numeric value')
  # 4- print the result 
  if operation == '+':
        result = first_number + second_number
  elif operation == '-':  
        result = first_number - second_number
  elif operation == '*': 
        result = first_number * second_number
  elif operation == '/':
        result = first_number / second_number
  print('Result is: ', result)
  
    # 5- ask if user wants to continue
  while True:
    repeat = input('Do u want to perform another operation? (Yes/No) ')
    if repeat in ('Yes' , 'No') :
      break
    else:
      print('invalid input, please try again')
  if repeat == 'No':
    print('Thanks for using our calculator <3')
    break
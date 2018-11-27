def get_valid_command(valid):
  '''Prompt for and return a string that is a valid command
  i.e., a string in the list "valid".'''
    
  command = raw_input("Please enter a command: ")    
  while command not in valid:
    print "Invalid command"
    command = raw_input("Please enter a command: ")            
  
  return command # command is valid here

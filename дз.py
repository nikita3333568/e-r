def ignore_command(command): 
    ignore = ['sql', 'alias', 'ip', 'select', 'update', 'del'] 
    for word in ignore: return word in command


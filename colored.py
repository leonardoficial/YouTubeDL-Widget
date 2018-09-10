from colorama import init, Fore, Back, Style

init(autoreset=True)

default_config = {
  "print_value":        Fore.YELLOW,
  "print_pair_key":     Fore.YELLOW,
  "print_pair_val":     Fore.WHITE,

  "list_message":       Fore.YELLOW,
  "list_item":          Fore.GREEN,
  
  "list_options_index": Fore.GREEN,
  "list_options_value": Fore.WHITE
}

class Colored(object):

  def __init__(self, obj={}):
    self.config = default_config.copy()
    self.config.update(obj)
  
  
    
  def print_value(self, value):
    val_color = self.config.get("print_value")
    
    print("{}{}".format(val_color, value))
    
    
    
  def print_pair(self, key, val):
    key_color = self.config.get("print_pair_key")
    val_color = self.config.get("print_pair_val")
    
    print("{}{}: {}{}".format(key_color, key, val_color, val))
    
    
    
  
  # print message followed by a list of items
  def list(self, message, iterable):
    """  
    """
    
    temp = []
    item_color    = self.config.get("list_item")
    message_color = self.config.get("list_message")
    
    for k in iterable:
      temp.append("{}{} ".format(item_color, k))
  
    print("{}{}".format(message_color, message))
    print(*temp)
    
    return input()
  
  
  # print a list of options with [index] format
  def list_options(self, iterable):
    """  
    """
    
    index_color = self.config.get("list_options_index")
    value_color = self.config.get("list_options_value")
    
    """
    for index, value in enumerate(iterable):
      print("{} [{}] {} {}".format(index_color, index, value_color, value))
    """
    
    for key, value in iterable.items():
      print("{} [{}] {} {}".format(index_color, key, value_color, value))
    
      
    chosen = int(input())
    
    return list(iterable.values())[chosen]
    



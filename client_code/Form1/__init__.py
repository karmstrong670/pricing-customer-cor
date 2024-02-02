from ._anvil_designer import Form1Template
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.  
    #anvil.users.login_with_form()
    
item_list = []
for row in list(app_tables.costdata.search()):
    item_list.append((row["itemNumber"], row))
    print((row["itemNumber"], row))
  
#drop_down_cost_items.items = item_list
  #self.drop_down_cost_items.items = [(row["itemNumber"], row) for row in app_tables.costdata.search()]
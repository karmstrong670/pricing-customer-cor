from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables





class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    #anvil.server.call('import_excel_data', "AnvilTestFile.xlsx")
  
    # Any code you write here will run before the form opens.  
    #anvil.users.login_with_form()
    #self.drop_down_cost_items.items = [(row["itemNumber"], row) for row in app_tables.costdata.search(itemNumber=q.like('%10%'))]
 
  def txtboxItem_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    "need to add distinct search"
    self.drop_down_cost_items.items = set((row["itemNumber"]) for row in app_tables.costdata.search(
      tables.order_by("itemNumber"),
      itemNumber=q.like('%'+self.txtboxItem.text+'%')))
    
    pass
  
  def drop_down_cost_items_change(self, **event_args):
    """This method is called when an item is selected"""
    print(self.drop_down_cost_items.selected_value)
    self.drop_down_cost_uofm.items = [(row["unitOfMeasure"], row) for row in app_tables.costdata.search(
      itemNumber=self.drop_down_cost_items.selected_value) ]
    
    pass

  def drop_down_cost_uofm_change(self, **event_args):
    """This method is called when an item is selected"""
    self.label_price_final.text = [(row["price"]) for row in app_tables.costdata.search(
      itemNumber=self.drop_down_cost_items.selected_value,
      unitOfMeasure= self.drop_down_cost_uofm.selected_value["unitOfMeasure"] ) ]
    pass


    
  

  
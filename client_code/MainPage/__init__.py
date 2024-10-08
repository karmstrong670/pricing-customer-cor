from ._anvil_designer import MainPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables





class MainPage(MainPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    #anvil.server.call('import_excel_data', "AnvilTestFile.xlsx")
  
    # Any code you write here will run before the form opens.  
    anvil.users.login_with_form()
    
  
  
  def txtboxItem_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    "need to add distinct search"
    items = []
    prices = []
    
    # resets dropdown for qty and price text
    
    self.drop_down_cost_uofm.items = items
    self.label_price_final.text = "" 
    
    self.drop_down_cost_items.items = set((row["itemNumber"]) for row in app_tables.costdata.search(
      tables.order_by("itemNumber"),
      itemNumber=q.like(''+self.txtboxItem.text+'%')))
    #clears selected value
    self.drop_down_cost_items.selected_value = None
    
    # if one item set item field and get data for unit of measure
    if len(self.drop_down_cost_items.items) == 1 :
      self.drop_down_cost_items.selected_value = self.txtboxItem.text

      self.drop_down_cost_uofm.items = set((row["unitOfMeasure"]) for row in app_tables.costdata.search(
        itemNumber=self.drop_down_cost_items.selected_value) )
      self.label_price_final.text = ""
    # checks if one unit of measure 
    if len(self.drop_down_cost_uofm.items) == 1:
      self.drop_down_cost_uofm.selected_value = self.drop_down_cost_uofm.items[0]
      
      prices = [(row["price"]) for row in app_tables.costdata.search(
      itemNumber=self.drop_down_cost_items.selected_value,
      unitOfMeasure= self.drop_down_cost_uofm.selected_value ) ]
      self.label_price_final.text = prices[0]

    
    pass
  
  def drop_down_cost_items_change(self, **event_args):
    """This method is called when an item is selected"""
    #print(self.drop_down_cost_items.selected_value)
    self.drop_down_cost_uofm.items = set((row["unitOfMeasure"]) for row in app_tables.costdata.search(
      itemNumber=self.drop_down_cost_items.selected_value) )
    #clears selected value
    self.drop_down_cost_uofm.selected_value = None
    self.label_price_final.text = "" #resets price text 
    pass

  def drop_down_cost_uofm_change(self, **event_args):
    """This method is called when an item is selected"""
    prices = []
    prices = [(row["price"]) for row in app_tables.costdata.search(
      itemNumber=self.drop_down_cost_items.selected_value,
      unitOfMeasure= self.drop_down_cost_uofm.selected_value ) ]
    self.label_price_final.text = prices[0]
    pass


    
  

  
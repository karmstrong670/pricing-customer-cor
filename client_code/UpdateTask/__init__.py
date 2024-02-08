from ._anvil_designer import UpdateTaskTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class UpdateTask(UpdateTaskTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
    anvil.server.call('import_excel_data', "AnvilTestFile.xlsx")
    # Any code you write here will run before the form opens.

import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
from anvil.tables import app_tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd 


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

#import anvil.server
#anvil.server.connect("server_T7BB4FRZ2ZQPS7LGZYP4VY4F-T4DSUVPVTZK3CXVC")

@anvil.server.callable
def import_excel_data(file):
  with anvil.files.data_files.open(file,"rb") as f:
  #with open(file, "rb") as f:
    df = pd.read_excel(f)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      app_tables.costdata.add_row(**d)

#import_excel_data("AnvilTestFile.xlsx")
from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    app_tables.table_0.delete_all_rows()
    self.repeating_panel_1.items = app_tables.table_0.search()
   


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    compartment_value = self.new_compartment.selected_value
    compartments = [r['compartment'] for r in app_tables.table_0.search()]
 
    if (compartment_value in compartments):
      alert("A Compartment is already in use")
      new_value = int(self.new_compartment.selected_value) + 1
      self.new_compartment.selected_value = str(new_value)
      return

    names = [r['compartment'] for r in app_tables.table_0.search()]

    app_tables.table_0.add_row(medication_name = self.new_medication_name.text, dosage = self.new_dosage.selected_value, dosage_time = self.new_dosage_time.date, compartment = self.new_compartment.selected_value)
    self.repeating_panel_1.items = app_tables.table_0.search()
    
    self.new_medication_name.text =""
    self.new_dosage.selected_value = "1"
    self.new_dosage_time.date = self.new_dosage_time.placeholder
    self.new_compartment.selected_value = "1"
 

    self.refresh_data_bindings()
    
    pass

  def new_medication_name_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def new_dosage_time_change(self, **event_args):
    """This method is called when the selected date changes"""
    pass

  def send_to_box_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    # Get an iterable object with all the rows in my_table
    all_records = app_tables.table_0.search()
    # For each row, pull out only the data we want to put into pandas
    

    records = []
    
    medication_names = []
    dosages = []
    dosage_times = []
    compartments = []
    for r in all_records:
       medication_names.append(r['medication_name'])
       dosages.append(r['dosage'])
       dosage_times.append(r['dosage_time'])
       compartments.append(r['compartment'])
     
    records.append(medication_names)
    records.append(dosages)
    records.append(dosage_times)
    records.append(compartments)
    
    records.append(self.text_box_1.text)

    alert("Thank you for recording your responses")
    anvil.server.call('bring_back_medication_data', records)

    app_tables.table_0.delete_all_rows()
    self.repeating_panel_1.items = app_tables.table_0.search()

    pass

  def new_compartment_change(self, **event_args):
    """This method is called when an item is selected"""        
    compartment_value = self.new_compartment.selected_value
    compartments = [r['compartment'] for r in app_tables.table_0.search()]
 
    if (compartment_value in compartments):
      alert("Compartment already in use")
      new_value = int(self.new_compartment.selected_value) + 1
      self.new_compartment.selected_value = str(new_value)
    pass


  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
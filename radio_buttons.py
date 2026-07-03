import streamlit as st

def radio_buttons_exclusive(row_labels = ["one", "two", "three"], col_headers = [1, 2, 3], reassignment_strategy = "first"):
  """Enables the creation of a 2D grid of radio buttons that disallow multiple selections in a row or column (zero selections is allowed).
  
  Args:
    row_labels (list): A list that dictates the names of the labels of the rows. The values entered should be 
                       able to be converted to a string (though you only need to do the conversion yourself if 
                       it's an object that requires a custom to_string(). The length of this list will be the 
                       number of rows of buttons.
    col_headers (list): A list that dictates the names of the headers of the columns. The values entered should 
                        be able to be converted to a string (though you only need to do the conversion yourself if 
                        it's an object that requires a custom to_string())The length of this list will be the number 
                        of columns of buttons.
    reassignment_strategy (string): The strategy that determines where a button is moved if it conflicts with the 
                                    recently changed button:
      - "first": The button conflicting with the recently selected button is moved to the first available slot
      - "swap": The conflicting selected button is swapped with the recently selected button
  """
  horizontal = len(col_headers) > len(row_labels)
  
  var_names = row_labels if horizontal else col_headers
  var_names = [str(val) for val in var_names] # var_names is used for the label arg in st.radio() which requires a string input

  button_options = col_headers if horizontal else row_labels

  '''
  Assign unique initial values to the session states that will later be assigned to the buttons
  This is how the buttons start with unique/non-conflicting selections
  '''
  for i, default_val in enumerate(button_options):
    key = f"rad{i}"
    if key not in st.session_state:
      st.session_state[key] = default_val

  '''
  Distinct columns are only necessary if the buttons are vertical
  The assignment of "var_names" is a subsitute of equal length to "cols" that doesn't cause issues in the enumeration of "cols" below
  '''
  cols = var_names if horizontal else st.columns(len(col_headers), border = False)

  def rad_change(changed):
    """rad_change is triggered when a radio button is updated. When triggered, it checks for another conflicting button, and, if it finds one, moves that button to the first available slot.

    Args:
      changed (int): The index of the changed radio button. "rad{chaaged}"` is the radio button's key, used to obtain its current value from the session_state.
    
    Returns:
      None:
    """
    for i in [i for i in range(len(var_names)) if i != changed]:
      if st.session_state[f"rad{changed}"] == st.session_state[f"rad{i}"]:
        available_indices = list(set(range(len(button_options))) ^ {button_options.index(st.session_state[f"rad{j}"]) for j in range(len(var_names)) if j != i}) # The available indices are the indices not currently being used (all indices xor in-use indices)
        st.session_state[f"rad{i}"] = button_options[available_indices[0]]
        break

  """
  Generates the radio buttons with keys given by f"rad{i}"
  Radio button are only put in columns if horizontal is False
  """
  for i, col in enumerate(cols):
    try:
      with col:
        st.radio(label = var_names[i], options = button_options, horizontal = horizontal, key = f"rad{i}", on_change = rad_change, args = (i,))
    except:
      st.radio(label = var_names[i], options = button_options, horizontal = horizontal, key = f"rad{i}", on_change = rad_change, args = (i,))
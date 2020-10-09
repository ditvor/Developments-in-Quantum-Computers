import wikipedia
import pandas as pd
import matplotlib.pyplot as plt

""" Demonstrates the max value of qubits in an industry. """

# Connect to the wikipedia page to get an url.
quant_comp_page = wikipedia.page("List of quantum processors")

# Pandas module allows to get page's tables as a feature of read_html.
# All we need is a page's url and the table's index.
url = quant_comp_page.url

# Download a table for universlal computer's qubits.
processors_table = pd.read_html(url)[0]

# Also download a table for noisy qubits.
dwave_table = pd.read_html(url)[1]


# Here we use list comprehension to clean the data in the cell.
# We do it by splitting it with a separator=' '.
# And also transform it to the int() in order to find the max value
processors_table['Qubits'] = [int(text.split(' ', 1)[0])
                              for text in processors_table['Qubits']]

# Creating a new dataframe with beautiful data
processors_df = pd.DataFrame(
    processors_table, columns=['Manufacturer', 'Name/Codename/Designation', 'Qubits'])

# Renaming a column name just for the better visualization
processors_df = processors_df.rename(
    columns={'Name/Codename/Designation': 'Name'})

# Find the max value of qubits
max_qubits = max(processors_df['Qubits'])

# Create a list of the top quantum computer in the industry
top_quantum_comp = list(*processors_df[processors_df['Qubits']
                                       == max_qubits].values.tolist())


# Perform a similar process for noisy qubits table.
# Here we transform data to int type for qubits.
dwave_table['Qubits'] = [int(text.split(' ', 1)[0])
                         for text in dwave_table['Qubits']]

# Transform date to int type.
dwave_table['Release date'] = [int(text.split(' ', 2)[-1])
                               for text in dwave_table['Release date']]

# Cleaning up a little bit our table with D-wave noisy qubits
dwave_df = pd.DataFrame(
    dwave_table, columns=['Qubits', 'Release date'])

dwave_df = dwave_df.rename(columns={'Release date': 'Year'})

# Prepare data for export as a list
dwave_qubits = dwave_df['Qubits'].values.tolist()
dwave_year = dwave_df['Year'].values.tolist()

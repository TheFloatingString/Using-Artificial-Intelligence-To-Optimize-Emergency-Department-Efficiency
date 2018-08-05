import pandas as pd
import numpy as np

# Read Dataset
df_data = pd.read_excel("Sample_Data_Modified.xlsx")

print("DATASET:")
print(df_data.head())

processed_dataset = []

X = []      # training dataset  [vector of doctors per 4-hour block]
y = []      # PIA time  [average PIA time per 4-hour block]

# Process data
for row in range(df_data.shape[0]):
    processed_temp_row = []
    processed_temp_row.append(df_data['Arrival '][row])
    processed_temp_row.append(df_data["PIA_NPIA"][row])
    processed_temp_row.append(df_data["StaffMD"][row])
    processed_dataset.append(processed_temp_row)

print("\nProcessed Data")
for row in processed_dataset:
    print(row)

list_of_doctors = list(df_data["StaffMD"].unique())
print("LIST OF DOCTORS:")
print(list_of_doctors)

block = 0

doctors_present = []    # list of doctors present
block_hours = []        # list of PIA times per 4-hour block
doctors_vector = [0]*len(list_of_doctors)
average_PIA = 0.0

date_codes = []
for row in processed_dataset:
    day = str(row[0].day)
    if len(str(row[0].day)) == 1:
        day = '0' + str(row[0].day)

    current_date = str(row[0].month)+'-'+day+'-'+str(row[0].year)+' '+str((row[0].hour) % 6)
    date_codes.append(current_date)

date_codes = np.array(date_codes)

df_data['date_codes'] = date_codes

print(np.sort(np.unique(date_codes)))
date_codes_unique = np.sort(np.unique(date_codes))

for date_code in date_codes_unique:
    print()
    print(date_code)
    df_selection = df_data.ix[df_data["date_codes"] == date_code]

    block_hours = []
    doctors_vector = [0]*len(list_of_doctors)

    for df_row in df_selection.iterrows():
        index, row = df_row

        # compute doctor vector
        for doctor_index in range(len(list_of_doctors)):
            if list_of_doctors[doctor_index] == row["StaffMD"]:
                doctors_vector[doctor_index] = 1    #TODO equals or increment?

        # compute PIA time
        PIA = row["PIA_NPIA"] - row["Arrival "]
        # PIA = PIA.total_seconds()
        print(row["Arrival "])
        print(row["PIA_NPIA"])

        #TODO HERE SHOULD BE THE PIA TIME! :D

    X.append(doctors_vector)
    y.append(sum(block_hours)/len(block_hours))

for row, value in zip(X, y):
    print(row, value)

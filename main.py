from datetime import datetime
import pandas as pd

filename = 'glucose_10-19-2022-unsorted.csv'
timestamp_label = 'Enhetens tidsstämpel'
value_label = 'Historiskt glukosvärde mmol/L'

df = pd.read_csv(filename, header=1)

df_filter = df[df['Registertyp'] == 0]

df_clean = df_filter.loc[:, [timestamp_label, value_label]]

print("\nBefore datetime converter")
print(df_clean)

df_clean[timestamp_label] = pd.to_datetime(df_clean[timestamp_label], format="%m-%d-%Y %I:%M %p")

print("\nAfter datetime converter")
print(df_clean)

df_sorted = df_clean.sort_values(by=timestamp_label)

print("\nAfter sorting")
print(df_sorted)

print("After resampling")
print(df_sorted.resample("H", on=timestamp_label).mean())

print("After resampling")
print(df_resampled)

# for i, row in df.iterrows():
#     date = datetime.strptime(row[timestamp_label], "%m-%d-%Y %H:%M %p")
#     df_clean[i, timestamp_label] = "test"

# print(df_clean)





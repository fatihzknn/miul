import seaborn as sns

df = sns.load_dataset("car_crashes")

df.columns = [x.upper() for x in df.columns]

new_list = [("FLAG_" + col) if "INS" in col else ("NO_FLAG_" + col)   for col in df.columns]

print(new_list)

import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

df.groupby(["sex", "embark_town", "class"]).agg({
    "age":"mean",
    "survived": "mean",
    "sex" : "count"
})


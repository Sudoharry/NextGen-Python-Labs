# To create dataframe from your own columns and data

import pandas as pd

data = {
    'Element': ['Earth','Water','Fire','Air'],
    'Symbol': ['🜃','🜄','🜂','🜁']
}
df = pd.DataFrame(data)
print(df)
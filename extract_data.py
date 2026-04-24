#import pandas library
import pandas as pd

#create dictionary with data
data = {
    "id": [1,2,3,4,5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 35, 40, 45],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}

# convert to tabluar format using pandas
df = pd.DataFrame(data)

# show data
print(df)
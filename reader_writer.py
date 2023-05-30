import pandas as pd

def xyz_to_df(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[2:] # Skip first two lines
    data = []
    for line in lines:
        data.append(line.split()) # Split each line into a list

    df = pd.DataFrame(data, columns=['atom', 'x', 'y', 'z'])
    df[['x', 'y', 'z']] = df[['x', 'y', 'z']].apply(pd.to_numeric)

    return df

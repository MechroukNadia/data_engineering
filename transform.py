import glob
import json

import pandas as pd


def get_all_filenames():
    # this function should return a list of filenames
    # you should look at glob library
    # Example: it should return ["raw_data_1686027160.json", "raw_data_1686027165.json", "raw_data_1686027170.json"]
    filenames = glob.glob('raw_data_*')
    return filenames
    

def transform_one_file(filename):
    # this function should return a list of dictionaries
    # each dictionnary should look like that: { "city": city, "latitude": latitude, "longitude": longitude , "temperature": tempature, "time": time}
    with open(filename, 'r') as file:
        data = json.load(file)

    Liste = []
    for key, value in data.items():
        Liste.append({
            "city" : key,
            "latitude": value["latitude"],
            "longitude": value["longitude"],
            "temperature": value["current_weather"]["temperature"],
            "time" : value["current_weather"]["time"]
        })
    return Liste
   

def merge_all_files_in_pandas_df(files):
    output = []
    for fname in files:
        output_one_file = transform_one_file(fname)
        output.extend(output_one_file)
    df = pd.DataFrame(output)
    return df

def drop_duplicates(df_):
    # drop duplicated rows using a function of pandas.DataFrame
    df_deduplicated = df_.drop_duplicates()
    return df_deduplicated


def main_transform():
    files = get_all_filenames()
    df = merge_all_files_in_pandas_df(files)
    df = drop_duplicates(df)
    df.to_csv("transformed_data.csv", index=False)
    print(df)


main_transform()
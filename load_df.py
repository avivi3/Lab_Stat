def load_df(data_type):

  urls = {"city" : "https://raw.githubusercontent.com/avivi3/Lab_Stat/master/votes%20per%20city%202020.csv?token=AO7MXJSWRSCU6UKZM4PVMQS7TFS7E",
          "ballot" : "https://raw.githubusercontent.com/avivi3/Lab_Stat/master/votes%20per%20ballot%202020.csv?token=AO7MXJRUEM5CTRE3PSFND527TFTAU",
          "eshkol" : "https://raw.githubusercontent.com/avivi3/Lab_Stat/master/Eshkol%20Hevrati%20Calcali.csv",
          "ballot2019" : "https://raw.githubusercontent.com/avivi3/Lab_Stat/master/vote%20per%20ballot%202019.csv",
          "city2019" : "https://raw.githubusercontent.com/avivi3/Lab_Stat/master/votes%20per%20city%202019.csv"}

  raw = bool(" raw" in data_type)
  if raw:
    data_type = data_type.split()[0]
  
  if not (data_type in urls.keys() or " raw" in data_type):
    print("Wrong input - no such database exists")
    return 

  elif data_type == "city" or data_type == "city raw":
    df_2020_raw = pd.read_csv(urls[data_type], encoding = 'iso-8859-8', index_col='שם ישוב')
    df_2020_raw = df_2020_raw.drop(index = 'מעטפות חיצוניות')
    if raw:
      return df_2020_raw
    df_2020 = df_2020_raw.drop('סמל ועדה', axis=1) # new column added in Sep 2019
    df_2020 = df_2020[df_2020.columns[5:-1]] # removing "metadata" columns
    df_2020.style.set_properties(**{'text-align': 'right'})
    return df_2020

  elif data_type == "ballots":
    df_2020_ballots_raw = pd.read_csv(urls[data_type], encoding = 'iso-8859-8', index_col='שם ישוב')
    df_2020_ballots = df_2020_ballots_raw.drop('סמל ועדה', axis=1) # new column added in Sep 2019
    df_2020_ballots = df_2020_ballots.drop(index = 'מעטפות חיצוניות')
    return df_2020_ballots

  elif data_type == "eshkol":
    df_eshkol = pd.read_csv(urls[data_type], encoding = "utf8", index_col='name')
    df_eshkol.columns.values[0] = "סמל ישוב"
    return df_eshkol

  elif data_type == "city2019" or data_type == "city2019 raw":
    df_2019_raw = pd.read_csv(urls[data_type], encoding = 'iso-8859-8', index_col='שם ישוב')
    df_2019_raw = df_2019_raw.drop(index = 'מעטפות חיצוניות')
    if raw:
      return df_2019_raw
    df_2019 = df_2019_raw.drop('סמל ועדה', axis=1) # new column added in Sep 2019
    df_2019 = df_2019[df_2019.columns[5:]] # removing "metadata" columns
    df_2019.style.set_properties(**{'text-align': 'right'})
    return df_2019
  
  elif data_type == "ballot2019":
    df_2019_ballots_raw = pd.read_csv(urls[data_type], encoding = 'iso-8859-8', index_col='שם ישוב')
    df_2019_ballots = df_2019_ballots_raw.drop('סמל ועדה', axis=1) # new column added in Sep 2019
    df_2019_ballots = df_2019_ballots.drop(index = 'מעטפות חיצוניות')
    return df_2019_ballots
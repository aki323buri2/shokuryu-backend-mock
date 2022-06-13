# %%
from utilities.common import fullpath, ensure_dir, dotdict, load_csv, save_csv
from dateutil.parser import parse 

def query_urias(kjob, syozok):
  # kjob = "2022-04-30"
  # syozok="170"
  # syozok="910"
  kjob = parse(kjob).date()
  syozok = str(syozok)
  filename = fullpath(f"csv/{kjob}_{syozok}_urias.csv")
  df = load_csv(filename, dtype=str)
  # float: 
  for name in [
    "uirisu_h", 
    "ukosu_h", 
    "usuryo_h", 
    "ujyury_h", 
    "utanka_h", 
    "zkmtan_h", 
    "kkosu", 
    "ksuryo", 
    "kjyury", 
    "knsury", 
    "knjyur", 
    "genkak", 
    "uirisu", 
    "ukosu", 
    "usuryo", 
    "ujyury", 
    "utanka", 
    "zkmtan", 
  ]:
    df[name] = df[name].replace("", 0).astype(float)
  # int: 
  for name in [
    "knrino", 
    "tokuno", 
    "syaten_n", 
    "ukin_h", 
    "zkmkin_h", 
    "kkin", 
    "knrnor", 
    "tokuno_b", 
    "ukin", 
    "zkmkin", 
  ]:
    df[name] = df[name].replace("", 0).astype(float).astype(int) 
  return df



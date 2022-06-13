# %%
from utilities.common import fullpath, ensure_dir, dotdict, load_csv, save_csv
from dateutil.parser import parse 

def query_buka():
  filename = fullpath("csv/buka.csv")
  df = load_csv(filename, dtype=dict(
    syozok=str, 
    hidden=bool, 
    disp_order=int, 
    suffix=str, 
  ))
  return df

# %%




# %%
from utilities.common import fullpath, ensure_dir, dotdict, load_csv, save_csv
from dateutil.parser import parse 

def query_toktan(st, ed, syozok):
  st = parse(st).date()
  ed = parse(ed).date()
  syozok = str(syozok)
  filename = fullpath(f"csv/{st}_{ed}_{syozok}_toktan.csv")
  df = load_csv(filename, dtype=dict(
    syozok=str, 
    tokuno=int,
    ukin=int, 
    genkak=int, 
    arari=int, 
    ritsu=float, 
  ))
  return df



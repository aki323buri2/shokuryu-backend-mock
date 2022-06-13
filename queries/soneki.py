# %%
from utilities.common import fullpath, ensure_dir, dotdict, load_csv, save_csv
from dateutil.parser import parse 

# kjob = "2022-04-30"
# syozok = "170"
# syozok = "910"
def query_soneki(st, ed, syozok):
  kjob = parse(kjob).date()
  syozok = str(syozok)
  filename = fullpath(f"csv/{kjob}_{syozok}_soneki.csv")
  df = load_csv(filename, dtype=dict(
    kjob=str, yyyymm=str, syozok=str, knrino=int, tokuno=int, tnamen=str, tnamek=str,
    ryakun=str, ryakuk=str, shcds=str, shcdt=str, shnm1=str, shnm2=str, utani=str,
    ukosu=float, usuryo=float, ujyury=float, utanka=float, ukin=int, zkmtan=float,
    zkmkin=int, kkosu_h=float, ksuryo_h=float, kjyury_h=float, kkin_h=float, knsury_h=float,
    knjyur_h=float, genkak_h=float, bunrui=str, uriku=str, densyu=str, uriymd=str, denymd=str,
    syoymd=str, butkbn=str, jancd=str, add_ymd=str, edit_ymd=str, knrnor=str, shiren=int,
    hatno=int, ktani=str, kirime=float, kawase=float, kkosu=float, ksuryo=float, kjyury=float,
    ktanka=float, kkin=int, genkak=int, ssku=str, nkuran=str, kntani=str, knsury=float,
    knjyur=float, syoken=str, zaikon=str, sainyu=str, 
  ))
  return df 

# %%




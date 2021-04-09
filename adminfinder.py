import sys,requests,string

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def finder():
    list1 = ["/admin/login.php", "/admin/login.asp", "/admin", "/adm", "/administrator", "/administrador", "/admin_login", "/administrator/login.php", "/cgi-local/", "/sys/admin/"]
    url = input(bcolors.YELLOW + '[*] Enter the page url --> ')
    for i in list1:
        a = url + i 
        resp = requests.get(a)
        if resp.status_code == 200:
            print (bcolors.GREEN + f"[+[+[ WE FOUND THE ADMIN PAGE:{a}")
        else:
            print(bcolors.RED + f"[!] ADMIN PAGE ARE NOT IN {a}")
finder()

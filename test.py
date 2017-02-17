import urllib.request

# Conrad Addo
arg1 = "https://codeproject.global.ssl.fastly.net/App_Themes/CodeProject/Img/logo250x135.gif"
arg2 = "our.gif"
source = urllib.request.urlretrieve(arg1, arg2)
#source = urllib.request.urlopen("http://www.codeproject.com")
#print(*source)

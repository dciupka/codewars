
'''
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
'''

url = "http://www.zombie-bites.com"
print(url.split("//"))
print(url.split("//")[-1])
print(url.split("//")[-1].split("www.")[-1])
print(url.split("//")[-1].split("www.")[-1].split(".")[0])

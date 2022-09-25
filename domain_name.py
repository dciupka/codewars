"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

"""


from urllib.parse import urlparse


def domain_name(url):
    res = urlparse(url)
    res_str = str(res.hostname)
    print(res_str)
    if res_str == "None":
        splited = url.split('.')
        if splited[0]=='www':
            return splited[1]
        else:
            return splited[0]
    else:
        if res_str.startswith('www'):
            return res_str.split('.')[1]
        else:
            return res_str.split('.')[0]


url = "http://github.com/carbonfive/raygun"
print(domain_name(url))
url = "http://www.zombie-bites.com"
print(domain_name(url))

url = "www.xakep.ru"
print(domain_name(url))

url = "https://www.cnet.pl"
print(domain_name(url))

url = "www.xhacker.ss.pl"
print(domain_name(url))

url = "xhacker.ss.pl"
print(domain_name(url))

##other from codewars

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


def domain_name(url):
    url = url.replace('www.', '')
    url = url.replace('https://', '')
    url = url.replace('http://', '')

    return url[0:url.find('.')]


def domain_name(url):
    if ("www" not in url):
        return url.split("//")[1].split(".")[0]
    else:
        return url.split(".")[1]

    def domain_name(url):
        url = url.split('//')[-1]
        url = url.split('/')[0]
        url = url.split('.')[-2]
        return url
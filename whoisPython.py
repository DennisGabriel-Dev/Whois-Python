import whois
import os
os.system('clear')
print('Type the domain name, for example: https:www.yourdomain.com')
domain = input('->')
print(whois.whois(domain))
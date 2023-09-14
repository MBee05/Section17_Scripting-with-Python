import requests

# url ='https://api.pwnedpasswords.com/range/' + 'password123'
# res=requests.get(url)
# print(res)

# output <Response [400]> means not good prob with your Api             200 means its ok but  400 not good



# url ='https://api.pwnedpasswords.com/range/' + 'EF92B'
# #to crypt pwd go to passwordgenerator.net to get the 5 char crypted one then replace 5char the actual pwd with it 'password123'
# res=requests.get(url)
# print(res)

# output    <Response [200]>


'''Hash generator
we give an input(pwd) and it gives a crypted, but each time you give the same pwd, it will give the same output until you change atleast one char of the input
This is what we call 'idempotent' a function that gives the same output until we change one char
There is 2 types of HASH function 
SHA-1 generator and SHA-256 hash generator(this takes long time to generate a HASH)
'''


# check if pwd has been hacked


import hashlib
import sys

def request_api_data(query_char):
    url ='https://api.pwnedpasswords.com/range/' + query_char
    res=requests.get(url)
    # print(res)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching:{res.status_code}, check the api and try again')
    return res


# def read_response(response):
#     print(response.text)
''' output get all the hashes which match the beginning of our hashed PWD
005BA21B62A7D0DA863D9858C6239FB8E3A:1
00684A10635394CC9D4524FC8C41580159E:1
00F6F1EFBEC383A639129970B019A4FB1A9:3 .... numb at the end tells how many times the PWD has been hacked'''

def get_password_leaks_count(hashes, hash_to_check):
    hashes= (line.split(':') for line in hashes.text.splitlines())
    # print(hashes)
# <generator object get_password_leaks_count.<locals>.<genexpr> at 0x00000159CAA4E260>
    for h, count in hashes: 
        # print(h, count)
# FF6A1EC0A713E73C73A0DDAA8438AF1438E 1
# FF803FACF96FC5C8C5DF1308F2413BBC55F 3 .... we get hash and counted separated 
        
        # we want to check if the tail of the our hash has been leaked
        if h == hash_to_check:
            return count
    return 0
        
def pwned_api_check(password):
    # check password if it exists in API response
    # print(password.encode('utf-8'))
    # output    b'123'
    
    
    # print(hashlib.sha1(password.encode('utf-8')))
    # output  obj   <sha1 _hashlib.HASH object @ 0x000002787FA322B0>
    
    # print(hashlib.sha1(password.encode('utf-8')).hexdigest())
    # output    40bd001563085fc35165329ea1ff5c5ecbdbbeef
    
    # print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    # output    40BD001563085FC35165329EA1FF5C5ECBDBBEEF
    
    #  print(hashlib.sha1(password).hexdigest().upper())
    #  output Error
    
    sha1password= hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
# need to send this password to the request_api_data
    
    first5_char, tail= sha1password[:5], sha1password[5:]
    response= request_api_data(first5_char)
    # print(first5_char, tail)
    # 40BD0 01563085FC35165329EA1FF5C5ECBDBBEEF
    # print(response)
    # <Response [200]>
    
    # return read_response(response)
    return get_password_leaks_count(response, tail)


# pwned_api_check('123')


def main(args):
    for password in args:
        count= pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times ... you should probably change your password')
        else:
            print(f'{password} was NOT found')
    return 'done!'
    

if __name__== '__main__':
    # main(sys.argv[1:])
    sys.exit(main(sys.argv[1:]))        #to exit the program
    
    
    
# PS C:\Users\Mohamed Bee\Desktop\Python_w_Udemy\Section17_Scripting with Python\PWD> python checkmypass.py hi   ('hi' is my pwd to check)
# hi was found 24398 times ... you should probably change your password
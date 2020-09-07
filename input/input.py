from pwn import *

hostname = "pwnable.kr"
portnum  = 2222
username = "input2"
passwd   = "guest"

def main():

    args = ["./input"]
    print("./input", end="")
    for x in range(99):
        print(" AA", end="")
        args.append("AA")

    print(args)

'''
    s = ssh(host=hostname,
            port=portnum,
            user=username,
            password=passwd)
    p = s.process(args)

    p.interactive()
'''

if __name__ == "__main__":
    main()

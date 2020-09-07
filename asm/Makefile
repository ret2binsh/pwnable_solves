CC     = nasm
CFLAGS = -f elf64 
LD     = ld
IN     = readflag.asm
OBJ    = readflag.o
OUT    = prog
OBJC   = objcopy
OFLAGS = -O binary
SHELLC = shellcode

default: compile link shellcode

compile:
	$(CC) $(CFLAGS) $(IN) -o $(OBJ)

link:
	$(LD) -o $(OUT) $(OBJ)
	rm -f $(OBJ)

shellcode:
	$(OBJC) $(OFLAGS) $(OUT) $(SHELLC)

clean:
	rm -f $(OUT) $(SHELLC)

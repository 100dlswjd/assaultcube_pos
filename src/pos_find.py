import time
import struct

from class_gather.process_class import ProcessMemoryControl

ac_clinet_process = ProcessMemoryControl("ac_client")

# x -> 0x17e090, y -> 0x17e094, z -> 0x17e098
def find_pos(process : ProcessMemoryControl, add_addr):
    target_addr = process.base_addr + add_addr
    pos = process.read(target_addr, 4)
    pos = struct.unpack('f', pos)[0]
    return pos

while True:
    x_pos = find_pos(ac_clinet_process, 0x17e090)
    y_pos = find_pos(ac_clinet_process, 0x17e094)
    z_pos = find_pos(ac_clinet_process, 0x17e098)

    print(f"x : {x_pos}\ny : {y_pos}\nz : {z_pos}")
    time.sleep(0.5)
#!/usr/bin/python
import sys
import time
import struct
from pymodbus.client import ModbusSerialClient

serial_port = str(sys.argv[1])
unit_id_1 = int(sys.argv[2])
unit_id_2 = int(sys.argv[3])

client = ModbusSerialClient(method="rtu", port=serial_port, baudrate=9600, stopbits=1, bytesize=8, timeout=1)

resp = client.read_input_registers(0x00, 2, slave=unit_id_1)
print(struct.unpack('>f', struct.pack('>HH', *resp.registers)))
resp = client.read_input_registers(0x06, 2, slave=unit_id_1)
print(struct.unpack('>f', struct.pack('>HH', *resp.registers)))
resp = client.read_input_registers(0x0C, 2, slave=unit_id_1)
print(struct.unpack('>f', struct.pack('>HH', *resp.registers)))
resp = client.read_input_registers(0x1E, 2, slave=unit_id_1)
print(struct.unpack('>f', struct.pack('>HH', *resp.registers)))
resp = client.read_input_registers(0x0156, 2, slave=unit_id_1)
print(struct.unpack('>f', struct.pack('>HH', *resp.registers)))
time.sleep(0.3)
resp = client.read_input_registers(0x00, 2, slave=unit_id_2)
print(struct.unpack('>f', struct.pack('>HH', *resp.registers)))
resp = client.read_input_registers(0x06, 2, slave=unit_id_2)
print(struct.unpack('>f', struct.pack('>HH', *resp.registers)))
resp = client.read_input_registers(0x0C, 2, slave=unit_id_2)
print(struct.unpack('>f', struct.pack('>HH', *resp.registers)))
resp = client.read_input_registers(0x1E, 2, slave=unit_id_2)
print(struct.unpack('>f', struct.pack('>HH', *resp.registers)))
resp = client.read_input_registers(0x0156, 2, slave=unit_id_2)
print(struct.unpack('>f', struct.pack('>HH', *resp.registers)))

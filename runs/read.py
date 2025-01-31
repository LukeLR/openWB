#!/usr/bin/python
from pymodbus.client import ModbusSerialClient

client = ModbusSerialClient(method="rtu", port="/dev/virtualcom1", baudrate=9600, stopbits=1, bytesize=8, timeout=1)
rq = client.read_holding_registers(1000, 7, slave=1)
print(rq.registers)

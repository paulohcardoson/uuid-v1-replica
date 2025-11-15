import datetime
import random

def generate_uuid():
  mac_addr = "00e01e756166"

  uuid_epoch = datetime.datetime(1582, 10, 15, tzinfo=datetime.timezone.utc)
  now = datetime.datetime.now(tz=datetime.timezone.utc)

  timestamp = int((now - uuid_epoch).total_seconds() * 10 ** 7)

  time_low = bitsToHex(bin(timestamp)[-32:])
  time_mid = bitsToHex(bin(timestamp)[-48:-32])
  time_hi = bitsToHex(bin(timestamp)[-60:-48])

  time_hi_and_version = removePrefix(hex(int(time_hi, 16) | 0x1000))
  
  random_hex = f"{random.getrandbits(4 * 4):04x}"

  return f"{time_low}-{time_mid}-{time_hi_and_version}-{random_hex}-{mac_addr}"

def removePrefix(bitsOrHex):
  result = bitsOrHex[2:]

  return result
  
def bitsToHex(bits, prefix=False):
  result = hex(int(bits, 2))

  if not prefix:
    result = removePrefix(result)
  
  return result

def hexToBits(hex_string, prefix=False):
  result = bin(int(hex_string, 16))

  if not prefix:
    result = removePrefix(result)

  return result

for i in range(20):
  print(generate_uuid())
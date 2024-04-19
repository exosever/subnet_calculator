#Subnet calculator by Joshua Harrison
print("Subnet Calculator by Joshua Harrison")
hosts=input('Please input number of hosts required:')

hosts = int(hosts)

#Changes - changed subsequent IF statements for ELIF statements

#Seperate statements for each CIDR. Manually entered ranges for available hosts to the appropriate subnet mask with regards to total hosts-(network id+broadcast address).
if hosts == 2:
  subnet="255.255.255.252"
  print("Your subnet mask is " + subnet)

elif hosts >= 2 and hosts <= 7:
  subnet="255.255.255.248"
  print("Your subnet mask is " + subnet)

elif hosts >= 8 and hosts <= 17:
  subnet="255.255.255.240"
  print("Your subnet mask is " + subnet)

elif hosts >= 18 and hosts <= 31:
  subnet="255.255.255.224"
  print("Your subnet mask is " + subnet)

elif hosts >= 32 and hosts <= 63:
  subnet="255.255.255.192"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 64 and hosts <= 127:
  subnet="255.255.255.128"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 128 and hosts <= 255:
  subnet="255.255.255.0"
  print("Your subnet mask is " + subnet)

elif hosts >= 256 and hosts <= 511:
  subnet="255.255.254.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 512 and hosts <= 1023:
  subnet="255.255.252.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 1024 and hosts <= 2047:
  subnet="255.255.248.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 2047 and hosts <= 4095:
  subnet="255.255.240.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 4096 and hosts <= 8191:
  subnet="255.255.224.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 8192 and hosts <= 16383:
  subnet="255.255.192.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 16384 and hosts <= 32767:
  subnet="255.255.128.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 32768 and hosts <= 65535:
  subnet="255.255.0.0"
  print("Your subnet mask is " + subnet)

elif hosts >= 65536 and hosts <= 131071:
  subnet="255.254.0.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 131072 and hosts <= 262143:
  subnet="255.252.0.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 262144 and hosts <= 524287:
  subnet="255.248.0.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 524288 and hosts <= 1048575:
  subnet="255.240.0.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 1048576 and hosts <= 2097151:
  subnet="255.224.0.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 2097152 and hosts <= 4194303:
  subnet="255.192.0.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 4194304 and hosts <= 8388607:
  subnet="255.128.0.0"
  print("Your subnet mask is " + subnet)
  
elif hosts >= 8388608 and hosts <= 16777215:
  subnet="255.0.0.0"
  print("Your subnet mask is " + subnet)

  

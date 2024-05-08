#Subnet calculator by Joshua Harrison aka Severx
print("-----------------------------------------------")
print("Subnet Calculator by Joshua Harrison aka SeverX")
print("-----------------------------------------------")
print()

while True:
  while True:
    hosts=input('Please input number of hosts required: ')
    print()
    if hosts.isnumeric():
      break
    else:
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("Please enter a number, you entered '"f"{hosts}""'")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print()
  hosts = int(hosts)
  print(" ___________________________________")

  #Seperate statements for each CIDR. Manually entered ranges for available hosts to the appropriate subnet mask with regards to total hosts-(network id+broadcast address)
  if hosts == 0:
    print("If you have 0 hosts, you do not require a subnet.")

  elif hosts <= 2:
    subnet="255.255.255.252"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 7:
    subnet="255.255.255.248"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 17:
    subnet="255.255.255.240"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 31:
    subnet="255.255.255.224"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 63:
    subnet="255.255.255.192"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 127:
    subnet="255.255.255.128"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 255:
    subnet="255.255.255."f"{'0':3}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 511:
    subnet="255.255.254."f"{'0':3}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 1023:
    subnet="255.255.252."f"{'0':3}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 2047:
    subnet="255.255.248."f"{'0':3}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 4095:
    subnet="255.255.240."f"{'0':3}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 8191:
    subnet="255.255.224."f"{'0':3}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 16383:
    subnet="255.255.192."f"{'0':3}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 32767:
    subnet="255.255.128."f"{'0':3}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 65535:
    subnet="255.255."f"{'0'}."f"{'0':5}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 131071:
    subnet="255.254."f"{'0'}."f"{'0':5}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 262143:
    subnet="255.252."f"{'0'}."f"{'0':5}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 524287:
    subnet="255.248."f"{'0'}."f"{'0':5}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 1048575:
    subnet="255.240."f"{'0'}."f"{'0':5}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 2097151:
    subnet="255.224."f"{'0'}."f"{'0':5}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 4194303:
    subnet="255.192."f"{'0'}."f"{'0':5}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 8388607:
    subnet="255.128."f"{'0'}."f"{'0':5}"
    print("|Your subnet mask is " + subnet + "|")

  elif hosts <= 16777215:
    subnet="255."f"{'0':0}."f"{'0':0}."f"{'0':9}"
    print("|Your subnet mask is " + subnet + "|")

  else:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Invalid number submitted '"f"{hosts}""' \nPlease check and try again.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

  print()

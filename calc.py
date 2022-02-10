import math

mainui = "[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division\n[5] Square root"


x = int(input("First number: "))
y = int(input("Second number: "))

print(f"\n{mainui}\n")

cchoice = int(input("Choice: "))
print("")

if cchoice == 1:
  sum = x + y
  cnum = "{:,}".format(sum)
  print(f"Sum {x} + {y}: {cnum}")
elif cchoice == 2:
  sum = x - y
  cnum = "{:,}".format(sum)
  print(f"Sum of {x} - {y}: {cnum}")
elif cchoice == 3:
  sum = x * y
  cnum = "{:,}".format(sum)
  print(f"Sum of {x} * {y}: {cnum}")
elif cchoice == 4:
  sum = x / y
  cnum = "{:,}".format(sum)
  print(f"Sum of {x} / {y}: {cnum}")
elif cchoice == 5:
  sumx = math.sqrt(x)
  sumy = math.sqrt(y)
  suma = sumx + sumy
  cnum = "{:,}".format(suma)
  print(f"{x} square rooted: {sumx}")
  print(f"{y} square rooted: {sumy}")
  print(f"{sumx} + {sumy}: {suma}")

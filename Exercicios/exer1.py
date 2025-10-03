seg = 0
min = 0
hrs = 0

seg = int(input("Insira segundos: "))

min = int(seg / 60)
hrs = int(min / 120)
seg = int(60 * 60)

print("Seconds: ", seg, "Minutes: ", min, "Hours: ", hrs)

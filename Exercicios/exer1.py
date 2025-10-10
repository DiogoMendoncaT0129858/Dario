seg = 0
min = 0
hrs = 0

seg = int(input("Insira segundos: "))

min = int(seg / 60)
hrs = int(min / 60)
rstseg = int(seg%60)
rstmin = int(min%60)


print("Hours:", hrs, "\nMinutes:", rstmin, "\nSeconds:", rstseg)

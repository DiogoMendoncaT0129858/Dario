seg = int(input("Digite os segundos: "))

hrs = seg // 3600
min = (seg % 3600) // 60
segRest = seg % 60

print(hrs, " hora(s), ", min," minuto(s) e ",segRest," segundo(s)")
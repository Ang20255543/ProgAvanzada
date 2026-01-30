temp = int(input("Temperatura: "))

if temp >= 30:
    print("Playera sin mangas y short")
elif temp > 15:
    print("Playera y jeans")
elif temp < 0:
    print("Gabardinas y calentadores")
else:
    print("Suéter y pantalón")
def wykres_ascii(values):
    max_v = max(values)
    for v in values:
        dl = int((v / max_v) * 40)
        print("|" + "#" * dl)

if __name__ == "__main__":
    dane = [3, 7, 2, 9, 5]
    wykres_ascii(dane)

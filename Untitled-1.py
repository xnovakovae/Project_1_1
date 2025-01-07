# Vstupní hodnoty uživatele
vyska = 2
vaha = 80
jmeno = 'Martin'

# Výpočet BMI
bmi = vaha / vyska ** 2

# Vytvoř proměnnou "kategorie", kam uložíš slovní ohodnocení BMI
if bmi > 40:
    kategorie = 'těžká obezita'
elif bmi > 30:
    kategorie = 'obezita'
elif bmi > 25:
    kategorie = 'mírná nadváha'
elif bmi > 18.5:
    kategorie = 'zdravá váha'
else:
    kategorie = 'podvýživa'

# Vytiskni odpoved s vysledkem
print(jmeno, "tvé BMI je", bmi, ", což spadá do kategorie", kategorie, ".")
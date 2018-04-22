#DIALOG

pl_lang = "Wybrano język polski."
en_lang = "You've picked English."

pl_uni_metric = "Wybrano system metryczny."
pl_uni_imperial = "Wybrano system imperialny."

en_uni_metric = "You've picked metric system."
en_uni_imperial = "You've picked imperial system."

pl_again = "Spróbuj ponownie!"
en_again = "Try again!"
again = "Try again! / Spróbuj ponownie!"

lg_input = "English[EN]/ Polski[PL]: "
pl_uni_input = "Metryczny[M]/ Imperialny[I]/: "
en_uni_input = "Metric[M]/ Imperial[I]: "

pl_wm = "Waga[kg]: "
pl_hm = "Wzrost[cm]: "
pl_wi = "Waga[lb]: "
pl_hi = "Wzrost[ft]: "

en_wm = "Weight[kg]: "
en_hm = "Height[cm]: "
en_wi = "Weight[lb]: "
en_hi = "Height[ft]: "

pl_bmi_print_dialog = "Twój wskaźnik masy ciała wynosi: "
en_bmi_print_dialog = "Your body mass index is: "

pl_list = """
<15 Wygłodzenie
15-16 Wychudzenie
16-18.5 Niedowaga
18.5-25 Wartość prawidłowa
25-30 Nadwaga
30-35 I stopień otyłości
35-40 II stopień otyłości (otyłość kliniczna)
>40 III stopień otyłości (otyłość skrajna)"""

pl_1 = "Wygłodzenie"
pl_2 = "Wychudzenie"
pl_3 = "Niedowaga"
pl_4 = "Wartość prawidłowa"
pl_5 = "Nadwaga"
pl_6 = "I stopień otyłości"
pl_7 = "II stopień otyłości (otyłość kliniczna)"
pl_8 = "III stopień otyłości (otyłość skrajna)"

en_list = """
<15 Very severely underweight
15-16 Severely underweight
16-18.5 Underweight
18.5-25 Normal (healthy weight)
25-30 Overweight
30-35 Obese Class I (Moderately obese)
35-40 Obese Class II (Severely obese)
>40 Obese Class III (Very severely obese)"""

en_1 = "Very severely underweight"
en_2 = "Severely underweight"
en_3 = "Underweight"
en_4 = "Normal (healthy weight)"
en_5 = "Overweight"
en_6 = "Obese Class I (Moderately obese)"
en_7 = "Obese Class II (Severely obese)"
en_8 = "Obese Class III (Very severely obese)"

sum_pl = "Twój wynik to: "
sum_en = "You're: "

#VARIABLES

lg = "lg"
uni = "uni"

#DEF

def lang():
    global lg
    lg = input(lg_input)
    lg = lg.lower()
    if lg == "pol" or lg == "polski":
        lg = "pl"
    elif lg == "eng" or lg == "english":
        lg = "en"
    if lg == "pl":
        print(pl_lang)
    elif lg == "en":
        print(en_lang)
    else:
        print(again)
        lang()

def pl_units():
    global uni
    uni = input(pl_uni_input)
    uni = uni.lower()
    if uni == "metryczny":
        uni = "m"
    elif uni == "imperialny":
        uni = "i"
    if uni == "m":
        print(pl_uni_metric)
    elif uni == "i":
        print(pl_uni_imperial)
    else:
        print(pl_again)
        pl_units()

def en_units():
    global uni
    uni = input(en_uni_input)
    uni = uni.lower()
    if uni == "metric":
        uni = "m"
    elif uni == "imperial":
        uni = "i"
    if uni == "m":
        print(en_uni_metric)
    elif uni == "i":
        print(en_uni_imperial)
    else:
        print(en_again)
        en_units()

def pl_data_m():
    global w
    global h
    w = input(pl_wm)
    h = input(pl_hm)
    if not w.isnumeric() or not h.isnumeric():
        print(pl_again)
        pl_data_m()

def pl_data_i():
    global w
    global h
    w = input(pl_wi)
    h = input(pl_hi)
    if not w.isnumeric() or not h.isnumeric():
        print(pl_again)
        pl_data_i()

def en_data_m():
    global w
    global h
    w = input(en_wm)
    h = input(en_hm)
    if not w.isnumeric() or not h.isnumeric():
        print(en_again)
        en_data_m()

def en_data_i():
    global w
    global h
    w = input(en_wi)
    h = input(en_hi)
    if not w.isnumeric() or not h.isnumeric():
        print(en_again)
        en_data_i()

def m_bmi(w, h):
    global bmi
    bmi = (float(w) / ((float(h)) / 100) ** 2)

def i_bmi(w, h):
    global bmi
    bmi = (float(w) / float(h) ** 2) * 703

def pl_0():
    if bmi >= 40.:
        return pl_8
    elif bmi >= 35.:
        return pl_7
    elif bmi >= 30.:
        return pl_6
    elif bmi >= 25.:
        return pl_5
    elif bmi >= 18.5:
        return pl_4
    elif bmi >= 16.:
        return pl_3
    elif bmi >= 15.:
        return pl_2
    elif bmi <= 15.:
        return pl_1
    else:
        return "Error"

def en_0():
    if bmi >= 40.:
        return en_8
    elif bmi >= 35.:
        return en_7
    elif bmi >= 30.:
        return en_6
    elif bmi >= 25.:
        return en_5
    elif bmi >= 18.5:
        return en_4
    elif bmi >= 16.:
        return en_3
    elif bmi >= 15.:
        return en_2
    elif bmi <= 15.:
        return en_1
    else:
        return "Error"

def summary_pl():
    print("%s %s" % (sum_pl, pl_0()))

def summary_en():
    print("%s %s" % (sum_en, en_0()))

def print_bmi_pl():
    print(pl_bmi_print_dialog + "%.2f" % (bmi))
    (summary_pl())

def print_bmi_en():
    print(en_bmi_print_dialog + "%.2f" % (bmi))
    (summary_en())

#CODE

print("""PyBMICalc - 2018
""")

lang()

print()

if lg == "pl":
    pl_units()
elif lg == "en":
    en_units()

print()

if lg == "pl":
    if uni == "m":
        pl_data_m()
    elif uni == "i":
        pl_data_i()
elif lg == "en":
    if uni == "m":
        en_data_m()
    elif uni == "i":
        en_data_i()

print()

if uni == "m":
    m_bmi(w, h)
elif uni == "i":
    i_bmi(w, h)

if lg == "pl":
    print_bmi_pl()
    print(pl_list)
elif lg == "en":
    print_bmi_en()
    print(en_list)

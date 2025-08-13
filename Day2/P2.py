'''l=["ICSE","CBSE","HSE"]
dic={"I":"INDIAN","C1":"CERTIFICATE","C2":"CENTRAL","S":"SECONDARY","E":"EDUCATION"}

for i in l:
    for j in i:
        print(j,end=" - ")

        print(dic[j])
        print()
    print("============")'''


abbreviations = {
    "ICSE": ["INDIAN", "CERTIFICATE", "SECONDARY", "EDUCATION"],
    "CBSE": ["CENTRAL", "BOARD", "SECONDARY", "EDUCATION"],
    "HSE":  ["HIGHER", "SECONDARY", "EDUCATION"]
}

for i, j in abbreviations.items():
    for l, f in zip(i, j):
        print(f"{l} - {f}")
        print()
    print("============")

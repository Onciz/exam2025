uchazeci = [
    {'jmeno':'Jan Cizek','matematika':70,'cestina':60,'anglictina':75},
    {'jmeno':'Ondrej Cizek','matematika':98,'cestina':80,'anglictina':100},
    {'jmeno':'Martin Miko','matematika':70,'cestina':71,'anglictina':80}
]

def vyber_prijate(lidi):
    prijati = []
    a = 1
    for i in lidi:
        if a <= 15:
            znamky = [i['matematika'], i['cestina'], i['anglictina']]
            soucet = i['matematika'] + i['cestina'] + i['anglictina']
            nice_znamky = [a for a in znamky if a >= 60]
            print(nice_znamky)
            print(i['matematika'])
            if len(nice_znamky) == 3:
                prijati.append([i, soucet])
            a+=1
    return prijati

def quicksort(seznam):
    if len(seznam) <= 1:
        return seznam
    else:
        a = seznam[0]
        l = []
        p = []
        s = []
        for i in seznam:
            if i[1] > a[1]:
                l.append(i)
            elif i[1] == a[1]:
                a_math = a[0]['matematika']
                i_math = i[0]['matematika']
                if i_math > a_math:
                    l.append(i)
                elif i_math == a_math:
                    s.append(i)
                else:
                    p.append(i)
            else:
                p.append(i)
    return quicksort(l) + s + quicksort(p)

accepted = vyber_prijate(uchazeci)
accepted = quicksort(accepted)
for i in accepted:
    score = i[1]
    me = i[0]
    poradi = accepted.index(i) + 1
    print(f'{poradi}. {i[0]['jmeno']} - {i[0]['matematika']} (M), {i[0]['cestina']} (ČJ), {i[0]['anglictina']} (AJ) - Celkem: {score}')

# funkcija za izracun deleza mladih med prebivalci

def delez(mladi, prebivalci):
    print mladi / float(prebivalci)
    vmesna_vrednost = mladi / float(prebivalci)
    return vmesna_vrednost

def procent_delez(trenutni_delez):
    return str(int(round(trenutni_delez * float(100), 0))) + "%"

def obtener_serie(l: str) -> list:
    serie: list = l.split(",")
    serie[1] = int(serie[1])
    serie[2] = int(serie[2])
    serie[3] = serie[3].strip()
    return serie


def leer() -> list:
    f = open("series.txt")
    lista: list = []
    for l in f:
        serie = obtener_serie(l)
        lista.append(serie)

    f.close()
    return lista


def añadir_duración(series: list) -> None:
    for serie in series:
        duración = serie[1] * serie[2]
        serie.append(duración)


def serie_más_larga(series: list) -> list:
    mas_larga: list = series[0]
    for serie in series:
        if serie[4] > mas_larga[4]:
            mas_larga = serie
    return mas_larga


s: list = leer()
añadir_duración(s)
print(serie_más_larga(s))

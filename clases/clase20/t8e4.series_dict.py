def obtener_serie(l: str) -> dict:
    serie: list = l.split(",")
    serie_dict: dict = {
        "serie": serie[0].strip(),
        "episodios": int(serie[1]),
        "duración": int(serie[2]),
        "plataforma": serie[3].strip()
    }
    return serie_dict


def leer() -> list:
    f = open("series.txt")
    lista: list = []
    for l in f:
        serie: dict = obtener_serie(l)
        lista.append(serie)

    f.close()
    return lista


def añadir_duración(series: list) -> None:
    for serie in series:
        duración: int = serie["episodios"] * serie["duración"]
        serie["duración_total"] = duración


def serie_más_larga(series: list) -> dict:
    mas_larga: dict = series[0]
    for serie in series:
        if serie["duración_total"] > mas_larga["duración_total"]:
            mas_larga = serie
    return mas_larga


s: list = leer()
añadir_duración(s)
print(serie_más_larga(s))


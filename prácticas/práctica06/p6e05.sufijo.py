def hay_solapamiento(a: str, b: str, n: int) -> bool:
    solapan: bool = False
    if len(a) >= n and len(b) >= n:
        if a[-n:] == b[:n]:
            solapan = True
    return solapan


def max_solapamiento(a: str, b: str) -> int:
    max_solapan: int = 0
    for tam in range(len(b)):
        if hay_solapamiento(a, b, tam):
            max_solapan = tam
    return max_solapan


a = "AAACGTT"
b = "CACGTTAC"
print(max_solapamiento(a,b))
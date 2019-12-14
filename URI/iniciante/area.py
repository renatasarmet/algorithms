# https://www.urionlinejudge.com.br/judge/pt/problems/view/1012

#RUNTIMEERROR: they are using an old version of python

A, B, C = map(float, input().split(" "))

triangulo = (A * C)/ 2
circulo = 3.14159 * (C ** 2)
trapezio = ((A + B) * C)/ 2
quadrado = B ** 2
retangulo = A * B

# print(f"TRIANGULO: {triangulo:0.3f}")
# print(f"CIRCULO: {circulo:0.3f}")
# print(f"TRAPEZIO: {trapezio:0.3f}")
# print(f"QUADRADO: {quadrado:0.3f}")
# print(f"RETANGULO: {retangulo:0.3f}")

print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))

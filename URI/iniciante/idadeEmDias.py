# https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

dias = int(input())

meses = dias % 365
anos = (dias - meses) / 365

dias = meses % 30
meses = (meses - dias) / 30

print(str(int(anos)) + " ano(s)")
print(str(int(meses)) + " mes(es)")
print(str(int(dias)) + " dia(s)")
"""14- Se buscan dos nümeros de tres cifras que cumplen con la siguiente condiciån:
ABC * 2 = CAB — 151. Encontrar esos nümeros sabiendo que A, B y C representan sus
cifras."""


A,B,C = 0,0,0
condicion1 = (A*100 + B*10 + C) * 2
condicion2 = (C*100 + A*10 + B) - 151

for i in range(10):
    for j in range(10):
        for k in range(10):
            condicion1 = (i*100 + j*10 + k) * 2
            condicion2 = (k*100 + i*10 + j) - 151
            if (condicion1 == condicion2):
                print(f"Los numeros son {(i*100 + j*10 + k)} y {(k*100 + i*10 + j)}")
                break
x_pontos = [10, 20, 30, 40]
y_pontos = [45.0, 52.0, 60.0, 71.0]
h = 10
x_alvo = 25


def gregory_newton(x_pts, y_pts, h_passo, x):
    n = len(y_pts)

    delta = []
    delta.append([y_pts[i] for i in range(n)]) 

    for ordem in range(1, n):
        linha_anterior = delta[ordem - 1]
        nova_linha = []
        for i in range(n - ordem):
            nova_linha.append(linha_anterior[i + 1] - linha_anterior[i])
        delta.append(nova_linha)

    print("\n  Tabela de diferenças finitas:")
    print(f"  {'i':>3}  {'x':>6}  {'y':>8}", end="")
    for k in range(1, n):
        print(f"  {'Δ'*k+'y':>8}", end="")
    print()
    for i in range(n):
        print(f"  {i:>3}  {x_pts[i]:>6}  {delta[0][i]:>8.4f}", end="")
        for k in range(1, n - i):
            print(f"  {delta[k][i]:>8.4f}", end="")
        print()

    p = (x - x_pts[0]) / h_passo

    resultado = delta[0][0]
    p_acum = 1.0
    fatorial = 1.0

    for k in range(1, n):
        p_acum *= (p - (k - 1))
        fatorial *= k
        resultado += (p_acum / fatorial) * delta[k][0]

    return resultado


# execução

print("=" * 55)
print("  INTERPOLAÇÃO — GREGORY-NEWTON")
print("=" * 55)
print(f"  Dados: x={x_pontos}")
print(f"         y={y_pontos}")
print(f"  h={h}, interpolar em x={x_alvo}")
print("-" * 55)

res = gregory_newton(x_pontos, y_pontos, h, x_alvo)

print("-" * 55)
print(f"  p = ({x_alvo} - {x_pontos[0]}) / {h} = {(x_alvo - x_pontos[0]) / h}")
print(f"  Temperatura estimada em x={x_alvo}: {res:.6f} °C")
print("=" * 55)

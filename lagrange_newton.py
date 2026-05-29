x_pontos = [1.0, 2.0, 3.0, 4.0, 5.0]
y_pontos = [1.2, 1.9, 3.2, 5.5, 8.2]
x_alvo = 3.5

def lagrange(x_pts, y_pts, x):
    n = len(x_pts)
    resultado = 0.0

    for i in range(n):

        li = 1.0
        for j in range(n):
            if j != i:
                li *= (x - x_pts[j]) / (x_pts[i] - x_pts[j])
        resultado += y_pts[i] * li

    return resultado

def newton(x_pts, y_pts, x):
    n = len(x_pts)
    tabela = [y_pts[i] for i in range(n)]
    coef = [tabela[0]]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            tabela[i] = (tabela[i] - tabela[i - 1]) / (x_pts[i] - x_pts[i - j])
        coef.append(tabela[j])

    resultado = coef[n - 1]
    for i in range(n - 2, -1, -1):
        resultado = resultado * (x - x_pts[i]) + coef[i]

    return resultado

# execução

res_lagrange = lagrange(x_pontos, y_pontos, x_alvo)
res_newton   = newton(x_pontos, y_pontos, x_alvo)

print("=" * 50)
print("  INTERPOLAÇÃO — LAGRANGE E NEWTON")
print("=" * 50)
print(f"  Dados: t={x_pontos}")
print(f"         y={y_pontos}")
print(f"  Interpolar em x = {x_alvo}")
print("-" * 50)
print(f"  Lagrange : y({x_alvo}) = {res_lagrange:.6f} m")
print(f"  Newton   : y({x_alvo}) = {res_newton:.6f} m")
print("=" * 50)

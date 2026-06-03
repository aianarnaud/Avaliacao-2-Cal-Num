
t_pontos = [0.0, 1.0, 2.0, 3.0]
y_pontos = [2.5, 4.5, 3.0, 6.0]
t_alvo = 1.5


def spline_linear(t_pts, y_pts, t):
    n = len(t_pts)
    for i in range(n - 1):
        if t_pts[i] <= t <= t_pts[i + 1]:
            h = t_pts[i + 1] - t_pts[i]
            return y_pts[i] + (y_pts[i + 1] - y_pts[i]) / h * (t - t_pts[i])
    return None



def resolver_tridiagonal(a, b, c, d):

    n = len(b)

    b_ = [b[i] for i in range(n)]
    d_ = [d[i] for i in range(n)]
    c_ = [c[i] for i in range(n)]


    for i in range(1, n):
        m = a[i] / b_[i - 1]
        b_[i] -= m * c_[i - 1]
        d_[i] -= m * d_[i - 1]

    x = [0.0] * n
    x[n - 1] = d_[n - 1] / b_[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (d_[i] - c_[i] * x[i + 1]) / b_[i]

    return x


def spline_cubica_natural(t_pts, y_pts, t):
    n = len(t_pts)
    k = n - 1  

    h = [t_pts[i + 1] - t_pts[i] for i in range(k)]

    
    m = k - 1

    diag_a = []  
    diag_b = []  
    diag_c = []  
    rhs    = []  

    for i in range(1, k):
        diag_b.append(2 * (h[i - 1] + h[i]))
        rhs.append(
            6 * ((y_pts[i + 1] - y_pts[i]) / h[i]
               - (y_pts[i] - y_pts[i - 1]) / h[i - 1])
        )

    for i in range(m - 1):
        idx = i + 1 
        diag_c.append(h[idx])
        diag_a.append(h[idx])

    
    M_internos = resolver_tridiagonal(
        [0.0] + diag_a, 
        diag_b,
        diag_c + [0.0], 
        rhs
    )


    M = [0.0] + M_internos + [0.0]


    print(f"\n  Momentos M: {[round(m_, 6) for m_ in M]}")

    for i in range(k):
        if t_pts[i] <= t <= t_pts[i + 1]:
            hi = h[i]
            ti = t_pts[i]
            ti1 = t_pts[i + 1]
            yi = y_pts[i]
            yi1 = y_pts[i + 1]
            Mi = M[i]
            Mi1 = M[i + 1]

            resultado = (
                (Mi  * (ti1 - t)**3) / (6 * hi)
              + (Mi1 * (t  - ti)**3) / (6 * hi)
              + (yi  - Mi  * hi**2 / 6) * (ti1 - t) / hi
              + (yi1 - Mi1 * hi**2 / 6) * (t  - ti) / hi
            )
            return resultado, i

    return None, None

# execução

print("=" * 55)
print("  INTERPOLAÇÃO — SPLINE LINEAR E CÚBICA NATURAL")
print("=" * 55)
print(f"  Dados: t={t_pontos}")
print(f"         y={y_pontos}")
print(f"  Interpolar em t={t_alvo}")
print("-" * 55)

res_linear = spline_linear(t_pontos, y_pontos, t_alvo)

res_cubica, intervalo = spline_cubica_natural(t_pontos, y_pontos, t_alvo)

print("-" * 55)
print(f"  Spline Linear  : y({t_alvo}) = {res_linear:.6f} cm")
print(f"  Spline Cúbica  : y({t_alvo}) = {res_cubica:.6f} cm  (intervalo {intervalo})")
print("=" * 55)
import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Sección 'G1 — Degradación'
st.title("G1 — Cinética de primer orden en tratamiento térmico")

# Símbolos
C0, C, k, t, C_lim = sp.symbols('C0 C k t C_lim', positive=True, real=True)
Ea, R, T = sp.symbols('Ea R T', positive=True, real=True)

# Expresión de vida útil
C_t = C0 * sp.exp(-k * t)

# Despeje para t dado C(t) = C_lim
t_sol = sp.solve(sp.Eq(C_t, C_lim), t)[0]

# Expresión de k(T) por Arrhenius
k_T = sp.exp(-Ea / (R * T))

# Sliders para parámetros
st.sidebar.header("Parámetros cinéticos")
C0_val = st.sidebar.number_input("Concentración inicial (C0)", min_value=0.1, value=1.0)
C_lim_val = st.sidebar.number_input("Concentración límite (C_lim)", min_value=0.01, value=0.1)
Ea_val = st.sidebar.slider("Energía de activación (Ea, J/mol)", min_value=20000, max_value=120000, value=60000)
R_val = st.sidebar.slider("Constante de gas (R, J/mol·K)", min_value=8.0, max_value=9.0, value=8.314, step=0.001)
T_val = st.sidebar.slider("Temperatura (T, K)", min_value=273, max_value=373, value=333)

# Cálculo de k(T)
k_num = float(sp.N(k_T.subs({Ea: Ea_val, R: R_val, T: T_val})))

# Cálculo de t para C(t) = C_lim
t_num = float(sp.N(t_sol.subs({C0: C0_val, C_lim: C_lim_val, k: k_num})))

st.write("### Derivaciones simbólicas")
st.latex(r"C(t) = C_0 e^{-kt}")
st.latex(r"t = -\frac{1}{k} \ln\left(\frac{C_{lim}}{C_0}\right)")
st.latex(r"k(T) = e^{-E_a/(R T)}")

st.write(f"**Vida útil (t) para C(t) = C_lim:** {t_num:.2f} horas")

# Gráfica de C(t)
t_vals = np.linspace(0, t_num * 1.5, 100)
C_vals = C0_val * np.exp(-k_num * t_vals)

fig, ax = plt.subplots()
ax.plot(t_vals, C_vals, label="C(t)")
ax.axhline(C_lim_val, color='r', linestyle='--', label="C_lim")
ax.set_xlabel("Tiempo (h)")
ax.set_ylabel("Concentración")
ax.set_title("Cinética de degradación de primer orden")
ax.legend()
st.pyplot(fig)

st.write("#### Análisis de sensibilidad")
st.write("Modifica los parámetros en la barra lateral para observar el efecto sobre la vida útil y la cinética de degradación.")

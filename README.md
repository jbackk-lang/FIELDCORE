## ANALIZA — Toruso‑Möbius jako Model Globalnej Struktury Pola

FIELDCORE opisuje pole jako strukturę skrętu, rezonansu i przejść Λ–τ–ρ–J, działającą na wszystkich skalach — od lokalnych rezonansów po globalną organizację kosmosu. Toruso‑Möbius jest geometryczną reprezentacją tej struktury.

### 1. Konstrukcja Toruso‑Möbiusa

Parametry:
- u ∈ [0, 2π] — kierunek globalny (zamknięcie torusa)
- v ∈ [-1, 1] — szerokość paska (lokalna zmienność)
- R > 1 — odsunięcie od centrum (gradient pola)
- a > 0 — szerokość skrętu
- skręt lewostronny — sin(u/2), cos(u/2)

Powierzchnia:

x(u,v) = (R + a v cos(u/2)) cos u  
y(u,v) = (R + a v cos(u/2)) sin u  
z(u,v) =  a v sin(u/2)

Interpretacja:
- torus = stabilność Λ (globalna spójność pola)
- skręt Möbiusa = asymetria τ (strzałka ewolucji)
- odsunięcie od centrum = gradient ρ (miejsca pęknięcia struktury)
- skręt o 180° = punkt przejścia J (zmiana reżimu)

### 2. Interpretacja Kosmologiczna

FIELDCORE zakłada, że ta sama struktura działa na wszystkich skalach (zasada samopodobieństwa). Toruso‑Möbius pełni rolę symbolicznego modelu Wszechświata:

- Λ — globalna spójność (zamknięcie torusa)
- τ — kierunek ewolucji (skręt Möbiusa)
- ρ — gradient niestabilności (odsunięcie od centrum)
- J — punkt skrętu (lokalny rezonans)

### 3. Klasyfikacja Galaktyk według fazy skrętu

| Faza | Kąt | Stan | Typ galaktyk |
|------|------|--------|----------------|
| Λ | 45° | liniowy | eliptyczne, soczewkowate |
| τ | 60° | przejście | spiralne luźne, nieregularne |
| ρ | 90° | rezonans | spiralne wyraźne, stabilne |

Galaktyki nie są klasyfikowane po wyglądzie, lecz po stanie informacji w strukturze pola.

### 4. Zgodność z FIELDCORE

Analiza odnosi się do istniejących sekcji repozytorium:
- /docs — diagram toruso‑Möbiusa
- /models — model globalnego pola
- /examples — przykład kosmologiczny
- /src — implementacja symboliczna skrętu

Toruso‑Möbius ujawnia globalną interpretację FIELDCORE bez zmiany jego natury.
### 5. Implementacja: program rysujący toruso‑Möbiusa

W ramach warstwy modeli kosmicznych dołączony zostanie:

- wzór parametryczny toruso‑Möbiusa (lewostronny, odsunięty od centrum),
- działający program w Pythonie (Thonny / matplotlib) rysujący tę strukturę.

#### 5.1. Wzór na toruso‑Möbiusa

Parametry:
- u ∈ [0, 2π] — kierunek globalny (zamknięcie torusa),
- v ∈ [-1, 1] — szerokość paska,
- R > 1 — odsunięcie od centrum,
- a > 0 — szerokość paska (brak samoprzecięć przy małym a).

Wzór:

x(u,v) = (R + a v cos(u/2)) cos u  
y(u,v) = (R + a v cos(u/2)) sin u  
z(u,v) =  a v sin(u/2)

Lewostronność wynika z użycia sin(u/2), cos(u/2).

#### 5.2. Program rysujący toruso‑Möbiusa (Python)

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# parametry toruso‑Möbiusa
R = 2.0     # odsunięcie od centrum
a = 0.5     # szerokość paska

u = np.linspace(0, 2*np.pi, 300)
v = np.linspace(-1, 1, 50)
u, v = np.meshgrid(u, v)

x = (R + a * v * np.cos(u/2)) * np.cos(u)
y = (R + a * v * np.cos(u/2)) * np.sin(u)
z =  a * v * np.sin(u/2)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')

ax.set_title("Lewostronny toruso‑Möbius (FIELDCORE)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

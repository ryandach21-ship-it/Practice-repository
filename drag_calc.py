# drag_calc.py
# Place this file in the same folder as index.html.
# All physics and math live here. The HTML only reads inputs and calls Python.

def compute_drag(rho, V, Cd, A):
    """
    Standard form: D = 0.5 * rho * V^2 * Cd * A
    Returns a dictionary with results and echoed inputs.
    """
    # Ensure numeric types and basic validation
    rho = float(rho)
    V = float(V)
    Cd = float(Cd)
    A = float(A)
    # dynamic pressure
    q = 0.5 * rho * V * V
    drag = q * Cd * A
    return {"drag": drag, "q": q, "rho": rho, "V": V, "Cd": Cd, "A": A}

def compute_drag_alt(rho, V, Cd, A):
    """
    Alternate formulation that computes using stepwise operations,
    included to show that the HTML calls Python-only logic.
    """
    rho = float(rho)
    V = float(V)
    Cd = float(Cd)
    A = float(A)
    # compute kinetic energy per unit volume then scale
    ke_per_vol = 0.5 * rho * V * V
    drag = Cd * A * ke_per_vol
    q = ke_per_vol
    return {"drag": drag, "q": q, "rho": rho, "V": V, "Cd": Cd, "A": A}

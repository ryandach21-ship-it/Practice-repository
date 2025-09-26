def calculate_parasitic_drag(rho, velocity, area, cd):
    """
    Calculate parasitic drag force.
    
    Parameters:
    rho (float): Air density in kg/m^3
    velocity (float): Velocity in m/s
    area (float): Reference area in m^2
    cd (float): Drag coefficient
    
    Returns:
    float: Parasitic drag in Newtons
    """
    drag = 0.5 * rho * velocity**2 * area * cd
    return drag

# Example usage
rho = 1.225       # Sea level standard air density (kg/m^3)
velocity = 70.0   # m/s
area = 1.5        # m^2
cd = 0.03         # Typical for streamlined body

drag = calculate_parasitic_drag(rho, velocity, area, cd)
print(f"Parasitic Drag: {drag:.2f} N")

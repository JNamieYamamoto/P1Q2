import numpy as np
import matplotlib.pyplot as plt

def y(t):
    return 2/(1 - np.exp(-2 * t - np.log(2)))

def f(t, y):
    y_t = y
    return 2 * y_t - y_t ** 2

def euler_method(f, t_range, y0):
    num_steps = 40
    t_values = np.linspace(t_range[0], t_range[1], num_steps)
    y_values = np.zeros_like(t_values)
    y_values[0] = y0
    
    for i in range(1, num_steps):
        y_values[i] = y_values[i - 1] + 0.1 * f(t_values[i - 1], y_values[i - 1])
    
    return t_values, y_values

def modified_euler_method(f, t_range, y0, dt, n):
    num_steps = int((t_range[1] - t_range[0]) / dt) + 1
    t_values = np.linspace(t_range[0], t_range[1], num_steps)
    y_values = np.zeros_like(t_values)
    y_values[0] = y0
    
    for i in range(1, n):
        y_n_aprox = y_values[i - 1] + 0.1 * (2 * y_values[i - 1] - y_values[i - 1] ** 2)
        y_values[i] = y_values[i - 1] + 0.05 * ((2 * y_values[i - 1] - y_values[i - 1] ** 2) + (2 * y_n_aprox - y_n_aprox ** 2))
    
    return t_values[:n], y_values[:n]

def plot_direction_field(f, t_range, y_range, dt=0.1, y0=4):
    t_values = np.linspace(t_range[0], t_range[1], int((t_range[1] - t_range[0]) / dt) + 1)
    y_values = np.linspace(y_range[0], y_range[1], int((y_range[1] - y_range[0]) / dt) + 1)
    
    T, Y = np.meshgrid(t_values, y_values)
    
    dY_dt = f(T, Y)
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(t_values, y(t_values), 'b-', label='y(t)')
    
    plt.quiver(T, Y, dt*np.ones_like(dY_dt), dY_dt*dt, scale=20, color='r', alpha=0.5)
    
    t_euler, y_euler = euler_method(f, t_range, y0)
    plt.plot(t_euler, y_euler, 'g--', label=f'Euler Method (dt={dt})')
    
    t_modified_euler, y_modified_euler = modified_euler_method(f, t_range, y0, dt, len(t_values))
    plt.plot(t_modified_euler, y_modified_euler, 'm--', label=f'Modified Euler Method (dt={dt})')
    
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Direction Field with y(t), Euler and Modified Euler Methods')
    plt.grid(True)
    plt.xlim(t_range)
    plt.ylim(y_range)
    plt.legend()
    plt.show()

# Define the interval for t and y
t_range = (0, 4)
y_range = (0, 4)

# Plot the direction field with y(t), Euler method and Modified Euler method with dt=0.1
plot_direction_field(f, t_range, y_range, dt=0.1)

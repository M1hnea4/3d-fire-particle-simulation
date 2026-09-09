# 🔥 3D Interactive Fire Particle System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![VPython](https://img.shields.io/badge/VPython-3D_Simulation-11557c?style=for-the-badge)
![Physics](https://img.shields.io/badge/Physics-Particle_Kinematics-FF6F00?style=for-the-badge)

A real-time 3D particle system built with Python and VPython that simulates the thermodynamic and kinetic behavior of fire. The simulation dynamically adjusts particle vectors, color temperature, and convection draft based on a user-controlled intensity slider.

### ⚙️ Physics & Rendering Engine
* **Particle Lifecycle Management:** Independently tracks and renders 400 sphere entities. Particles are continuously recycled upon reaching their maximum calculated height or dropping below the opacity threshold.
* **Vector Mathematics & Kinematics:** Implements real-time spatial calculations for convection draft (pulling particles toward the central Y-axis as they rise) and randomized X/Z axis flickering.
* **Dynamic Linear Interpolation (Lerp):** smoothly transitions the RGB color vectors from a low-intensity state (wide, slow, orange/red) to a high-intensity state (thin, fast, blue) based on real-time UI slider input.
* **Procedural Scaling:** Radius and opacity of each particle decay non-linearly relative to its progress along the Y-axis, simulating the natural dissipation of thermal energy.

### 🎮 Interactive UI
* Features a built-in graphical slider linked to a global state variable, allowing users to instantly mutate the physical properties of the entire 3D environment at 60 FPS without frame drops.

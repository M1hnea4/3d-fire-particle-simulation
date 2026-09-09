from vpython import *
import random

# Scene configuration
scene.background = color.black
scene.width = 900
scene.height = 700
scene.title = "Fire Simulation: Low (Orange/Wide) to High (Blue/Thin)"
scene.caption = "\nSlide right to increase intensity: Orange -> Blue \n"

fire_strength = 0.5 
base_size = 10.0

floor = box(pos=vec(0, -5.1, 0), size=vec(15, 0.1, 15), color=vec(0.1, 0.1, 0.1))

fire_box = box(pos=vec(0, 0, 0), size=vec(base_size, base_size, base_size), 
               opacity=0.0, color=color.white)

def get_base_y():
    return fire_box.pos.y - base_size / 2

def get_fire_color(strength):
    c_orange = vec(1, 0.3, 0)
    c_blue = vec(0, 0.3, 1)  
    
    if strength <= 0.2: 
        return c_orange
    elif strength >= 0.8: 
        return c_blue
    else:
        factor = (strength - 0.2) / 0.6
        return c_orange + (c_blue - c_orange) * factor

# Create caption_text FIRST so the slider can use it
caption_text = wtext(text="Intensity: 50%", pos=scene.caption_anchor)

def set_strength(s):
    global fire_strength
    fire_strength = s.value
    caption_text.text = f"Intensity: {int(fire_strength*100)}%"

slider(min=0.01, max=1.0, value=fire_strength, length=scene.width * 0.8, bind=set_strength)

def reset_particle(p):
    r_max = (base_size / 3) * (1.2 - fire_strength) 
    
    angle = random.uniform(0, 2*pi)
    r = sqrt(random.uniform(0, 1)) * r_max
    
    p.pos = vec(fire_box.pos.x + r * cos(angle), 
                get_base_y(), 
                fire_box.pos.z + r * sin(angle))
    
    v_y = (0.05 + fire_strength * 0.35) * random.uniform(0.8, 1.2)
    p.velocity = vec(0, v_y, 0)
    p.opacity = 1.0

N_PARTICLES = 400
particles = []
for _ in range(N_PARTICLES):
    p = sphere(radius=0.3, emissive=True)
    reset_particle(p)
    particles.append(p)

while True:
    rate(60) 
    
    current_base_y = get_base_y()
    max_height = 2.5 + (fire_strength * 6.5) 

    for p in particles:
        p.pos += p.velocity
        
        flicker_amp = 0.02 + (1 - fire_strength) * 0.05
        p.pos.x += random.uniform(-flicker_amp, flicker_amp)
        p.pos.z += random.uniform(-flicker_amp, flicker_amp)
        
        pull_factor = 0.02 + (fire_strength * 0.12)
        dist_x = p.pos.x - fire_box.pos.x
        dist_z = p.pos.z - fire_box.pos.z
        p.pos.x -= dist_x * pull_factor
        p.pos.z -= dist_z * pull_factor
        
        progress = (p.pos.y - current_base_y) / max_height

        p.color = get_fire_color(fire_strength)
        p.opacity = max(0, 1.0 - progress)

        p.radius = (0.35 - fire_strength * 0.15) * (1 - progress * 0.4)

        if progress >= 1.0 or p.opacity <= 0.02:
            reset_particle(p)
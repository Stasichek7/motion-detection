import numpy as np
import matplotlib.pyplot as plt
import os

# ==============================================================================
# MSAP - Practice 7: ASSIGNMENT - MOTION DETECTION
# ==============================================================================

output_dir = "student_output"
os.makedirs(output_dir, exist_ok=True)

# ------------------------------------------------------------------------------
# 1. SETUP THE IMAGES (The Security Camera Feed)
# ------------------------------------------------------------------------------
size = 100

# Let's generate a "Background" - a simple striped wall
bg = np.zeros((size, size))
for i in range(size):
    if i % 10 < 5:
        bg[:, i] = 0.8  # Light gray stripe
    else:
        bg[:, i] = 0.4  # Dark gray stripe

# Now the "Current" frame - someone walked in!
current = bg.copy()
# We draw the intruder (a dark rectangular shadow)
current[40:80, 20:50] = 0.1 

# Add some camera noise to both images (nothing is perfect in real life)
np.random.seed(42)
bg += np.random.normal(0, 0.05, (size, size))
current += np.random.normal(0, 0.05, (size, size))

# ------------------------------------------------------------------------------
# TODO: IMPLEMENT BACKGROUND SUBTRACTION
# ------------------------------------------------------------------------------
# 1. Calculate the absolute difference between 'current' and 'bg'. 
difference = np.abs(current - bg)

# 2. Apply a Threshold (T). If the difference is > T, it's motion (1). 
#    Else, it's just noise (0). Try threshold T = 0.15
detection_mask = difference > 0.15

# ------------------------------------------------------------------------------
# VISUALIZATION
# ------------------------------------------------------------------------------

if detection_mask is not None:
    fig, axs = plt.subplots(1, 4, figsize=(16, 4))
    
    axs[0].imshow(bg, cmap='gray', vmin=0, vmax=1)
    axs[0].set_title("1. Background")
    
    axs[1].imshow(current, cmap='gray', vmin=0, vmax=1)
    axs[1].set_title("2. Current Frame")
    
    axs[2].imshow(difference, cmap='gray')
    axs[2].set_title("3. Absolute Difference")
    
    # Using astype(float) or similar just ensures it plots cleanly as 0/1
    axs[3].imshow(detection_mask.astype(float), cmap='gray', vmin=0, vmax=1)
    axs[3].set_title("4. Motion Detection (Alarm!)")
    
    plt.tight_layout()
    plt.show()
else:
    print("⚠️ Background subtraction is not implemented yet.")
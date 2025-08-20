# chart.py
# Author: SIDHAARTH SHREE
# Email: 22f3001480@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# ------------------------------
# 1. Generate synthetic dataset
# ------------------------------
np.random.seed(42)

data = {
    "Team": np.repeat(["Tier 1", "Tier 2", "Tier 3"], 100),
    "Response Time (min)": np.concatenate([
        np.random.normal(loc=15, scale=5, size=100),   # Tier 1
        np.random.normal(loc=30, scale=7, size=100),   # Tier 2
        np.random.normal(loc=50, scale=10, size=100)   # Tier 3
    ])
}

df = pd.DataFrame(data)

# ------------------------------
# 2. Set Seaborn professional style
# ------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# ------------------------------
# 3. Create violinplot
# ------------------------------
plt.figure(figsize=(8, 8))  # base size
sns.violinplot(
    x="Team",
    y="Response Time (min)",
    data=df,
    palette="Set2",
    inner="quartile"
)

plt.title("Support Efficiency Analysis", fontsize=16, weight="bold")
plt.xlabel("Support Team", fontsize=12)
plt.ylabel("Response Time (minutes)", fontsize=12)

# ------------------------------
# 4. Save raw image
# ------------------------------
plt.savefig("chart_raw.png", dpi=64)  # don't use bbox_inches="tight"
plt.close()

# ------------------------------
# 5. Force exact 512x512 pixels
# ------------------------------
img = Image.open("chart_raw.png")
img_resized = img.resize((512, 512))
img_resized.save("chart.png")

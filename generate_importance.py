import matplotlib.pyplot as plt
import numpy as np

# Data based on the model features
features = ["Credit Utilization", "Age", "Debt Ratio", "Late Pay Count", "Monthly Income"]
importance = [0.35, 0.20, 0.18, 0.15, 0.12]

# Professional styling
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#1f77b4', '#3498db', '#5dade2', '#85c1e9', '#aed6f1']
bars = ax.barh(features, importance, color=colors[::-1])

ax.set_xlabel('Importance Score', fontsize=12, fontweight='bold')
ax.set_title('Model Feature Importance - Credit Risk Scoring', fontsize=14, fontweight='bold', pad=20)
ax.invert_yaxis()  # Highest importance at top

# Add value labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.01, bar.get_y() + bar.get_height()/2, f'{width:.2f}', 
            va='center', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('importance.png', dpi=300, bbox_inches='tight')
print("Chart saved as importance.png")

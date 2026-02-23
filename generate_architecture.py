import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis('off')

# Define boxes
boxes = [
    (0.5, 1.5, 2, 1, "Raw Data\n(CSVs/JSON)"),
    (3, 1.5, 2, 1, "Preprocessing\n(Cleaning/Scaling)"),
    (5.5, 1.5, 2, 1, "Random Forest\n(Classification)"),
    (8, 1.5, 1.5, 1, "Risk Score\n(Output)")
]

# Draw boxes and arrows
for i, (x, y, w, h, label) in enumerate(boxes):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", 
                                  linewidth=2, edgecolor='#2c3e50', facecolor='#ecf0f1')
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, label, ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Add arrows
    if i < len(boxes) - 1:
        ax.arrow(x + w + 0.1, y + h/2, 0.3, 0, head_width=0.2, head_length=0.1, fc='#2c3e50', ec='#2c3e50')

plt.title("System Architecture Overview", fontsize=14, fontweight='bold', pad=20)
plt.savefig('architecture.png', dpi=300, bbox_inches='tight')
print("Diagram saved as architecture.png")

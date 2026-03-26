import matplotlib.pyplot as plt

def create_impact_chart():
    # 1. Define the Data
    # This represents a list of names and a numerical value assigned to them
    labels = ['Figure A', 'Figure B', 'Figure C', 'Figure D', 'Figure E']
    impact_scores = [95, 88, 75, 92, 80]

    # 2. Create the Figure and Axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # 3. Build the Bar Chart
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    bars = ax.bar(labels, impact_scores, color=colors)

    # 4. Add Professional Styling
    ax.set_ylabel('Impact Score (0-100)')
    ax.set_title('Comparative Analysis of Historical Figures', fontsize=14)
    ax.set_ylim(0, 110) # Set limit slightly higher than max score for spacing
    
    # Add gridlines for readability
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)

    # Add data labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height}', ha='center', va='bottom')

    # 5. Show the Plot
    plt.tight_layout()
    print("Generating chart... (A window should pop up shortly)")
    plt.show()

if __name__ == "__main__":
    create_impact_chart()

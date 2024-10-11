import matplotlib.pyplot as plt
import numpy as np

# Activities and corresponding emotional connection (0 to 10) and frequency (0 to 10)
activities = ["Coding", "FIFA", "Talking to GF", "Spending time with H'shil", "Work", "Parks and Rec", "LeetCode Prep", "Self-care", "Worrying about future"]
emotional_connection = [8, 7, 10, 9, 6, 8, 7, 5, 9]
frequency = [5, 4, 10, 6, 7, 6, 5, 4, 8]

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(frequency, emotional_connection, color='teal', s=100)

# Add labels for each activity
for i, activity in enumerate(activities):
    plt.text(frequency[i] + 0.1, emotional_connection[i] - 0.1, activity, fontsize=12)

# Labels and title
plt.xlabel("Frequency of Activity", fontsize=12)
plt.ylabel("Emotional Connection", fontsize=12)
plt.title("Emotional Connection vs Frequency of Activities", fontsize=14)
plt.xlim(0, 11)
plt.ylim(0, 11)

# Show the plot
plt.grid(True)
plt.show()
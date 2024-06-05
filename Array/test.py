import matplotlib.pyplot as plt
import pandas as pd

# Sample data for the survey
data = {
    "Category": ["Job Satisfaction", "Communication", "Leadership", "Work Environment", "Professional Development"],
    "Very Satisfied": [30, 20, 25, 28, 18],
    "Satisfied": [40, 30, 35, 32, 30],
    "Neutral": [15, 20, 20, 20, 25],
    "Dissatisfied": [10, 20, 15, 15, 20],
    "Very Dissatisfied": [5, 10, 5, 5, 7]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting bar charts for each category
fig, ax = plt.subplots(3, 2, figsize=(14, 10))

categories = df["Category"]
x = range(len(categories))

ax[0, 0].bar(x, df["Very Satisfied"], label='Very Satisfied')
ax[0, 0].bar(x, df["Satisfied"], bottom=df["Very Satisfied"], label='Satisfied')
ax[0, 0].bar(x, df["Neutral"], bottom=df["Very Satisfied"] + df["Satisfied"], label='Neutral')
ax[0, 0].bar(x, df["Dissatisfied"], bottom=df["Very Satisfied"] + df["Satisfied"] + df["Neutral"], label='Dissatisfied')
ax[0, 0].bar(x, df["Very Dissatisfied"], bottom=df["Very Satisfied"] + df["Satisfied"] + df["Neutral"] + df["Dissatisfied"], label='Very Dissatisfied')
ax[0, 0].set_xticks(x)
ax[0, 0].set_xticklabels(categories, rotation=45, ha='right')
ax[0, 0].set_ylabel('Number of Responses')
ax[0, 0].set_title('Survey Results by Category')
ax[0, 0].legend()

# Plotting pie charts for each category
for i, category in enumerate(categories):
    sizes = [df.loc[i, "Very Satisfied"], df.loc[i, "Satisfied"], df.loc[i, "Neutral"], df.loc[i, "Dissatisfied"], df.loc[i, "Very Dissatisfied"]]
    labels = ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"]
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
    explode = (0.1, 0, 0, 0, 0)  # only "explode" the 1st slice
    ax_flat = ax.flatten()
    ax_flat[i + 1].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax_flat[i + 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax_flat[i + 1].set_title(category)

plt.tight_layout()
plt.show()

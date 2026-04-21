# Fun Project - Student Performance Dashboard
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
# ── Generate Dataset ──────────────────────────────────────────────────────────
np.random.seed(42)
n = 50
subjects = ['Math', 'Science', 'English', 'History', 'Computer']
students = [f'Student_{i+1}' for i in range(n)]
data = {'Student': students}
for sub in subjects:
    data[sub] = np.random.randint(40, 100, n)
df = pd.DataFrame(data)
df['Total'] = df[subjects].sum(axis=1)
df['Average'] = df[subjects].mean(axis=1).round(2)
df['Grade'] = pd.cut(df['Average'],
bins=[0, 50, 60, 70, 80, 100],
labels=['F', 'D', 'C', 'B', 'A'])
print("=== Student Performance Dashboard ===")
print(df.head())
print(f"\nGrade Distribution:\n{df['Grade'].value_counts()}")
print(f"\nSubject Averages:")
for s in subjects:
    print(f" {s}: {df[s].mean():.2f}")
# ── Create Dashboard (6 charts) ───────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Student Performance Dashboard', fontsize=16, fontweight='bold')
colors = ['#FF6B6B','#4ECDC4','#45B7D1','#96CEB4','#FFEAA7']
# 1. Bar - avg per subject
ax = axes[0, 0]
avgs = [df[s].mean() for s in subjects]
bars = ax.bar(subjects, avgs, color=colors)
ax.set_title('Average Score per Subject')
ax.set_ylim(0, 100)
for bar, avg in zip(bars, avgs):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1,
    f'{avg:.1f}', ha='center', fontsize=9)
# 2. Histogram
ax = axes[0, 1]
ax.hist(df['Average'], bins=15, color='steelblue', edgecolor='white')
ax.axvline(df['Average'].mean(), color='red', linestyle='--',
label=f'Mean: {df["Average"].mean():.1f}')
ax.set_title('Distribution of Averages')
ax.legend()
# 3. Pie - grades
ax = axes[0, 2]
gc = df['Grade'].value_counts().sort_index()
pie_colors = ['#e74c3c','#e67e22','#f1c40f','#2ecc71','#3498db']
ax.pie(gc.values, labels=gc.index, autopct='%1.1f%%',
colors=pie_colors[:len(gc)], startangle=90)
ax.set_title('Grade Distribution')
# 4. Scatter Math vs Science
ax = axes[1, 0]
sc = ax.scatter(df['Math'], df['Science'],
c=df['Average'], cmap='RdYlGn', alpha=0.7, s=50)
plt.colorbar(sc, ax=ax, label='Overall Avg')
ax.set_title('Math vs Science Scores')
ax.set_xlabel('Math'); ax.set_ylabel('Science')
# 5. Box plot
ax = axes[1, 1]
bp = ax.boxplot([df[s].values for s in subjects],
labels=subjects, patch_artist=True)
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
ax.set_title('Score Spread per Subject')
# 6. Top 10 students
ax = axes[1, 2]
top10 = df.nlargest(10, 'Average')[['Student','Average']]
ax.barh(top10['Student'], top10['Average'], color='#6c5ce7')
ax.set_title('Top 10 Students')
ax.set_xlabel('Average Score'); ax.set_xlim(0, 100)
for i, (_, row) in enumerate(top10.iterrows()):
    ax.text(row['Average']+0.5, i, f'{row["Average"]:.1f}', va='center', fontsize=8)
plt.tight_layout()
plt.savefig('fun_project_dashboard.png', dpi=100, bbox_inches='tight')
# plt.show() # Commented out for non-interactive environment
print("\nDashboard saved as fun_project_dashboard.png")

from matplotlib.widgets import Cursor
import matplotlib.pyplot as plt

# Sample data
teams = ['Team A', 'Team B', 'Team C', 'Team D']
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
team_labels = ['Team A', 'Team B', 'Team C', 'Team D']

fig, ax = plt.subplots()
scatter = ax.scatter(x, y)

# Annotate the plot
annot = ax.annotate("", xy=(0, 0), xytext=(10, 10),
                    textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    pos = scatter.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = f"{team_labels[ind['ind'][0]]}"
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.8)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = scatter.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

# Calculate the average of y values and add a horizontal line
y_avg = sum(y) / len(y)
ax.axhline(y=y_avg, color='red', linestyle='--', label=f'Average (y={y_avg:.2f})')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatterplot with Hover Info and Average Line")
plt.legend()
plt.show()
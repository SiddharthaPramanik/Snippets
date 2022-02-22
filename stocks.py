import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation  

itc_df = pd.read_csv('data/ITC-EQ-20-02-2021-to-20-02-2022.csv')
ntpc_df = pd.read_csv('data/NTPC-EQ-20-02-2021-to-20-02-2022.csv')
itc_df.columns = itc_df.columns.str.strip()
ntpc_df.columns = ntpc_df.columns.str.strip()


frame_amt = len(itc_df)

# Setup figure 
fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(2, 2)

ax0 = fig.add_subplot(gs[0, :], facecolor=(0.9, 0.9, 0.9))

itc_line, = ax0.plot([], [], 'b', linewidth=2)
ntpc_line, = ax0.plot([], [], 'r', linewidth=2)

# Define animation function
def update_plot(num):
    itc_line.set_data(itc_df.index[0:num], itc_df['OPEN'][0:num])
    ntpc_line.set_data(ntpc_df.index[0:num], ntpc_df['OPEN'][0:num])

    return itc_line, ntpc_line

# Animation
ani = animation.FuncAnimation(fig, update_plot, frames=frame_amt, interval=20, repeat=True, blit=True)

plt.xlim(itc_df.index[0], itc_df.index[-1])
plt.ylim(0, max(max(itc_df['OPEN']), max(ntpc_df['OPEN'])) + 10)

plt.show()
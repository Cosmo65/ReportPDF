import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np
import os

file_name = "../img/antenna_1.png"
xs = np.arange(7)
ys = xs**2

#fig = plt.figure(figsize=(5, 10))
fig = plt.figure(dpi=300, figsize=(5,5))


# offset_copy works for polar plots also.
#ax = plt.subplot(2, 1, 2, projection='polar')
#ax = plt.plot(projection='polar')

#trans_offset = mtransforms.offset_copy(ax.transData, fig=fig, y=6, units='dots')

for x, y in zip(xs, ys):
    plt.polar(x, y, 'ro')
    plt.text(x, y, '%d, %d' % (int(x), int(y)))

if os.path.exists(file_name):
    os.remove(file_name)
plt.savefig(file_name)

plt.show()

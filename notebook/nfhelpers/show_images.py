import matplotlib.pyplot as plt
import math

def show_images(images, size_multiplier=1):
    cols = min(7, len(images))
    rows = math.ceil(len(images)/cols)
    plt.figure(num=None, figsize=(rows*5*size_multiplier, cols*5*size_multiplier), facecolor='w', edgecolor='k')
    ax = [plt.subplot(rows, cols, i+1) for i in range(len(images))]
    for a in ax:
        a.set_xticklabels([])
        a.set_yticklabels([])
        a.tick_params(bottom=False, left=False)
    plt.subplots_adjust(wspace=0, hspace=0.1)

    for i in range(len(images)):
#         ax[i].title.set_text(f"skyview zone {i}")
        ax[i].imshow(images[i])
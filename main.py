# %%
import tkinter as tk
from PIL import ImageTk as itk
from PIL import Image
import pyautogui as gui
# %%
old_coords = None
done = False
a = False


def click(event):

    global old_coords
    global done
    if old_coords and done:
        old_coords = None
        done = False
    if not old_coords:
        old_coords = (event.x, event.y)
    else:
        done = True


rect = None


def motion(event):
    global rect
    if done:
        return
    if rect:
        event.widget.delete(rect)
    if old_coords:
        x, y = old_coords
        rect = event.widget.create_rectangle(
            x, y, event.x, event.y, outline="#fb0",)


# %%

root = tk.Tk()
root.state('zoomed')
# root.attributes("-fullscreen", True)

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)


canvas = tk.Canvas(main_frame, cursor='tcross', relief=tk.SUNKEN)
canvas.bind("<Button-1>", click)
canvas.bind('<Motion>', motion)

xscrollbar = tk.ttk.Scrollbar(
    main_frame, orient=tk.HORIZONTAL, command=canvas.xview)
xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

yscrollbar = tk.ttk.Scrollbar(
    main_frame, orient=tk.VERTICAL, command=canvas.yview)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# canvas.bind('<Configure>', lambda e: canvas.configure(
#     scrollregion=canvas.bbox("all")))


img = gui.screenshot()
width, height = img.size
canvas.config(scrollregion=(0, 0, width, height))
tkimg = itk.PhotoImage(image=img)
canvas.create_image(20, 20, anchor=tk.NW, image=tkimg)

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


root.mainloop()

# %%

# %%

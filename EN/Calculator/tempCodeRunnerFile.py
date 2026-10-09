btn = tk.Button(window, image=icon, command=lambda: count_areaStTriang())
btn.pack(pady=1)

def count_areaStTriang():
    return figure_classes_area.StandardTriangle.areaStTriang()
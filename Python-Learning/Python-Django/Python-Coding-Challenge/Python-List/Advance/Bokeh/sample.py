from bokeh.plotting import figure, show

p = figure(title="Simple Line Example")
p.line([1, 2, 3], [4, 6, 5])
show(p)

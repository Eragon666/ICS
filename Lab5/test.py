from glumpy import figure, show
  
fig   = figure(size=(800,400))
  
fig1  = fig.add_figure(cols=2,rows=1, position=[0,0])
frame1 = fig1.add_frame(aspect=1)
  
fig2  = fig.add_figure(cols=2,rows=1, position=[1,0])
frame2 = fig2.add_frame(aspect=1)
  
@fig.event
def on_draw():
    fig.clear(0.85,0.85,0.85,1.00)
    frame1.draw(x=frame1.x, y=frame1.y)
    frame2.draw(x=frame2.x, y=frame2.y)
  
show()

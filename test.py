import numpy as np

# position: x,y. Color: r,g,b
data = np.zeros(4, dtype = [ ("position", np.float32, 2),
                                ("color",    np.float32, 3)] )

print data


# position shader
uniform float scale;
attribute vec2 position;
attribute vec4 color;
varying vec4 v_color;
void main()
{
    gl_Position = vec4(position*scale, 0.0, 1.0);
    v_color = color;
}

# color fragment
varying vec4 v_color;
void main()
{
    gl_FragColor = v_color;
}


import colorsys

colors = {
    "red0": "#710100",
    "red1": "#FB3048",
    "red2": "#FF5048",
    "yellow0": "#FDF500",
    "yellow1": "#CFED58",
    "green0": "#28C775",
    "cyan0": "#1AC5B0",
    "blue0": "#5DF4FE",
    "purple0": "#9370DB",
    "pink0": "#E455AE",
    "magenta0": "#CB1DCD",
    "redblack0": "#272932",
    "redblack1": "#331319",
    "redblack2": "#210E15",
    "black0": "#040A10",
    "deepblue0": "#14101F",
    "dred0": "#551C1B",
    "dred1": "#B11B22",
    "dred2": "#DE4F60",
    "dred3": "#E16C66",
    "dylw0": "#FFF700",
    "dylw1": "#CFDB48",
    "dylw2": "#C9E364",
    "dgreen0": "#54C98D",
    "dgreen1": "#24D6C1",
    "dblue0": "#78DCE3",
    "dpurple0": "#8A68CF",
    "dpink0": "#D562A9",
    "dpink1": "#CE40B4",
    "dpink2": "#BC2DBE"
}

def hex_to_hsl(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        raise ValueError("Invalid hex color")
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h_deg = round(h * 360)
    s_percent = round(s * 100)
    l_percent = round(l * 100)
    return f"hsl({h_deg},{s_percent},{l_percent})"

for name, hex_value in colors.items():
    hsl_value = hex_to_hsl(hex_value)
    print(f"local {name} = \"{hsl_value}\"")
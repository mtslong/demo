import colorsys

# gold
r, g, b = 1.00, 0.84, 0.00

print "RGB", (r, g, b)

y, i, q = colorsys.rgb_to_yiq(r, g, b)
print "YIQ", (y, i, q), "=>", colorsys.yiq_to_rgb(y, i, q)

h, l, s = colorsys.rgb_to_hls(r, g, b)
print "HLS", (h, l, s), "=>", colorsys.hls_to_rgb(h, l, s)

h, s, v = colorsys.rgb_to_hsv(r, g, b)
print "HSV", (h, s, v), "=>", colorsys.hsv_to_rgb(h, s, v)

## RGB (1.0, 0.84, 0.0)
## YIQ (0.7956, 0.3648, -0.2268) => (0.9999998292, 0.8400000312, 0.0)
## HLS (0.14, 0.5, 1.0) => (1.0, 0.84, 0.0)
## HSV (0.14, 1.0, 1.0) => (1.0, 0.84, 0.0)

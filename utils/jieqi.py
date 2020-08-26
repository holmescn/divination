"""用天文方法计算二十四节气

参考：
- https://github.com/hotoo/nong/wiki
- https://blog.csdn.net/orbit/article/details/7749723
- https://blog.csdn.net/orbit/article/details/7825004
- https://blog.csdn.net/orbit/article/details/7910220
- https://blog.csdn.net/orbit/article/details/7944248
"""
from math import pi, radians, degrees, cos, sin, tan

_DATA = {
    "chunfen": {
        "name": "春分",
        "center_deg": 0.0,
        "calibrate": {
            # year range -> slope, intercept
            (None, 2025): (-2.435482637536e-04,  4.929336937169e-01),
            (2026, None): ( 2.432633976960e-04, -4.923377247071e-01),
        }
    },
    "qingming": {
        "name": "清明",
        "center_deg": 15.0,
        "calibrate": {
            (): (-2.435755031547e-04, 7.547131264927e-01),
        }
    },
}
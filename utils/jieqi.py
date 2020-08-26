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
    "guyu": {
        "name": "谷雨",
        "center_deg": 30.0,
        "calibrate": {
            (): (-2.435813687136e-04, 1.016451635187e+00),
        }
    },
    "lixia": {
        "name": "立夏",
        "center_deg": 45.0,
        "calibrate": {
            (): (-2.435874621099e-04, 1.278193128332e+00),
        }
    },
    "xiaoman": {
        "name": "小满",
        "center_deg": 60.0,
        "calibrate": {
            (): (-2.435999015843e-04, 1.539953046123e+00),
        }
    },
    "mangzhong": {
        "name": "芒种",
        "center_deg": 75.0,
        "calibrate": {
            (): (-2.436146215103e-04, 1.801725933376e+00),
        }
    },
    "xiazhi": {
        "name": "夏至",
        "center_deg": 90.0,
        "calibrate": {
            (): (-2.436364195019e-04, 2.063524554429e+00),
        }
    },
    "xiaoshu": {
        "name": "小暑",
        "center_deg": 105.0,
        "calibrate": {
            (): (-2.436581162278e-04, 2.325337615917e+00),
        }
    },
    "dashu": {
        "name": "大暑",
        "center_deg": 120.0,
        "calibrate": {
            (): (-2.436806132588e-04, 2.587168294143e+00),
        }
    },
    "liqiu": {
        "name": "立秋",
        "center_deg": 135.0,
        "calibrate": {
            (): (-2.437038769339e-04, 2.849017680568e+00),
        }
    },
    "chushu": {
        "name": "处暑",
        "center_deg": 150.0,
        "calibrate": {
            (): (-2.437255202828e-04, 3.110881202799e+00),
        }
    },
    "bailu": {
        "name": "白露",
        "center_deg": 165.0,
        "calibrate": {
            (): (-2.437458074977e-04, 3.372755533186e+00),
        }
    },
    "qiufen": {
        "name": "秋分",
        "center_deg": 180.0,
        "calibrate": {
            (): (-2.437565093008e-04, 3.634622264703e+00),
        }
    },
    "hanlu": {
        "name": "寒露",
        "center_deg": 195.0,
        "calibrate": {
            (): (-2.437630670008e-04, 3.896486256744e+00),
        }
    },
    "shuangjiang": {
        "name": "霜降",
        "center_deg": 210.0,
        "calibrate": {
            (): (-2.437681456538e-04, 4.158349213711e+00),
        }
    },
    "lidong": {
        "name": "立冬",
        "center_deg": 225.0,
        "calibrate": {
            (): (-2.437588212201e-04, 4.420181682744e+00),
        }
    },
    "xiaoxue": {
        "name": "小雪",
        "center_deg": 240.0,
        "calibrate": {
            (): (-2.437473723179e-04, 4.682003357744e+00),
        }
    },
    "daxue": {
        "name": "大雪",
        "center_deg": 255.0,
        "calibrate": {
            (): (-2.437272722366e-04, 4.943797938620e+00),
        }
    },
    "dongzhi": {
        "name": "冬至",
        "center_deg": 270.0,
        "calibrate": {
            (): (-2.437042802203e-04, 5.205574819033e+00),
        }
    },
    "xiaohan": {
        "name": "小寒",
        "center_deg": 285.0,
        "calibrate": {
            (): (-2.436822804822e-04, 5.467583575670e+00),
        }
    },
    "dahan": {
        "name": "大寒",
        "center_deg": 300.0,
        "calibrate": {
            (): (-2.436508561672e-04, 5.729311616748e+00),
        }
    },
    "lichun": {
        "name": "立春",
        "center_deg": 315.0,
        "calibrate": {
            (): (-2.436249824692e-04, 5.991033162840e+00),
        }
    },
    "yushui": {
        "name": "雨水",
        "center_deg": 330.0,
        "calibrate": {
            (): (-2.436030406637e-04, 6.252746753395e+00),
        }
    },
    "jingzhe": {
        "name": "惊蛰",
        "center_deg": 345.0,
        "calibrate": {
            (): (-2.435872515067e-04, 6.514459099483e+00),
        }
    }
}
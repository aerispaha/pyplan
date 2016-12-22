# pyplan

The pyplan project is being developed to provide tools for planning-level alternative analysis of progresive capital improvement projects. pyplan is well suited to illustrate the cost/benefit dynamics of projects made up of several independent and combinable sub-projects.

#### Example use case:
A utility is interested in addresing a regional flooding issue with new releif sewers. Relief sewers are being considered in three different areas, each of which may be implemented at 1, 2, or 3 mile lengths. The relief sewers in each area can be combined with relief sewers in the other two areas, regardless of how long any reach is.

Engineers then produce cost estimates and measure the performance of every logical combination of flood releif sewer installation. (The [swmmio](https://github.com/aerispaha/swmmio) package is being developed to generate flood releif models with EPA SWMMM5 for this exact use case). With

<div id="python-plot"></div>
<script type="text/javascript" src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<script type="text/javascript">
Plotly.newPlot("python-plot", [{
        "name": "All Projects",
        "text": ["M01<br>(17 parcels/$M)", "M02<br>(15 parcels/$M)", "M03<br>(34 parcels/$M)", "M01_R01<br>(12 parcels/$M)", "M03_R01<br>(16 parcels/$M)", "M02_R01<br>(14 parcels/$M)", "M01_R02<br>(18 parcels/$M)", "M03_R02<br>(23 parcels/$M)", "M02_R02<br>(20 parcels/$M)", "M01_R04<br>(21 parcels/$M)", "R01<br>(17 parcels/$M)", "R04<br>(25 parcels/$M)", "M03_R04<br>(23 parcels/$M)", "M02_R04<br>(22 parcels/$M)", "M01_W02<br>(27 parcels/$M)", "M02_W01<br>(24 parcels/$M)", "M01_W01<br>(25 parcels/$M)", "R02<br>(27 parcels/$M)", "W01<br>(27 parcels/$M)", "M03_W01<br>(30 parcels/$M)", "M01_R01_W01<br>(23 parcels/$M)", "M02_W02<br>(21 parcels/$M)", "M01_R01_W02<br>(20 parcels/$M)", "M02_R01_W02<br>(22 parcels/$M)", "M03_W02<br>(24 parcels/$M)", "M02_R01_W01<br>(21 parcels/$M)", "M01_R03<br>(25 parcels/$M)", "M03_R01_W01<br>(23 parcels/$M)", "R01_W01<br>(25 parcels/$M)", "M03_R01_W02<br>(22 parcels/$M)", "M03_R03<br>(25 parcels/$M)", "R01_W04<br>(22 parcels/$M)", "R01_W02<br>(22 parcels/$M)", "M02_R03<br>(23 parcels/$M)", "W02<br>(32 parcels/$M)", "R01_W05<br>(21 parcels/$M)", "W05<br>(23 parcels/$M)", "M03_R04_W01<br>(30 parcels/$M)", "M01_R04_W01<br>(28 parcels/$M)", "M01_W03<br>(20 parcels/$M)", "M02_R04_W01<br>(29 parcels/$M)", "M01_R04_W02<br>(28 parcels/$M)", "W04<br>(26 parcels/$M)", "M03_R04_W02<br>(29 parcels/$M)", "M01_R02_W01<br>(29 parcels/$M)", "R04_W01<br>(30 parcels/$M)", "M01_R02_W02<br>(27 parcels/$M)", "R03<br>(30 parcels/$M)", "R04_W02<br>(31 parcels/$M)", "M02_R04_W02<br>(25 parcels/$M)", "R04_W04<br>(25 parcels/$M)", "M03_R02_W01<br>(30 parcels/$M)", "M03_R02_W02<br>(29 parcels/$M)", "R04_W05<br>(26 parcels/$M)", "M01_R01_W03<br>(20 parcels/$M)", "M03_W03<br>(22 parcels/$M)", "M02_R02_W01<br>(25 parcels/$M)", "M01_W04<br>(24 parcels/$M)", "R02_W01<br>(32 parcels/$M)", "M02_R02_W02<br>(26 parcels/$M)", "M02_R01_W03<br>(17 parcels/$M)", "R02_W04<br>(30 parcels/$M)", "M01_R04_W03<br>(26 parcels/$M)", "M01_R01_W04<br>(22 parcels/$M)", "M01_R01_W05<br>(21 parcels/$M)", "M01_R04_W05<br>(29 parcels/$M)", "M02_W03<br>(18 parcels/$M)", "M03_R01_W03<br>(19 parcels/$M)", "M01_R04_W04<br>(27 parcels/$M)", "M02_R04_W03<br>(25 parcels/$M)", "M02_W04<br>(24 parcels/$M)", "M03_R04_W03<br>(26 parcels/$M)", "R02_W05<br>(27 parcels/$M)", "M01_W05<br>(24 parcels/$M)", "M02_R01_W04<br>(22 parcels/$M)", "M03_W04<br>(24 parcels/$M)", "R02_W02<br>(27 parcels/$M)", "M02_R04_W04<br>(28 parcels/$M)", "R04_W03<br>(26 parcels/$M)", "R01_W03<br>(20 parcels/$M)", "M03_R01_W04<br>(24 parcels/$M)", "M02_W05<br>(23 parcels/$M)", "M03_R04_W05<br>(29 parcels/$M)", "M03_R04_W04<br>(27 parcels/$M)", "W03<br>(27 parcels/$M)", "M03_R01_W05<br>(24 parcels/$M)", "M02_R04_W05<br>(28 parcels/$M)", "M01_R02_W04<br>(28 parcels/$M)", "M03_W05<br>(25 parcels/$M)", "M02_R01_W05<br>(24 parcels/$M)", "M01_R02_W03<br>(26 parcels/$M)", "M01_R02_W05<br>(30 parcels/$M)", "M02_R02_W03<br>(24 parcels/$M)", "M01_R03_W01<br>(31 parcels/$M)", "M02_R02_W04<br>(27 parcels/$M)", "M03_R02_W03<br>(27 parcels/$M)", "M03_R03_W02<br>(31 parcels/$M)", "M03_R02_W04<br>(29 parcels/$M)", "R02_W03<br>(29 parcels/$M)", "M03_R03_W01<br>(31 parcels/$M)", "M02_R02_W05<br>(29 parcels/$M)", "M03_R02_W05<br>(31 parcels/$M)", "M01_R03_W02<br>(29 parcels/$M)", "M02_R03_W01<br>(30 parcels/$M)", "R03_W05<br>(30 parcels/$M)", "R03_W04<br>(27 parcels/$M)", "M02_R03_W02<br>(28 parcels/$M)", "R03_W01<br>(33 parcels/$M)", "M01_R03_W03<br>(29 parcels/$M)", "R03_W02<br>(31 parcels/$M)", "M01_R03_W04<br>(29 parcels/$M)", "M03_R03_W03<br>(29 parcels/$M)", "M01_R03_W05<br>(31 parcels/$M)", "M02_R03_W03<br>(28 parcels/$M)", "M02_R03_W04<br>(28 parcels/$M)", "M02_R03_W05<br>(29 parcels/$M)", "M03_R03_W04<br>(30 parcels/$M)", "M03_R03_W05<br>(30 parcels/$M)", "R03_W03<br>(28 parcels/$M)"],
        "visible": true,
        "mode": "markers",
        "y": [165, 187, 452, 240, 381, 330, 629, 876, 777, 1223, 179, 1182, 1401, 1328, 1150, 1037, 1014, 698, 835, 1356, 1188, 976, 1071, 1264, 1115, 1136, 1402, 1262, 1065, 1268, 1512, 1238, 958, 1354, 1136, 1224, 1166, 2760, 2476, 1063, 2619, 2528, 1281, 2733, 1965, 2337, 1851, 1374, 2493, 2347, 2380, 2112, 2070, 2487, 1245, 1264, 1756, 1343, 1802, 1825, 1141, 2138, 2556, 1498, 1449, 3053, 989, 1311, 2798, 2548, 1395, 2677, 1959, 1361, 1534, 1459, 1602, 2924, 2353, 1081, 1698, 1393, 3154, 2873, 1243, 1745, 3006, 2310, 1509, 1730, 2047, 2459, 1956, 2749, 2258, 2181, 2857, 2452, 2027, 2833, 2484, 2646, 2562, 2750, 2807, 2542, 2605, 2574, 2846, 2467, 2956, 2972, 3239, 2832, 2914, 3064, 3132, 3232, 2533],
        "x": [9.65, 12.55, 13.27, 20.49, 24.11, 23.38, 35.27, 38.89, 38.16, 56.9, 10.84, 47.25, 60.52, 59.8, 42.55, 43.98, 41.09, 25.62, 31.43, 44.71, 51.92, 45.45, 53.39, 56.28, 46.17, 54.82, 56.13, 55.54, 42.27, 57.01, 59.75, 57.18, 43.74, 59.02, 35.62, 58.1, 49.98, 91.95, 88.33, 52.88, 91.23, 89.8, 49.06, 93.42, 66.7, 78.68, 68.17, 46.48, 80.15, 92.7, 93.59, 70.32, 71.79, 94.51, 63.71, 56.5, 69.6, 55.99, 57.05, 71.06, 66.61, 71.96, 100.12, 66.83, 67.75, 104.16, 55.77, 67.33, 103.24, 103.02, 58.89, 103.74, 72.88, 56.91, 69.73, 59.62, 58.52, 106.14, 90.47, 54.06, 70.45, 59.81, 107.78, 106.86, 45.94, 71.37, 107.06, 81.61, 60.53, 70.64, 78.49, 82.53, 81.39, 87.56, 84.51, 82.11, 92.65, 85.23, 68.84, 91.18, 85.42, 86.15, 89.03, 90.46, 93.74, 92.82, 91.92, 77.91, 99.35, 79.38, 102.47, 102.97, 103.39, 102.25, 105.37, 106.28, 106.09, 107.01, 89.7],
        "line": {
            "width": 2,
            "shape": "hv"
        },
        "type": "scatter",
        "marker": {
            "symbol": "circle-open"
        }
    }, {
        "name": "Most Efficient",
        "text": ["W01<br>$835.0M for 835 parcels<br>(26 parcels/$M)", "W02<br>$4.2M for 301 parcels<br>(71 parcels/$M)", "W03<br>$10.3M for 107 parcels<br>(10 parcels/$M)", "W04<br>$3.1M for 38 parcels<br>(12 parcels/$M)", "M01_W04<br>$6.9M for 62 parcels<br>(8 parcels/$M)", "M01_W05<br>$0.9M for 18 parcels<br>(19 parcels/$M)", "M02_W05<br>$2.9M for 32 parcels<br>(11 parcels/$M)", "M03_W05<br>$0.7M for 116 parcels<br>(161 parcels/$M)", "M03_R01_W05<br>$10.8M for 236 parcels<br>(21 parcels/$M)", "M03_R02_W05<br>$14.8M for 901 parcels<br>(60 parcels/$M)", "M03_R03_W05<br>$20.9M for 586 parcels<br>(28 parcels/$M)", "M03_R04_W05<br>$0.8M for -78 parcels<br>(-101 parcels/$M)"],
        "visible": true,
        "mode": "lines+markers",
        "y": [835.0, 1136.0, 1243.0, 1281.0, 1343.0, 1361.0, 1393.0, 1509.0, 1745.0, 2646.0, 3232.0, 3154.0],
        "x": [31.43, 35.62, 45.94, 49.06, 55.99, 56.91, 59.81, 60.53, 71.37, 86.15, 107.01, 107.78],
        "line": {
            "width": 2,
            "shape": "hv"
        },
        "type": "scatter",
        "marker": {
            "symbol": "circle"
        }
    }, {
        "name": "Oregon Start",
        "text": ["R01<br>$10.8M for 179 parcels<br>(16 parcels/$M)", "R02<br>$14.8M for 519 parcels<br>(35 parcels/$M)", "R02_W01<br>$31.4M for 1104 parcels<br>(35 parcels/$M)", "R03_W01<br>$20.9M for 772 parcels<br>(37 parcels/$M)", "M01_R03_W01<br>$9.7M for 175 parcels<br>(18 parcels/$M)", "M02_R03_W01<br>$2.9M for 1 parcels<br>(0 parcels/$M)", "M03_R03_W01<br>$0.7M for 83 parcels<br>(115 parcels/$M)", "M03_R03_W02<br>$1.5M for 24 parcels<br>(16 parcels/$M)", "M03_R03_W03<br>$10.3M for 115 parcels<br>(11 parcels/$M)", "M03_R03_W04<br>$3.1M for 160 parcels<br>(51 parcels/$M)", "M03_R03_W05<br>$0.9M for 100 parcels<br>(108 parcels/$M)", "M03_R04_W05<br>$0.8M for -78 parcels<br>(-101 parcels/$M)"],
        "visible": true,
        "mode": "lines+markers",
        "y": [179.0, 698.0, 1802.0, 2574.0, 2749.0, 2750.0, 2833.0, 2857.0, 2972.0, 3132.0, 3232.0, 3154.0],
        "x": [10.84, 25.62, 57.05, 77.91, 87.56, 90.46, 91.18, 92.65, 102.97, 106.09, 107.01, 107.78],
        "line": {
            "width": 2,
            "shape": "hv"
        },
        "type": "scatter",
        "marker": {
            "symbol": "circle"
        }
    }, {
        "name": "Weccacoe Start",
        "text": ["W01<br>$31.4M for 835 parcels<br>(26 parcels/$M)", "W02<br>$4.2M for 301 parcels<br>(71 parcels/$M)", "W03<br>$10.3M for 107 parcels<br>(10 parcels/$M)", "W04<br>$3.1M for 38 parcels<br>(12 parcels/$M)", "M01_W04<br>$6.9M for 62 parcels<br>(8 parcels/$M)", "M01_W05<br>$0.9M for 18 parcels<br>(19 parcels/$M)", "M02_W05<br>$2.9M for 32 parcels<br>(11 parcels/$M)", "M03_W05<br>$0.7M for 116 parcels<br>(161 parcels/$M)", "M03_R01_W05<br>$10.8M for 236 parcels<br>(21 parcels/$M)", "M03_R02_W05<br>$14.8M for 901 parcels<br>(60 parcels/$M)", "M03_R03_W05<br>$20.9M for 586 parcels<br>(28 parcels/$M)", "M03_R04_W05<br>$0.8M for -78 parcels<br>(-101 parcels/$M)"],
        "visible": true,
        "mode": "lines+markers",
        "y": [835.0, 1136.0, 1243.0, 1281.0, 1343.0, 1361.0, 1393.0, 1509.0, 1745.0, 2646.0, 3232.0, 3154.0],
        "x": [31.43, 35.62, 45.94, 49.06, 55.99, 56.91, 59.81, 60.53, 71.37, 86.15, 107.01, 107.78],
        "line": {
            "width": 2,
            "shape": "hv"
        },
        "type": "scatter",
        "marker": {
            "symbol": "circle"
        }
    }, {
        "name": "Mifflin Start",
        "text": ["M01<br>$9.7M for 165 parcels<br>(17 parcels/$M)", "M01_W01<br>$31.4M for 849 parcels<br>(27 parcels/$M)", "M01_W02<br>$1.5M for 136 parcels<br>(93 parcels/$M)", "M01_R01_W02<br>$10.8M for -79 parcels<br>(-7 parcels/$M)", "M02_R01_W02<br>$2.9M for 193 parcels<br>(66 parcels/$M)", "M02_R02_W02<br>$14.8M for 561 parcels<br>(37 parcels/$M)", "M03_R02_W02<br>$0.7M for 245 parcels<br>(335 parcels/$M)", "M03_R03_W02<br>$20.9M for 787 parcels<br>(37 parcels/$M)", "M03_R03_W03<br>$10.3M for 115 parcels<br>(11 parcels/$M)", "M03_R03_W04<br>$3.1M for 160 parcels<br>(51 parcels/$M)", "M03_R03_W05<br>$0.9M for 100 parcels<br>(108 parcels/$M)", "M03_R04_W05<br>$0.8M for -78 parcels<br>(-101 parcels/$M)"],
        "visible": true,
        "mode": "lines+markers",
        "y": [165.0, 1014.0, 1150.0, 1071.0, 1264.0, 1825.0, 2070.0, 2857.0, 2972.0, 3132.0, 3232.0, 3154.0],
        "x": [9.65, 41.09, 42.55, 53.39, 56.28, 71.06, 71.79, 92.65, 102.97, 106.09, 107.01, 107.78],
        "line": {
            "width": 2,
            "shape": "hv"
        },
        "type": "scatter",
        "marker": {
            "symbol": "circle"
        }
    }, {
        "name": "Oregon-Favored",
        "text": ["R01<br>$10.8M for 179 parcels<br>(16 parcels/$M)", "R02<br>$14.8M for 519 parcels<br>(35 parcels/$M)", "R03<br>$20.9M for 676 parcels<br>(32 parcels/$M)", "R03_W01<br>$31.4M for 1200 parcels<br>(38 parcels/$M)", "M01_R03_W01<br>$9.7M for 175 parcels<br>(18 parcels/$M)", "M02_R03_W01<br>$2.9M for 1 parcels<br>(0 parcels/$M)", "M03_R03_W01<br>$0.7M for 83 parcels<br>(115 parcels/$M)", "M03_R03_W02<br>$1.5M for 24 parcels<br>(16 parcels/$M)", "M03_R03_W03<br>$10.3M for 115 parcels<br>(11 parcels/$M)", "M03_R03_W04<br>$3.1M for 160 parcels<br>(51 parcels/$M)", "M03_R03_W05<br>$0.9M for 100 parcels<br>(108 parcels/$M)", "M03_R04_W05<br>$0.8M for -78 parcels<br>(-101 parcels/$M)"],
        "visible": true,
        "mode": "lines+markers",
        "y": [179.0, 698.0, 1374.0, 2574.0, 2749.0, 2750.0, 2833.0, 2857.0, 2972.0, 3132.0, 3232.0, 3154.0],
        "x": [10.84, 25.62, 46.48, 77.91, 87.56, 90.46, 91.18, 92.65, 102.97, 106.09, 107.01, 107.78],
        "line": {
            "width": 2,
            "shape": "hv"
        },
        "type": "scatter",
        "marker": {
            "symbol": "circle"
        }
    }, {
        "name": "Mifflin-Favored",
        "text": ["M01<br>$9.7M for 165 parcels<br>(17 parcels/$M)", "M02<br>$2.9M for 22 parcels<br>(7 parcels/$M)", "M03<br>$0.7M for 265 parcels<br>(368 parcels/$M)", "M03_R01<br>$10.8M for -71 parcels<br>(-6 parcels/$M)", "M03_R02<br>$14.8M for 495 parcels<br>(33 parcels/$M)", "M03_R03<br>$20.9M for 636 parcels<br>(30 parcels/$M)", "M03_R03_W01<br>$31.4M for 1321 parcels<br>(42 parcels/$M)", "M03_R03_W02<br>$1.5M for 24 parcels<br>(16 parcels/$M)", "M03_R03_W03<br>$10.3M for 115 parcels<br>(11 parcels/$M)", "M03_R03_W04<br>$3.1M for 160 parcels<br>(51 parcels/$M)", "M03_R03_W05<br>$0.9M for 100 parcels<br>(108 parcels/$M)", "M03_R04_W05<br>$0.8M for -78 parcels<br>(-101 parcels/$M)"],
        "visible": true,
        "mode": "lines+markers",
        "y": [165.0, 187.0, 452.0, 381.0, 876.0, 1512.0, 2833.0, 2857.0, 2972.0, 3132.0, 3232.0, 3154.0],
        "x": [9.65, 12.55, 13.27, 24.11, 38.89, 59.75, 91.18, 92.65, 102.97, 106.09, 107.01, 107.78],
        "line": {
            "width": 2,
            "shape": "hv"
        },
        "type": "scatter",
        "marker": {
            "symbol": "circle"
        }
    }], {
        "title": "Example Flood Relief Program: Implementation Sequences with Parcel-level Flood Risk Elimination per Cost",
        "plot_bgcolor": "E5E5E5",
        "yaxis": {
            "title": "Parcels with Flood Risk Eliminated"
        },
        "xaxis": {
            "tickprefix": "$",
            "title": "Capital Cost (Millions)"
        },
        "hovermode": "closest",
        "legend": {
            "y": 0.9,
            "x": 0.05
        }
    }, {
        "linkText": "Export to plot.ly",
        "showLink": true
    })
</script>

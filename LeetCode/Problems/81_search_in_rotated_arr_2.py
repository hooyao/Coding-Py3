import sys


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return self.unordered_bsearch(nums, target)

    def ordered_bsearch(self, nums, target):
        left, right = 0, len(nums) - 1
        if target > nums[-1] or target < nums[0]:
            return False
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def unordered_bsearch(self, nums, target):
        if len(nums) == 0:
            return False
        found = False
        left, right = 0, len(nums) - 1
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        if nums[left] == nums[mid]:
            left += 1
            found = self.unordered_bsearch(nums[left:right + 1], target)
        elif nums[right] == nums[mid]:
            right -= 1
            found = self.unordered_bsearch(nums[left:right + 1], target)
        elif nums[mid] < nums[left]:  # left side of mid is unordered, right side is ordered
            if nums[mid] < target <= nums[-1]:
                found = self.ordered_bsearch(nums[mid + 1:], target)
            else:
                found = self.unordered_bsearch(nums[0:mid], target)
        else:  # left side of mid is ordered, right side is unordered
            if nums[0] <= target < nums[mid]:
                found = self.ordered_bsearch(nums[0:mid], target)
            else:
                found = self.unordered_bsearch(nums[mid + 1:], target)
        return found


def main(*args):
    solution = Solution()
    num1 = [-3596, -3593, -3589, -3588, -3588, -3583, -3578, -3577, -3576, -3576, -3574, -3568, -3567, -3565, -3563,
            -3560, -3559, -3558, -3558, -3556, -3551, -3551, -3549, -3549, -3546, -3545, -3545, -3545, -3544, -3542,
            -3542, -3542, -3539, -3539, -3538, -3533, -3531, -3519, -3518, -3518, -3515, -3511, -3511, -3511, -3507,
            -3505, -3504, -3504, -3503, -3501, -3490, -3484, -3478, -3478, -3478, -3478, -3476, -3474, -3474, -3473,
            -3471, -3470, -3469, -3468, -3464, -3464, -3462, -3460, -3453, -3450, -3449, -3445, -3437, -3435, -3434,
            -3431, -3430, -3426, -3424, -3413, -3413, -3412, -3403, -3400, -3400, -3400, -3397, -3396, -3392, -3389,
            -3389, -3388, -3388, -3386, -3384, -3382, -3380, -3379, -3379, -3379, -3377, -3376, -3375, -3374, -3374,
            -3373, -3371, -3370, -3369, -3369, -3367, -3367, -3367, -3366, -3365, -3363, -3361, -3360, -3360, -3359,
            -3357, -3356, -3356, -3356, -3355, -3352, -3351, -3351, -3350, -3345, -3345, -3344, -3341, -3339, -3336,
            -3332, -3331, -3327, -3327, -3325, -3325, -3323, -3298, -3296, -3292, -3290, -3290, -3287, -3287, -3286,
            -3285, -3285, -3281, -3275, -3275, -3273, -3267, -3266, -3266, -3265, -3258, -3257, -3256, -3253, -3251,
            -3246, -3244, -3243, -3238, -3232, -3227, -3227, -3227, -3220, -3218, -3217, -3215, -3214, -3211, -3205,
            -3203, -3203, -3198, -3198, -3186, -3185, -3174, -3172, -3172, -3168, -3159, -3158, -3156, -3154, -3153,
            -3152, -3149, -3147, -3139, -3139, -3139, -3136, -3136, -3127, -3125, -3123, -3120, -3109, -3107, -3101,
            -3099, -3091, -3088, -3087, -3085, -3082, -3077, -3076, -3075, -3072, -3071, -3070, -3067, -3066, -3056,
            -3051, -3050, -3043, -3040, -3039, -3037, -3036, -3034, -3034, -3031, -3028, -3025, -3022, -3022, -3019,
            -3019, -3018, -3016, -3014, -3010, -3008, -3007, -3006, -3000, -2992, -2990, -2989, -2988, -2988, -2983,
            -2978, -2975, -2972, -2968, -2967, -2965, -2952, -2951, -2950, -2948, -2948, -2947, -2937, -2936, -2934,
            -2933, -2933, -2930, -2928, -2923, -2919, -2919, -2918, -2917, -2915, -2915, -2911, -2911, -2910, -2907,
            -2903, -2900, -2900, -2897, -2891, -2891, -2886, -2884, -2883, -2883, -2880, -2877, -2870, -2866, -2859,
            -2857, -2850, -2843, -2840, -2839, -2839, -2835, -2835, -2834, -2831, -2828, -2826, -2825, -2825, -2824,
            -2823, -2820, -2818, -2818, -2817, -2813, -2809, -2807, -2806, -2806, -2803, -2803, -2802, -2801, -2800,
            -2797, -2796, -2794, -2792, -2790, -2787, -2787, -2786, -2777, -2776, -2772, -2772, -2771, -2770, -2755,
            -2752, -2751, -2749, -2749, -2747, -2747, -2747, -2746, -2744, -2742, -2741, -2739, -2736, -2731, -2725,
            -2719, -2717, -2717, -2715, -2711, -2710, -2705, -2703, -2702, -2702, -2702, -2696, -2694, -2693, -2688,
            -2687, -2686, -2683, -2683, -2683, -2683, -2678, -2677, -2677, -2676, -2674, -2673, -2669, -2658, -2657,
            -2656, -2652, -2645, -2643, -2643, -2640, -2638, -2635, -2632, -2631, -2631, -2630, -2630, -2629, -2625,
            -2622, -2619, -2617, -2615, -2612, -2608, -2606, -2604, -2601, -2597, -2594, -2593, -2588, -2583, -2583,
            -2583, -2580, -2576, -2570, -2569, -2568, -2568, -2565, -2563, -2560, -2554, -2553, -2551, -2548, -2545,
            -2544, -2540, -2537, -2536, -2535, -2534, -2529, -2518, -2513, -2511, -2509, -2508, -2504, -2504, -2502,
            -2494, -2493, -2490, -2489, -2487, -2485, -2480, -2479, -2479, -2477, -2476, -2475, -2472, -2472, -2471,
            -2465, -2461, -2458, -2458, -2456, -2454, -2453, -2452, -2449, -2444, -2440, -2436, -2435, -2434, -2432,
            -2429, -2423, -2422, -2421, -2421, -2419, -2418, -2415, -2410, -2406, -2400, -2399, -2393, -2391, -2389,
            -2388, -2388, -2387, -2384, -2380, -2380, -2379, -2378, -2377, -2376, -2375, -2370, -2370, -2368, -2366,
            -2363, -2361, -2360, -2356, -2354, -2349, -2348, -2346, -2345, -2343, -2342, -2342, -2336, -2334, -2330,
            -2329, -2327, -2325, -2324, -2323, -2321, -2320, -2313, -2309, -2306, -2306, -2305, -2304, -2296, -2293,
            -2291, -2286, -2283, -2281, -2274, -2274, -2267, -2263, -2260, -2258, -2255, -2253, -2252, -2251, -2249,
            -2248, -2246, -2243, -2241, -2238, -2237, -2236, -2234, -2234, -2233, -2229, -2225, -2224, -2224, -2219,
            -2216, -2211, -2205, -2204, -2199, -2192, -2192, -2190, -2189, -2189, -2188, -2184, -2179, -2176, -2168,
            -2159, -2157, -2156, -2151, -2149, -2146, -2146, -2146, -2140, -2134, -2128, -2128, -2125, -2124, -2122,
            -2118, -2116, -2114, -2111, -2108, -2102, -2101, -2100, -2095, -2092, -2088, -2084, -2082, -2081, -2081,
            -2075, -2074, -2069, -2067, -2062, -2062, -2059, -2059, -2058, -2056, -2054, -2050, -2047, -2045, -2043,
            -2033, -2032, -2032, -2031, -2028, -2022, -2018, -2018, -2017, -2016, -2014, -2014, -2013, -2010, -2008,
            -2006, -2006, -1987, -1980, -1979, -1973, -1966, -1963, -1963, -1958, -1957, -1956, -1954, -1949, -1946,
            -1941, -1939, -1939, -1938, -1937, -1936, -1936, -1935, -1931, -1930, -1929, -1925, -1923, -1913, -1910,
            -1908, -1903, -1901, -1900, -1900, -1898, -1896, -1894, -1893, -1893, -1891, -1888, -1888, -1886, -1883,
            -1882, -1877, -1874, -1873, -1872, -1872, -1870, -1869, -1860, -1857, -1856, -1855, -1854, -1851, -1850,
            -1849, -1848, -1845, -1842, -1839, -1831, -1825, -1822, -1816, -1816, -1815, -1813, -1807, -1806, -1806,
            -1802, -1800, -1799, -1794, -1792, -1790, -1785, -1783, -1778, -1777, -1775, -1772, -1772, -1762, -1752,
            -1752, -1751, -1751, -1751, -1750, -1748, -1748, -1745, -1744, -1741, -1739, -1738, -1738, -1734, -1734,
            -1732, -1732, -1729, -1720, -1718, -1717, -1714, -1712, -1699, -1697, -1694, -1686, -1685, -1680, -1680,
            -1676, -1676, -1672, -1671, -1670, -1669, -1669, -1667, -1665, -1665, -1661, -1652, -1650, -1650, -1650,
            -1643, -1641, -1637, -1635, -1634, -1633, -1630, -1629, -1624, -1622, -1620, -1620, -1618, -1617, -1616,
            -1611, -1608, -1605, -1601, -1598, -1597, -1592, -1591, -1590, -1585, -1583, -1579, -1576, -1572, -1571,
            -1571, -1567, -1566, -1565, -1565, -1565, -1563, -1560, -1560, -1553, -1552, -1546, -1546, -1546, -1546,
            -1545, -1545, -1543, -1542, -1539, -1539, -1538, -1532, -1528, -1527, -1526, -1525, -1518, -1518, -1517,
            -1515, -1515, -1514, -1506, -1505, -1502, -1502, -1497, -1492, -1488, -1472, -1468, -1464, -1463, -1461,
            -1461, -1457, -1456, -1455, -1445, -1444, -1444, -1443, -1442, -1441, -1441, -1441, -1441, -1435, -1434,
            -1431, -1430, -1423, -1421, -1420, -1419, -1415, -1409, -1400, -1396, -1396, -1390, -1388, -1383, -1382,
            -1380, -1380, -1379, -1375, -1374, -1374, -1372, -1371, -1369, -1362, -1361, -1360, -1360, -1358, -1358,
            -1352, -1351, -1350, -1347, -1346, -1338, -1335, -1335, -1332, -1330, -1330, -1327, -1325, -1324, -1320,
            -1316, -1310, -1307, -1301, -1301, -1299, -1299, -1299, -1296, -1295, -1291, -1286, -1285, -1282, -1281,
            -1280, -1275, -1268, -1268, -1267, -1260, -1259, -1259, -1257, -1256, -1253, -1251, -1248, -1248, -1248,
            -1245, -1244, -1233, -1233, -1232, -1220, -1215, -1214, -1213, -1213, -1212, -1210, -1205, -1204, -1199,
            -1199, -1196, -1195, -1191, -1191, -1190, -1187, -1184, -1182, -1179, -1177, -1173, -1172, -1172, -1167,
            -1166, -1165, -1162, -1161, -1161, -1160, -1155, -1150, -1148, -1146, -1142, -1141, -1140, -1139, -1139,
            -1136, -1132, -1132, -1128, -1113, -1112, -1109, -1109, -1109, -1103, -1102, -1100, -1092, -1091, -1086,
            -1085, -1081, -1075, -1074, -1070, -1068, -1065, -1064, -1061, -1058, -1055, -1055, -1053, -1052, -1047,
            -1045, -1044, -1044, -1043, -1039, -1037, -1037, -1033, -1032, -1031, -1031, -1030, -1027, -1020, -1020,
            -1015, -1009, -1008, -1007, -1007, -1006, -1003, -1000, -999, -999, -998, -998, -997, -992, -991, -991,
            -986, -986, -984, -980, -980, -980, -977, -975, -972, -968, -963, -959, -958, -957, -952, -952, -950, -949,
            -945, -945, -944, -942, -932, -932, -926, -921, -920, -919, -919, -914, -913, -913, -906, -906, -906, -904,
            -902, -902, -901, -901, -896, -895, -895, -893, -892, -877, -872, -871, -869, -869, -868, -866, -866, -864,
            -854, -852, -852, -851, -850, -847, -846, -841, -838, -837, -834, -833, -833, -831, -829, -827, -823, -822,
            -822, -821, -809, -806, -805, -805, -805, -804, -801, -798, -794, -789, -787, -780, -780, -776, -775, -774,
            -773, -773, -772, -771, -768, -768, -755, -754, -752, -750, -750, -747, -741, -739, -735, -732, -719, -718,
            -712, -710, -709, -708, -704, -703, -699, -698, -697, -691, -682, -670, -665, -664, -663, -658, -654, -653,
            -649, -643, -642, -639, -639, -639, -637, -634, -632, -630, -628, -624, -623, -618, -617, -615, -615, -614,
            -612, -612, -609, -609, -609, -606, -601, -601, -601, -600, -599, -593, -591, -591, -587, -583, -582, -582,
            -582, -581, -581, -576, -575, -573, -572, -568, -567, -564, -564, -558, -555, -554, -553, -551, -549, -549,
            -548, -544, -538, -532, -525, -521, -511, -510, -507, -505, -502, -497, -496, -496, -493, -490, -489, -485,
            -481, -481, -479, -478, -474, -473, -469, -467, -464, -464, -461, -459, -458, -457, -454, -452, -449, -449,
            -448, -447, -447, -445, -439, -434, -434, -434, -430, -427, -425, -423, -416, -415, -414, -412, -410, -408,
            -404, -401, -396, -392, -390, -389, -384, -383, -381, -380, -379, -376, -376, -371, -370, -368, -367, -364,
            -362, -362, -355, -353, -352, -346, -344, -343, -343, -341, -341, -341, -340, -340, -338, -334, -334, -327,
            -326, -325, -324, -324, -323, -321, -321, -317, -316, -315, -315, -308, -305, -303, -302, -302, -297, -297,
            -297, -295, -288, -286, -282, -281, -281, -277, -273, -271, -271, -271, -270, -267, -266, -265, -265, -265,
            -262, -258, -258, -258, -254, -253, -247, -245, -240, -235, -223, -220, -217, -214, -214, -209, -208, -201,
            -201, -201, -201, -200, -198, -196, -191, -187, -185, -183, -183, -183, -180, -175, -174, -173, -170, -160,
            -159, -151, -151, -148, -148, -147, -146, -144, -143, -141, -136, -133, -122, -121, -120, -118, -111, -108,
            -107, -99, -94, -83, -78, -77, -76, -75, -73, -72, -72, -68, -68, -67, -66, -61, -61, -60, -59, -56, -54,
            -54, -51, -48, -42, -41, -38, -38, -38, -37, -37, -36, -36, -33, -30, -28, -28, -28, -26, -25, -18, -17, -7,
            -7, -5, -3, 2, 5, 6, 8, 9, 11, 15, 17, 19, 20, 20, 25, 27, 27, 29, 30, 32, 32, 33, 34, 35, 47, 48, 49, 52,
            53, 66, 66, 67, 72, 74, 81, 86, 88, 90, 92, 94, 95, 95, 98, 102, 107, 109, 110, 111, 114, 118, 118, 124,
            126, 127, 128, 129, 130, 135, 136, 138, 138, 140, 141, 146, 149, 151, 152, 153, 158, 159, 164, 167, 170,
            177, 182, 183, 184, 184, 185, 189, 190, 191, 199, 200, 210, 211, 214, 217, 221, 226, 227, 228, 230, 232,
            233, 234, 239, 241, 248, 250, 253, 254, 257, 261, 262, 263, 263, 264, 267, 269, 269, 272, 275, 283, 284,
            287, 287, 289, 290, 291, 291, 293, 294, 297, 297, 300, 302, 303, 312, 317, 318, 321, 321, 322, 326, 326,
            330, 337, 339, 340, 342, 342, 343, 344, 353, 358, 367, 368, 370, 370, 371, 373, 374, 374, 376, 379, 380,
            381, 382, 383, 387, 393, 394, 404, 407, 413, 415, 419, 422, 422, 424, 430, 435, 436, 436, 441, 442, 444,
            447, 449, 450, 452, 456, 456, 459, 469, 469, 470, 471, 474, 476, 479, 482, 483, 484, 487, 490, 493, 494,
            494, 495, 502, 503, 506, 512, 512, 517, 520, 520, 524, 526, 531, 531, 538, 543, 546, 546, 546, 548, 551,
            552, 553, 561, 562, 563, 564, 566, 567, 571, 571, 577, 580, 583, 590, 590, 592, 594, 597, 599, 602, 604,
            609, 612, 613, 614, 615, 621, 623, 623, 625, 626, 627, 632, 632, 634, 637, 638, 640, 642, 651, 653, 657,
            659, 665, 668, 668, 668, 670, 672, 673, 676, 679, 682, 685, 685, 687, 690, 695, 697, 701, 703, 708, 709,
            709, 711, 712, 713, 731, 734, 735, 735, 735, 736, 738, 739, 745, 746, 750, 753, 755, 756, 756, 757, 761,
            764, 770, 774, 775, 776, 777, 788, 789, 789, 791, 792, 797, 801, 802, 806, 807, 808, 810, 811, 812, 812,
            816, 817, 818, 818, 818, 820, 824, 824, 827, 829, 833, 836, 836, 838, 842, 842, 845, 850, 855, 858, 859,
            859, 859, 859, 861, 861, 864, 865, 869, 871, 873, 874, 876, 877, 878, 880, 881, 883, 885, 887, 891, 891,
            895, 896, 897, 898, 901, 903, 904, 904, 907, 908, 910, 911, 913, 914, 914, 915, 924, 926, 933, 933, 934,
            938, 938, 939, 947, 948, 950, 950, 951, 965, 974, 975, 980, 981, 982, 982, 987, 988, 990, 995, 997, 997,
            999, 1001, 1001, 1003, 1004, 1008, 1009, 1009, 1011, 1011, 1011, 1013, 1016, 1016, 1018, 1019, 1019, 1025,
            1026, 1030, 1033, 1036, 1037, 1041, 1044, 1045, 1045, 1046, 1047, 1049, 1050, 1051, 1052, 1055, 1057, 1058,
            1065, 1067, 1067, 1070, 1076, 1078, 1079, 1080, 1080, 1085, 1087, 1089, 1091, 1096, 1102, 1103, 1108, 1119,
            1121, 1121, 1123, 1125, 1130, 1130, 1133, 1133, 1133, 1134, 1139, 1141, 1147, 1156, 1159, 1159, 1160, 1162,
            1167, 1173, 1176, 1177, 1185, 1192, 1192, 1194, 1198, 1201, 1205, 1206, 1206, 1217, 1217, 1219, 1219, 1219,
            1221, 1222, 1222, 1227, 1237, 1240, 1243, 1245, 1246, 1247, 1248, 1253, 1254, 1257, 1264, 1265, 1270, 1283,
            1285, 1286, 1288, 1293, 1294, 1297, 1298, 1303, 1305, 1306, 1312, 1314, 1315, 1317, 1323, 1326, 1328, 1338,
            1339, 1339, 1339, 1344, 1345, 1347, 1348, 1350, 1358, 1359, 1359, 1360, 1364, 1365, 1369, 1370, 1371, 1376,
            1379, 1383, 1384, 1387, 1389, 1391, 1394, 1395, 1396, 1399, 1400, 1402, 1403, 1404, 1404, 1406, 1406, 1407,
            1409, 1410, 1418, 1418, 1425, 1438, 1439, 1444, 1445, 1448, 1454, 1455, 1457, 1457, 1457, 1458, 1459, 1460,
            1472, 1474, 1475, 1476, 1478, 1489, 1491, 1491, 1494, 1495, 1496, 1497, 1498, 1501, 1502, 1506, 1506, 1509,
            1511, 1511, 1516, 1521, 1521, 1521, 1522, 1525, 1526, 1532, 1533, 1537, 1540, 1541, 1541, 1542, 1543, 1552,
            1553, 1554, 1554, 1555, 1557, 1566, 1567, 1567, 1570, 1570, 1570, 1575, 1575, 1580, 1584, 1585, 1587, 1587,
            1589, 1593, 1594, 1597, 1598, 1604, 1607, 1607, 1608, 1608, 1611, 1612, 1615, 1618, 1618, 1619, 1620, 1620,
            1622, 1624, 1627, 1631, 1632, 1633, 1638, 1639, 1646, 1647, 1648, 1648, 1649, 1650, 1651, 1652, 1658, 1660,
            1661, 1663, 1666, 1668, 1668, 1669, 1669, 1676, 1677, 1678, 1685, 1687, 1690, 1690, 1693, 1704, 1704, 1707,
            1709, 1709, 1714, 1718, 1718, 1718, 1720, 1722, 1722, 1723, 1728, 1734, 1736, 1737, 1743, 1744, 1746, 1750,
            1757, 1759, 1760, 1761, 1767, 1771, 1774, 1776, 1780, 1780, 1781, 1783, 1784, 1788, 1790, 1793, 1799, 1800,
            1803, 1807, 1807, 1813, 1816, 1819, 1822, 1828, 1833, 1837, 1838, 1838, 1847, 1848, 1850, 1856, 1858, 1859,
            1869, 1874, 1878, 1880, 1885, 1887, 1891, 1891, 1892, 1894, 1894, 1894, 1896, 1901, 1904, 1906, 1910, 1910,
            1920, 1921, 1922, 1923, 1923, 1926, 1926, 1927, 1930, 1931, 1931, 1931, 1933, 1934, 1936, 1941, 1944, 1946,
            1947, 1950, 1950, 1956, 1956, 1956, 1960, 1961, 1961, 1962, 1972, 1972, 1979, 1984, 1985, 1993, 1997, 1999,
            2000, 2003, 2009, 2009, 2019, 2019, 2020, 2022, 2024, 2025, 2036, 2037, 2039, 2040, 2045, 2046, 2046, 2046,
            2052, 2053, 2055, 2056, 2056, 2056, 2057, 2059, 2062, 2070, 2071, 2074, 2076, 2076, 2078, 2079, 2079, 2082,
            2083, 2083, 2083, 2085, 2085, 2086, 2093, 2097, 2097, 2098, 2098, 2099, 2100, 2101, 2102, 2105, 2105, 2110,
            2112, 2113, 2121, 2128, 2136, 2138, 2139, 2139, 2144, 2144, 2145, 2147, 2149, 2151, 2151, 2152, 2156, 2157,
            2158, 2158, 2161, 2163, 2166, 2170, 2174, 2176, 2180, 2180, 2185, 2204, 2213, 2217, 2218, 2219, 2221, 2221,
            2221, 2223, 2224, 2228, 2231, 2233, 2236, 2237, 2244, 2247, 2251, 2252, 2253, 2254, 2257, 2258, 2260, 2264,
            2268, 2269, 2269, 2274, 2276, 2277, 2278, 2280, 2280, 2282, 2282, 2285, 2298, 2302, 2303, 2306, 2307, 2316,
            2317, 2320, 2324, 2330, 2332, 2335, 2340, 2343, 2343, 2345, 2346, 2347, 2350, 2354, 2357, 2357, 2360, 2365,
            2372, 2376, 2379, 2389, 2391, 2392, 2393, 2397, 2403, 2410, 2412, 2413, 2414, 2417, 2419, 2421, 2422, 2428,
            2428, 2428, 2429, 2429, 2432, 2439, 2439, 2442, 2447, 2450, 2452, 2458, 2461, 2463, 2465, 2466, 2467, 2469,
            2470, 2472, 2472, 2474, 2477, 2485, 2486, 2493, 2498, 2500, 2501, 2506, 2506, 2509, 2515, 2519, 2520, 2521,
            2531, 2531, 2535, 2538, 2542, 2544, 2545, 2549, 2557, 2558, 2559, 2560, 2563, 2564, 2566, 2569, 2571, 2571,
            2572, 2572, 2574, 2587, 2590, 2596, 2596, 2598, 2598, 2603, 2604, 2607, 2610, 2610, 2617, 2623, 2626, 2626,
            2627, 2629, 2631, 2632, 2633, 2635, 2636, 2637, 2638, 2638, 2638, 2639, 2645, 2646, 2648, 2651, 2658, 2661,
            2661, 2663, 2669, 2669, 2670, 2673, 2673, 2676, 2677, 2682, 2684, 2692, 2693, 2693, 2695, 2695, 2696, 2696,
            2697, 2698, 2702, 2703, 2704, 2707, 2708, 2709, 2711, 2716, 2722, 2722, 2724, 2725, 2727, 2732, 2733, 2742,
            2751, 2753, 2753, 2757, 2757, 2762, 2762, 2762, 2766, 2771, 2778, 2779, 2780, 2781, 2781, 2787, 2790, 2791,
            2796, 2796, 2799, 2800, 2802, 2810, 2810, 2811, 2812, 2815, 2823, 2829, 2835, 2835, 2838, 2838, 2840, 2844,
            2846, 2846, 2846, 2847, 2847, 2848, 2850, 2856, 2856, 2857, 2857, 2857, 2857, 2859, 2864, 2866, 2870, 2871,
            2874, 2876, 2877, 2879, 2883, 2891, 2893, 2893, 2898, 2898, 2903, 2904, 2906, 2907, 2911, 2912, 2913, 2917,
            2918, 2918, 2919, 2924, 2927, 2929, 2930, 2930, 2931, 2933, 2936, 2939, 2940, 2943, 2943, 2943, 2943, 2945,
            2945, 2951, 2953, 2967, 2967, 2968, 2973, 2975, 2982, 2984, 2987, 2995, 2995, 2996, 3000, 3001, 3003, 3003,
            3008, 3015, 3015, 3023, 3029, 3030, 3030, 3031, 3034, 3041, 3044, 3044, 3045, 3047, 3048, 3051, 3059, 3062,
            3063, 3063, 3065, 3065, 3071, 3072, 3073, 3074, 3079, 3080, 3080, 3080, 3086, 3086, 3087, 3087, 3095, 3096,
            3098, 3104, 3111, 3112, 3115, 3115, 3116, 3118, 3118, 3118, 3126, 3126, 3129, 3130, 3135, 3136, 3146, 3146,
            3146, 3149, 3149, 3150, 3150, 3154, 3154, 3158, 3158, 3163, 3164, 3166, 3167, 3174, 3175, 3176, 3180, 3180,
            3183, 3186, 3186, 3186, 3188, 3189, 3189, 3191, 3195, 3195, 3196, 3197, 3199, 3199, 3202, 3205, 3206, 3208,
            3212, 3212, 3213, 3214, 3216, 3217, 3223, 3226, 3226, 3230, 3231, 3235, 3237, 3237, 3247, 3250, 3251, 3253,
            3254, 3258, 3259, 3260, 3266, 3266, 3267, 3270, 3273, 3273, 3275, 3278, 3278, 3279, 3280, 3280, 3282, 3284,
            3285, 3286, 3290, 3294, 3295, 3298, 3298, 3299, 3303, 3306, 3307, 3316, 3316, 3322, 3323, 3325, 3328, 3330,
            3332, 3333, 3335, 3336, 3336, 3336, 3339, 3342, 3342, 3344, 3351, 3352, 3353, 3354, 3356, 3356, 3358, 3361,
            3364, 3372, 3373, 3385, 3392, 3398, 3401, 3408, 3409, 3411, 3412, 3413, 3413, 3413, 3414, 3418, 3418, 3419,
            3420, 3420, 3421, 3426, 3426, 3427, 3428, 3429, 3429, 3431, 3434, 3438, 3438, 3441, 3442, 3445, 3445, 3450,
            3452, 3453, 3457, 3461, 3463, 3464, 3465, 3471, 3472, 3473, 3475, 3476, 3488, 3490, 3490, 3492, 3493, 3493,
            3493, 3495, 3497, 3501, 3503, 3506, 3506, 3507, 3509, 3513, 3516, 3516, 3519, 3521, 3521, 3523, 3523, 3524,
            3524, 3524, 3525, 3526, 3538, 3539, 3547, 3550, 3551, 3552, 3556, 3559, 3562, 3562, 3568, 3568, 3577, 3577,
            3579, 3584, 3584, 3589, 3589, 3590, 3591, 3592, 3593, 3595, 3598, 3601, 3606, 3608, 3613, 3614, 3616, 3617,
            3618, 3621, 3622, 3625, 3628, 3634, 3636, 3636, 3637, 3639, 3640, 3640, 3645, 3651, 3653, 3654, 3655, 3655,
            3657, 3668, 3670, 3673, 3674, 3676, 3676, 3677, 3681, 3683, 3687, 3695, 3695, 3697, 3701, 3709, 3712, 3714,
            3718, 3719, 3722, 3725, 3726, 3740, 3749, 3750, 3750, 3752, 3753, 3754, 3755, 3757, 3758, 3758, 3761, 3762,
            3764, 3766, 3775, 3775, 3778, 3779, 3779, 3780, 3783, 3785, 3787, 3789, 3790, 3792, 3796, 3798, 3807, 3809,
            3811, 3814, 3814, 3820, 3824, 3827, 3835, 3838, 3848, 3850, 3854, 3854, 3854, 3860, 3862, 3863, 3863, 3868,
            3870, 3875, 3886, 3888, 3891, 3897, 3897, 3898, 3900, 3902, 3904, 3905, 3908, 3909, 3910, 3910, 3915, 3921,
            3924, 3924, 3924, 3933, 3934, 3935, 3936, 3939, 3940, 3943, 3950, 3951, 3953, 3954, 3955, 3957, 3962, 3965,
            3966, 3967, 3968, 3970, 3972, 3972, 3973, 3975, 3977, 3978, 3980, 3982, 3983, 3984, 3984, 3985, 3989, 3990,
            3995, 3995, 3996, 3997, 3997, 3999, 4005, 4005, 4017, 4018, 4021, 4022, 4024, 4028, 4029, 4031, 4031, 4032,
            4036, 4036, 4038, 4040, 4040, 4040, 4041, 4042, 4042, 4046, 4048, 4048, 4050, 4052, 4054, 4054, 4056, 4057,
            4058, 4061, 4068, 4073, 4075, 4077, 4078, 4078, 4078, 4087, 4096, 4098, 4099, 4106, 4106, 4107, 4109, 4111,
            4111, 4115, 4119, 4122, 4126, 4127, 4127, 4130, 4131, 4135, 4136, 4138, 4141, 4146, 4148, 4167, 4171, 4171,
            4179, 4181, 4192, 4196, 4197, 4197, 4201, 4202, 4204, 4206, 4208, 4209, 4212, 4217, 4223, 4225, 4226, 4232,
            4234, 4235, 4236, 4237, 4239, 4240, 4242, 4244, 4246, 4246, 4246, 4250, 4251, 4254, 4263, 4272, 4272, 4274,
            4274, 4276, 4277, 4278, 4278, 4280, 4280, 4283, 4284, 4289, 4290, 4292, 4292, 4295, 4297, 4298, 4299, 4300,
            4305, 4307, 4307, 4308, 4312, 4319, 4319, 4321, 4322, 4325, 4328, 4332, 4335, 4337, 4338, 4342, 4342, 4344,
            4345, 4345, 4351, 4351, 4353, 4358, 4358, 4360, 4361, 4363, 4366, 4367, 4370, 4375, 4376, 4377, 4380, 4380,
            4383, 4384, 4385, 4389, 4389, 4390, 4390, 4391, 4392, 4393, 4393, 4395, 4401, 4402, 4402, 4404, 4404, 4405,
            4407, 4410, 4412, 4412, 4417, 4422, 4427, 4429, 4430, 4434, 4435, 4436, 4437, 4439, 4439, 4443, 4444, 4450,
            4452, 4456, 4458, 4462, 4463, 4466, 4467, 4468, 4472, 4483, 4484, 4485, 4489, 4497, 4499, 4499, 4502, 4508,
            4521, 4526, 4531, 4534, 4537, 4542, 4544, 4547, 4548, 4549, 4549, 4551, 4551, 4554, 4555, 4556, 4557, 4559,
            4565, 4565, 4567, 4568, 4573, 4580, 4580, 4580, 4581, 4582, 4586, 4594, 4598, 4599, 4600, 4601, 4604, 4611,
            4614, 4615, 4619, 4620, 4622, 4623, 4625, 4626, 4628, 4628, 4632, 4636, 4637, 4638, 4641, 4649, 4650, 4654,
            4655, 4656, 4657, 4657, 4661, 4666, 4676, 4677, 4677, 4680, 4687, 4688, 4689, 4693, 4703, 4715, 4715, 4715,
            4721, 4731, 4736, 4736, 4740, 4744, 4750, 4751, 4754, 4755, 4755, 4758, 4758, 4760, 4762, 4764, 4769, 4772,
            4772, 4776, 4777, 4780, 4782, 4784, 4787, 4787, 4796, 4798, 4809, 4810, 4812, 4815, 4819, 4819, 4821, 4821,
            4828, 4828, 4833, 4834, 4835, 4840, 4841, 4844, 4847, 4847, 4847, 4849, 4851, 4852, 4852, 4854, 4856, 4858,
            4859, 4861, 4865, 4867, 4869, 4870, 4873, 4880, 4882, 4882, 4883, 4884, 4891, 4893, 4894, 4896, 4898, 4899,
            4900, 4903, 4904, 4905, 4907, 4909, 4909, 4913, 4915, 4916, 4917, 4918, 4921, 4922, 4923, 4924, 4924, 4925,
            4926, 4926, 4927, 4931, 4936, 4939, 4942, 4945, 4949, 4952, 4955, 4955, 4956, 4957, 4970, 4973, 4982, 4987,
            4988, 4994, 4995, 4996, 4996, -4999, -4997, -4995, -4989, -4983, -4981, -4980, -4975, -4974, -4973, -4973,
            -4973, -4964, -4964, -4962, -4961, -4960, -4960, -4958, -4955, -4954, -4950, -4948, -4947, -4944, -4943,
            -4943, -4940, -4939, -4939, -4936, -4934, -4929, -4928, -4928, -4925, -4924, -4923, -4923, -4920, -4919,
            -4918, -4917, -4916, -4916, -4914, -4912, -4907, -4903, -4902, -4898, -4897, -4897, -4896, -4891, -4890,
            -4886, -4885, -4884, -4883, -4882, -4880, -4875, -4868, -4866, -4861, -4859, -4852, -4851, -4836, -4830,
            -4828, -4827, -4824, -4821, -4819, -4814, -4812, -4811, -4810, -4809, -4808, -4803, -4801, -4795, -4792,
            -4781, -4781, -4773, -4773, -4772, -4769, -4766, -4765, -4761, -4760, -4752, -4752, -4748, -4748, -4745,
            -4741, -4741, -4738, -4738, -4729, -4728, -4728, -4717, -4716, -4711, -4709, -4708, -4707, -4707, -4705,
            -4703, -4703, -4702, -4697, -4697, -4695, -4695, -4694, -4694, -4686, -4685, -4678, -4675, -4674, -4673,
            -4670, -4669, -4668, -4667, -4662, -4660, -4660, -4656, -4653, -4643, -4632, -4632, -4631, -4629, -4627,
            -4627, -4626, -4623, -4623, -4622, -4615, -4612, -4609, -4608, -4606, -4606, -4605, -4604, -4603, -4599,
            -4593, -4589, -4584, -4581, -4579, -4574, -4570, -4570, -4568, -4566, -4557, -4556, -4556, -4556, -4551,
            -4549, -4549, -4549, -4547, -4544, -4543, -4543, -4543, -4536, -4533, -4532, -4528, -4521, -4520, -4518,
            -4512, -4512, -4510, -4510, -4510, -4508, -4507, -4501, -4501, -4499, -4497, -4495, -4493, -4491, -4489,
            -4488, -4486, -4485, -4478, -4475, -4471, -4465, -4464, -4464, -4463, -4454, -4445, -4440, -4438, -4438,
            -4438, -4436, -4434, -4429, -4429, -4421, -4421, -4421, -4419, -4414, -4414, -4413, -4412, -4405, -4397,
            -4394, -4390, -4390, -4390, -4389, -4389, -4384, -4373, -4368, -4366, -4364, -4363, -4361, -4359, -4356,
            -4352, -4346, -4345, -4339, -4339, -4335, -4331, -4329, -4321, -4319, -4319, -4318, -4316, -4312, -4308,
            -4303, -4302, -4300, -4300, -4293, -4290, -4287, -4280, -4277, -4276, -4275, -4274, -4274, -4274, -4273,
            -4271, -4267, -4267, -4264, -4262, -4262, -4260, -4259, -4256, -4255, -4253, -4248, -4247, -4247, -4246,
            -4240, -4238, -4238, -4236, -4232, -4229, -4225, -4225, -4224, -4222, -4221, -4219, -4217, -4217, -4215,
            -4210, -4203, -4201, -4197, -4184, -4182, -4181, -4180, -4177, -4171, -4168, -4164, -4157, -4155, -4149,
            -4145, -4145, -4145, -4144, -4143, -4141, -4140, -4130, -4129, -4129, -4126, -4124, -4122, -4116, -4101,
            -4099, -4094, -4094, -4089, -4089, -4085, -4079, -4078, -4071, -4070, -4062, -4061, -4060, -4060, -4058,
            -4056, -4055, -4045, -4037, -4036, -4032, -4029, -4029, -4026, -4024, -4023, -4022, -4020, -4019, -4015,
            -4014, -4009, -4005, -4003, -4001, -4001, -3994, -3988, -3988, -3988, -3983, -3981, -3980, -3974, -3973,
            -3969, -3969, -3968, -3966, -3960, -3958, -3958, -3956, -3953, -3952, -3944, -3940, -3936, -3935, -3934,
            -3933, -3932, -3926, -3918, -3916, -3915, -3914, -3904, -3902, -3902, -3902, -3901, -3898, -3896, -3894,
            -3893, -3893, -3891, -3891, -3888, -3883, -3882, -3882, -3879, -3879, -3874, -3870, -3868, -3866, -3864,
            -3862, -3862, -3859, -3859, -3859, -3857, -3855, -3855, -3852, -3852, -3850, -3848, -3846, -3845, -3839,
            -3835, -3833, -3832, -3832, -3831, -3831, -3831, -3827, -3824, -3820, -3817, -3814, -3812, -3810, -3804,
            -3801, -3799, -3798, -3795, -3783, -3776, -3776, -3772, -3771, -3767, -3764, -3764, -3762, -3762, -3758,
            -3756, -3756, -3755, -3750, -3748, -3737, -3736, -3733, -3728, -3720, -3719, -3719, -3715, -3714, -3713,
            -3712, -3711, -3711, -3709, -3709, -3701, -3701, -3697, -3692, -3691, -3690, -3684, -3682, -3681, -3671,
            -3671, -3669, -3669, -3666, -3662, -3658, -3655, -3653, -3652, -3645, -3642, -3640, -3639, -3639, -3639,
            -3637, -3635, -3630, -3620, -3615, -3613, -3612, -3607, -3602]

    result = solution.search(num1, -2815)

    # result = solution.ordered_bsearch([1, 2, 3, 4, 6], 2)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])

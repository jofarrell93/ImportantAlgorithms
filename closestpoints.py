#Find the closest 2 points in a 2D plane 

#Brute force method: for N points find the distance to all other N-1 points (O(n**2))
#Can reduce time using divide and conquer approach 

#General method
#sort points according to X coordinate 
#split points into two equal groups (left and right hand side)
#find the minimum distance between the two groups 
#NB: have not yet considered close points which lie in separate groups (i.e., along/near the divison)
#collect points along/near division which may have a distance less than current minimum
#iterate through the gathered points and update minimum distance accordingly

#Using recursion this general method can be applied repeatedly on ever decreasing groups of points
#until the solution becomes relatively simple

import random
import math

#Either generate random points OR import given points 
#Points are unique and have positive x & y integer values 
#Sort the points according to their X coordinate

#Generate random points
#Define the plane and the number of points
x_limit, y_limit, num_points = 1000, 1000, 200 
x_values = random.sample(range(x_limit), num_points)
y_values = random.sample(range(y_limit), num_points)
points_unsorted = list(zip(x_values, y_values))
points = sorted(points_unsorted, key=lambda point: point[0])

"""
#Import given points 
#NB points are in a text file in the format...[(x1, y1),.....(xn, yn)]
#Example:
#[(5556, 7602), (7583, 4125), (7164, 6402), (3623, 4573), (7831, 4352), (3708, 2346), (8453, 1658), (2792, 2920), (8609, 6626), (9024, 2267), (6638, 2585), (5380, 5748), (4101, 2768), (8577, 7468), (5043, 8986), (8404, 816), (7501, 3664), (8254, 434), (2128, 9353), (1388, 3131), (2228, 149), (914, 4518), (9543, 7415), (437, 6512), (4782, 82), (7954, 2484), (3883, 3088), (3261, 723), (9313, 7672), (6237, 3423), (4882, 8618), (6310, 484), (2884, 5793), (8178, 2257), (5223, 8408), (6141, 2123), (1666, 9912), (1947, 3656), (1497, 333), (459, 806), (976, 8369), (7613, 1463), (7929, 3253), (4413, 4119), (8370, 3300), (7819, 1781), (5658, 5844), (8384, 3166), (6359, 405), (984, 7352), (3092, 5818), (7696, 5911), (1932, 9946), (4986, 9523), (3310, 1522), (580, 8033), (3512, 8057), (8638, 3085), (7798, 4903), (1380, 6067), (4219, 4950), (6769, 44), (3533, 7376), (3933, 3383), (6970, 5945), (9869, 964), (7069, 1367), (3243, 63), (2439, 9850), (2788, 9841), (8081, 3562), (2702, 1111), (70, 5924), (3894, 6481), (6441, 6682), (7473, 6262), (6615, 4433), (258, 9584), (6956, 5907), (8973, 9871), (5953, 5952), (8061, 2468), (1555, 5490), (4741, 6137), (3553, 6902), (761, 8142), (2398, 1827), (3168, 3381), (8333, 8002), (6055, 2106), (2030, 6697), (1311, 189), (9595, 7937), (1012, 529), (9211, 6901), (6116, 9637), (7834, 4434), (6123, 9753), (9533, 4622), (4787, 267), (7623, 4141), (7946, 341), (8161, 27), (1578, 8667), (5942, 6843), (2050, 9344), (2293, 8980), (5860, 1566), (3496, 8381), (1995, 1132), (8522, 4532), (7538, 1255), (7310, 7491), (519, 9418), (1407, 8362), (7111, 4322), (1575, 2165), (716, 2321), (6292, 2922), (2189, 8219), (8801, 123), (4667, 6070), (6812, 9731), (299, 2352), (5391, 7886), (8315, 5338), (8337, 212), (694, 5632), (754, 3294), (7718, 3683), (2689, 296), (2250, 430), (2752, 9308), (435, 339), (8400, 4164), (2627, 7895), (4725, 9542), (6365, 7944), (8292, 6435), (9391, 8452), (6397, 2845), (2265, 7824), (2928, 4311), (534, 8960), (4532, 7297), (3085, 4781), (796, 3934), (4548, 7457), (7499, 447), (1367, 8947), (6137, 1168), (4126, 3510), (7719, 8999), (824, 2742), (4951, 535), (5185, 9393), (932, 5231), (4266, 8004), (9572, 3456), (4007, 4500), (7220, 4178), (5160, 8639), (2470, 1442), (8305, 5543), (5836, 7446), (3537, 1228), (3425, 3156), (8845, 2145), (8684, 5237), (9785, 1227), (729, 197), (1001, 4328), (3921, 9526), (1270, 765), (8777, 1635), (1290, 4259), (5976, 8476), (6424, 9957), (1897, 7263), (1170, 7175), (1258, 9973), (2124, 8307), (5229, 5596), (2138, 3487), (8411, 9321), (5821, 9653), (8837, 5081), (3777, 6296), (6485, 8098), (4233, 5566), (8779, 6423), (4870, 421), (1987, 3292), (5838, 8732), (7159, 9453), (521, 5202), (2312, 4281), (732, 894), (1006, 1031), (1721, 525), (648, 4489), (5661, 6212), (5771, 6699), (1745, 5377), (1460, 1360), (9867, 1494), (9403, 1183), (6117, 6605), (1954, 153), (6610, 5106), (4724, 1452), (7505, 6046), (9893, 6084), (5440, 5414), (673, 3834), (8014, 7323), (7742, 5492), (2252, 8692), (3066, 5614), (7050, 9980), (1316, 9157), (6298, 9305), (6684, 8220), (1525, 752), (3467, 2241), (5539, 4380), (9699, 2846), (6914, 6434), (9829, 1757), (1066, 785), (3996, 4185), (4653, 7990), (8064, 3766), (4620, 1600), (3368, 6636), (1506, 4626), (9166, 1771), (3043, 7984), (8876, 2103), (1927, 2129), (5028, 4555), (5585, 830), (6451, 1714), (8924, 3104), (1408, 6490), (1479, 3279), (7495, 7254), (9860, 6242), (2368, 9610), (5899, 9042), (6863, 3400), (5837, 4649), (2253, 6123), (8409, 3973), (482, 1181), (1295, 4918), (3726, 4379), (9754, 6860), (863, 1583), (5644, 5831), (9837, 7865), (2670, 4940), (564, 3529), (1483, 7561), (1204, 5499), (591, 9470), (2133, 1627), (2159, 7637), (9990, 1616), (9179, 5426), (6048, 7172), (2595, 361), (5430, 8027), (4205, 5196), (8975, 4943), (6275, 120), (619, 3577), (2327, 4183), (8003, 1597), (5413, 7089), (7233, 8885), (8617, 3065), (6140, 4643), (651, 3287), (4756, 8203), (6210, 4087), (8344, 5880), (5488, 9013), (391, 3390), (9189, 2140), (5502, 4825), (718, 4933), (4177, 1805), (4974, 5013), (8426, 9076), (3283, 1158), (490, 6583), (6717, 8919), (6005, 7917), (4060, 7442), (927, 2214), (4666, 7411), (5782, 9349), (9606, 9295), (2471, 83), (4450, 2900), (5780, 4294), (3428, 7702), (9824, 4837), (3638, 9356), (9012, 3743), (9424, 6226), (5159, 7241), (7525, 9586), (4124, 4706), (2660, 9160), (3407, 9190), (4080, 7150), (1728, 3970), (6341, 9084), (6130, 8159), (7873, 290), (7273, 897), (1486, 4060), (1356, 557), (7017, 3876), (6021, 9197), (1186, 7000), (5937, 5573), (9030, 3453), (9775, 220), (2112, 7127), (1493, 7341), (5610, 6384), (1571, 7295), (5833, 6027), (8756, 5542), (638, 6380), (4583, 5155), (4884, 5348), (3810, 410), (5103, 2144), (2526, 1711), (6040, 5684), (3222, 4016), (3877, 5800), (893, 8869), (4928, 5199), (896, 6879), (5932, 547), (5438, 8446), (6728, 3582), (3420, 2023), (8550, 526), (7611, 9645), (6032, 8789), (4926, 7930), (6231, 456), (8066, 8034), (6527, 1480), (133, 4388), (1109, 2435), (8006, 4787), (7546, 622), (2349, 8200), (7474, 3807), (2027, 1618), (8731, 304), (2522, 9587), (1154, 2369), (1618, 3794), (8184, 4707), (4571, 465), (7513, 6297), (4468, 9277), (3816, 8506), (8771, 2864), (434, 1073), (5602, 3775), (6312, 9735), (5930, 4880), (3944, 8532), (5690, 6047), (4601, 3528), (2887, 8288), (4396, 3669), (707, 7383), (3855, 6150), (337, 4738), (575, 5260), (9745, 4712), (4982, 1762), (4559, 9049), (5573, 1972), (1637, 8231), (669, 2324), (7674, 6292), (7900, 1716), (2033, 103), (9503, 3002), (2676, 6873), (1119, 5209), (9031, 9132), (9575, 4788), (5354, 6915), (4454, 4732), (5679, 7162), (1490, 9463), (6870, 9163), (8548, 5150), (4260, 9812), (2629, 6711), (2267, 3747), (3748, 2002), (2678, 6126), (8442, 5424), (5748, 8443), (6250, 6190), (2805, 552), (219, 7288), (4172, 2851), (844, 8569), (9439, 2424), (1039, 3963), (5318, 6216), (7151, 2482), (8170, 3730), (6977, 4827), (2106, 8490), (3737, 5498), (1254, 5280), (507, 9723), (3701, 100), (9229, 2858), (6180, 8086), (5309, 6590), (2932, 5931), (7080, 2731), (7978, 6379), (6497, 6729), (6553, 5921), (5739, 92), (5749, 8611), (6542, 8245), (8811, 9621), (8010, 6637), (9866, 4104), (1872, 663), (6680, 1315), (7402, 8018), (149, 1194), (8820, 1391), (6098, 7941), (2946, 7571), (9361, 4268), (6076, 4461), (327, 6973), (8277, 4492), (3353, 1888), (9393, 3023), (8963, 2014), (8925, 1491), (7676, 8912), (168, 1677), (5879, 1072), (7141, 946), (5409, 8941), (4832, 6396), (8464, 4004), (2226, 8222), (9580, 2038), (2502, 829), (4331, 8581), (7064, 4393), (3180, 4290), (4034, 4292), (2145, 468), (6157, 192), (2626, 9527), (3561, 7754), (2811, 6299), (7518, 6025), (1340, 618), (1395, 2560), (7591, 5462), (200, 1700), (4145, 735), (6407, 4137), (7004, 1467), (5085, 9776), (1519, 2104), (6861, 4177), (8899, 6323), (9256, 4124), (9997, 7251), (8226, 3353), (687, 6710), (5617, 7771), (3084, 4472), (9931, 6185), (3968, 2740), (8532, 4494), (9719, 6080), (7986, 3574), (993, 881), (917, 3770), (8613, 7428), (4731, 8597), (6793, 8192), (3214, 8040), (4773, 8414), (5851, 9620), (6921, 6555), (5381, 4321), (9001, 5358), (4658, 8609), (2407, 9571), (3200, 1067), (1585, 5804), (7475, 5117), (9637, 2995), (9638, 3028), (4243, 581), (3632, 1018), (9105, 4376), (1711, 3548), (7197, 4254), (9592, 3597), (1259, 4673), (2126, 8015), (5482, 4609), (7061, 8396), (4347, 2540), (9499, 784), (6099, 3247), (9446, 1042), (1099, 9968), (5336, 5034), (5107, 6739), (7697, 2844), (8892, 1577), (1167, 6304), (4566, 1393), (9938, 7016), (7621, 2447), (5063, 2399), (8893, 2810), (8996, 5519), (2837, 182), (6762, 4559), (6295, 627), (4010, 1007), (1150, 4514), (4894, 8634), (242, 124), (7969, 4384), (3676, 6383), (7113, 6669), (3360, 7568), (6302, 6890), (9108, 8537), (5694, 451), (2760, 5395), (5730, 3481), (7796, 4037), (9855, 2680), (1685, 128), (1069, 1296), (5763, 8619), (1016, 6266), (8910, 8095), (5052, 2955), (3461, 2859), (7788, 4990), (3604, 2116), (2920, 3632), (4795, 9201), (5534, 9015), (1957, 5223), (3005, 9612), (994, 5475), (4691, 8660), (1062, 8275), (6832, 9367), (2548, 3619), (1272, 1474), (3904, 9672), (9631, 2053), (758, 988), (4999, 2114), (6724, 6215), (4466, 2118), (9674, 49), (3231, 2546), (3217, 8365), (1465, 9237), (4025, 6064), (7917, 368), (512, 9164), (6580, 6376), (740, 6764), (2415, 8297), (3846, 8720), (7371, 6166), (6323, 5458), (3452, 3677), (2359, 9216), (962, 6322), (4855, 133), (5654, 6348), (8887, 7731), (5855, 6656), (9303, 8379), (6455, 2710), (2765, 3365), (2691, 4015), (7924, 6894), (6862, 5758), (3419, 7209), (2399, 1290), (9649, 9391), (3675, 3689), (8607, 7102), (6380, 7739), (8596, 1045), (4416, 9392), (197, 2541), (5891, 325), (8262, 6833), (1321, 5483), (3899, 7222), (7045, 848), (8649, 39), (6947, 9659), (1515, 2962), (1974, 7590), (6779, 2101), (7280, 4166), (7032, 8830), (7905, 5938), (2296, 2838), (2979, 8691), (8229, 3924), (8198, 3290), (53, 1768), (7090, 4799), (7836, 1816), (1174, 4892), (5584, 147), (6957, 6205), (8781, 134), (3153, 7221), (8745, 1041), (2164, 7313), (3887, 2232), (2825, 9525), (6771, 2921), (9327, 1637), (9441, 9079), (3354, 7783), (915, 3352), (4420, 6300), (3089, 5625), (384, 4833), (453, 1396), (6637, 9529), (7856, 2489), (7158, 2083), (3767, 8488), (5653, 7833), (3233, 8108), (7648, 3740), (5543, 9025), (5271, 9350), (5261, 8186), (1417, 9695), (3383, 1180), (187, 4346), (4027, 7626), (8749, 5056), (2853, 4962), (3753, 4941), (785, 2978), (889, 2775), (209, 1927), (6156, 7460), (2536, 6820), (2504, 9468), (8486, 6698), (165, 644), (649, 9230), (6182, 9916), (1008, 2544), (561, 7181), (5980, 6849), (9457, 740), (1847, 6594), (2373, 5567), (8896, 3608), (8618, 6733), (9034, 2356), (2065, 5249), (5195, 9355), (4405, 3504), (9777, 2074), (9964, 5318), (3362, 8734), (4078, 8269), (6351, 1068), (6387, 5431), (6259, 5886), (5516, 540), (7451, 3815), (978, 5061), (8032, 6499), (6084, 2492), (2320, 9423), (2693, 1507), (142, 8121), (4757, 8354), (2449, 1280), (2786, 9270), (3756, 9854), (2477, 4042), (9005, 376), (2727, 9604), (7431, 5661), (9485, 5598), (334, 2802), (2177, 3913), (1913, 7903), (9605, 4420), (6196, 8964), (6403, 4442), (8793, 7007), (6502, 3704), (3917, 2809), (469, 2548), (5497, 8371), (9420, 1981), (7098, 7960), (6152, 8616), (6650, 9648), (120, 152), (6940, 8724), (6917, 193), (6689, 6469), (8875, 572), (1608, 6146), (2650, 3509), (5212, 4534), (8528, 291), (3640, 9705), (2208, 1746), (1594, 9096), (4834, 2488), (2948, 2368), (8420, 9675), (3913, 4704), (659, 3914), (3367, 446), (2446, 4460), (2147, 5137), (3834, 5177), (810, 3682), (4971, 9009), (6528, 2682), (8888, 9409), (4049, 6165), (3995, 9235), (2910, 52), (9848, 7366), (7044, 7759), (2374, 970), (9835, 6043), (8726, 427), (4465, 9585), (3465, 2094), (6136, 8274), (1713, 2049), (152, 2580), (7208, 7708), (1955, 1432), (4907, 606), (8423, 772), (5911, 719), (7962, 2573), (2151, 1564), (8758, 7577), (232, 1818), (5306, 5910), (4863, 1812), (9015, 6521), (2078, 9791), (3930, 132), (9806, 4672), (2931, 9938), (3824, 9136), (8889, 8626), (5876, 3672), (3318, 3094), (3570, 2121), (3661, 6159), (7081, 7289), (5691, 7048), (3221, 1445), (8077, 9047), (3127, 9974), (5645, 439), (192, 3626), (154, 2857), (2048, 113), (4312, 1038), (5668, 4096), (7649, 3771), (4166, 7299), (2241, 6641), (3093, 5604), (8977, 5005), (3825, 3769), (9738, 5853), (8984, 8509), (779, 3535), (9986, 8855), (1875, 3036), (6242, 4206), (3451, 4232), (8835, 6332), (6822, 4497), (1855, 1126), (2572, 7918), (5636, 1325), (3786, 58), (7882, 2005), (4282, 7292), (9636, 8023), (4286, 5656), (1045, 8202), (2484, 949), (9937, 4841), (4715, 7370), (342, 7569), (6619, 5344), (3189, 5197), (3154, 2050), (8806, 1879), (5236, 3816), (3312, 2409), (4708, 1519), (1310, 4829), (74, 3027), (1291, 1645), (9367, 746), (2896, 3862), (2561, 5466), (7213, 4399), (9679, 8756), (9348, 3811), (7707, 2358), (3013, 2390), (7596, 4325), (4391, 6903), (3266, 2631), (5214, 67), (4434, 1620), (90, 6221), (222, 9748), (9212, 7114), (5311, 2761), (5496, 106), (7494, 194), (3165, 2508), (1436, 7320), (3024, 2081), (7997, 7391), (7636, 3319), (423, 8938), (8493, 4687), (7936, 1630), (234, 1128), (1651, 5365), (9768, 8620), (3498, 8807), (2550, 7252), (8514, 4309), (7595, 6708), (4271, 3096), (5121, 2852), (4753, 3985), (6891, 3267), (7094, 2865), (7875, 314), (6776, 5060), (9732, 6206), (6670, 230), (537, 8064), (9694, 9327), (8943, 9910), (3390, 5575), (6660, 6503), (6529, 5913), (4244, 1543), (438, 3636), (7617, 7028), (1653, 8253), (9352, 6944), (2495, 3246), (2005, 6738), (6027, 234), (1131, 9708), (2668, 5346), (4039, 8303), (2916, 3610), (8001, 3046), (6038, 5062), (5045, 3317), (7210, 6567), (5924, 783), (3677, 2888), (5936, 9286), (3976, 157), (8116, 6660), (4350, 6935), (5463, 7163), (7476, 8875), (1714, 379), (6590, 7153), (6570, 773), (7692, 5248), (126, 1497), (3012, 8595), (5169, 7070), (127, 7842), (897, 4375), (3664, 7653), (3212, 6189), (3431, 209), (3811, 6448), (4081, 9949), (2186, 7212), (4848, 3082), (6454, 2092), (5345, 6085), (8088, 5602), (3025, 116), (4802, 6948), (9250, 1274), (3374, 6442), (684, 6129), (4626, 1372), (8747, 4150), (2116, 3613), (1371, 5047), (4822, 778), (211, 3681), (1720, 912), (7187, 498), (1234, 7600), (4512, 6900), (4239, 2027), (4732, 2256), (8084, 4814), (5777, 4356), (4817, 3697), (2541, 8228), (8461, 2242), (3347, 624), (1614, 4191), (3587, 3274), (4768, 6325), (5733, 6135), (9522, 1752), (3344, 9794), (9540, 3998), (5406, 884), (7846, 6032), (9548, 4720), (4629, 7843), (1591, 5035), (7200, 6404), (1399, 2414), (7293, 6997), (3925, 9345), (1940, 4186), (6475, 6285), (7390, 2956), (1276, 6333), (508, 94), (9795, 3329), (7365, 5626), (9622, 38), (1970, 5670), (473, 7750), (4659, 4618), (1558, 1546), (4955, 579), (5404, 8927), (9182, 5410), (2034, 5983), (5743, 5006)]
#Answer: The minimum distance is 13.45362404707371 between points: [[5534, 9015], [5543, 9025]]

with open('points.txt') as file:
	points_as_list_strings=file.read().strip("[").strip("]").strip("(").strip(")").split("), (")

points_unsorted=[]

for str in points_as_list_strings:
	split_str = str.split(", ")
	split_int=list(map(int,split_str))
	points_unsorted.append(split_int)
	
points = sorted(points_unsorted, key=lambda point: point[0])
"""

#Function to calculate and return the distance between two points
def distance(point1, point2):
	rel_x = point2[0] - point1[0]
	rel_y = point2[1] - point1[1]
	dis = math.sqrt(rel_x**2 + rel_y**2)
	return dis
	
#Function to find the minimum distance between a small group of points using brute force 
#Returns both the minimum distance and the associated points in the format....[min_dis, [point1, point2]]
def minimumdistance_inplane(list_2D):
	min_dis = float('inf')
	min_points = [(0,0),(0,0)]
	for i in range(len(list_2D)):
		for j in range(i+1, len(list_2D)):
			dis = distance(list_2D[i], list_2D[j])
			if dis < min_dis:
				min_dis = dis
				min_points[0], min_points[1] = list_2D[i], list_2D[j]
	return [min_dis, min_points]

#Function to find the closest two points in a list of (sorted on x) 2D points
#if the list of 2D points is large the plane will be broken into two halves
#this division will continue (recursion) until the amount of points passed to the function
#is small enough to satisfy the first if statement and be solved using the brute force method 
#in function minimumdistance_inplane()  
def minimumdistance(list_2D):
	#if amount of points is small enough to be easily solved using brute force then...
	if len(list_2D) <= 3:
		return minimumdistance_inplane(list_2D)
	#else need to break down the list of points ito more managible chunks and recall minimumdistance
	else:
		mid_index = len(list_2D)//2
		left_side = list_2D[:mid_index]
		right_side = list_2D[mid_index:]
		left = minimumdistance(left_side)
		right = minimumdistance(right_side)
		#if minimum distance is in the left half of the plane save that distance and associated points 
		if left[0]<right[0]:
			min_details = left
		#else save the minimum distance on the right half of the plane and associated points 
		else:
			min_details = right
		min_dis = min_details[0]
		#empty strip=[] to store points which lie along/near the division of the left and right plane 
		#these points have the potential to disrupt the current minimum distance 
		strip=[]
		for point in list_2D:
			if abs(list_2D[mid_index][0]-point[0])<min_dis:
				strip.append(point)
		#sorting the strip=[...] of points on the Y coordinate reduces the O complexity from 
		#n**2 (for each n points in the strip calculate the distance to all other n-1 in the strip)
		#to n. This is because for any given point i in the strip there is at most 7 proceeding points
		#in the sorted strip which have the potential to change the current minimum distance 		
		strip.sort(key=lambda point: point[1])
		min_details_strip = minimumdistance_instrip(strip, min_details)
		if min_details[0] < min_details_strip[0]:
			return min_details
		else:
			return min_details_strip
			
#Function to find the minimum distance and associated points in the strip of points
#located near/around the plane division 	
def minimumdistance_instrip(list_2D, min_details):
	min_dis = min_details[0]
	min_points = min_details[1].copy()
	for i in range(len(list_2D)):
		j = i+1
		while j<len(list_2D) and abs(list_2D[i][1]-list_2D[j][1])<min_dis:
			dis = distance(list_2D[i], list_2D[j])
			if dis < min_dis:
				min_dis = dis
				min_points[0], min_points[1] = list_2D[i], list_2D[j]
			j += 1
	return [min_dis, min_points]
		
dis_and_points = minimumdistance(points)
min_dis = dis_and_points[0]
min_points= dis_and_points[1]
print(f"The minimum distance is {min_dis} between points: {min_points}")

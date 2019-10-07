Input deck created by FRIDGe
c **************************Axial_Smear_Assembly_Test**************************
c ************************Cell Cards for Assembly: 01A01*********************** 
100 100 0.03045 -100 u=100 imp:n=1 $Assembly: Test_Region
101 101 0.05513 -101 u=100 imp:n=1 $Assembly: Test_Region2
102 102 0.04896 -102 u=100 imp:n=1 $Assembly: Test_Region3
103 0 -103 fill=100 imp:n=1 $Assembly
104 0 103 imp:n=0 $Everything Else

c ********************Surface Cards for Fuel Assembly: 01A01*******************
100 RHP 0.0 0.0 -50.1 0 0 110.1 0 5.85029 0 $Assembly: Test_Region
101 RHP 0.0 0.0 60.0 0 0 110 0 5.85029 0 $Assembly: Test_Region2
102 RHP 0.0 0.0 170.0 0 0 50 0 5.85029 0 $Assembly: Test_Region3
103 RHP 0.0 0.0 -50.0 0 0 270.0 0 5.85 0 $Assembly: Full Assembly Surface

c **********************************Data Cards*********************************
c ******************************k-code Information*****************************
kcode 1000000 1.0 300 2300
ksrc 0 0 10
PRDMP 100 10 100 1 
kopts BLOCKSIZE=10 KINETICS=YES PRECURSOR=Yes 
DBCN 68J 50000 
c *****************************Material Information****************************
c Material: ['LiquidNa', 'HT9']; Density: 0.03045 atoms/bn*cm 
m100 11023.82c 7.1765E-1 6000.82c 2.5929E-3 14028.82c 2.0452E-3
     14029.82c 1.0390E-4 14030.82c 6.8570E-5 15031.82c 1.5082E-4
     16032.82c 9.2262E-5 16033.82c 7.2846E-7 16034.82c 4.1280E-6
     16036.82c 9.7128E-9 23050.82c 2.2925E-6 23051.82c 9.1471E-4
     24050.82c 1.4964E-3 24052.82c 2.8856E-2 24053.82c 3.2720E-3
     24054.82c 8.1448E-4 25055.82c 1.7006E-3 26054.82c 1.3845E-2
     26056.82c 2.1733E-1 26057.82c 5.0191E-3 26058.82c 6.6795E-4
     28058.82c 9.0303E-4 28060.82c 3.4784E-4 28061.82c 1.5122E-5
     28062.82c 4.8218E-5 28064.82c 1.2270E-5 42092.82c 2.3577E-4
     42094.82c 1.4847E-4 42095.82c 2.5703E-4 42096.82c 2.7050E-4
     42097.82c 1.5578E-4 42098.82c 3.9577E-4 42100.82c 1.5935E-4
     74180.82c 5.0819E-7 74182.82c 1.1223E-4 74183.82c 6.0602E-5
     74184.82c 1.2976E-4 74186.82c 1.2040E-4
c Material: ['LiquidNa', 'HT9']; Density: 0.05513 atoms/bn*cm 
m101 11023.82c 2.2022E-1 6000.82c 7.1609E-3 14028.82c 5.6483E-3
     14029.82c 2.8694E-4 14030.82c 1.8937E-4 15031.82c 4.1652E-4
     16032.82c 2.5480E-4 16033.82c 2.0118E-6 16034.82c 1.1400E-5
     16036.82c 2.6824E-8 23050.82c 6.3313E-6 23051.82c 2.5262E-3
     24050.82c 4.1326E-3 24052.82c 7.9693E-2 24053.82c 9.0365E-3
     24054.82c 2.2494E-3 25055.82c 4.6966E-3 26054.82c 3.8235E-2
     26056.82c 6.0022E-1 26057.82c 1.3862E-2 26058.82c 1.8447E-3
     28058.82c 2.4939E-3 28060.82c 9.6066E-4 28061.82c 4.1763E-5
     28062.82c 1.3316E-4 28064.82c 3.3887E-5 42092.82c 6.5115E-4
     42094.82c 4.1005E-4 42095.82c 7.0986E-4 42096.82c 7.4705E-4
     42097.82c 4.3022E-4 42098.82c 1.0930E-3 42100.82c 4.4007E-4
     74180.82c 1.4035E-6 74182.82c 3.0994E-4 74183.82c 1.6737E-4
     74184.82c 3.5836E-4 74186.82c 3.3251E-4
c Material: ['LiquidNa', 'HT9']; Density: 0.04896 atoms/bn*cm 
m102 11023.82c 2.9756E-1 6000.82c 6.4506E-3 14028.82c 5.0881E-3
     14029.82c 2.5848E-4 14030.82c 1.7059E-4 15031.82c 3.7520E-4
     16032.82c 2.2953E-4 16033.82c 1.8123E-6 16034.82c 1.0270E-5
     16036.82c 2.4164E-8 23050.82c 5.7033E-6 23051.82c 2.2756E-3
     24050.82c 3.7227E-3 24052.82c 7.1788E-2 24053.82c 8.1402E-3
     24054.82c 2.0263E-3 25055.82c 4.2307E-3 26054.82c 3.4443E-2
     26056.82c 5.4068E-1 26057.82c 1.2487E-2 26058.82c 1.6617E-3
     28058.82c 2.2466E-3 28060.82c 8.6537E-4 28061.82c 3.7620E-5
     28062.82c 1.1996E-4 28064.82c 3.0525E-5 42092.82c 5.8656E-4
     42094.82c 3.6938E-4 42095.82c 6.3945E-4 42096.82c 6.7295E-4
     42097.82c 3.8754E-4 42098.82c 9.8460E-4 42100.82c 3.9642E-4
     74180.82c 1.2643E-6 74182.82c 2.7920E-4 74183.82c 1.5077E-4
     74184.82c 3.2281E-4 74186.82c 2.9953E-4
c Material: Liquid Sodium; Density: 0.02428 atoms/bn*cm 
m103 11023.82c 1.0000E+0
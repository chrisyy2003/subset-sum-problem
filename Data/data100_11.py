a0 = 411932160813009099596968768
a1 = 206223842814678119689155352
a2 = 1165583303451951244969522412
a3 = 1002638044019331153011927866
a4 = 233816287586745360041206385
a5 = 483623870296143976342607254
a6 = 1050310990517875188131549500
a7 = 917725109633944027616930084
a8 = 940186852470384684271100101
a9 = 1185781701307454372629841483
a10 = 820560905753503539733461089
a11 = 240493137234590661355383771
a12 = 688598200720113198366445967
a13 = 829663810480040290624352755
a14 = 637685049999056289625506058
a15 = 709802940709581207416077236
a16 = 666854736531769210075111106
a17 = 1174434140638890980975787143
a18 = 363764422762837505032517982
a19 = 277772371335696186234142429
a20 = 1191018740036282916845174318
a21 = 722264000807056562031277782
a22 = 766987517082059707231860984
a23 = 811943911834193178505266378
a24 = 883457011458449275313902574
a25 = 954598973612992820603101052
a26 = 887883440513839616955446779
a27 = 317537178979620651851826765
a28 = 1210130210346021013288750985
a29 = 854201742728924212893811255
a30 = 184710422507839712390485789
a31 = 105544720123187807500065889
a32 = 331023808952188511017342875
a33 = 360753437644216812621871870
a34 = 221653414255353369348339102
a35 = 68277580053139910520075776
a36 = 82341906981058660949980532
a37 = 367745944087605010243614868
a38 = 301257361011568893954993341
a39 = 852906026237816654058084639
a40 = 128202333168297688467525158
a41 = 301779854679546602009826969
a42 = 600458191536860483185909449
a43 = 786881079658369788002881642
a44 = 1139685457689098666026089640
a45 = 158298906158964766453158173
a46 = 992328283942144699580406991
a47 = 196635672069276344141483156
a48 = 1091441923343258427560059421
a49 = 262710869423944220446160008
a50 = 83239505561924900526734354
a51 = 299613600810755699752373627
a52 = 174168655300802157741935842
a53 = 923582443079642672001527205
a54 = 550759358139708604277656498
a55 = 753797574205607940592938385
a56 = 568487970226498117892751124
a57 = 903781830781517993245948978
a58 = 57539759117318738717717614
a59 = 485754745177424980219202194
a60 = 909624071387635104101390614
a61 = 965253095439991730727669232
a62 = 475657621959355568079940474
a63 = 106177278470117836294639524
a64 = 982017862155679179751510573
a65 = 279266373235701075526448485
a66 = 459300965550262519882995960
a67 = 46519446052525795122645311
a68 = 225779646103550983346623896
a69 = 963474101795368940401027141
a70 = 1087542063394463969767328029
a71 = 503596208456450876081126903
a72 = 549917285077238243910529138
a73 = 1192320517696502894652063460
a74 = 749672991483493936647866722
a75 = 882814678218302388677829026
a76 = 739854598920812079469590160
a77 = 407274572677529179720211450
a78 = 1237093131416207319822591416
a79 = 965829800821200772643192417
a80 = 1098824294285732232129137784
a81 = 257618775382860052144612776
a82 = 738049954247558147301410295
a83 = 523361109907488786546603186
a84 = 742019564319343924610957595
a85 = 62950677228043172425481552
a86 = 844891243558179500123095305
a87 = 490920704290570235227071909
a88 = 894181515263133384368860639
a89 = 799953668546750403320988010
a90 = 343212017156409028412243218
a91 = 571757041803707231995502076
a92 = 441480994058568755819307303
a93 = 786624011797719648704609532
a94 = 165705181598250574952238505
a95 = 87526096238651280335932257
a96 = 653986960148459549718671670
a97 = 84079681912540595437280738
a98 = 898890585008121578121182631
a99 = 265910902642054747512047728

n = 100
k = 12
target = 7052297882425420144395439173

alist = []
for i in range(n):
    eval("alist.append({})".format('a' + str(i)))
alist_index = [i for i in range(n)]


[2, 12, 34, 9, 57, 89, 21, 58, 99, 45, 62, 77]
    #   "21 45 77 28 77 98 2 9 34 12 89 99".split()
ans = [2, 12, 34, 9, 57, 89, 21, 62, 99, 45, 58, 77]
a = [2, 12, 34, 9, 57, 89, 21, 62, 99, 45, 58, 77]
b = [9, 57, 89, 2, 12, 34, 21, 45, 99, 58, 62, 77]
print(sorted(a))
print(sorted(b))
# print(sorted(ans))
# [2, 9, 12, 21, 34, 45, 57, 58, 62, 77, 89, 99]
ans = "2 12 89 9 34 57 21 62 77 45 58 99".split()
ans = [int(i) for i in ans]
print(sorted(ans))

check = ''.join(['1' if i in ans else '0' for i in range(n)])
summ = 0
for i in range(len(check)):
    summ += int(check[i]) * alist[i]
print(summ)
if summ == target:
    print('solved!')

# ans = "21 45 77 28 77 98 2 9 34 12 89 99".split()
# ss = 0
# for i in ans:
#     ss += alist[int(i)]
# print(ss)
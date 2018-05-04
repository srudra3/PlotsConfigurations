# bsub -q 1nd -o jobs/ZB_500_150__MVA_em_muccamvaZbaradaptFull.out -e jobs/ZB_500_150__MVA_em_muccamvaZbaradaptFull.err submitMonoH.sh em muccamvaZbaradaptFull MVA ZB 500_150_

import os
import sys
import time

if len(sys.argv) < 3 :
    print "Please insert all the inputs I need: variable"
    print ""
    print "python mkMonoHiggsAnalysisCombination.py muccamva2HDMadaptFull_All_Bin800 em"
    print ""
    print "python mkMonoHiggsAnalysisCombination.py muccamvaZbaradaptFull_All_Bin100 em"
    print ""
    print ""

    sys.exit()
    
variable = sys.argv[1]
print "Variable: " + variable

channel = sys.argv[2]
print "Channel: " + channel

#channel = "em"
cut = "MVA"

os.system("mkdir -p jobs")

print "2HDM Model Mass Points:"

# ZpMasses = {"600","800","1000","1200","1400","1700","2000","2500"}
# A0Masses = {"300","400","500","600","700","800"}

ZpMasses={"450","500","550","600","650","700","750","800","850","900","950","1000","1050","1100","1150","1200","1250","1300","1350","1400","1450","1500","1550","1600","1650","1700","1750","1800","1850","1900","1950","2000","2050","2100","2150","2200","2250","2300","2350","2400","2450","2500"}
A0Masses={"300","325","350","375","400","425","450","475","500","525","550","575","600","625","650","675","700","725","750","775","800","825","850","875","900","925","950","975"}

#ttDMmasses={"scalar00010_","scalar00020_","scalar00050_","scalar00100_","scalar00200_","scalar00300_","scalar00500_","pseudo00010_","pseudo00020_","pseudo00050_","pseudo00100_","pseudo00200_","pseudo00300_","pseudo00500_"}

#os.system("cp /afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/monoHWW/Apr2017/submitMonoH.sh .")
#os.system("chmod +x submitMonoH.sh")

if "Zbar" not in variable :                                                                                                                 
    
    for mzp in ZpMasses :
        for ma0 in A0Masses :
            print 'bsub -q 8nh -o jobs/' + mzp + '_' + ma0 + '_' + cut + '_'  + channel + '_' + variable + '_Combination.out -e jobs/' + mzp + '_' + ma0 + '_' + cut + '_' + channel + '_' + variable + '_Combination.err /afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/monoHWW/Apr2017/submitMonoHCombination.sh ' + channel + ' ' + variable + ' ' + cut + ' ' + mzp + ' ' + ma0
            os.system('bsub -q 8nh -o jobs/' + mzp + '_' + ma0 + '_' + cut + '_'  + channel + '_' + variable + '_Combination.out -e jobs/' + mzp + '_' + ma0 + '_' + cut + '_' + channel + '_' + variable + '_Combination.err /afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/monoHWW/Apr2017/submitMonoHCombination.sh ' + channel + ' ' + variable + ' ' + cut + ' ' + mzp + ' ' + ma0)
            time.sleep(5)

    # for ttdm in ttDMmasses :
    #     print 'bsub -q 8nh -o jobs/' + mzp + '_' + ma0 + '_' + cut + '_'  + channel + '_' + variable + '.out -e jobs/' + mzp + '_' + ma0 + '_' + cut + '_' + channel + '_' + variable + '.err /afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/monoHWW/Apr2017/submitMonoH.sh ' + channel + ' ' + variable + ' ' + cut + '  ttdm ' + ttdm
    #     os.system('bsub -q 8nh -o jobs/' + mzp + '_' + ma0 + '_' + cut + '_'  + channel + '_' + variable + '.out -e jobs/' + mzp + '_' + ma0 + '_' + cut + '_' + channel + '_' + variable + '.err /afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/monoHWW/Apr2017/submitMonoH.sh ' + channel + ' ' + variable + ' ' + cut + ' ttdm ' + ttdm)

# python scriptMonoHSplit80.py em muccamva2HDMadaptFull_All_Bin800 MVA ttDM scalar00010_
            #os.system('.//afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/monoHWW/Apr2017/submitMonoH.sh ' + channel + ' ' + variable + ' ' + cut + ' ' + mzp + ' ' + ma0)


print "Zbar Model Mass Points:"

ZB = "ZB"
ZBmasses={"10000_1000_","10000_500_","10000_150_","10000_50_","10000_1_","2000_1_","1995_1000_","1000_1000_","1000_150_","1000_1_","995_500_","500_500_","500_150_","500_1_","300_50_","300_1_","295_150_","200_150_","200_50_","200_1_","100_10_","100_1_","95_50_","50_50_","50_10_","50_1_","20_1_","15_10_","10_1000_","10_500_","10_150_","10_50_","10_10_","10_1_","50_40_","50_45_","50_60_","50_70_","50_80_","50_90_","40_50_","40_10_","40_40_","40_45_","40_60_","40_70_","40_80_","40_90_","50_150_","50_175_","50_200_","50_225_","50_275_","100_150_","100_175_","100_200_","100_225_","100_250_","100_275_","100_300_","100_325_","10_100_","10_125_","10_175_","10_200_","10_225_","10_250_","10_300_","10_325_","20_100_","20_125_","20_150_","20_175_","20_250_","20_300_","30_125_","30_250_","30_275_","30_300_","40_125_","40_175_","40_200_","40_225_","40_250_","40_300_","40_325_","75_150_","75_225_","75_250_","75_300_","75_325_","50_350_","50_375_","50_425_","50_450_","50_550_","50_600_","50_650_","50_675_","50_700_","50_750_","100_350_","100_375_","100_425_","100_450_","100_500_","100_525_","100_600_","100_625_","100_650_","100_675_","100_700_","100_750_","150_350_","150_375_","150_400_","150_425_","150_450_","150_475_","150_500_","150_525_","150_550_","150_575_","150_600_","150_625_","150_650_","150_675_","150_700_","150_725_","150_750_","200_400_","200_425_","200_450_","200_525_","200_650_","200_675_","200_700_","200_750_","250_425_","250_450_","250_500_","250_525_","250_550_","250_575_","250_600_","250_625_","250_650_","250_675_","250_725_","250_750_","10_350_","10_400_","10_450_","10_475_","10_525_","10_550_","10_575_","10_600_","10_625_","10_675_","10_700_","20_375_","20_400_","20_425_","20_450_","20_475_","20_500_","20_525_","20_550_","20_575_","20_600_","20_625_","20_650_","20_675_","20_725_","20_750_","30_350_","30_375_","30_400_","30_450_","30_475_","30_500_","30_525_","30_575_","30_600_","30_625_","30_650_","30_675_","30_725_","30_750_","40_350_","40_375_","75_675_","75_700_","75_725_","50_800_","50_850_","50_875_","50_975_","100_775_","100_800_","100_825_","100_850_","100_875_","100_900_","100_925_","100_975_","100_1000_","150_825_","150_850_","150_875_","150_900_","150_925_","150_950_","150_1000_","200_800_","200_825_","200_850_","200_875_","200_900_","200_925_","200_950_","200_1000_","250_775_","250_800_","250_825_","250_850_","250_900_","250_925_","250_975_","250_1000_","300_800_","300_825_","300_850_","300_875_","300_925_","300_950_","300_1000_","350_850_","350_875_","350_900_","350_925_","350_950_","350_1000_","400_900_","400_925_","400_950_","400_975_","450_950_","450_975_","500_1000_","10_775_","10_800_","10_825_","10_850_","10_900_","10_950_","10_975_","20_775_","20_800_","20_825_","20_875_","20_950_","20_975_","20_1000_","30_775_","30_800_","30_825_","30_850_","30_875_","30_900_","40_800_","40_850_","40_875_","40_900_","40_925_","40_950_","40_975_","40_1000_","75_775_","75_800_","75_925_","75_950_","75_975_","75_1000_","50_5_","40_5_","50_15_","50_30_","40_25_","40_10_","40_30_","100_25_","100_15_","100_20_","100_30_","150_25_","150_10_","150_15_","150_30_","75_25_","75_10_","75_15_","75_20_","100_125_","100_35_","100_60_","100_70_","100_80_","100_90_","75_50_","75_30_","75_35_","75_40_","75_45_","75_60_","75_70_","75_80_","75_90_","100_5_","150_1_","150_5_","150_50_","150_35_","150_40_","150_45_","150_60_","150_70_","150_90_","200_40_","200_45_","200_80_","200_90_","250_50_","250_40_","250_45_","250_60_","250_70_","250_80_","250_90_","150_100_","150_125_","150_150_","150_200_","150_225_","150_250_","150_300_","150_325_","200_125_","200_175_","200_200_","200_250_","200_275_","200_300_","200_325_","200_375_","150_100_","150_125_","150_150_","150_200_","150_225_","150_250_","150_300_","150_325_","200_125_","200_175_","200_200_","200_250_","200_275_","200_300_","200_325_","200_375_","200_25_","200_5_","200_15_","200_20_","250_25_","250_1_","250_5_","250_10_","250_15_","250_20_","250_100_","250_150_","250_175_","250_200_","250_225_","250_250_","250_275_","250_300_","250_325_","250_350_","250_375_","250_400_","300_125_","300_175_","300_200_","300_225_","300_250_","300_275_","300_300_","300_325_","300_350_","300_375_","350_350_","300_25_","300_5_","300_10_","300_20_","350_25_","350_1_","350_5_","350_15_","350_20_","400_1_","400_5_","400_20_","300_100_","300_30_","300_35_","300_40_","300_45_","300_60_","300_70_","300_80_","300_90_","350_100_","350_30_","350_35_","350_40_","350_45_","350_60_","350_70_","400_50_","400_30_","400_35_","400_40_","400_45_","400_60_","400_70_","300_425_","300_475_","300_500_","300_525_","300_550_","300_575_","300_625_","300_675_","300_700_","300_775_","350_375_","350_450_","350_475_","350_525_","350_550_","350_625_","350_650_","350_675_","350_700_","350_725_","350_825_","400_375_","400_400_","400_450_","400_500_","400_575_","400_600_","400_625_","400_700_","400_725_","400_750_","400_775_","400_800_","400_850_","400_875_","450_350_","450_375_","450_400_","450_475_","450_500_","450_525_","450_550_","450_575_","450_650_","450_775_","450_800_","450_825_","450_850_","450_875_","450_900_","500_350_","500_375_","500_400_","500_425_","500_450_","500_525_","500_550_","500_575_","500_600_","500_625_","500_675_","500_700_","500_725_","500_750_","500_825_","500_850_","500_875_","500_950_","500_975_","550_400_","550_425_","550_450_","550_500_","550_525_","550_550_","550_575_","550_600_","550_625_","550_650_","550_675_","550_700_","550_725_","550_750_","550_775_","550_800_","550_825_","550_850_","550_875_","550_900_","550_925_","600_375_","600_400_","600_425_","600_450_","600_475_","600_525_","600_550_","600_675_","650_600_","650_650_","650_675_","650_700_","650_725_","650_775_","650_800_","650_825_","700_375_","700_400_","700_425_","700_450_","700_475_","700_500_","700_525_","700_600_","700_650_","700_700_","700_725_","700_750_","450_25_","450_50_","450_1_","450_5_","450_35_","450_45_","450_60_","450_70_","500_25_","500_50_","500_5_","500_20_","500_35_","500_40_","500_45_","550_25_","550_50_","550_1_","550_5_","550_15_","550_20_","550_30_","550_40_","550_45_","550_60_","550_70_","600_25_","600_50_","600_1_","600_5_","600_10_","600_15_","600_20_","600_30_","600_45_","600_60_","650_25_","650_50_","650_1_","650_5_","650_10_","650_15_","650_20_","650_30_","650_45_","650_60_","700_25_","700_1_","700_10_","700_20_","700_30_","700_35_","700_40_","700_45_","700_60_","700_70_","400_125_","400_225_","400_300_","400_325_","450_125_","450_175_","450_200_","450_250_","450_275_","450_80_","450_90_","500_100_","500_125_","500_200_","500_225_","500_300_","500_80_","500_90_","550_100_","550_125_","550_150_","550_225_","550_250_","550_325_","550_80_","550_90_","600_125_","600_175_","600_200_","600_225_","600_250_","600_275_","600_325_","600_80_","650_100_","650_125_","650_150_","650_175_","650_200_","650_250_","650_300_","650_80_","700_100_","700_150_","700_175_","700_225_","700_250_","700_275_","700_300_","700_80_","700_90_","550_950_","550_975_","550_1000_","600_900_","600_925_","600_975_","600_1000_","650_875_","650_900_","650_925_","650_950_","650_975_","650_1000_","700_825_","700_875_","700_900_","700_925_","700_950_","750_825_","750_850_","750_900_","750_925_","750_950_","750_1000_","800_775_","800_800_","800_825_","800_850_","800_900_","800_925_","800_950_","800_975_","800_1000_","850_775_","850_800_","850_850_","850_875_","850_925_","850_950_","850_975_","850_1000_","900_775_","900_800_","900_825_","900_850_","900_875_","900_900_","900_925_","900_950_","900_975_","900_1000_","950_775_","950_900_","950_925_","950_950_","950_1000_","1000_750_","1000_775_","1000_825_","1000_850_","1000_875_","1000_900_","1000_975_","1100_750_","1100_775_","1100_800_","1100_825_","1100_850_","1100_875_","1100_925_","1100_950_","1100_975_","1200_750_","1200_775_","1200_825_","1200_850_","1200_875_","1200_900_","1200_925_","1200_950_","1200_975_","1300_750_","1300_775_","1300_800_","1300_850_","1300_875_","1300_975_","1300_1000_","1400_750_","1400_775_","1400_800_","1400_875_","1400_900_","1400_925_","1400_950_","1400_975_","1400_1000_","750_100_","750_150_","750_225_","750_250_","750_275_","750_300_","750_80_","750_90_","800_150_","800_175_","800_200_","800_225_","800_250_","800_275_","800_300_","800_80_","850_100_","850_125_","850_200_","850_250_","850_275_","850_300_","850_80_","850_90_","900_100_","900_150_","900_175_","900_200_","900_225_","900_250_","900_275_","900_90_","950_100_","950_150_","950_175_","950_200_","950_225_","950_275_","950_300_","950_80_","950_90_","1000_100_","1000_125_","1000_225_","1000_275_","1000_300_","1000_325_","1000_80_","1000_90_","1100_200_","1100_225_","1100_275_","1100_300_","1100_90_","1200_125_","1200_150_","1200_175_","1200_200_","1200_225_","1200_250_","1200_275_","1200_300_","1200_325_","1200_80_","1200_90_","1300_100_","1300_125_","1300_150_","1300_175_","1300_225_","1300_275_","1300_300_","1300_80_","1400_100_","1400_125_","1400_150_","1400_200_","1400_225_","1400_250_","1400_275_","1400_300_","1400_325_","1400_80_","1400_90_","1500_100_","1500_125_","1500_175_","1500_200_","1500_225_","1500_250_","1500_275_","1500_300_","1500_80_","1500_90_","750_325_","750_350_","750_400_","750_425_","750_450_","750_475_","750_500_","750_525_","750_550_","750_575_","750_600_","750_625_","750_650_","750_675_","750_725_","800_325_","800_350_","800_375_","800_450_","800_475_","800_525_","800_550_","800_575_","800_600_","800_625_","800_650_","800_675_","800_700_","800_725_","800_750_","850_325_","850_375_","850_400_","850_450_","850_475_","850_500_","850_525_","850_550_","850_600_","850_625_","850_650_","850_675_","850_700_","900_325_","900_400_","900_500_","900_525_","900_550_","900_600_","900_625_","900_650_","900_700_","900_725_","950_325_","950_350_","950_375_","950_400_","950_450_","950_525_","950_550_","950_575_","950_600_","950_625_","950_675_","950_700_","1000_350_","1000_450_","1000_475_","1000_525_","1000_550_","1000_575_","1000_600_","1000_625_","1000_700_","1000_725_","1100_400_","1100_475_","1100_525_","1100_575_","1100_600_","1100_625_","1100_650_","1100_675_","1100_700_","1100_725_","1200_350_","1200_375_","1200_400_","1200_425_","1200_450_","1200_475_","1200_500_","1200_550_","1200_575_","1300_700_","1300_725_","1400_375_","1400_400_","1400_425_","1400_450_","1400_500_","1400_525_","1400_550_","1400_575_","1400_625_","1400_650_","1400_675_","1400_725_","750_50_","750_1_","750_5_","750_15_","750_20_","750_30_","750_35_","750_40_","750_45_","750_60_","750_70_","800_50_","800_1_","800_10_","800_15_","800_20_","800_30_","800_35_","800_45_","800_60_","800_70_","850_25_","850_50_","850_5_","850_10_","850_15_","850_20_","850_35_","850_40_","850_60_","900_25_","900_50_","900_5_","900_10_","900_15_","900_20_","900_35_","900_40_","900_45_","900_60_","900_70_","950_50_","950_5_","950_10_","950_20_","950_35_","950_45_","950_60_","950_70_","1000_25_","1000_50_","1000_5_","1000_15_","1000_30_","1000_40_","1000_45_","1000_60_","1000_70_","1100_25_","1100_50_","1100_1_","1100_5_","1100_10_","1100_15_","1100_20_","1100_45_","1100_70_","1200_25_","1200_50_","1200_1_","1200_5_","1200_10_","1200_15_","1200_20_","1200_30_","1200_35_","1200_40_","1200_45_","1200_60_","1200_70_","1300_25_","1300_50_","1300_1_","1300_5_","1300_20_","1300_30_","1300_35_","1300_40_","1300_45_","1300_60_","1300_70_","1400_25_","1400_1_","1400_5_","1400_10_","1400_15_","1400_30_","1400_35_","1400_40_","1400_45_","1400_60_","1400_70_","1500_25_","1500_50_","1500_1_","1500_5_","1500_10_","1500_20_","1500_30_","1500_35_","1500_45_","1500_60_","1500_70_","1500_400_","1500_425_","1500_500_","1500_600_","1500_650_","1500_675_","1500_700_","1500_725_","1600_300_","1600_325_","1600_350_","1600_375_","1600_400_","1600_425_","1600_500_","1600_575_","1600_600_","1600_650_","1600_675_","1700_275_","1700_300_","1700_325_","1700_350_","1700_375_","1700_400_","1700_425_","1700_450_","1700_475_","1700_525_","1700_550_","1700_600_","1700_625_","1700_650_","1700_675_","1700_700_","1700_725_","1800_275_","1800_325_","1800_350_","1800_375_","1800_400_","1800_425_","1800_450_","1800_475_","1800_500_","1800_525_","1800_550_","1800_575_","1800_600_","1800_625_","1800_650_","1800_675_","1800_700_","1800_725_","1900_275_","1900_300_","1900_325_","1900_350_","1900_375_","1900_400_","1900_425_","1900_450_","1900_475_","1900_500_","1900_525_","1900_550_","1900_575_","1900_600_","1900_625_","1900_650_","1900_675_","1900_700_","1900_725_","2000_300_","2000_350_","2000_375_","2000_400_","2000_425_","2000_450_","2000_475_","2000_525_","2000_550_","2000_575_","2000_700_","2000_750_","2500_275_","2500_300_","2500_325_","2500_425_","2500_450_","2500_475_","2500_500_","2500_525_","2500_550_","2500_575_","2500_600_","2500_625_","2500_650_","2500_675_","2500_700_","2500_725_","1500_800_","1500_825_","1500_850_","1500_875_","1500_950_","1500_975_","1600_750_","1600_775_","1600_825_","1600_850_","1600_875_","1600_900_","1600_925_","1600_950_","1600_975_","1600_1000_","1700_775_","1700_800_","1700_875_","1700_900_","1700_925_","1700_950_","1700_975_","1700_1000_","1800_750_","1800_775_","1800_850_","1800_875_","1800_925_","1800_950_","1800_975_","1800_1000_","1900_750_","1900_775_","1900_800_","1900_825_","1900_875_","1900_900_","1900_925_","1900_975_","1900_1000_","2000_775_","2000_800_","2000_900_","2000_925_","2000_950_","2000_975_","2500_775_","2500_800_","2500_950_","2500_975_","2500_1000_","1600_25_","1600_50_","1600_125_","1600_150_","1600_175_","1600_200_","1600_225_","1600_250_","1600_5_","1600_20_","1600_30_","1600_35_","1600_70_","1600_90_","1700_25_","1700_50_","1700_100_","1700_125_","1700_150_","1700_200_","1700_225_","1700_250_","1700_1_","1700_5_","1700_10_","1700_15_","1700_20_","1700_30_","1700_35_","1700_40_","1700_60_","1700_80_","1700_90_","1800_25_","1800_50_","1800_100_","1800_125_","1800_150_","1800_175_","1800_200_","1800_225_","1800_250_","1800_1_","1800_5_","1800_10_","1800_20_","1800_30_","1800_35_","1800_40_","1800_45_","1800_60_","1800_70_","1800_90_","1900_25_","1900_50_","1900_100_","1900_125_","1900_150_","1900_175_","1900_200_","1900_225_","1900_250_","1900_1_","1900_5_","1900_20_","1900_30_","1900_35_","1900_40_","1900_45_","1900_60_","1900_70_","1900_80_","1900_90_","2000_25_","2000_50_","2000_100_","2000_125_","2000_175_","2000_200_","2000_225_","2000_250_","2000_15_","2000_20_","2000_35_","2000_40_","2000_45_","2000_80_","2000_90_","2500_25_","2500_100_","2500_125_","2500_150_","2500_175_","2500_200_","2500_225_","2500_250_","2500_1_","2500_5_","2500_10_","2500_15_","2500_30_","2500_80_","2500_90_","10_25_","10_15_","10_30_","10_35_","10_40_","10_45_","10_60_","10_80_","20_50_","20_40_","20_45_","20_60_","20_70_","20_80_","20_90_","30_40_","30_45_","30_60_","30_70_","30_80_","30_90_","20_5_","20_30_","30_25_","30_20_"}
###ZBmasses={"10000_1000_","10000_500_","10000_150_","10000_50_","10000_1_","2000_1_","1995_1000_","1000_1000_","1000_150_","1000_1_","995_500_","500_500_","500_150_","500_1_","300_50_","300_1_","295_150_","200_150_","200_50_","200_1_","100_10_","100_1_","95_50_","50_50_","50_10_","50_1_","20_1_","15_10_","10_1000_","10_500_","10_150_","10_50_","10_10_","10_1_"}

if "2HDM" not in variable :                                                                                                                 
    for ma0 in ZBmasses :
        print 'bsub -q 8nh -o jobs/' + ZB + '_' + ma0 + '_' + cut + '_'  + channel + '_' + variable + '_Combination.out -e jobs/' + ZB + '_' + ma0 + '_' + cut + '_' + channel + '_' + variable + '_Combination.err /afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/monoHWW/Apr2017/submitMonoHCombination.sh ' + channel + ' ' + variable + ' ' + cut + ' ' + ZB + ' ' + ma0
        os.system('bsub -q 8nh -o jobs/' + ZB + '_' + ma0 + '_' + cut + '_'  + channel + '_' + variable + '_Combination.out -e jobs/' + ZB + '_' + ma0 + '_' + cut + '_' + channel + '_' + variable + '_Combination.err /afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/monoHWW/Apr2017/submitMonoHCombination.sh ' + channel + ' ' + variable + ' ' + cut + ' ' + ZB + ' ' + ma0)
        time.sleep(5)
        #os.system('.//afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/monoHWW/Apr2017/submitMonoH.sh ' + channel + ' ' + variable + ' ' + cut + ' ' + ZB + ' ' + ma0)


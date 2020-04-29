import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
################# SKIMS ########################
################################################

mcProduction = 'Summer16_102X_nAODv5_Full2016v6'

dataReco = 'Run2016_102X_nAODv5_Full2016v6'

mcSteps = 'MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6{var}'

fakeSteps = 'DATAl1loose2016v6__l2loose__fakeW'

fakeReco = 'Run2016_102X_nAODv5_Full2016v6_ForNewWPs'

dataSteps = 'DATAl1loose2016v6__l2loose__l2tightOR2016v6'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
        # return '/afs/cern.ch/user/y/yiiyama/public/hwwvirtual/Summer16/l2tightOR__{var}'.format(var=var)
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))
        # return '/afs/cern.ch/user/y/yiiyama/public/hwwvirtual/Summer16/l2tightOR'

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['B','Run2016B-Nano1June2019_ver2-v1'],
    ['C','Run2016C-Nano1June2019-v1'],
    ['D','Run2016D-Nano1June2019-v1'],
    ['E','Run2016E-Nano1June2019-v1'],
    ['F','Run2016F-Nano1June2019-v1'],
    ['G','Run2016G-Nano1June2019-v1'],
    ['H','Run2016H-Nano1June2019-v1']
]

DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']

DataTrig = {
    'MuonEG'         : ' Trigger_ElMu' ,
    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
    'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
}

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights

mcCommonWeight        = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeightMatched = 'XSWeight*SFweight*PromptGenLepMatch3l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight': mcCommonWeightMatched + '*nllW', # temporary - nllW module not run on PS and UE variation samples
    # 'weight': mcCommonWeightMatched + '*nllWOTF', # temporary
    'FilesPerJob': 5
}

######## Vg ########

samples['Wg'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM'),
    'weight': "*".join([mcCommonWeight, "(Gen_ZGstar_mass <= 0)"]),
    'FilesPerJob': 4
}
samples['Zg'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'Zg'),
    'weight': "*".join([mcCommonWeight, "(Gen_ZGstar_mass <= 0)"]),
    # 'FilesPerJob': 4
    'FilesPerJob': 1
}

######## VgS ########

samples['WgS'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM'),
    'weight': "*".join([mcCommonWeightMatched, "(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)"]),
    'FilesPerJob': 4,
}
samples['ZgS'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'Zg'),
    'weight': "*".join([mcCommonWeightMatched, "(Gen_ZGstar_mass > 0)"]),
    # 'FilesPerJob': 4,
    'FilesPerJob': 1,
}

############ ZZ ############

samples['ZZ'] = {
    'name': nanoGetSampleFiles(mcDirectory,'ZZTo4L'),
    'weight': mcCommonWeightMatched,
    # 'FilesPerJob' : 5,
    'FilesPerJob' : 1,
}

############ WZ ############

samples['WZ'] = {
    'name': nanoGetSampleFiles(mcDirectory,'WZTo3LNu_mllmin01'),
    'weight': mcCommonWeightMatched,
    # 'FilesPerJob' : 5,
    'FilesPerJob' : 2,
}
addSampleWeight(samples,'WZ','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass>=0.1)')

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeightMatched,
    'FilesPerJob': 4
}

###########################################
#############   SIGNALS  ##################
###########################################

signals = []

############ WH H->WW ############

samples['WH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125'),
    'weight': mcCommonWeightMatched,
    'FilesPerJob': 4
}

signals.append('WH_hww')

############ H->TauTau ############

samples['H_htt'] = {
    'name':  nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToTauTau_M125')
           + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125')
           + nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125')
           + nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125')
           + nanoGetSampleFiles(mcDirectory, 'HZJ_HToTauTau_M125'),
    'weight': mcCommonWeightMatched,
    'FilesPerJob': 4
}
signals.append('H_htt')


###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 100
  # 'FilesPerJob': 50
  # 'FilesPerJob': 25
}

for _, sd in DataRun:
  for pd in DataSets:
    if ('2016E' in sd and 'MuonEG' in pd):
      files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd.replace('v1', 'v3'))

    else:
      files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 200
  # 'FilesPerJob': 25
}

for _, sd in DataRun:
  for pd in DataSets:
    if ('2016E' in sd and 'MuonEG' in pd):
      files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd.replace('v1', 'v3'))
      print(files)

    else:
      files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
      print(files)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))



# example of configuration file
tag = 'HWWhighMass2016_SF_embeddedWeights_mm_VBF'

# used by mkShape to define output directory for root files
outputDir = 'rootFile_SF_mm_VBF'

# file with list of variables
variablesFile = 'variables_SF.py'

# file with list of cuts
cutsFile = 'cuts_mm.py' 

# file with list of samples
samplesFile = 'samples_SF_mm.py' 

# file with list of samples
plotFile = 'plot_SF.py' 

# luminosity to normalize to (in 1/fb)
lumi = 35.9

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plotHWWhighMass_SF_mm'

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards_SF_mm_VBF'

# structure file for datacard
structureFile = 'structure_SF_merge.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances_SF_mm.py'
#nuisancesFile = 'nuisances_VUOTO.py'

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'EPOSLHC_Nov2017_PbPb5020GeV_accre200kv1'
config.General.workArea = 'crab_EPOSLHC_Nov2017_PbPb5020GeV_accre200kv1'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'ReggeGribovPartonMC_EposLHC_5020GeV_PbPb_cfi_py_GEN_SIM.py'

config.Data.outputPrimaryDataset = 'MinBias'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 20
NJOBS = 10000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/tuos/EPOSLHC/crab/Nov2017PbPb5020GeV/200kv1'
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_EPOSLHC_Nov2017_PbPb5020GeV_accre200kv1'

config.Site.storageSite = 'T2_US_Vanderbilt'



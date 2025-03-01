import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',          action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',             action='store_true',    help="Update current entry in db?")
    argParser.add_argument('--check_completeness', action='store_true',    help="Check competeness?")
    return argParser
    
# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite
    if options.update:
        ov = 'update'
else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

# Redirector
try:
    redirector = sys.modules['__main__'].redirector
except:
    if "clip" in os.getenv("HOSTNAME").lower():
        if __name__ == "__main__" and not options.check_completeness:
            from Samples.Tools.config import redirector_global as redirector
        else:
            from Samples.Tools.config import redirector_clip as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_Run2017_ULnanoAODv2.sql'
logger.info("Using db file: %s", dbFile)

# DoubleMuon
DoubleMuon_Run2017B_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2017B_UL",        "/DoubleMuon/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2017C_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2017C_UL",        "/DoubleMuon/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2017D_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2017D_UL",        "/DoubleMuon/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2017E_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2017E_UL",        "/DoubleMuon/Run2017E-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2017F_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2017F_UL",        "/DoubleMuon/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
#DoubleMuon_Run2017G_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2017G_UL",        "/DoubleMuon/Run2017G-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

DoubleMuon = [
    DoubleMuon_Run2017B_UL,
    DoubleMuon_Run2017C_UL,
    DoubleMuon_Run2017D_UL,
    DoubleMuon_Run2017E_UL,
    DoubleMuon_Run2017F_UL,
    #DoubleMuon_Run2017G_UL,
]

# MuonEG
MuonEG_Run2017B_UL       = Sample.nanoAODfromDAS("MuonEG_Run2017B_UL",        "/MuonEG/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2017C_UL       = Sample.nanoAODfromDAS("MuonEG_Run2017C_UL",        "/MuonEG/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2017D_UL       = Sample.nanoAODfromDAS("MuonEG_Run2017D_UL",        "/MuonEG/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2017E_UL       = Sample.nanoAODfromDAS("MuonEG_Run2017E_UL",        "/MuonEG/Run2017E-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2017F_UL       = Sample.nanoAODfromDAS("MuonEG_Run2017F_UL",        "/MuonEG/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

MuonEG = [
    MuonEG_Run2017B_UL,
    MuonEG_Run2017C_UL,
    MuonEG_Run2017D_UL,
    MuonEG_Run2017E_UL,
    MuonEG_Run2017F_UL,

]

# DoubleEG
DoubleEG_Run2017B_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2017B_UL",        "/DoubleEG/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2017C_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2017C_UL",        "/DoubleEG/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2017D_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2017D_UL",        "/DoubleEG/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2017E_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2017E_UL",        "/DoubleEG/Run2017E-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2017F_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2017F_UL",        "/DoubleEG/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

DoubleEG = [
    DoubleEG_Run2017B_UL,
    DoubleEG_Run2017C_UL,
    DoubleEG_Run2017D_UL,
    DoubleEG_Run2017E_UL,
    DoubleEG_Run2017F_UL,

]

# SingleMuon
SingleMuon_Run2017B_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2017B_UL",        "/SingleMuon/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2017C_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2017C_UL",        "/SingleMuon/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2017D_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2017D_UL",        "/SingleMuon/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2017E_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2017E_UL",        "/SingleMuon/Run2017E-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2017F_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2017F_UL",        "/SingleMuon/Run2017F-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
#SingleMuon_Run2017G_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2017G_UL",        "/SingleMuon/Run2017G-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

SingleMuon = [
    SingleMuon_Run2017B_UL,
    SingleMuon_Run2017C_UL,
    SingleMuon_Run2017D_UL,
    SingleMuon_Run2017E_UL,
    SingleMuon_Run2017F_UL,
    #SingleMuon_Run2017G_UL,

]

# SingleElectron
SingleElectron_Run2017B_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2017B_UL",        "/SingleElectron/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2017C_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2017C_UL",        "/SingleElectron/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2017D_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2017D_UL",        "/SingleElectron/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2017E_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2017E_UL",        "/SingleElectron/Run2017E-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2017F_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2017F_UL",        "/SingleElectron/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

SingleElectron = [
    SingleElectron_Run2017B_UL,
    SingleElectron_Run2017C_UL,
    SingleElectron_Run2017D_UL,
    SingleElectron_Run2017E_UL,
    SingleElectron_Run2017F_UL,

]

# JetHT
JetHT_Run2017B_UL       = Sample.nanoAODfromDAS("JetHT_Run2017B_UL",        "/JetHT/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2017C_UL       = Sample.nanoAODfromDAS("JetHT_Run2017C_UL",        "/JetHT/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2017D_UL       = Sample.nanoAODfromDAS("JetHT_Run2017D_UL",        "/JetHT/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2017E_UL       = Sample.nanoAODfromDAS("JetHT_Run2017E_UL",        "/JetHT/Run2017E-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2017F_UL       = Sample.nanoAODfromDAS("JetHT_Run2017F_UL",        "/JetHT/Run2017F-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

JetHT = [
    JetHT_Run2017B_UL,
    JetHT_Run2017C_UL,
    JetHT_Run2017D_UL,
    JetHT_Run2017E_UL,
    JetHT_Run2017F_UL,
    
]

# MET
#MET_Run2017A_UL       = Sample.nanoAODfromDAS("MET_Run2017A_UL",        "/MET/Run2017A-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2017B_UL       = Sample.nanoAODfromDAS("MET_Run2017B_UL",        "/MET/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2017C_UL       = Sample.nanoAODfromDAS("MET_Run2017C_UL",        "/MET/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2017D_UL       = Sample.nanoAODfromDAS("MET_Run2017D_UL",        "/MET/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2017E_UL       = Sample.nanoAODfromDAS("MET_Run2017E_UL",        "/MET/Run2017E-UL2017_MiniAODv1_NanoAODv2-v3/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2017F_UL       = Sample.nanoAODfromDAS("MET_Run2017F_UL",        "/MET/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

MET = [
    #MET_Run2017A_UL,
    MET_Run2017B_UL,
    MET_Run2017C_UL,
    MET_Run2017D_UL,
    MET_Run2017E_UL,
    MET_Run2017F_UL,
]

allSamples = DoubleMuon + MuonEG + DoubleEG + SingleMuon + SingleElectron + JetHT + MET

for s in allSamples:
    s.json      = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt")
    s.isData    = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 ) 

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
            #from Samples.Tools.config import redirector_clip_local as redirector
            from Samples.Tools.config import redirector_global as redirector
    else:
        from Samples.Tools.config import redirector as redirector
print redirector
# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_UL18_nanoAODv9.sql'

logger.info("Using db file: %s", dbFile)

################################################################################
# DY

DYJetsToLL_M10to50       = Sample.nanoAODfromDAS("DYJetsToLL_M10to50_LO",   "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=18610)
DYJetsToLL_M50           = Sample.nanoAODfromDAS("DYJetsToLL_M50",     "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2075.14*3)
# DYJetsToLL_M50_ext      = Sample.nanoAODfromDAS("DYJetsToLL_M50_ext", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2075.14*3)


DY = [
    DYJetsToLL_M10to50,
    DYJetsToLL_M50,
]

################################################################################
# ttbar

TTLep_pow_CP5       = Sample.nanoAODfromDAS("TTLep_pow_CP5",            "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",             dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*((3*0.108)**2))
TTSingleLep_pow_CP5 = Sample.nanoAODfromDAS("TTSingleLep_pow_CP5",      "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*(3*0.108)*(1-3*0.108)*2)
TTHad_pow_CP5       = Sample.nanoAODfromDAS("TTHad_pow_CP5",            "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*((1-3*0.108)**2))

TTbar = [
    TTLep_pow_CP5,
    TTSingleLep_pow_CP5,
    TTHad_pow_CP5,
]

################################################################################
# TTX 

TTHTobb         = Sample.nanoAODfromDAS("TTHTobb",   "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5085*(0.577))
TTHnobb         = Sample.nanoAODfromDAS("TTHnobb",   "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5085*(1-0.577))
# THQ                 = Sample.nanoAODfromDAS("THQ",           "/THQ_4f_Hincl_13TeV_madgraph_pythia8",                     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.07096)
# THW                 = Sample.nanoAODfromDAS("THW",           "/THW_5f_Hincl_13TeV_madgraph_pythia8",                     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1472)
TTWToLNu            = Sample.nanoAODfromDAS("TTWToLNu",      "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2043)
TTWToQQ             = Sample.nanoAODfromDAS("TTWToQQ",       "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.40620)
TTZToQQ             = Sample.nanoAODfromDAS("TTZToQQ",          "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5297)
TTZToLLNuNu         = Sample.nanoAODfromDAS("TTZToLLNuNu",        "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2728)
TTZToLLNuNu_m1to10  = Sample.nanoAODfromDAS("TTZToLLNuNu_m1to10", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0493)
TTZ_LO              = Sample.nanoAODfromDAS("TTZ_LO",           "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5297/0.692)


TTX = [
    TTHTobb,
    TTHnobb,
    # THQ,
    # THW,
    TTWToLNu,
    TTWToQQ,
    TTZToQQ,
    TTZToLLNuNu,
    TTZToLLNuNu_m1to10,
    TTZ_LO,
]

################################################################################
# single top 

T_tch_pow           = Sample.nanoAODfromDAS("T_tch_pow",        "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=136.02) # inclusive sample
TBar_tch_pow        = Sample.nanoAODfromDAS("TBar_tch_pow",     "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=80.95) # inclusive sample
T_tWch              = Sample.nanoAODfromDAS("T_tWch",           "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
TBar_tWch           = Sample.nanoAODfromDAS("TBar_tWch",        "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect

tZq_ll              = Sample.nanoAODfromDAS("tZq_ll",           "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.09418 ) #0.0758 )

tWll_thad_Wlept_DR  = Sample.nanoAODfromDAS("tWll_thad_Wlept_DR",  "/TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
tWll_thad_Wlept_DS  = Sample.nanoAODfromDAS("tWll_thad_Wlept_DS",  "/TWZToLL_thad_Wlept_5f_DS_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
tWll_tlept_Whad_DR  = Sample.nanoAODfromDAS("tWll_tlept_Whad_DR",  "/TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
tWll_tlept_Whad_DS  = Sample.nanoAODfromDAS("tWll_tlept_Whad_DS",  "/TWZToLL_tlept_Whad_5f_DS_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
tWll_tlept_Wlept_DR = Sample.nanoAODfromDAS("tWll_tlept_Wlept_DR", "/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.001501 )
tWll_tlept_Wlept_DS = Sample.nanoAODfromDAS("tWll_tlept_Wlept_DS", "/TWZToLL_tlept_Wlept_5f_DS_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.001501 )


SingleTop = [
    T_tch_pow,
    TBar_tch_pow,
    T_tWch,
    TBar_tWch,
    tZq_ll,
    tWll_thad_Wlept_DR,
    tWll_thad_Wlept_DS,
    tWll_tlept_Whad_DR,
    tWll_tlept_Whad_DS,
    tWll_tlept_Wlept_DR,
    tWll_tlept_Wlept_DS,
]

################################################################################
# multiboson

# VVTo2L2Nu           = Sample.nanoAODfromDAS("VVTo2L2Nu",            "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/",                  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=14.00)
WW                  = Sample.nanoAODfromDAS("WW",                   "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=63.21 * 1.82)
WZ                  = Sample.nanoAODfromDAS("WZ",                   "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=47.13)
ZZ                  = Sample.nanoAODfromDAS("ZZ",                   "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=16.523)
WWW_4F              = Sample.nanoAODfromDAS("WWW_4F",               "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",            dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2086)
WWZ_4F              = Sample.nanoAODfromDAS("WWZ_4F",               "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",            dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1651)
WZZ                 = Sample.nanoAODfromDAS("WZZ",                  "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.05565)
ZZZ                 = Sample.nanoAODfromDAS("ZZZ",                  "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.01398)
WZTo3LNu            = Sample.nanoAODfromDAS("WZTo3LNu",             "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.42965)

multiboson = [
    # VVTo2L2Nu,
    WW,
    WZ,
    ZZ,
    WWW_4F,
    WWZ_4F,
    WZZ,
    ZZZ,
    WZTo3LNu
]

################################################################################
## rare
TTTT = Sample.nanoAODfromDAS("TTTT", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.009103)
TTWW = Sample.nanoAODfromDAS("TTWW", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.007829)
TTWZ = Sample.nanoAODfromDAS("TTWZ", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.002919)
TTZZ = Sample.nanoAODfromDAS("TTZZ", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.001573)

rareTop = [
    TTTT,
    TTWW,
    TTWZ,
    TTZZ,
]
################################################################################
## QCD mu enriched
## XS from GenXSecAnalyzer (AN2020_170_v7 from TOP-20-010 or UHH data base)

QCD_MuEnriched_15to20 = Sample.nanoAODfromDAS("QCD_MuEnriched_15to20", "/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=2810000)
QCD_MuEnriched_20to30 = Sample.nanoAODfromDAS("QCD_MuEnriched_20to30", "/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=2530000)
QCD_MuEnriched_30to50 = Sample.nanoAODfromDAS("QCD_MuEnriched_30to50", "/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=1370000)
QCD_MuEnriched_50to80 = Sample.nanoAODfromDAS("QCD_MuEnriched_50to80", "/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=378000)
QCD_MuEnriched_80to120 = Sample.nanoAODfromDAS("QCD_MuEnriched_80to120", "/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=88600)
QCD_MuEnriched_120to170 = Sample.nanoAODfromDAS("QCD_MuEnriched_120to170", "/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=21200)
QCD_MuEnriched_170to300 = Sample.nanoAODfromDAS("QCD_MuEnriched_170to300", "/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=7020)
QCD_MuEnriched_300to470 = Sample.nanoAODfromDAS("QCD_MuEnriched_300to470", "/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=620)
QCD_MuEnriched_470to600 = Sample.nanoAODfromDAS("QCD_MuEnriched_470to600", "/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=59.1)
QCD_MuEnriched_600to800 = Sample.nanoAODfromDAS("QCD_MuEnriched_600to800", "/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=18.2)
QCD_MuEnriched_800to1000 = Sample.nanoAODfromDAS("QCD_MuEnriched_800to1000", "/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=3.28)
QCD_MuEnriched_1000toInf = Sample.nanoAODfromDAS("QCD_MuEnriched_1000toInf", "/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=1.08)

QCD_MuEnriched = [
    QCD_MuEnriched_15to20,
    QCD_MuEnriched_20to30,
    QCD_MuEnriched_30to50,
    QCD_MuEnriched_50to80,
    QCD_MuEnriched_80to120,
    QCD_MuEnriched_120to170,
    QCD_MuEnriched_170to300,
    QCD_MuEnriched_300to470,
    QCD_MuEnriched_470to600,
    QCD_MuEnriched_600to800,
    QCD_MuEnriched_800to1000,
    QCD_MuEnriched_1000toInf,
]
################################################################################
## QCD em enriched
## XS from GenXSecAnalyzer (AN2020_170_v7 from TOP-20-010 or UHH data base)

QCD_EMEnriched_15to20 = Sample.nanoAODfromDAS("QCD_EMEnriched_15to20", "/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=1320000)
QCD_EMEnriched_20to30 = Sample.nanoAODfromDAS("QCD_EMEnriched_20to30", "/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=4910000)
QCD_EMEnriched_30to50 = Sample.nanoAODfromDAS("QCD_EMEnriched_30to50", "/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=6420000)
QCD_EMEnriched_50to80 = Sample.nanoAODfromDAS("QCD_EMEnriched_50to80", "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=1990000)
QCD_EMEnriched_80to120 = Sample.nanoAODfromDAS("QCD_EMEnriched_80to120", "/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=367000)
QCD_EMEnriched_120to170 = Sample.nanoAODfromDAS("QCD_EMEnriched_120to170", "/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=66500)
QCD_EMEnriched_170to300 = Sample.nanoAODfromDAS("QCD_EMEnriched_170to300", "/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=16600)
QCD_EMEnriched_300toInf = Sample.nanoAODfromDAS("QCD_EMEnriched_300toInf", "/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=1100)

QCD_EMEnriched = [
    QCD_EMEnriched_15to20,
    QCD_EMEnriched_20to30,
    QCD_EMEnriched_30to50,
    QCD_EMEnriched_50to80,
    QCD_EMEnriched_80to120,
    QCD_EMEnriched_120to170,
    QCD_EMEnriched_170to300,
    QCD_EMEnriched_300toInf,
]

################################################################################
## QCD bcToE 
## XS from GenXSecAnalyzer (AN2020_170_v7 from TOP-20-010 or UHH data base)

QCD_bcToE_15to20 = Sample.nanoAODfromDAS("QCD_bcToE_15to20", "/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=187000)
QCD_bcToE_20to30 = Sample.nanoAODfromDAS("QCD_bcToE_20to30", "/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=305000)
QCD_bcToE_30to80 = Sample.nanoAODfromDAS("QCD_bcToE_30to80", "/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=361000)
QCD_bcToE_80to170 = Sample.nanoAODfromDAS("QCD_bcToE_80to170", "/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=33800)
QCD_bcToE_170to250 = Sample.nanoAODfromDAS("QCD_bcToE_170to250", "/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=2130) # NanoAODv9 not available
QCD_bcToE_250toInf = Sample.nanoAODfromDAS("QCD_bcToE_250toInf", "/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=563)

QCD_bcToE = [
    QCD_bcToE_15to20,
    QCD_bcToE_20to30,
    QCD_bcToE_30to80,
    QCD_bcToE_80to170,
    QCD_bcToE_170to250,
    QCD_bcToE_250toInf,
]

################################################################################

QCD = QCD_MuEnriched + QCD_EMEnriched + QCD_bcToE

################################################################################
# W+jets 
WJetsToLNu = Sample.nanoAODfromDAS("WJetsToLNu", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=61500)


################################################################################
allSamples = DY + TTbar + SingleTop + multiboson + TTX + rareTop + QCD + [WJetsToLNu]

for s in allSamples:
    s.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=10 )

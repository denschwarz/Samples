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
dbFile = dbDir+'/DB_UL17_nanoAODv2.sql'

logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_LO        = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO",	    "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2075.14*3)
DYJetsToLL_M10to50_LO    = Sample.nanoAODfromDAS("DYJetsToLL_M10to50_LO",   "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=18610)
#DYJetsToLL_M50           = Sample.nanoAODfromDAS("DYJetsToLL_M50",          "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=2075.14*3)
# DYJetsToLL_M10to50       = Sample.nanoAODfromDAS("DYJetsToLL_M10to50",      "",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=18610)


#DYJetsToLL_M50_HT70to100       =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT70to100"    ,     "",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=169.9*1.23)
DYJetsToLL_M50_HT100to200      =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT100to200",        "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=147.4*1.23)
DYJetsToLL_M50_HT200to400      =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400",        "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=40.99*1.23)
DYJetsToLL_M50_HT400to600      =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600",        "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.678*1.23)
DYJetsToLL_M50_HT600to800      =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT600to800"   ,     "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.367*1.23 )
DYJetsToLL_M50_HT800to1200     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT800to1200"  ,     "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.6304*1.23 )
DYJetsToLL_M50_HT1200to2500    =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT1200to2500" ,     "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1514*1.23 )
DYJetsToLL_M50_HT2500toInf     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT2500toInf"  ,     "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003565*1.23 )

DYJetsM50HT = [
    #DYJetsToLL_M50_HT70to100   , 
    DYJetsToLL_M50_HT100to200,
    DYJetsToLL_M50_HT200to400,
    DYJetsToLL_M50_HT400to600,
    DYJetsToLL_M50_HT600to800  ,
    DYJetsToLL_M50_HT800to1200 ,
    DYJetsToLL_M50_HT1200to2500,
    DYJetsToLL_M50_HT2500toInf ,
]

#DYJetsToLL_M5to50_HT70to100      = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT70to100"     , "",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=303.4) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT100to200     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT100to200"    , "",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=224.2) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT100to200_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT100to200_ext", "",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=224.2) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT200to400     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT200to400"    , "",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=37.2) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT200to400_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT200to400_ext", "",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=37.2) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT400to600     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT400to600"    , "",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3.581) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT400to600_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT400to600_ext", "",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3.581) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT600toInf     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT600toInf"    , "",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.124) #LO without 1.23 k-factor

#DYJetsM5to50HT = [
#    DYJetsToLL_M5to50_HT70to100,
#    DYJetsToLL_M5to50_HT100to200,
#    DYJetsToLL_M5to50_HT100to200_ext,
#    DYJetsToLL_M5to50_HT200to400,
#    DYJetsToLL_M5to50_HT200to400_ext,
#    DYJetsToLL_M5to50_HT400to600,
#    DYJetsToLL_M5to50_HT400to600_ext,
#    DYJetsToLL_M5to50_HT600toInf,
#]

# x-secs using runXSecAnalyzer
DYJetsToNuNu_HT100to200       = Sample.nanoAODfromDAS("DYJetsToNuNu_HT100to200",       "/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=280.35*1.23)
DYJetsToNuNu_HT200to400       = Sample.nanoAODfromDAS("DYJetsToNuNu_HT200to400",       "/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=77.67*1.23)
DYJetsToNuNu_HT400to600       = Sample.nanoAODfromDAS("DYJetsToNuNu_HT400to600",       "/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=10.73*1.23)
DYJetsToNuNu_HT600to800       = Sample.nanoAODfromDAS("DYJetsToNuNu_HT600to800",       "/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2.559*1.23)
DYJetsToNuNu_HT800to1200      = Sample.nanoAODfromDAS("DYJetsToNuNu_HT800to1200",      "/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.1796*1.23)
DYJetsToNuNu_HT1200to2500     = Sample.nanoAODfromDAS("DYJetsToNuNu_HT1200to2500",     "/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.28833*1.23)
DYJetsToNuNu_HT2500toInf      = Sample.nanoAODfromDAS("DYJetsToNuNu_HT2500toInf",      "/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.006945*1.23)

DYJetsNuNuHT = [
   DYJetsToNuNu_HT100to200,
   DYJetsToNuNu_HT200to400,
   DYJetsToNuNu_HT400to600,
   DYJetsToNuNu_HT600to800,
   DYJetsToNuNu_HT800to1200,
   DYJetsToNuNu_HT1200to2500,
   DYJetsToNuNu_HT2500toInf,
]

#DYJetsToNuNu_PT100to200      = Sample.nanoAODfromDAS("DYJetsToNuNu_PT100to200",     "",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.99*1.23)
##DYJetsToNuNu_PT100to200_ext = Sample.nanoAODfromDAS("DYJetsToNuNu_PT100to200_ext", "",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.99*1.23)
#DYJetsToNuNu_PT200toInf      = Sample.nanoAODfromDAS("DYJetsToNuNu_PT200toInf",     "",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.201*1.23)
##DYJetsToNuNu_PT200toInf_ext = Sample.nanoAODfromDAS("DYJetsToNuNu_PT200toInf_ext", "",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.201*1.23)

#DYJetsNuNuPT = [
    #DYJetsToNuNu_PT100to200,
    #DYJetsToNuNu_PT100to200_ext,
    #DYJetsToNuNu_PT200toInf,
    #DYJetsToNuNu_PT200toInf_ext,
#]

DY = [
    #DYJetsToLL_M10to50,
    DYJetsToLL_M10to50_LO,
    DYJetsToLL_M50_LO,
    #DYJetsToLL_M50,
#] + DYJetsM50HT + DYJetsM5to50HT + DYJetsNuNuHT + DYJetsNuNuPT
]  + DYJetsNuNuHT + DYJetsM50HT 

## ttbar
TTLep_pow_CP5       = Sample.nanoAODfromDAS("TTLep_pow_CP5",            "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",             dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*((3*0.108)**2))
#TTLep_pow_noSC      = Sample.nanoAODfromDAS("TTLep_pow_noSC",       "",                dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*((3*0.108)**2))
TTSingleLep_pow_CP5 = Sample.nanoAODfromDAS("TTSingleLep_pow_CP5",      "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*(3*0.108)*(1-3*0.108)*2)
#TTbar               = Sample.nanoAODfromDAS("TTbar",                "",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762)
TTJets_amcatnlo     = Sample.nanoAODfromDAS("TTJets_amcatnlo",          "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762)
TTHad_pow_CP5       = Sample.nanoAODfromDAS("TTHad_pow_CP5",            "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*((1-3*0.108)**2))

## single top
#TToLeptons_sch_amcatnlo = Sample.nanoAODfromDAS("TToLeptons_sch_amcatnlo", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=(7.20+4.16)*0.108*3)
#TToHad_sch              = Sample.nanoAODfromDAS("TToHad_sch",              "",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=(7.20+4.16)*(1-0.108*3))
#
#T_tch_pow           = Sample.nanoAODfromDAS("T_tch_pow",        "/ST_t-channel_top_5f_TuneCP5_13TeV-powheg-pythia8/",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=136.02) # inclusive sample
#TBar_tch_pow        = Sample.nanoAODfromDAS("TBar_tch_pow",     "",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=80.95) # inclusive sample
#
T_tWch_ext          = Sample.nanoAODfromDAS("T_tWch_ext",       "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
TBar_tWch_ext       = Sample.nanoAODfromDAS("TBar_tWch_ext",    "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect

#T_tWch_incl         = Sample.nanoAODfromDAS("T_tWch_incl",      "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.85)
#TBar_tWch_incl      = Sample.nanoAODfromDAS("TBar_tWch_incl",   "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.85)

## ttH
#TTHbb_pow           = Sample.nanoAODfromDAS("TTHbb_pow",        "/ttHTobb_M125_13TeV_powheg_pythia8/",                                 dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5085*(0.577)) #powheg samples previously
#TTHnobb_pow         = Sample.nanoAODfromDAS("TTHnobb_pow",      "/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5085*(1-0.577)) 

TTHbb               = Sample.nanoAODfromDAS("TTHbb",            "/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5085*(0.577))
TTHnobb             = Sample.nanoAODfromDAS("TTHnobb",          "/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5085*(1-0.577))

#THQ                 = Sample.nanoAODfromDAS("THQ",              "",                     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.07096)
#THW                 = Sample.nanoAODfromDAS("THW",              "",                     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1472)

## ttV
#TGJets              = Sample.nanoAODfromDAS("TGJets",           "", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2.967)
#TGJets_ext          = Sample.nanoAODfromDAS("TGJets_ext",       "", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2.967)
#TGJets_lep          = Sample.nanoAODfromDAS("TGJets_lep",       "", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2.967*0.108*3)
tZq_ll               = Sample.nanoAODfromDAS("tZq_ll",           "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",                             dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.09418 ) #0.0758 )
#tWll                = Sample.nanoAODfromDAS("tWll",             "/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/",                              dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.01123)
#tWnunu              = Sample.nanoAODfromDAS("tWnunu",           "/ST_tWnunu_5f_LO_13TeV-MadGraph-pythia8/",                            dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.01123*1.9822)
TTWToLNu_CP5        = Sample.nanoAODfromDAS("TTWToLNu_CP5" ,    "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2043)
#TTWToQQ             = Sample.nanoAODfromDAS("TTWToQQ",          "/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.40620)
TTZToQQ             = Sample.nanoAODfromDAS("TTZToQQ",           "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",                  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5297)
TTZToLLNuNu         = Sample.nanoAODfromDAS("TTZToLLNuNu",       "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2728)
#TTZToLLNuNu_m1to10  = Sample.nanoAODfromDAS("TTZToLLNuNu_m1to10", "/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0493)
#TTZ_LO              = Sample.nanoAODfromDAS("TTZ_LO",           "/ttZJets_13TeV_madgraphMLM-pythia8/",                                 dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5297/0.692)
TTGJets             = Sample.nanoAODfromDAS("TTGJets",           "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3.697)

## fixed samples!!
#TTGHad_LO                   = Sample.nanoAODfromDAS("TTGHad_LO",             "/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.213*2.565)
#TTGHad_ptG100To200_LO       = Sample.nanoAODfromDAS("TTGHad_ptG100To200_LO", "/TTGamma_Hadronic_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1273*2.565)
#TTGHad_ptG200_LO            = Sample.nanoAODfromDAS("TTGHad_ptG200_LO",      "/TTGamma_Hadronic_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.02727*2.565)

#TTGSingleLep_LO             = Sample.nanoAODfromDAS("TTGSingleLep_LO",             "/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.125*1.994)
#TTGSingleLep_TuneUp_LO      = Sample.nanoAODfromDAS("TTGSingleLep_TuneUp_LO",      "/TTGamma_SingleLept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.125*1.994)
#TTGSingleLep_TuneDown_LO    = Sample.nanoAODfromDAS("TTGSingleLep_TuneDown_LO",    "/TTGamma_SingleLept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.125*1.994)
#TTGSingleLep_erdOn_LO       = Sample.nanoAODfromDAS("TTGSingleLep_erdOn_LO",       "/TTGamma_SingleLept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.125*1.994)
#TTGSingleLep_ptG100To200_LO = Sample.nanoAODfromDAS("TTGSingleLep_ptG100To200_LO", "/TTGamma_SingleLept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1334*1.994)
#TTGSingleLep_ptG200_LO      = Sample.nanoAODfromDAS("TTGSingleLep_ptG200_LO",      "/TTGamma_SingleLept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.02735*1.994)

TTGLep_LO                   = Sample.nanoAODfromDAS("TTGLep_LO",             "/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.512*1.616)
#TTGLep_TuneUp_LO            = Sample.nanoAODfromDAS("TTGLep_TuneUp_LO",      "/TTGamma_Dilept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.512*1.616)
#TTGLep_TuneDown_LO          = Sample.nanoAODfromDAS("TTGLep_TuneDown_LO",    "/TTGamma_Dilept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.512*1.616)
#TTGLep_erdOn_LO             = Sample.nanoAODfromDAS("TTGLep_erdOn_LO",       "/TTGamma_Dilept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.512*1.616)
#TTGLep_ptG100To200_LO       = Sample.nanoAODfromDAS("TTGLep_ptG100To200_LO", "/TTGamma_Dilept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.03469*1.616)
#TTGLep_ptG200_LO            = Sample.nanoAODfromDAS("TTGLep_ptG200_LO",      "/TTGamma_Dilept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.006874*1.616)
TTV = [TTGLep_LO, tZq_ll, TTZToQQ, TTGLep_LO, TTWToLNu_CP5 ]
#TTV = [
#    TGJets,
#    TGJets_ext,
#    TGJets_lep,
#    TTGHad_LO,
#    TTGHad_ptG100To200_LO,
#    TTGHad_ptG200_LO,
#    TTGSingleLep_LO,
#    TTGSingleLep_TuneUp_LO,
#    TTGSingleLep_TuneDown_LO,
#    TTGSingleLep_erdOn_LO,
#    TTGSingleLep_ptG100To200_LO,
#    TTGSingleLep_ptG200_LO,
#    TTGLep_LO,
#    TTGLep_TuneUp_LO,
#    TTGLep_TuneDown_LO,
#    TTGLep_erdOn_LO,
#    TTGLep_ptG100To200_LO,
#    TTGLep_ptG200_LO,
#    tZq_ll_ext,
#    tWll,
#    tWnunu,
#    TTWToLNu_ext2,
#    TTWToQQ,
#    TTZToQQ,
#    TTZToLLNuNu_ext2,
#    TTZToLLNuNu_ext3,
#    TTZToLLNuNu_m1to10,
#    TTZ_LO,
#    TTGJets,
#    TTGJets_ext,
#]

TTVV = [
    ]

top = [
    
    #TTLep_pow_noSC,
    #TTbar,
    TTLep_pow_CP5,
    TTSingleLep_pow_CP5,
    TTHad_pow_CP5,
    #TToLeptons_sch_amcatnlo,
    TTJets_amcatnlo,
    #T_tch_pow,
    #TBar_tch_pow,
    T_tWch_ext,
    TBar_tWch_ext,
    #T_tWch_incl,
    #TBar_tWch_incl,
    TTHbb,
    TTHnobb,
    #THQ,
    #THW,
    ] + TTV + TTVV

## di/multiboson
WWTo2L2Nu           = Sample.nanoAODfromDAS("WWTo2L2Nu",        "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",                dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=12.178)
#WWToLNuQQ           = Sample.nanoAODfromDAS("WWToLNuQQ",        "/WWToLNuQQ_13TeV-powheg/",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=49.997)
#WWTo1L1Nu2Q         = Sample.nanoAODfromDAS("WWTo1L1Nu2Q",      "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=49.997 )
#WWTo4Q              = Sample.nanoAODfromDAS("WWTo4Q",           "/WWTo4Q_13TeV-powheg/",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=51.723 )

ZZTo2L2Nu           = Sample.nanoAODfromDAS("ZZTo2L2Nu",        "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",                dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.564)
#ZZTo2L2Q            = Sample.nanoAODfromDAS("ZZTo2L2Q",             "/ZZTo2L2Q_13TeV_powheg_pythia8/",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3.28)
#ZZTo2Q2Nu           = Sample.nanoAODfromDAS("ZZTo2Q2Nu",            "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.04)
#ZZTo4L              = Sample.nanoAODfromDAS("ZZTo4L",               "/ZZTo4L_13TeV_powheg_pythia8/",                           dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.256*1.1)

#WZTo1L3Nu           = Sample.nanoAODfromDAS("WZTo1L3Nu"  ,          "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=(47.13)*(3*0.108)*(0.2) )
#WZTo1L1Nu2Q         = Sample.nanoAODfromDAS("WZTo1L1Nu2Q",          "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=10.71)
#WZTo2L2Q            = Sample.nanoAODfromDAS("WZTo2L2Q"   ,          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/",           dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.60)
#WZTo3LNu            = Sample.nanoAODfromDAS("WZTo3LNu",             "/WZTo3LNu",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.42965)
#WZTo3LNu_ext        = Sample.nanoAODfromDAS("WZTo3LNu_ext",         "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.42965)
#WZTo3LNu_amcatnlo   = Sample.nanoAODfromDAS("WZTo3LNu_amcatnlo",    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.666)
#WZTo2Q2Nu           = Sample.nanoAODfromDAS("WZTo2Q2Nu"   ,         "/WZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/",           dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=6.317)

#VVTo2L2Nu           = Sample.nanoAODfromDAS("VVTo2L2Nu",            "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=11.95)
#VVTo2L2Nu_ext       = Sample.nanoAODfromDAS("VVTo2L2Nu_ext",        "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=11.95)


WGToLNuG                = Sample.nanoAODfromDAS("WGToLNuG", 	     "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=377.7*1.295) # NLO xsec from TOP-17-016 for 2016
WGToLNuG_amcatnlo       = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo", "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=203.3) 

#ZGTo2LG_ext         = Sample.nanoAODfromDAS("ZGTo2LG_ext",          "/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=131.3)
ZGToLLG             = Sample.nanoAODfromDAS("ZGToLLG",              "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=50.2)
#ZGToLLG_lowMLL      = Sample.nanoAODfromDAS("ZGToLLG_lowMLL",       "/ZGToLLG_01J_5f_lowMLL_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=98.3)
#ZGToLLG_LoosePtlPtg = Sample.nanoAODfromDAS("ZGToLLG_LoosePtlPtg",  "/ZGToLLG_01J_LoosePtlPtg_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=124.9) #SMP 19 013

#WWDoubleTo2L        = Sample.nanoAODfromDAS("WWDoubleTo2L",         "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/",              dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1729)

WW                  = Sample.nanoAODfromDAS("WW",                   "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=63.21 * 1.82)
#WZ                  = Sample.nanoAODfromDAS("WZ",                   "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=47.13)
ZZ                  = Sample.nanoAODfromDAS("ZZ",                   "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=16.523)

WWW_4F              = Sample.nanoAODfromDAS("WWW_4F",               "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",            dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2086)
WWW_4F_ext          = Sample.nanoAODfromDAS("WWW_4F_ext",           "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8_ext1-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2086)
WWZ                 = Sample.nanoAODfromDAS("WWZ",                  "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",            dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1651)
#WWZ_ext             = Sample.nanoAODfromDAS("WWZ_ext",              "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1651)
WZZ                 = Sample.nanoAODfromDAS("WZZ",                  "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.05565)
WZZ_ext             = Sample.nanoAODfromDAS("WZZ_ext",              "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8_ext1-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.05565)
ZZZ                 = Sample.nanoAODfromDAS("ZZZ",                  "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.01398)
ZZZ_ext             = Sample.nanoAODfromDAS("ZZZ_ext",              "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8_ext1-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.01398)



boson = [
    WWTo2L2Nu,
    #WWToLNuQQ,
    #WWTo1L1Nu2Q,
    #WWTo4Q,
    ZZTo2L2Nu,
    #ZZTo2L2Q,
    #ZZTo2Q2Nu,
    #ZZTo4L,
    #WZTo1L3Nu,
    #WZTo1L1Nu2Q,
    #WZTo2L2Q,
    #WZTo3LNu,
    #WZTo3LNu_ext,
    #WZTo3LNu_amcatnlo,
    #WZTo2Q2Nu,
    #VVTo2L2Nu,
    #VVTo2L2Nu_ext,
    WGToLNuG,
    WGToLNuG_amcatnlo,
    #ZGTo2LG_ext,
    ZGToLLG,
    #ZGToLLG_lowMLL,
    #ZGToLLG_LoosePtlPtg,
    #WWDoubleTo2L,
    WW,
    #WZ,
    ZZ,
    WWW_4F, WWW_4F_ext, 
    WWZ, #WWZ_ext,
    WZZ, WZZ_ext,
    ZZZ, ZZZ_ext, 
    ]

# W+jets
WJetsToLNu      = Sample.nanoAODfromDAS("WJetsToLNu",           "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3* 20508.9)
#WJetsToLNu_ext  = Sample.nanoAODfromDAS("WJetsToLNu_ext",       "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3* 20508.9)

W1JetsToLNu     = Sample.nanoAODfromDAS("W1JetsToLNu",          "/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=11524.) #9602. #NLO xsec from AN-2016/289
W2JetsToLNu     = Sample.nanoAODfromDAS("W2JetsToLNu",          "/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3788.) #3167. #NLO xsec from AN-2016/289
W3JetsToLNu     = Sample.nanoAODfromDAS("W3JetsToLNu",          "/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1144.) #948.5 #NLO xsec from AN-2016/289
#W4JetsToLNu     = Sample.nanoAODfromDAS("W4JetsToLNu",          "/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=636.) #492.9 #NLO xsec from AN-2016/289

#W1JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W1JetsToLNu_NuPt_200", "/W1JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2.049)
#W2JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W2JetsToLNu_NuPt_200", "/W2JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3.555)
#W3JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W3JetsToLNu_NuPt_200", "/W3JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3.274)
#W4JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W4JetsToLNu_NuPt_200", "/W4JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.991)

wjets = [
    WJetsToLNu,
#    WJetsToLNu_ext,
    W1JetsToLNu,
    W2JetsToLNu,
    W3JetsToLNu,
#    W4JetsToLNu,
#    W1JetsToLNu_NuPt_200,
#    W2JetsToLNu_NuPt_200,
#    W3JetsToLNu_NuPt_200,
#    W4JetsToLNu_NuPt_200,
    ]

## HT-binned
#WJetsToLNu_HT70to100        = Sample.nanoAODfromDAS("WJetsToLNu_HT70to100",        "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1637.13)
WJetsToLNu_HT100to200       = Sample.nanoAODfromDAS("WJetsToLNu_HT100to200",       "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1627.45)
WJetsToLNu_HT200to400       = Sample.nanoAODfromDAS("WJetsToLNu_HT200to400",       "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=435.237)
WJetsToLNu_HT400to600       = Sample.nanoAODfromDAS("WJetsToLNu_HT400to600",       "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=59.1811)
WJetsToLNu_HT600to800       = Sample.nanoAODfromDAS("WJetsToLNu_HT600to800",       "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",    dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=14.5805)
WJetsToLNu_HT800to1200      = Sample.nanoAODfromDAS("WJetsToLNu_HT800to1200",      "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=6.65621)
WJetsToLNu_HT1200to2500     = Sample.nanoAODfromDAS("WJetsToLNu_HT1200to2500",     "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.60809)
#WJetsToLNu_HT2500toInf      = Sample.nanoAODfromDAS("WJetsToLNu_HT2500toInf",      "",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.0389136)


wjets_ht = [
    #WJetsToLNu_HT70to100,
    WJetsToLNu_HT100to200,
    WJetsToLNu_HT200to400,
    WJetsToLNu_HT400to600,
    WJetsToLNu_HT600to800,
    WJetsToLNu_HT800to1200,
    WJetsToLNu_HT1200to2500,
    #WJetsToLNu_HT2500toInf,
    ]

wjets += wjets_ht

## rare
#TTTT = Sample.nanoAODfromDAS("TTTT", "/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/", dbFile=dbFile, redirector=redirector, xSection=0.009103)
TTWW = Sample.nanoAODfromDAS("TTWW", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.007829)
#TTWZ = Sample.nanoAODfromDAS("TTWZ", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/", dbFile=dbFile, redirector=redirector, xSection=0.002919)
TTZZ = Sample.nanoAODfromDAS("TTZZ", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.001573)

rare = [
    #TTTT,
    TTWW,
    #TTWZ,
    TTZZ,
    ]


signals = [
    ]


#GluGluHToZZTo4L             = Sample.nanoAODfromDAS("GluGluHToZZTo4L",   "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.01297)
#GluGluToContinToZZTo2e2mu   = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2mu",   "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.005423)
#GluGluToContinToZZTo2e2tau  = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2tau",  "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.005423)
#GluGluToContinToZZTo2mu2tau = Sample.nanoAODfromDAS("GluGluToContinToZZTo2mu2tau", "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.005423)
#GluGluToContinToZZTo4e      = Sample.nanoAODfromDAS("GluGluToContinToZZTo4e",      "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0027)
#GluGluToContinToZZTo4mu     = Sample.nanoAODfromDAS("GluGluToContinToZZTo4mu",     "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0027)
#GluGluToContinToZZTo4tau    = Sample.nanoAODfromDAS("GluGluToContinToZZTo4tau",    "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0027)

gluglu = [
#    GluGluHToZZTo4L,
#    GluGluToContinToZZTo2e2mu,
#    GluGluToContinToZZTo2e2tau,
#    GluGluToContinToZZTo2mu2tau,
#    GluGluToContinToZZTo4e,
#    GluGluToContinToZZTo4mu,
#    GluGluToContinToZZTo4tau,
]

#QCD_Mu_pt15to20         = Sample.nanoAODfromDAS("QCD_Mu_pt15to20",            "/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3629000.0)
#QCD_Mu_pt20to30         = Sample.nanoAODfromDAS("QCD_Mu_pt20to30",            "/QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3168000.0)
#QCD_Mu_pt30to50         = Sample.nanoAODfromDAS("QCD_Mu_pt30to50",            "/QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1649000.0)
#QCD_Mu_pt50to80         = Sample.nanoAODfromDAS("QCD_Mu_pt50to80",            "/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=445700.0)
#QCD_Mu_pt80to120        = Sample.nanoAODfromDAS("QCD_Mu_pt80to120",           "/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=105500.0)
#QCD_Mu_pt80to120_ext1   = Sample.nanoAODfromDAS("QCD_Mu_pt80to120_ext1",      "/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=105500.0)
#QCD_Mu_pt120to170       = Sample.nanoAODfromDAS("QCD_Mu_pt120to170",          "/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=25540.0)
#QCD_Mu_pt170to300       = Sample.nanoAODfromDAS("QCD_Mu_pt170to300",          "/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=8670.0)
#QCD_Mu_pt170to300_ext1  = Sample.nanoAODfromDAS("QCD_Mu_pt170to300_ext1",     "/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=8670.0)
#QCD_Mu_pt300to470       = Sample.nanoAODfromDAS("QCD_Mu_pt300to470",          "/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=797.5)
#QCD_Mu_pt300to470_ext1  = Sample.nanoAODfromDAS("QCD_Mu_pt300to470_ext1",     "/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=797.5)
#QCD_Mu_pt470to600       = Sample.nanoAODfromDAS("QCD_Mu_pt470to600",          "/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=78.67)
#QCD_Mu_pt470to600_ext1  = Sample.nanoAODfromDAS("QCD_Mu_pt470to600_ext1",     "/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=78.67)
#QCD_Mu_pt600to800       = Sample.nanoAODfromDAS("QCD_Mu_pt600to800",          "/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=25.33)
#QCD_Mu_pt600to800_ext1  = Sample.nanoAODfromDAS("QCD_Mu_pt600to800_ext1",     "/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=25.33)
#QCD_Mu_pt800to1000      = Sample.nanoAODfromDAS("QCD_Mu_pt800to1000",         "/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.715)
#QCD_Mu_pt800to1000_ext1 = Sample.nanoAODfromDAS("QCD_Mu_pt800to1000_ext1",    "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.715)
#QCD_Mu_pt1000toInf      = Sample.nanoAODfromDAS("QCD_Mu_pt1000toInf",         "/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.605)
#QCD_Mu_pt1000toInf_ext1 = Sample.nanoAODfromDAS("QCD_Mu_pt1000toInf_ext1",    "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.605)


#QCD_Ele_pt20to30        = Sample.nanoAODfromDAS("QCD_Ele_pt20to30",           "/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5533000.0)
#QCD_Ele_pt30to50        = Sample.nanoAODfromDAS("QCD_Ele_pt30to50",           "/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=9928000.0)
#QCD_Ele_pt30to50_ext1   = Sample.nanoAODfromDAS("QCD_Ele_pt30to50_ext1",      "/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=9928000.0)
#QCD_Ele_pt50to80        = Sample.nanoAODfromDAS("QCD_Ele_pt50to80",           "/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2890800.0)
#QCD_Ele_pt50to80_ext1   = Sample.nanoAODfromDAS("QCD_Ele_pt50to80_ext1",      "/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2890800.0)
#QCD_Ele_pt80to120       = Sample.nanoAODfromDAS("QCD_Ele_pt80to120",          "/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=415400.0)
#QCD_Ele_pt80to120_ext1  = Sample.nanoAODfromDAS("QCD_Ele_pt80to120_ext1",     "/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=415400.0)
#QCD_Ele_pt120to170      = Sample.nanoAODfromDAS("QCD_Ele_pt120to170",         "/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=75820.0)
#QCD_Ele_pt120to170_ext1 = Sample.nanoAODfromDAS("QCD_Ele_pt120to170_ext1",    "/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=75820.0)
#QCD_Ele_pt170to300      = Sample.nanoAODfromDAS("QCD_Ele_pt170to300",         "/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=18860.0)
#QCD_Ele_pt300toInf      = Sample.nanoAODfromDAS("QCD_Ele_pt300toInf",         "/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1210.0)

QCD = [
    #    QCD_Mu_pt15to20,
    #    QCD_Mu_pt20to30,
    #    QCD_Mu_pt30to50,
    #    QCD_Mu_pt50to80,
    #    QCD_Mu_pt80to120,
    #    QCD_Mu_pt80to120_ext1,
    #    QCD_Mu_pt120to170,
    #    QCD_Mu_pt170to300,
    #    QCD_Mu_pt170to300_ext1,
    #    QCD_Mu_pt300to470,
    #    QCD_Mu_pt300to470_ext1,
    #    QCD_Mu_pt470to600,
    #    QCD_Mu_pt470to600_ext1,
    #    QCD_Mu_pt600to800,
    #    QCD_Mu_pt600to800_ext1,
    #    QCD_Mu_pt800to1000,
    #    QCD_Mu_pt800to1000_ext1,
    #    QCD_Mu_pt1000toInf,
    #    QCD_Mu_pt1000toInf_ext1,

    #   QCD_Ele_pt20to30,
    #    QCD_Ele_pt30to50,
    #    QCD_Ele_pt30to50_ext1,
    #    QCD_Ele_pt50to80,
    #    QCD_Ele_pt50to80_ext1,
    #    QCD_Ele_pt80to120,
    #    QCD_Ele_pt80to120_ext1,
    #    QCD_Ele_pt120to170,
    #    QCD_Ele_pt120to170_ext1,
    #    QCD_Ele_pt170to300,
    #    QCD_Ele_pt300toInf,
]

### QCD

## QCD HT bins (cross sections from McM)
#QCD_HT50to100        = Sample.nanoAODfromDAS("QCD_HT50to100",        "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/ ",         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=246400000.0)
#QCD_HT100to200       = Sample.nanoAODfromDAS("QCD_HT100to200",       "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=27850000.0)
#QCD_HT200to300       = Sample.nanoAODfromDAS("QCD_HT200to300",       "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/ ",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1717000)
#QCD_HT200to300_ext   = Sample.nanoAODfromDAS("QCD_HT200to300_ext",   "",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1717000)
#QCD_HT300to500       = Sample.nanoAODfromDAS("QCD_HT300to500",       "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=351300)
#QCD_HT300to500_ext   = Sample.nanoAODfromDAS("QCD_HT300to500_ext",   "",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=351300)
#QCD_HT500to700       = Sample.nanoAODfromDAS("QCD_HT500to700",       "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/ ",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=31630)
#QCD_HT500to700_ext   = Sample.nanoAODfromDAS("QCD_HT500to700_ext",   "",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=31630)
#QCD_HT700to1000      = Sample.nanoAODfromDAS("QCD_HT700to1000",      "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=6802)
#QCD_HT700to1000_ext  = Sample.nanoAODfromDAS("QCD_HT700to1000_ext",  "",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=6802)
#QCD_HT1000to1500     = Sample.nanoAODfromDAS("QCD_HT1000to1500",     "",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1206)
#QCD_HT1000to1500_ext = Sample.nanoAODfromDAS("QCD_HT1000to1500_ext", "", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1206)
#QCD_HT1500to2000     = Sample.nanoAODfromDAS("QCD_HT1500to2000",     "",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=120.4)
#QCD_HT1500to2000_ext = Sample.nanoAODfromDAS("QCD_HT1500to2000_ext", "", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=120.4)
#QCD_HT2000toInf      = Sample.nanoAODfromDAS("QCD_HT2000toInf",      "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=25.25)
#QCD_HT2000toInf_ext  = Sample.nanoAODfromDAS("QCD_HT2000toInf_ext",  "",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=25.25)

#QCD_HT = [
#    QCD_HT50to100,
#    QCD_HT100to200,
#    QCD_HT200to300,
#    QCD_HT200to300_ext,
#    QCD_HT300to500,
#    QCD_HT300to500_ext,
#    QCD_HT500to700,
#    QCD_HT500to700_ext,
#    QCD_HT700to1000,
#    QCD_HT700to1000_ext,
#    QCD_HT1000to1500,
#    QCD_HT1000to1500_ext,
#    QCD_HT1500to2000,
#    QCD_HT1500to2000_ext,
#    QCD_HT2000toInf,
#    QCD_HT2000toInf_ext,
#    ]
#QCD += QCD_HT

#QCD pT-hat binned samples
QCD_pt15to30            = Sample.nanoAODfromDAS("QCD_pt15to30",               "/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1837410000*1.0) #xSection = xsec * filter eff
QCD_pt30to50            = Sample.nanoAODfromDAS("QCD_pt30to50",               "/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=140932000*1.0)  #xSection = xsec * filter eff
QCD_pt50to80            = Sample.nanoAODfromDAS("QCD_pt50to80",               "/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=19204300*1.0)   #xSection = xsec * filter eff
QCD_pt80to120           = Sample.nanoAODfromDAS("QCD_pt80to120",              "/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2762530*1.0)    #xSection = xsec * filter eff
QCD_pt120to170          = Sample.nanoAODfromDAS("QCD_pt120to170",             "/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=471100*1.0)     #xSection = xsec * filter eff
QCD_pt170to300          = Sample.nanoAODfromDAS("QCD_pt170to300",             "/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=117276*1.0)     #xSection = xsec * filter eff
QCD_pt300to470          = Sample.nanoAODfromDAS("QCD_pt300to470",             "/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=7823*1.0)       #xSection = xsec * filter eff
QCD_pt470to600          = Sample.nanoAODfromDAS("QCD_pt470to600",             "/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=648.2*1.0)      #xSection = xsec * filter eff
QCD_pt600to800          = Sample.nanoAODfromDAS("QCD_pt600to800",             "/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=186.9*1.0)      #xSection = xsec * filter eff
QCD_pt800to1000         = Sample.nanoAODfromDAS("QCD_pt800to1000",            "/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=32.293*1.0)     #xSection = xsec * filter eff
QCD_pt1000to1400        = Sample.nanoAODfromDAS("QCD_pt1000to1400",           "/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=9.4183*1.0)     #xSection = xsec * filter eff
QCD_pt1400to1800        = Sample.nanoAODfromDAS("QCD_pt1400to1800",           "/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.84265*1.0)    #xSection = xsec * filter eff
QCD_pt1800to2400        = Sample.nanoAODfromDAS("QCD_pt1800to2400",           "/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.114943*1.0)   #xSection = xsec * filter eff
QCD_pt2400to3200        = Sample.nanoAODfromDAS("QCD_pt2400to3200",           "/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.00682981*1.0) #xSection = xsec * filter eff
QCD_pt3200toInf         = Sample.nanoAODfromDAS("QCD_pt3200toInf",            "/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.000165445*1.0)#xSection = xsec * filter eff

#https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
#QCD bcToE samples

## The 15to20 is missing 
# QCD_bcToE_pt15to20            = Sample.nanoAODfromDAS("QCD_bcToE_pt15to20",               "",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=557627000*0.00059) #xSection = xsec * filter eff
#QCD_bcToE_pt20to30            = Sample.nanoAODfromDAS("QCD_bcToE_pt20to30",               "",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=557627000*0.00059) #xSection = xsec * filter eff
#QCD_bcToE_pt30to80            = Sample.nanoAODfromDAS("QCD_bcToE_pt30to80",               "",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=159068000*0.00255) #xSection = xsec * filter eff
#QCD_bcToE_pt80to170           = Sample.nanoAODfromDAS("QCD_bcToE_pt80to170",              "",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3221000*0.01183) #xSection = xsec * filter eff
#QCD_bcToE_pt170to250          = Sample.nanoAODfromDAS("QCD_bcToE_pt170to250",             "",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=105771*0.02492) #xSection = xsec * filter eff
#QCD_bcToE_pt250toInf          = Sample.nanoAODfromDAS("QCD_bcToE_pt250toInf",             "",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=21094.1*0.03375) #xSection = xsec * filter eff

QCD += [

        QCD_pt15to30,                  
        QCD_pt30to50,            
        QCD_pt50to80,           
        QCD_pt80to120,          
        QCD_pt120to170,           
        QCD_pt170to300,          
        QCD_pt300to470,          
        QCD_pt470to600,          
        QCD_pt600to800,          
        QCD_pt800to1000,        
        QCD_pt1000to1400,        
        QCD_pt1400to1800,        
        QCD_pt1800to2400,        
        QCD_pt2400to3200,        
        QCD_pt3200toInf,  

     #   QCD_bcToE_pt20to30,           
     #   QCD_bcToE_pt30to80,           
     #   QCD_bcToE_pt80to170,           
     #   QCD_bcToE_pt170to250,           
     #   QCD_bcToE_pt250toInf, 

]

#GJets_HT40to100        = Sample.nanoAODfromDAS("GJets_HT40to100",      "/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=20730)
#GJets_HT100to200       = Sample.nanoAODfromDAS("GJets_HT100to200",     "/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=9226)
#GJets_HT100to200_ext   = Sample.nanoAODfromDAS("GJets_HT100to200_ext", "",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=9226)
#GJets_HT200to400       = Sample.nanoAODfromDAS("GJets_HT200to400",     "/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2300)
#GJets_HT400to600       = Sample.nanoAODfromDAS("GJets_HT400to600",     "/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=274.4)
#GJets_HT600toInf       = Sample.nanoAODfromDAS("GJets_HT600toInf",     "/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=93.38)

GJetsHT = [
           #GJets_HT40to100,
           #GJets_HT100to200,
           #GJets_HT100to200_ext,
           #GJets_HT200to400,
           #GJets_HT400to600,
           #GJets_HT600toInf,
]

other = [
    ]


allSamples = DY + top + boson + wjets + rare + other + signals + gluglu + QCD + GJetsHT

for s in allSamples:
    s.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples = AutoClass( DYJetsNuNuHT )
        samples.check_completeness( cores=1 )


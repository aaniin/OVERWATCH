""" TRD subsystem specific functions.

under development

.. codeauthor:: Sebastian Syrkowski <syrkowski@physi.uni-heidelberg.de>, Universitaet Heidelberg

"""

import ROOT

# Used for sorting and generating html
from processRuns import processingClasses

######################################################################################################
######################################################################################################
# Monitoring functions
######################################################################################################
######################################################################################################

def generalTRDOptions(subsystem, hist, processingOptions):
    # Show TPC titles (by request from Mikolaj)
    if "EMC" not in hist.histName:
        ROOT.gStyle.SetOptTitle(1)

def findFunctionsForTRDHistogram(subsystem, hist):
    # General TPC Options
    hist.functionsToApply.append(generalTRDOptions)

def createTRDHistogramGroups(subsystem):
    # Sort the filenames of the histograms into catagories for better presentation
    # The order in which these are added is the order in which they are processed!    

    #subsystem.histGroups.append(processingClasses.histogramGroupContainer("event_6", "event_6"))

    # Catch all other TPC hists
    subsystem.histGroups.append(processingClasses.histogramGroupContainer("Other TRD", "fHist"))

    # Catch all of the other hists
    # NOTE: We only want to do this if we are using a subsystem that actually has a file. Otherwise, you end up with lots of irrelevant histograms
    if subsystem.subsystem == subsystem.fileLocationSubsystem:
        subsystem.histGroups.append(processingClasses.histogramGroupContainer("Non TRD", ""))

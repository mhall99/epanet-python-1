# -*- coding -*-
#In progress. Currenly returns pressure, demand, head for specified node in specified network
import os
import epanet_module.epamodule as em

def HydraAna( inputFile, MyNode ):
    #Open the EPANET toolkit & hydraulic analysis, load system
    em.ENopen(inputFile, "task.rpt")
    em.ENopenH()

    #sets duration of analysis to 36000 seconds (10 hours)
    em.ENsettimeparam(em.EN_DURATION, 36000)
    nodeCount = em.ENgetcount(em.EN_NODECOUNT)
    linkCount = em.ENgetcount(em.EN_LINKCOUNT)

    #initializes tank volumes, link status, settings, duration, etc
    em.ENinitH()

    #runs single hydraulic analysis
    em.ENrunH()

    #pressureList = []
    #demandList = []
    #headList = []

    #node stuff
    #while nodeCount != 0:
    nodeindex = em.ENgetnodeindex(MyNode);
    pressure = em.ENgetnodevalue(nodeindex, em.EN_PRESSURE)
    demand = em.ENgetnodevalue(nodeindex, em.EN_DEMAND)
    head = em.ENgetnodevalue(nodeindex, em.EN_HEAD)

    #em.ENsolveQ()
    #link stuff 
    #linkindex = em.ENgetlinkindex(linkid);

    print('Node index is %d, node pressure is %d, node demand is %d, node head is %d.' % (nodeindex, pressure, demand, head))

#testing function call
HydraAna("Threenode-cl-2.inp","2")


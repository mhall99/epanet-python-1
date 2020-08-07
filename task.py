# -*- coding -*-
import os
import epanet_module.epamodule as em

def HydraAna( inputFile, MyNode, MyLink ):
    #Open the EPANET toolkit & hydraulic analysis, load 3-node system
    em.ENopen(inputFile, "task.rpt")
    em.ENopenH()

    #sets duration of analysis to 36000 seconds (10 hours)
    em.ENsettimeparam(em.EN_DURATION, 36000)
    #nodeCount = em.ENgetcount(em.EN_NODECOUNT)
    #linkCount = em.ENgetcount(em.EN_LINKCOUNT)

    #initializes tank volumes, link status, settings, duration, etc
    em.ENinitH()

    #em.ENsetpatternvalue(1, 1, 10) setting analysis period & step size?

    NpressureList = []
    NdemandList = []
    NheadList = []

    LflowList = []
   

    #iterates ten times to accrue values 
    for x in range(0,10):
        em.ENrunH() #runs single hydraulic analysis

        nodeindex = em.ENgetnodeindex(MyNode); #node stuff
        Npressure = em.ENgetnodevalue(nodeindex, em.EN_PRESSURE)
        Ndemand = em.ENgetnodevalue(nodeindex, em.EN_DEMAND)
        Nhead = em.ENgetnodevalue(nodeindex, em.EN_HEAD)

        NpressureList.append(Npressure)
        NdemandList.append(Ndemand)
        NheadList.append(Nhead)

        linkindex = em.ENgetlinkindex(MyLink); #link stuff 
        Lflow = em.ENgetlinkvalue(linkindex, em.EN_FLOW)

        LflowList.append(Lflow)

        em.ENnextH()
 

    print('List of calculated node pressures.')
    print(*NpressureList, sep = ' units\n')
    print('List of calculated link flowrates.')
    print(*LflowList, sep = ' units\n')

    #print('Node count is %d and link count is %d.' % (nodeCount, linkCount))
    #print('Node index is %d, node pressure is %d, node demand is %d, node head is %d.' % (nodeindex, pressure, demand, head))


    em.ENcloseH()
    em.ENclose()

HydraAna("Threenode-cl-2.inp","2", "1")


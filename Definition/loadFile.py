"""
Simple driver file to create a 2d plot of an platform locations in an array.
The input file only contains the bare minimum information to build a 2d plot 
of the turbine locations (no moorings, cables, anchors, platform design, turbines, 
                          site condition information, etc.)
"""

from famodel import Project
import matplotlib.pyplot as plt
import os

# define name of ontology input file
dir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(dir,'task49_deepwater_array.yaml')

# initialize Project class with input file, we don't need RAFT for this so mark False
project = Project(file=input_file,raft=False)

# plot
project.plot2d()

plt.show()

cost = 0
concost = 0
buoycost = 0
length = 0 
count = 0 
totcost = 0
dynlength = 0
staticlength = 0
        
# for cable in project.cableList:
#     print('cable ', cable)
#     if len(project.cableList[cable].subcomponents) > 1 and project.cableList[cable].subcomponents[0].dd['cable_type']['A'] == 1000:
#         project.cableList[cable].subcomponents[0].getCost()
#         cost = project.cableList[cable].subcomponents[0].cost
#         l = project.cableList[cable].subcomponents[0].L
#         break 
    

mcab = 0
for cable in project.cableList:
    if len(project.cableList[cable].subcomponents) > 1 and project.cableList[cable].subcomponents[0].dd['cable_type']['A'] == 1000:
        # count +=1
        # length += project.cableList[cable].subcomponents[0].L
        
        dynlength += project.cableList[cable].subcomponents[0].L +project.cableList[cable].subcomponents[4].L
        staticlength += project.cableList[cable].subcomponents[2].L
        
        cab = project.cableList[cable]
        cost = cab.getCost()
        
        # for line in cab.subcomponents[0].ss.lineList:
            # mcab += line.type['m']*line.L # 2 times bc there's a dynamic cable on either end
        # mcab += cab.subcomponents[2].dd['cable_type']['m']*cab.subcomponents[2].L
    project.cableList[cable].getCost()
    #totcost += project.cableList[cable].getCost()
    #concost += project.cableList[cable].getCost()[1]
    #buoycost += project.cableList[cable].getCost()
    
# #%%
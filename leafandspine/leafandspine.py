#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo

class LeafAndSpine(Topo):
    #Create Leaf and Spine Topology		
    def build(self, leaf=4, spine=2, fanout=2):

        # Add spine switches
        spineSwitch={}
        for s in range(spine):
            spineSwitch[s]=self.addSwitch('spine10%s' % (s+1))

        # Add leaf switches
	leafSwitch={}
        for l in range(leaf):
            leafSwitch[l]=self.addSwitch('leaf%s' % (l+1))

            # Connect leaf switches to all spine switches
            for s in range(spine):
                self.addLink(leafSwitch[l], spineSwitch[s])

            # Add fanout hosts under each leaf switch 
            for f in range(fanout):
                host=self.addHost('h%s' % (l*fanout+f+1))
                self.addLink(host, leafSwitch[l])

topos={'leafandspine': LeafAndSpine}

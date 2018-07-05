#!/usr/bin/python

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.util import quietRun
import time
import re

def iperfpair(self, param):

	aux=re.findall("h[0-9]+\s+h[0-9]+\s+[0-9]+\s+h[0-9]+\s+h[0-9]+\s+[0-9]+\s+[0-9]+$",param)
	
	if len(aux)!=1:
		print "*** Error in parameters"
		print "*** Usage: iperfpair server1 client1 transmission_time1 server2 client2 transmission_time2 time_gap"
		print "*** Example iperfpair h1 h3 20 h5 h8 10 5" 
		return
	
	net=self.mn
	
	h=re.findall('h\d+',param)
	
	for x in range(0, len(h)):
		h[x]=re.sub('h', '0', h[x])
		h[x]=int(h[x])

		if h[x]>len(net.hosts):
			print "*** Error in parameters: check hosts number"
			return
		else:
			quietRun("rm %s.txt" % net.hosts[int(h[x])-1].name)
	
	aux=re.findall("\s+\d+", param)
	transmission_time={}
	transmission_time[0]=aux[0]
	transmission_time[1]=aux[1]
	seconds=float(aux[2])

	quietRun("killall -9 iperf")

	popens={}
	
	x=0
	while x<=len(h)-1:
    		print "*** Starting server on %s" % net.hosts[h[x]-1].name
		popens[x]=net.hosts[h[x]-1].popen("iperf -s > %s.txt" % net.hosts[h[x]-1].name, shell=True)
   		x+=2
	
	x=1
	tx_t=0
	while x<=len(h)-1:
    		if x==len(h)-1:
			print "*** Waiting %s seconds" % seconds
			time.sleep(seconds)
	
		print "*** Starting client on %s (transmission time=%s)" % (net.hosts[h[x]-1].name, transmission_time[tx_t])
		popens[x]=net.hosts[h[x]-1].popen("iperf -c %s -t %s > %s.txt" % (net.hosts[h[x-1]-1].IP(), transmission_time[tx_t], net.hosts[h[x]-1].name), shell=True)
		tx_t+=1
    		x+=2

	print "*** Waiting until iperf finish"	
	x=1
	while x<=len(h)-1:
		popens[x].communicate()
		x+=2
	
	print "*** killing servers"
	x=0
	while x<=len(h)-1:
		popens[x].kill()
		x+=2	

	print "*** Done!"
	print "Results in %s.txt %s.txt %s.txt %s.txt" % (net.hosts[h[0]-1].name, net.hosts[h[1]-1].name, net.hosts[h[2]-1].name, net.hosts[h[3]-1].name)

CLI.do_iperfpair = iperfpair

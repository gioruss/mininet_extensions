# mininet_extensions
Some mininet extensions written in Python language.

Two extensions are actually implemented:

- leafandspine: this extension contains LeafAndSpine class that allow to emulate a Leaf-Spine topology. It can be used though the parameter --custom=leafandspine.py. Then use the parameter --topo to pass to the constructor three arguments: number of leaf-switches, number of spine-switches, fanout of each leaf-switch (example: --topo=leafandspine,10,4,15).

-iperfpair: this extension implements the command iperfpair. It can be launched in mininet CLI to execute two iperf tests, at the same time, between two couples of hosts. The command syntax is:

    mininet> iperfpair server1 client1 transmission_time1 server2 client2 transmission_time2 time_gap

 The parameters have the following meaning:
    server1: name of the host on which the first iperf server will run;
    client1: name of the host on which the first iperf client will run;
    server2: name of the host on which the second iperf server will run;
    client2: name of the host on which the second iperf client will run;
    transmission_time1: time that first iperf test will go on, expressed in seconds;
    transmission_time2: time that second iperf test will go on, expressed in seconds;
    time_gap: time gap between the two iperf tests, expressed in seconds.
    
Copyright(C) 2011 by Giovanni Russotto (russottogio@gmail.com) This is free software; you can redistribute it and/or modify it for accademic and scientific purposes, including a reference to its author. This software CANNOT be used, copied, included or modified for commercial purposes. It's distributed in the hope that it will be useful but WITHOUT ANY WARRANTY!!

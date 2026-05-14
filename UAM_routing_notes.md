## Notes on UAM routing 



May 13, Aadit

### Section 2B 

1. Will there be any conflict between theory and implementation - 
	- UrbanNav is discrete time system 
	vs
	- theoretical modeling assums CTMC 
1. what does waiting in a queue mean 
	since this is a state of UAV,
	- is it at the vertport's vertipad sitting idle 
	- or hovering around vertiport 

**Ans**: Q_{i}^{d} indicates UAV is hovering around vertiport waiting for a pad - 
	MAYBE, since UAV is hovering at vertiport i, but its destination is d  

2. what does in service on a landing pad mean 
	- loading/unloading passengers, charging, and other activities related to UAV on vertiport 
	
 
3. flight duration does not make sense, if \mu_{ij} is fight rate from vertiport i to j, and avg flight time is 1/ \mu_{ij}, that would mean, as flight rate between increases, the travel time will decrease, that does not make sense, unless, UAVs will fly faster, but, even then there is a physical limit to UAV speed, so ..... 



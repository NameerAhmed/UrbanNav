## Implementation details for UAM 



Date: May 13, Aadit 


### Implementation strategy 

1. Service duration 
    After a UAV has landed, sample timesteps for SERVICE DURATION - from an exponential distribution with mean, mu. UAV will have a new attr, wait\_time\_vertiport, after landing this attr will be used assigned value from the exp dist, and at each time step, will be decremented, after wait\_time variable has reached 0, we will assign UAV new mission/continue\_mission. 

2. 

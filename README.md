# slot

A Silly LOTtery program

OK. So I had a week off. For a few days it was too hot to paint, or do much else. I had time to think. Dangerous, or what?

For years I have dabbled with the lottery. Increasingly, this has become an integral part of my retirement plans. 

The thing is, every week the numbers drawn have an equal chance of selection. Probability says so, I get it. But wouldn't it be nice if you could have a system which tipped the odds a bit in your favour?

Here's a thought. Although every draw, the numbers have the same chance of being picked, what if you look at the numbers over a series of weeks? Repeated numbers in consecutive weeks is not common. I did study probability and statistics at University, but this was over forty years ago. I vaguely remember something about the probability of events based on previous events, independent events and sequences. The likelyhood of events happening in a sequence changes the probability, I think. So if you select numbers that have not been chosen in the previous few weeks you could improve you chances of picking a winning number. Of course it pays to hedge bets and allow a bit of leeway. So you might get the odd duplicate. So allow a bit of flexibility. I accept that I am probably (p=0.999) talking complete bollocks, at least mathematically, of course? It isn't the first time, and it definitely won't be the last. Empirically it feels like it is reasonable. Being pragmatic, you can see it happen, week on week.  

We also get different distributions of numbers. Sometimes they are evenly spread. Other times they can be bunched. Skewed low or high. Split low and high. There isn't any mathematical analysis applicable, but my observation is that you never get a single distribution pattern repeated indefinitely.

I will put something together to pick numbers on this basis. So my requirements are:

1. Pick how many duplicates you will allow
2. Pick the number distribution you want (they can skew, high or low, or be evenly distributed)
3. Pick how many weeks back you want to include.

Then randomly select numbers will fit the above criteria. Exclude numbers from previous weeks, except for the specified number of duplicates required, and apply the distribution specified.
 

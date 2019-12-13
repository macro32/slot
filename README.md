# slot

A Silly LOTtery program

OK. So I had a week off. For a few days it was too hot to paint, or do much else. I had time to think. Dangerous, or what?

For years I have dabbled with the lottery. Increasingly, this has become an integral part of my retirement plans. 

The thing is, every week the numbers drawn have an equal chance of selection. Probability says so, I get it. 

So it is perfectly possible to get the same numbers drawn on consecutive weeks. But this just never seems to happen. It is common to get one number repeated, sometimes two, but that is usually it. So if you look back a few weeks and exclude numbers that have appeared before you could be improving your chances of picking numbers that will appear. That's what I think, any road.

We also get different distributions of numbers. Sometimes they are evenly spread over the range. Other times they can be bunched. Skewed low or high. Split low and high. There isn't any mathematical analysis applicable, but my observation is that you never get a single distribution pattern repeated indefinitely. So being able to choose a distribution may help your chances.

I will put something together to pick numbers on this basis. So my requirements are:

1. Pick how many duplicates you will allow
2. Pick which duplicate(s) you want
3. Pick the distribution you want (they can skew, high, middle or low, or be evenly distributed)
4. Pick how many weeks back you want to include.

Then randomly select numbers will fit the above criteria. Exclude numbers from previous weeks, except for the specified number of duplicates required, and apply the distribution specified.
 

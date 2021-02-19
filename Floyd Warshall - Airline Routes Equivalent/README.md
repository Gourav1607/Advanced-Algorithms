# Floyd-Warshall Algorithm

### Airline Routes Equivalent

The airline carriers schedule the flights between pairs of cities through the shortest routes. If a direct flight is not available between two cities,
then they schedule a connecting flight. Two airline carriers are called equivalent if they offer the flights between the same pairs of cities.

Design an algorithm with less than cubic time complexity to compare whether two given airline carriers are equivalent or not. 
Direct and connecting flights are not differentiated here.

Use your solution to find out whether two airlines offering the following flights are equivalent or not. Here, the pair (Ci Cj)
denotes that a flight between city Cj and city Cj is offered.

```
Airline 1: (A B),(B E),(A E),(C F),(E C),(D A)
Airline 2: (A B),(D A),(E C),(C F),(D B),(B E),(D F)
```
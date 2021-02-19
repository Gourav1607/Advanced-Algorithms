# Gift Distribution

Suppose there are N gifts. The color of each gift is represented as a lowercase letter. We want to distribute N gifts to M people. They will be upset if they get two gifts of the same color. We can give any number of gifts to people, and they won’t be upset even if they do not get any gift, but we have to distribute all gifts, such that no one will be upset. 

Print YES, if it is possible, and NO otherwise.

Input
value of N and M
colors of given gifts

Output: YES or NO

<hr style="border:2px solid gray"> </hr>

Sample Input 1
```
4 2
ppqq
```

Sample Output 1
```
YES
```

Explanation: We can give 1st and 3rd gift to first person, and 2nd and 4th to the second.

<br>

Sample Input 2
```
6 3
pprppq
```

Sample Output 2
```
NO
```

Explanation: We need to give all gifts of color p, but one gift will stay, that is why the answer is NO.
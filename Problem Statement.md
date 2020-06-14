# Skill based Matchmaking

 You are given **N** players who want to play a **M** vs **M** match. Each Player has an attribute **Score** which is a
positive integer. <p></p>
The program needs to find possible unique matches of M vs M players depending on their Score . The
matches should be sorted based on the **quality** of each match. The **quality** of the match is defined as the
closeness of the scores between the teams. <p></p>

### Example for quality
Let's say we have 1vs1 matches with the following scores- <p></p>
Match1 100 vs 98 <p></p>
Match2 60 vs 40 <p></p>
Match3 62 vs 64 <p></p>

### The sorted order here would be:
Match1, Match3, Match2 <p></p>
For matches with multiple players on one side, the average score should be used.

### Input-
Number of players on each side: M

### Example-
2

### Input-
name of player 1 - score <p></p>
name of player 2 - score <p></p>
A blank line denotes end of input.

### Example
bleh 85 <p></p>
Aequitas 90 <p></p>
akS 87 <p></p>
lamiV 20 <p></p>

### Output
sorted list of (best to worst) <p></p>
(comma separated list of players in team A) (average score) vs (comma separated list of players in team
B) (average score)

### Example
bleh,akS (86) vs Aequitas,lamiV (55) <p></p>
bleh,Aequitas (87.5) vs akS,lamiV (53.5) <p></p>
bleh,lamiV (52.5) vs Aequitas,akS (88.5) <p></p>

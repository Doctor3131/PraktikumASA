# Bebek Nakal (Naughty Duck)

## Description
Pak Rifai is a successful duck farmer. The key to Pak Rifai's duck farming success is a duck behavior ranking system. With this system, Pak Rifai can regulate the amount of food and luxury of the cages depending on the duck's behavior ranking. The naughtier a duck is, the lower its behavior ranking, which is determined by the duck's naughtiness points.

At one point, Pak Rifai realized there was a problem with the duck behavior system. The order of the duck behavior rankings did not match the naughtiness points of Pak Rifai's ducks. Because he wants to fix the duck behavior system, Pak Rifai wants to count how many errors are in the system. An error in the system occurs if the following condition is met:

* If i and j are the rankings of 2 different ducks where i < j and the naughtiness value of the duck with the i-th ranking is greater than the duck with the j-th ranking (Xi > Xj), then this is considered an error.

If Pak Rifai has N ducks with Xi being the naughtiness value of the duck with the i-th ranking, help Pak Rifai count the errors that occur in the system.

## Input Format
The first line contains a number N which is the number of ducks with 2 ≤ N ≤ 10,000.
The second line contains N integers which are the naughtiness values of the ducks according to their rankings with 1 ≤ Xi ≤ 100,000.

## Output Format
Contains a number which is the count of errors in the duck behavior system.

## Example Input 1
```
3
2 2 1
```

## Example Output 1
```
2
```

## Explanation of Input 1
The pairs that meet the error criteria are:
* Rank 1 and 3
* Rank 2 and 3

## Hint
Use a modified merge sort. During the combine step, count the errors in the duck behavior system.
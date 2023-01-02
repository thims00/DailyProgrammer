# Challenge No. 399 - Letter Value Sum

### SOURCE: https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/?sort=new

### r/dailyprogrammer
### **SYNOPSIS**:
[2021-07-19] Challenge #399 [Easy] Letter value sum
Challenge
Assign every lowercase letter a value, from 1 for a to 26 for z. Given a string of lowercase letters, find the sum of the values of the letters in the string.

lettersum("") => 0
lettersum("a") => 1
lettersum("z") => 26
lettersum("cab") => 6
lettersum("excellent") => 100
lettersum("microspectrophotometries") => 317
Optional bonus challenges
Use the enable1 word list
 for the optional bonus challenges.

1. microspectrophotometries is the only word with a letter sum of 317. Find the only word with a letter sum of 319.

2. How many words have an odd letter sum?

3. There are 1921 words with a letter sum of 100, making it the second most common letter sum. What letter sum is most common, and how many words have it?

3. zyzzyva and biodegradabilities have the same letter sum as each other (151), and their lengths differ by 11 letters. Find the other pair of words with the same letter sum whose lengths differ by 11 letters.

4. cytotoxicity and unreservedness have the same letter sum as each other (188), and they have no letters in common. Find a pair of words that have no letters in common, and that have the same letter sum, which is larger than 188. (There are two such pairs, and one word appears in both pairs.)

5. The list of word { geographically, eavesdropper, woodworker, oxymorons } contains 4 words. Each word in the list has both a different number of letters, and a different letter sum. The list is sorted both in descending order of word length, and ascending order of letter sum. What's the longest such list you can find?

(This challenge is a repost of Challenge #52 [easy], originally posted by u/rya11111 in May 2012.)

It's been fun getting a little activity going in here these last 13 weeks. However, this will be my last post to this subreddit for the time being. Here's hoping another moderator will post some challenges soon!




### OUTPUT:
$ time python3 main.py
1) Find the only word with a letter sum of 319: reinstitutionalizations
 => 24
2) How many words have an odd letter Sum: 86339
3) What letter sum is most common, and how many words have it:
    Most common: 93
    Word Qty: 1965
4) Find the other pair of words with the same letter sum
   whose lengths differ by 11 letters: voluptuously and electroencephalographic

real    1m5.128s
user    1m2.234s
sys     0m0.031s


## 
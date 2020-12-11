TF: Tech for Troops 2020
Challenge: Silent Water

Category:  web

Points: 150

Difficulty: Introductory

## Instructions

***Description:****

None, beside the link the website.

## Solution

This was a pretty simple solve, if we go to inspect the page, we can go to
where the cookies are stored and see that there is a cookie called simply
loggedin. All we have to do is change that to True and then we succesfully
have the flag after we log in.

## Flag

`EAT_COOKIES`

## Mitigation

Here the problem is that the page only relies on the fact that a cookie
determines whether or not you can log in. That is bad security and there should
be a check to see whether or not the credentials are in fact correct.

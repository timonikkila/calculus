### To test

Production: https://calculus-prod.herokuapp.com/calculus?query=2%20*%20(23%2F(33))-%2023%20*%20(23)

staging: https://simplecalculus.herokuapp.com/calculus?query=2%20*%20(23%2F(33))-%2023%20*%20(23)


### Current deployment process

1. Push changes to master
2. Travis runs tests automatically
3. If tests pass, then changes are published in staging
4. Changes are pushed to production manually

There are room for improvement, like running tests per pull request and publishing pull request version in Heroku.

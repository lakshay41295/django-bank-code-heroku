# django-bank-code-heroku

This project describes how to deploy a django project on heruku. I have taken a simple django project add procfile, plpfile ,requirements to establish deployement on heroku.

My django project is hosted on https://myappbank.herokuapp.com/ . It uses database of bank which contain ifsc,branch,address,city,district,state, bank_name,bank_id. You can view the bank details using https://myappbank.herokuapp.com/bankdetails
as well if you wanna search on the basis of ifsc you just need to https://myappbank.herokuapp.com/bankdetails?ifsc=example. Please replace example with any ifsc code provide in the database and it will queried accordinly.

You can view the branches  using https://myappbank.herokuapp.com/bankbranch well if you wanna search on the basis of city and bank name you just need to https://myappbank.herokuapp.com/bankbranch?city=example&bank=example1. Please replace example, example1 with any city , bank name respectively provide in the database and it will query on it basis

I have used the database provided by :https://github.com/snarayanank2/indian_banks . Since i migrated my database from sqlite to postgres so only 25,000 rows are only transfered . If you wanna whole you could use post gres locally .

# Kind Cloud
An app for sharing kind words with others

## Running Locally
1. Populate an `.env` by copying and settings value from `example.env`
    1. Requires a RapidAPI account with a subscription to this API: https://rapidapi.com/twinword/api/sentiment-analysis
1. `poetry install`
1. `poetry shell`
1. `poetry run python app/manage.py runserver`

## Deploying
1. Setup `fly.io` command line: https://fly.io/docs/hands-on/install-flyctl
1. `fly deploy`

## TODO
- [x] Install Bootstrap
- [x] Integrate with font awesome for icons 
- [x] Allow upvoting
- [x] Create Admin delete view
- [x] Check longest post length
- [ ] Style presentation of upvoted Kinds
- [x] Sort the clouds by vote count
    - [ ] Make the height logarithmic
    - [ ] Add an animated transition
- [ ] Make upvote an Ajax call so page reload is not required
- [x] Add cloud frame to quotes
- [ ] Add copy button to quote 
- [x] Fix CSRF token error on create new
- [x] Integrate with Postgres on Fly.io
- [x] Add upvote button to quote
- [x] Find somewhere to deploy Django apps for free
    - [x] https://fly.io/docs/django/getting-started/
    - [x] Integrate gunicorn
- [ ] "You are not alone." --> debug negative sentiment
- [x] Add a zoom to view feature
- [ ] Add a separate page view of an individual quote
- [ ] Allow voting on zoomed in quotes
- [ ] Add a pastel like gradient background
- [ ] Add a cloud icon to create link/button 
- [ ] Add a share link to the site 
- [ ] Add a uniqueness check
- [x] Add a linter for kindness/wholesomeness 
    - [x] Sentiment analysis 
- [ ] Add anchor links 
- [x] Write a code of conduct
    - [x] Save whether a user has viewed to local storage on browser 
    - [x] No sensitive information 
    - [x] On the create page
- [x] Add a link to the source code
- [ ] Export to spreadsheet?
- [x] Make site responsive on mobile
- [ ] Add telemetry/analytics 
    - [ ] Mixpanel?
    - [ ] https://github.com/mixpanel/mixpanel-python
- [ ] Add share button to homepage 
- [ ] Add share button to quote 
- [ ] Add social links or a social link author link at bottom 

# Kind Cloud
An app for sharing kind words with others

## Running Locally
1. Populate an `.env` by copying and settings value from `example.env`
    1. Requires a RapidAPI account with a subscription to this API: https://rapidapi.com/twinword/api/sentiment-analysis
1. `poetry install`
1. `poetry shell`
1. `poetry run python app/manage.py runserver`

## TODO
- [x] Install Bootstrap
- [x] Integrate with font awesome for icons 
- [x] Allow upvoting
- [ ] Style presentation of upvoted Kinds
- [x] Sort the clouds by vote count
    - [ ] Make the height logarithmic
    - [ ] Add an animated transition
- [ ] Make upvote an Ajax call so page reload is not required
- [ ] Add cloud frame to quotes
- [ ] Add copy button to quote 
- [x] Add upvote button to quote 
- [ ] Find somewhere to deploy Django apps for free 
    - [ ] https://fly.io/docs/django/getting-started/
    - [ ] Integrate gunicorn
- [ ] Add a view of an individual quote or a zoom to view feature 
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
- [ ] Add a link to the source code
- [ ] Export to spreadsheet?
- [ ] Make site responsive on mobile
- [ ] Add telemetry/analytics 
    - [ ] Mixpanel?
    - [ ] https://github.com/mixpanel/mixpanel-python
- [ ] Add share button to homepage 
- [ ] Add share button to quote 
- [ ] Add social links or a social link author link at bottom 

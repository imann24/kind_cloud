# Kind Cloud
An app for sharing kind words with others

## Running Locally
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
- [ ] Add upvote button to quote 
- [ ] Find somewhere to deploy Django apps for free 
    - [ ] https://fly.io/docs/django/getting-started/
    - [ ] Integrate gunicorn
- [ ] Add a view of an individual quote or a zoom to view feature 
- [ ] Add a pastel like gradient background
- [ ] Add a cloud icon to create link/button 
- [ ] Add a share link to the site 
- [ ] Add a linter for kindness/wholesomeness 
    - [ ] Sentiment analysis 
    - [ ] GPT-4 integration?
    - [ ] https://huggingface.co/blog/sentiment-analysis-python
- [ ] Add anchor links 
- [ ] Write a code of conduct
    - [ ] Save whether a user has viewed to local storage on browser 
    - [ ] No sensitive information 
    - [ ] On the create page
- [ ] Add a link to the source code
- [ ] Export to spreadsheet?
- [ ] Make site responsive on mobile
- [ ] Add telemetry/analytics 
    - [ ] Mixpanel?
    - [ ] https://github.com/mixpanel/mixpanel-python
- [ ] Add share button to homepage 
- [ ] Add share button to quote 
- [ ] Add social links or a social link author link at bottom 

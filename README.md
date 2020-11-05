This is a python project to create a memory bank that can be used to store short categorised text entries.

The main tutorial used for this project was: https://realpython.com/flask-by-example-part-1-project-setup/


# Running locally:
Running the app locally:
Run: `python app.py`

# Heroku:
The service is hosted in two different heroku apps:
Production: https://archiememory.herokuapp.com/
Staging: https://archiememory-stage.herokuapp.com/

## Deploying the app:
Production: `git push pro master`
Staging: `git push stage master`

# Database:
The database currently consists of one table: memories, a memory has:
id: int, main key, auto incremental
content: string, the text to remember (eg: 'buy groceries')
category: string, the category of the memory (eg: 'to-dos')


TO DO:
Fix configs for pro and stage: Setting up the config was taught for a unix system, it doesnt seem to work for windows
<h1 align=center> Hangman</h1>

<p align=center>PLAY AND HAVE FUN!

"Hangman" is a classic paper and pencil guessing game where player needs to guess letters contained within a word, which ultimately brings user to the reveal of the secret word. <br>
 </p>

<img src="images/readme_images/hangman.jpg">

Live app link [here](https://hangman-pythonproject3.herokuapp.com/)

 ## Project Purpose

Create a fun game for users of all ages.

## User Experience

### User Stories

+ As a user, I would like to be able to …

1. have an easy interactive experience
2. easily see the feedback and progress
3. easily play again upon finishing the game


### App Owner Stories

+ As App Owner Stories, I would like to be able to provide …

1. a simple, straightforward intuitive user experience;
2. clear and input relevant feedback
3. possibility of restarting the game at the end

 ## Project Purpose

Create an app that can search tweets using Twitter API and outputs tweets with a chosen keyword in a max range of 100km. Also, create a table data with all tweets location grouped and counted. Data created can be viewed on terminal or stored on Google Spreadsheets. 

## User Experience

### User Stories

+ As a user, I would like to be able to …

1. easily add my preferred information like City, Country, language and keyword;
2. easily check if my information is correct;
3. decide if I want to get outputs on my terminal or just save data on Google spreadsheets;
4. check my created data on Google Spreadsheet.

### App Owner Stories

+ As App Owner Stories, I would like to be able to provide …

1. a simple, straightforward intuitive user experience;
2. clear output data on the terminal or cloud storage;
3. user's feedback in case of wrong input.
4. give the user the possibility to restart app in case of fatal errors.

## Functional Scope 

The following flowchart shows the flow of "Search your brand" graphically.

<img width= "800" src="images/readme_images/search_your_brand_flowchart.png">

## Features

### Welcome message 

Welcome user to the app. 

<img src="images/readme_images/greetings.png">

### User options

### Returning user defined options.

<img src="images/readme_images/tweets_table_explained.png">

### Option 3


## Future Features

I would like to ...

1. add more levels of difficulties with various words;
2. add hints which could help user to find out the secret word more easily;
3. add option for storing the highscores;

## Languages Used

Python 3.0

## Frameworks, Libraries & Programs Used

Git: Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
GitHub: GitHub is used to store the project's code after being pushed from Git.

## Testing and Code validation 


## Deployment 

This app is deployed using Heroku.

<details>
<summary>Heroku Deployment steps </summary>
 
 1. Ensure all dependencies are listed on requirements.txt. 
 
 Write on python terminal ` pip3 freeze > requirements.txt` and a list with all requirements will be created to be read by Heroku. 
 
 2. Setting up your Heroku

    2.1 Go to Heroku website (https://www.heroku.com/). 
    2.2 Login to Heroku and go to Create App.
    
    <img src="images/readme_images/deployment/heroku_login.png">
    
    <img src="images/readme_images/deployment/heroku_login2.png">
    
    2.3 Click in New and Create a new app
    
    <img src="images/readme_images/deployment/heroku_newapp.png">
    
    2.4 Choose a name and set your location
    
    <img src="images/readme_images/deployment/heroku_createnewapp.png">
    
    2.5. Navigate to the deploy tab
    
    <img src="images/readme_images/deployment/heroku_dashboard_deploy.png">
    
    2.6. Click in Connect to Github and search for 'nandabritto' GitHub account and 'search_your_brand' repository
    
    <img src="images/readme_images/deployment/heroku_github_deploy.png">
    
    2.7.  Navigate to the settings tab
    
    <img src="images/readme_images/deployment/heroku_dashboard_settings.png">
    
    2.8.  Click on Config Vars, and add your Twitter and Google Sheets API keys, Google Spreadsheets file and worksheets names.
    
    <img src="images/readme_images/deployment/heroku_vars_settings.png">
    
    2.9. Click on Add a buildpack on the same page. Select Python and node.js, ensuring Python is listed first after you save the changes.
    
    <img src="images/readme_images/deployment/heroku_buildpacks_settings.png">

3. Deployment on Heroku

    3.1.  Navigate to the Deploy tab.
    
    <img src="images/readme_images/deployment/heroku_dashboard_deploy.png">
    
    3.2.  Choose main branch to deploy and enable automatic deployment to build Heroku everytime any changes are pushed on the repository.
    
    <img src="images/readme_images/deployment/heroku_automatic_deploys.png">
    
    3.3 Click on manual deploy to build the app.  When complete, click on View to redirect to the live site. 
    
    <img src="images/readme_images/deployment/heroku_view.png">
</details>

<details>
<summary>Forking the GitHub Repository </summary>

* By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

    Log in to GitHub and locate the GitHub Repository
    At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
    You should now have a copy of the original repository in your GitHub account.

* Making a Local Clone

    Log in to GitHub and locate the GitHub Repository
    Under the repository name, click "Clone or download".
    To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
    Open Git Bash
    Change the current working directory to the location where you want the cloned directory to be made.
    Type git clone, and then paste the URL you copied in Step 3.

$ git clone https://github.com/nandabritto/search_your_brand

Press Enter. Your local clone will be created.

# Credits

### Work based on other code

[EarthLab](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/) - Used as a base for firsts pieces of code on this project.<br>

# Acknowledgements

+ To the Slack community as I have used the different channels to find answers to problems!
+ Stack Overflow is a valuable resource for solving lots of issues.
+ W3schools and Python libraries documentation for general reference.

I would also like to thank:

+ My fiancée Maja for her patience and support.
+ My mentor Rahul Lakhanpal for his time, support and guidance.


# Portafolio: Simulation of physical and not physicial systems
Kennet Julian Rueda Espinosa
Physics
Explora UN Mundo - Group 3
Proffesor: Andres Mican
2020-2
##About the project
This project is part of the asignature of Explora English at the National University of Colombia. I selected 6 documents between videos, books and articles which i think, are informative and useful for persons interested in simulations and modeling. I wrote a brief review or synopsis of each document. Also, i attached some simple simulations that i have make it for ilustrate part of the content. I hope you enjoy it.
*Links of each documents are atached in the tittle*

# [Project 1: Data Science Salary Estimator](https://github.com/PlayingNumbers/ds_salary_proj) 
* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing API using flask 

![](/images/positions_by_state.png)


# [Project 2: Ball Image Classifier](https://github.com/PlayingNumbers/ball_image_classifier) 
For this example project I built a ball classifier to identify balls from different sports. This could be useful for someone who is new to sports from a certain country. They could take a picture of a ball and an app could serve them some information about the history and rules of the game. This is the underlying model for building something with those capabilities. 

I was able to get the model to predict the sport of the ball with 94% accuracy after minimal tuning. For most of the cases this would meet the need of an end user of the app. To get these results I used transfer learning on a CNN trained on resnet34. This created time efficiencies and solid results. 

![](/images/matrix_results.png)

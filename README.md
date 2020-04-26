# Reddit Flair Detection. 
[Deployed on Heroku](https://asdasrfd.herokuapp.com/)
> This repositrory aim to detect Flairs( Special Tags) of Reddit post and deploying best model on Web. This have been done using diffrent classifier algorithm.
*** 
## Structure
``` bash
─── Reddit Flair Detector.  
    ├── Notebook  
        ├── Data_Scraping.ipyub (experiment log included)
        ├── EDA.ipyub (experiment log included)
        ├── Flair_Detector.ipyub (experiment log included) 
        ├── flair_dataset.csv
    ├── WebApp  
    ├── requirement.txt  
```
## Overview 
> After traning on multiple algorithm we came to this conclution.  
> `Random Forest Classifier` has best Accuracy with `Title + Body + Comments` as Input feature.  

| Model | Title | Body | Comments | Title + Body + Comments|
|-|-|-|-|-|
|Multinomial Naive Bayes | 64.92|33.27|40.69|69.44|
|Logistic Regression |68.72|38.16|41.77|79.57|
| Random Forest|69.26|42.13|42.86|84.27|
|Support Vector Machine |66.73| 35.26|41.05|74.14|
> Detailed Analysis [Here](https://github.com/ahmadkhan242/Reddit-flair-detection/blob/master/Notebook/3.%20Flair_Detector.ipynb)
## Installation and Execution.
- Clone the repository using `git clone` and then change the directory to root of the project
``` 
    git clone https://github.com/ahmadkhan242/Reddit-flair-detection.git
    cd Reddit-flair-detection
```
- Create a virtual Environament, activate it and install requirement.txt file
```
> virtualenv venv

> source ./venv/Scripts/activate 

> pip install -r requirement.txt
```
- For Jupyter Notebook
```
> cd Notebook
> jupyter lab or jupyter notebook
```
- For WebApp
```
> cd WebApp
> flask run
```
> Website Live at `http://127.0.0.1:5000/`.



## WebApp - [Deployment](https://asdasrfd.herokuapp.com/)
- `GET` request on `/` render main.html
- `POST` request with `post url` on `/` render main.html with result.
- `POST` request on `/automated_testing` returns `JSON` file.  

  ``` 
  > For testing purpose.  

      files = {'upload_file': open('file.txt','rb')}
      res = requests.post(url, files=files)

      with open('results.json', 'w') as f:
        f.write(res.text)
  ```
  > Screenshot [Here](https://github.com/ahmadkhan242/Reddit-flair-detection/tree/master/WebApp)

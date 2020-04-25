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

> pip install -r requirements.txt
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
- `GET` request on `/` render dashboard.html
- `POST` request with `post url` on `/` render dashboard.html with result.
- `POST` request on `/automated_testing` returns `JSON` file.  

  ``` 
      files = {'upload_file': open('file.txt','rb')}
      res = requests.post(url, files=files)

      with open('results.json', 'w') as f:
        f.write(res.text)
  ```

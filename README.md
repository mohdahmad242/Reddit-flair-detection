# Reddit Flair Detection.
> This repositrory aim to detect Flairs( Special Tags) of Reddit post and deploying best model on Web. This have been done using diffrent classifier algorithm.
*** 
## Structure
``` bash
─── Reddit Flair Detector.  
    ├── Notebook  
        ├── Data_Scraping.ipyub (experiment log included)
        ├── EDA.ipyub (experiment log included)
        ├── Flair_Detector.ipyub (experiment log included) 
    ├── WebApp  
    ├── requirement.txt  
```
## Installation and Execution.
- Clone the repository using `git clone` and then change the directory to root of the project
``` 
    git clone https://github.com/ahmadkhan242/SummerGeeks-2020.git
    cd SummerGeeks-2020
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
> python main.py
```
> Website Live at `http://127.0.0.1:5000/`.



## WebApp - [Deployment]()
- `GET` request on `/` render dashboard.html
- `POST` request with `post url` on `/` render dashboard.html with result.
- `POST` request on `/automated_testing` returns `JSON` file.  

  ``` 
      files = {'upload_file': open('file.txt','rb')}
      r = requests.post(url, files=files)

      with open('results.json', 'w') as f:
        f.write(result.text)
  ```

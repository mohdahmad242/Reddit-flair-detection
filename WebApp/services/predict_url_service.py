from ml_model.predict_flair import pred

def predict_url(text):
        flair = pred(text)
        return flair



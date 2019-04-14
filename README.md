# model-persistence

Scikit-learn pipeline (trained on Titanic data as an example) deployed as an API with Flask

Make a POST request to `/predict` with JSON data

```
{"columns":["sex","age","pclass"],
 "data":[["male",30,3],["female",NaN,1]]}
```

Get back an array of predictions

```
[0, 1]
```

### Links
- [Mike Bernico: Using Flask to serve a machine learning model as a RESTful webservice](https://www.youtube.com/watch?v=s-i6nzXQF3g)
- [Scikit-learn User Guide: Model Persistence](https://scikit-learn.org/stable/modules/model_persistence.html)
- [DataCamp: Turning Machine Learning Models into APIs in Python](https://www.datacamp.com/community/tutorials/machine-learning-models-api-python)
- [Transform ML models into native code with zero dependencies](https://news.ycombinator.com/item?id=19307740)
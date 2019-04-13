# model-persistence

Based on https://www.youtube.com/watch?v=s-i6nzXQF3g

Scikit-learn pipeline trained on Titanic data, deployed as an API with Flask

Make a POST request to `/predict` with JSON data

```
"columns":["sex","age","pclass"],
"data":[["male",30,3],["female",NaN,1]]
```

Get back a JSON array of predictions

```
[0, 1]
```
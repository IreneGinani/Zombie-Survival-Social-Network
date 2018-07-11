# ZSSN (Zombie Survival Social Network)

System for help non-infected people to share resources

## Requirements

* [Python](https://www.python.org/downloads/release/python-2712/) (2.7.12)
* [Django](https://docs.djangoproject.com/pt-br/2.0/)
* [Django Rest Framework](http://www.django-rest-framework.org/)
* [Model Mommy](http://model-mommy.readthedocs.io/en/latest/basic_usage.html)

Is important fill the default resources:

```
python manage.py makemigrations restApi
python manage.py migrate restApi
python manage.py loaddata restApi/fixture/default.json

```
To run the server:

```
python manage.py runserver

```
To run the tests:

```
python manage.py test

```
## Routes

### Survivors

**POST**  to register a new survivor.


```
api/v1/survivor/

{
  "name": "Maria Aparecida",
  "age": 30,
  "gender": "Feminino",
  "latitude": -16.346867430274,
  "longitude": -48.948227763174,
  "is_infected": false,
  "count_reports": 0,
  "inventory": {
  		"inventory_resources_attributes": [
	  	    {"id": 1 },
		    {"id": 2 },
                   {...}
	  	]
  }
}
```
The table shows the value of the ids. We have the score that each survivor will have when owning the item. 

| Item | id | points
| ------ | ------ | -----|
| Ammuntion | 4 | 1 |
| Medication | 3 | 2 |
| Food | 1 | 3 |
| Water | 2 | 4 | 


**PUT** to update a survivor location
```
api/v1/survivor/{id_survivor}/

{
    "longitude": 10,
    "latitude": 11,
}

```

**GET** to report a survivor as infected.

```
api/v1/survivor/report_infection/{id_survivor_infected}/
```


**PUT** to trade items between survivors.
```
api/v1/survivor/trade_items/{survivor1_id}/{item1}/{survivor2_id}/{item2}

```

The resources should follow the pattern `count-resource-count-resources-..` (e.g. 1-ammunition-1-food or 1-water)


### Reports

**GET** Percentage of infected survivors.
```
/api/v1/survivor/survivors_infected/
```

**GET** Percentage of non-infected survivors.
```
/api/v1/survivor/survivors_no_infected/
```

**GET** Average amount of each kind of resource by survivor
```
/api/v1/survivor/avg_items/
```
**GET**  Total of Points lost because of infected survivors
```
/api/v1/survivor/points_lost/
```
**GET**  Points lost because of a infected survivor
```
/api/v1/survivor/points_lost/{id}
```

# How use this project?

### Firstly install dependencies
```shell
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Then you can create new groups and promo codes
```shell
python manage.py addpromo [codes amount] [group name]
```

### Also, you can search for promo codes
```shell
python manage.py searchpromo [promo code]
```

### All data stored in groups.json in root directory

### Also, you can run test with pytest and coverage
```shell
coverage run -m pytest
coverage report
```

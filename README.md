# SBM - Skill based Matchmaking

## Pre-requisites
```python 3.8``` <p></p>
```git```

## Libraries Used
```itertools```  standard library for iterating and creating combinations or permutations. <p></p>
```unittest```  Python built in unit testing framework for creating test cases
# How to run Code

### Install Python instruments
1) Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
2) Install pip pckage manager  ```python get-pip.py``` <p></p>  upgrade using ```python -m pip install --upgrade pip```
3) Install virtualenv python3 package ```pip install virtualenv```

### Start virtualenv

```
> virtualenv -p python3.8 venv 
> source venv/bin/activate
```

### Run the code 
* Main script
```
python app.py
```
* <p>Test cases (it is advised to run the test cases one at a time).<p></p>
Used ```unittest``` library for testing.
List of test cases defined in ```test.py``` :<h5></h5>
```test_take_input``` ```test_take_input_no_of_players``` ```test_output``` ```test_output_2``` ```test_create_team```
```test_create_team_2``` ```test_form_matches``` ```test_find_average_score``` ```test_quality_check```

Run for validating:

> python -m unittest test.MyTestCase.'any_test_case_name'
```
> python -m unittest test.MyTestCase.test_take_input
> python -m unittest test.MyTestCase.test_take_input_no_of_players
...
```

## Versioning

I used [Git](https://git-scm.com/) for versioning.

## Authors

* **Akash Kumar** - [Linkedin](https://www.linkedin.com/in/akash-kumar-747931145/), [GitHub](https://github.com/Akash280999) 
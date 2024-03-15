# Cat Facts API Test


[Cat Facts](https://cat-fact.herokuapp.com/)

[API Documents](https://alexwohlbruck.github.io/cat-facts/docs/)

## Test Cases
All response should in JSON form.

| Method | Test                  | Expected Result                                                                             |
| ------ | --------------------- | ------------------------------------------------------------------------------------------- |
| GET    | Get a random fact     | Status code:<span style="color: green">200</span> "type" is "cat", "text" type is string.   |
| GET    | ?animal_type=cat      | Status code:<span style="color: green">200</span> Same as default.                          |
| GET    | ?animal_type=dog      | Status code:<span style="color: green">200</span> "type" is "dog".                          |
| GET    | ?animal_type=cat,dog  | Status code:<span style="color: green">200</span> "type" is "cat" or "dog"                  |
| GET    | ?animal_type=         | Status code:<span style="color: green">200</span> Same as default.                          |
| GET    | ?amount=1             | Status code:<span style="color: green">200</span> Same as default.                          |
| GET    | ?amount=2             | Status code:<span style="color: green">200</span> Response in array of Facts. length is 2   |
| GET    | ?amount=500           | Status code:<span style="color: green">200</span> Response in array of Facts. length is 500 |
| GET    | ?amount=501           | Status code:<span style="color: red">405</span>                                             |
| GET    | ?amount=0             | Status code:<span style="color: green">200</span> Response in empty array.                  |
| GET    | Get fact by ID        | Status code:<span style="color: green">200</span> "_id" is the same as query                |
| GET    | Get from not exist ID | Status code:<span style="color: red">404</span>                                             |

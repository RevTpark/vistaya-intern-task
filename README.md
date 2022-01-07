# Tech Stack
**Language:** Python\
**Framework:** Flask, Flask-REST\
**Database:** Postgresql
**Host**: Heroku

## Why Flask over Django?
I know Django and Flask quite well. But since what this task needed wasn't so heavy on server side. I knew Flask could do the job just right and more efficiently rather than having to handle unnecessary files in Django.

# API schema

## Question 1
## Items API 
* Route: ```/api/items```
* Method: ```POST```
* Input: ```items```. Takes a list of n items as JSON object.
* Output: ```valid_entries, invalid_entries, min, max, average``` returned as JSON object.
* Codes: 
    * ```200``` - For all inputs

### Example
- Input:
```
{
    "items": [1, 4, -1, "hello", "world", 0, 10, 7]
}
```
- Ouput:
```
{
    "valid_entries": 4,
    "invalid_entries": 4,
    "min": 1,
    "max": 10,
    "average": 5.5
}
```

## Question 2
## Book Slot API
* Route: ```/api/slot/booking```
* Method: ```POST```
* Input: ```slot, name```. Takes ```slot``` a number between 0 to 23 and ```name``` of the participant as JSON object.
* Output: ```status``` returned as JSON object.
* Codes:
    * ```404``` - If slot is not within 0 and 23.
    * ```201``` - If the slot booking is confirmed.
    * ```400``` - If slot is already full.
    
### Example 1  
- Input:
```
{
    "slot": 2,
    "name": "ian"
}
```
- Output:
```
    "status": "Confirmed"
```

### Example 2
- Input:
```
{
    "slot": 2,
    "name": "clint"
}
```

- Output:
```
{
    "status": "slot full, unable to save booking for clint in slot 2"
}
```

## Book Slot API
* Route: ```/api/slot/booking```
* Method: ```GET```
* Input: NONE.
* Output: ```length, slots``` returned as JSON object.
* Codes:
    * ```200``` - Default code.
    
### Example
 - Output:
 ```
 {
    "length": 4,
    "slots": [
        {
            "slot": 0,
            "name": [
                "john",
                "jane"
            ]
        },
        {
            "slot": 1,
            "name": [
                "mellisa"
            ]
        },
        {
            "slot": 2,
            "name": [
                "ian"
            ]
        },
        {
            "slot": 3,
            "name": [
                "ian"
            ]
        }
    ]
}
 ```

## Cancel Slot API
* Route: ```/api/slot/cancel```
* Method: ```POST```
* Input: ```slot, name```. Takes ```slot``` a number between 0 to 23 and ```name``` of the participant as JSON object.
* Output: ```status``` returned as JSON object.
* Codes:
    * ```404``` - If slot is not found or the name in that slot is not found.
    * ```200``` - If the slot is deleted successfully.

### Example 1
- Input:
```
{
    "slot": 2,
    "name": "ian"
}
```

- Output:
```
{
    "status": "canceled booking for ian in slot 2"
}
```

### Example 2
- Inout:
```
{
    "slot": 2,
    "name": "magnus"
}
```

- Output:
```
{
    "status": "no booking for the name magnus in slot 2"
}
```

## Question 3
## Sqaure Validator API
* Route: ```/api/plot```
* Method: ```POST```
* Input: ```x, y```. Takes ```x``` and ```y``` coordinates as JSON object.
* Output: ```status``` returned as JSON object.
* Codes:
    * ```200``` - For all inputs.
    
### Example 
- Input:
```
{
    "x": 1,
    "y": 1
}
```
- Output:
```
{
    "status": "Success (1, 1) (1, 5) (5, 5) (5, 1)"
}
```







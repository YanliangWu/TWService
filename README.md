# TWService
TW Service, this contains 2 part, a flask web service that accepts CLI, or a command line interface to do one-off request handling. 

## Assumptions
Currently there are some assumptions: 
- We require user to specify the id to update/delete the record.
- When update record, fields that user did not set, will not be updated. 


## TODO LIST
- Entitlement Check
- DML should check if the original record is there before proceed.
- Exception handling is broken, need to have better try catch block. 
- We should consider keep the update entry by using knowledge time model 
- Containerlize this and move to k8s
- WSGI for service
- Better service handler
- Config to connect to database
- MySQL connection
- CORS? (Not necessary)


## Effort Log
- Aug 18: 11:30 - 1:40AM (Aug19)
  - Create service, create a in memory DAO for testing
- Aug 20: 11:30 - 2:15 AM (Aug21)
  - Create cli, Mysql connector

## Swagger Doc

Check swagger.json for swagger document. 


## Connect to the project host
- Use the provided ssh pkey and run `ssh opc@168.138.207.149 -i [private.key]`
- This host is provisioned with a simple MySQL instance and everything are deployed. 


## Application CLI

Get all records from tower table
```
python -m application.twcli --action get
```

Insert new record into tower table
```
python -m application.twcli --action insert --username andrew --description desc 
```

Update record into tower table (by id)
```
python -m application.twcli --action update --id '723a8de9-3efd-4248-a955-1ff1f4957b77' --username andrew2
```

Delete record from tower table (by id)
```
python -m application.twcli --action delete --id '12295235-55e2-483e-950b-bc4ec464a746'
```

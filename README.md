# TWService
TW Service, this contains 2 part, a flask web service that accepts CLI, or a command line interface to do one-off request handling. 

## Assumptions
Currently there are some assumptions: 
- We require user to specify the id to update/delete the record.
- When update record, fields that user did not set, will not be updated. 

## TODO LIST
- Python timestamp -> MySQL timestamp
- ~~DML should check if the original record is there before proceed.~~
- Exception handling is broken, need to have better try catch block. 
- ~~Config to connect to database~~
- Fix service, currently it is broken due to some interface changes
- Unit Tests (made something but should be better)
- Credentials embedded in config file, should base64 it and put it to a vault. 
- Add CLI help function, also input validation is missing. 
- gitignore.. 



#### Good to have
- Keep the update history by using knowledge time model 
- Entitlement Check
- Containerlize this and move to k8s
- WSGI for service
- MySQL connection
- CORS?


## Effort Log
- Aug 18: 11:30 - 1:40AM (Aug19)
  - Create service, create a in memory DAO for testing
- Aug 20: 11:30 - 3:00 AM (Aug21)
  - Create CLI, Mysql connector, formatting, documents, bug fixes.
- Aug 21: 7:00 - 8:00 
  - Setting up subinterfacee in centos in oracle cloud
    - Confirm it won't work as it limits multiple VNIC in this host. 
    - Ended up with creating a new AWS account and created a EC2 instsance
- Aug 22: 9:00 - 10:00
  - Setting up the subinterface, mysql in EC2 instance. 
  - Some small fixes and setting up the repo. 
  - Also added some small fixes. 

## Swagger Doc
Check swagger.json for swagger document, this is only for the service only. 


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

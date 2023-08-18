# TWService
TW Service, this contains 2 part, a flask web service that accepts CLI, or a command line interface to do one-off request handling. 

## Assumptions
Currently there are some assumptions: 
- We require user to specify the id to update/delete the record.
- When update record, fields that user did not set, will not be updated. 


## TODO LIST
- Exception handling is broken.
- We should consider keep the update entry by using knowledge time model 
- Containerlize this and move to k8s
- WSGI for service
- Better service handler
- Config to connect to database
- MySQL connection


## Effort Log
- Aug 18: 11:30 - 1:40AM (Aug19)
  - Create service, create a in memory DAO for testing

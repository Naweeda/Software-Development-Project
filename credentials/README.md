# Credentials Folder

## The purpose of this folder is to store all credentials needed to log into your server and databases. This is important for many reasons. But the two most important reasons is
    1. Grading , servers and databases will be logged into to check code and functionality of application. Not changes will be unless directed and coordinated with the team.
    2. Help. If a class TA or class CTO needs to help a team with an issue, this folder will help facilitate this giving the TA or CTO all needed info AND instructions for logging into your team's server. 


# Below is a list of items required. Missing items will causes points to be deducted from multiple milestone submissions.

1. Server URL or IP : ec2-54-189-213-226.us-west-2.compute.amazonaws.com	
2. SSH username : ubuntu
3. SSH password or key.
    <br> If a ssh key is used please upload the key to the credentials folder.
4. Database URL or IP and port used.
    <br><strong> NOTE THIS DOES NOT MEAN YOUR DATABASE NEEDS A PUBLIC FACING PORT.</strong> But knowing the IP and port number will help with SSH tunneling into the database. The default port is more than sufficient for this class.
    host : csc648.cszroavxh2pu.us-west-2.rds.amazonaws.com
    port : 3306
5. Database username : root
6. Database password : mypass123
7. Database name : mydb
8. Instructions on how to use the above information.


## Accessing to database
Download mysql workbench for logging in the database server. Plug the information of database above to log in 
## SSH to server
First change permisision of the pem file that is included in the folder
```
chmod 400 margonguyen.pem
```
ssh to the server by using the command below

```
ssh -i "margonguyen.pem" ubuntu@ec2-52-12-39-147.us-west-2.compute.amazonaws.com 
```




# Most important things to Remember
## These values need to kept update to date throughout the semester. <br>
## <strong>Failure to do so will result it points be deducted from milestone submissions.</strong><br>
## You may store the most of the above in this README.md file. DO NOT Store the SSH key or any keys in this README.md file.

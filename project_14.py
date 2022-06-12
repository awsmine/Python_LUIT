#!/usr/bin/env python3.7
# create a variable to hold a place in memory for the list of AWS services
aws_services = []

# using 'append' method, add an object to the list
aws_services.append('Batch')
aws_services.append('CloudWatch')
aws_services.append('DynamoDB')
aws_services.append('EC2')
aws_services.append('Lambda')
aws_services.append('S3')


# using 'insert' method, add an object to the list by index
aws_services.insert(0, 'Athena')
aws_services.insert(1, 'Aurora')
aws_services.insert(5, 'FSx')


# print the list and the length of the list
length = len(aws_services)
print("This is the list of AWS services:", aws_services, " and the length of the list is: ", length)

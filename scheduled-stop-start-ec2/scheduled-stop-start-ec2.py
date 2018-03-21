#!/usr/bin/python

'''
Instances with tag nighstop=true should be stopped at STOP_TIME and started at START_TIME
start-stop.py START_TIME STOP_TIME
'''

import sys
import boto3
import datetime


START_TIME = str(sys.argv[1])
STOP_TIME = str(sys.argv[2])
#STOP_HOUR = 16
#START_HOUR = 18


def start_stop_instances(ec2,instances_id):
    current_time = datetime.datetime.utcnow()
    print("Current time is:{} ".format(current_time))
    print("DEBUG hora: {}".format(current_time.hour))
    if current_time.hour in range(STOP_HOUR,START_HOUR):
        print("DEBUG,instances stoppping instance_id: {}".format(instances_id))
        #ec2.instances.filter(InstanceIds=instances_id).stop()
    else:
        print("DEBUG,instances starting instance_id: {}".format(instances_id))
        ec2.instances.filter(InstanceIds=instances_id).start()


if len(sys.argv) == 1:
    print("Usage: sys.argv[0] STOP_TIME START_TIME")

# Connect to EC2
ec2 = boto3.resource('ec2')
# Get information for all running instances
running_instances = ec2.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running','stopped']}])
instances_id = []
for instance in running_instances:
    print("DEBUG intance: {}".format(instance.id))
    for tag in instance.tags:
        print("DEBUG tag: {}".format(tag))
        if 'nightstop' in tag['Key']:
            nighstop_value = tag['Value']
            if nighstop_value == "true":
               instances_id.append(instance.id)
               start_stop_instances(ec2,instances_id)




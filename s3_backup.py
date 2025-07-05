import boto3

s3= boto3.resource("s3")
def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3,bucket_name,region):
    s3.create_bucket(Bucket=bucket_name,
                     CreateBucketConfiguration={
                         'LocationConstraint': region,
                     },)
    print("Bucket created successfully")

def upload_backup(s3,file_name,bucket_name,key_name):
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup Uploaded Successfully")

bucket_name = "python-for-deops"
region= "us-east-2"
file_name = "C:/Users/NISHANT/Downloads/Pyhton-Devops/backups/backup_2025-07-05.tar.gz"

#create_bucket(s3,bucket_name,region)
#show_buckets(s3)
upload_backup(s3,file_name,bucket_name,"my-backup.tar.gz")
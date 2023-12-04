# Example for Code Engine jobs

## Contents

- [Example for Code Engine jobs](#example-for-code-engine-jobs)
  - [Contents](#contents)
  - [1. About Code Engine jobs](#1-about-code-engine-jobs)
  - [2. About IBM Cloud Object Storage SDK (S3)](#2-about-ibm-cloud-object-storage-sdk-s3)
  - [3. About this example](#3-about-this-example)
    - [3.1 Using this code in your environment](#31-using-this-code-in-your-environment)
  - [Sources](#sources)

## 1. About Code Engine jobs

IBM Cloud® Code Engine is a fully managed, serverless platform that runs your containerized workloads, including batch job or application workloads. Learn about running batch jobs in IBM Cloud® Code Engine.

A job runs one or more instances of your executable code. Unlike applications, which handle HTTP requests, jobs are designed to run one time and exit.

You can scale batch jobs by defining multiple instances. Workloads can be split into parallel tasks to reduce compute time. You can set the job to run with automatic retry to address failing workloads within a job instance. You can trigger batch jobs manually, programmatically, and by events, such as Object Storage events.

When you create a job, you can specify the workload configuration information that is used each time that the job is run.

Typical batch job workloads include:

- Machine model training
- Analyzing files, such as voice analysis or image recognition
- Compressing or decompressing files
- Archiving information

When you create a job, you can specify workload configuration information that is used each time that the job is run.

## 2. About IBM Cloud Object Storage SDK (S3)

IBM Cloud® Object Storage is a highly available, durable, and secure platform for storing unstructured data. Unstructured data (sometimes called binary or "blob" data) refers to data that is not highly structured in the manner of a database. Object storage is the most efficient way to store PDFs, media files, database backups, disk images, or even large structured datasets.

The files that are uploaded into IBM Cloud Object Storage are called objects. Objects can be anywhere from very small (a few bytes) [to very large] (up to 10TB). They are organized into buckets that serve as containers for objects, and which can be configured independently from one another in terms of locations, resiliency, billing rates, security, and object lifecycle. Objects themselves have their own metadata in the form of user-defined tags, legal holds, or archive status. Within a bucket, the hierarchy of objects is effectively "flat", although it is possible to add prefixes to object names to provide some organization and to provide flexibility in listing and other operations.

## 3. About this example

This little code in Node.Js syntax is intended to give a hint of how the jobs can be used to handle an ICOS trigger to Code Engine Jobs, you can find some help on the configuration of this trigger [here](https://cloud.ibm.com/docs/codeengine?topic=codeengine-eventing-cosevent-producer#obstorage_ev_job).

You will need this data in order to use the ICOS sdk:

- `endpoint`: the endpoint of your ICOS instance, [info](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints)
- `apiKeyId`: your API Key (need some permisions in IAM), [info](https://cloud.ibm.com/docs/account?topic=account-userapikey&interface=ui#create_user_key)
- `serviceInstanceId`: this value is in your HMAC Credentials of the Service Credentials of your instance, [info](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-service-credentials)

For security reasons, you can pass this information as environment variables of your job, in order to not show them in the code explicitly. The other environment variable showed in the code is [CE_DATA](https://cloud.ibm.com/docs/codeengine?topic=codeengine-eventing-cosevent-producer#subcos-envvar-cedata), which contains all the information of the ICOS event that triggers the job, you can use this information in order to make requests with the ICOS sdk, such as get the object, update it, copy to another bucket, etc.

### 3.1 Using this code in your environment

Once we have a Code Engine project ready, we can create a Job from this repository, and then add an event subscription in order to trigger this job every time we upload a file in the bucket that we choose.

- Create the job with the environment variables: [here](https://cloud.ibm.com/docs/codeengine?topic=codeengine-job-plan)
- Set up the ICOS instance and bucket you prefer: [here](https://cloud.ibm.com/docs/codeengine?topic=codeengine-eventing-cosevent-producer)
- Create event subscription for the job: [here](https://cloud.ibm.com/docs/codeengine?topic=codeengine-eventing-cosevent-producer#obstorage_ev_job)

## Sources

- [IBM Cloud Code Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-getting-started)
- [IBM Cloud Object Storage - Node.js SDK](https://ibm.github.io/ibm-cos-sdk-js/)

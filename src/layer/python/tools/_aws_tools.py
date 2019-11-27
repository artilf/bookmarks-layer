import boto3
from botocore.client import BaseClient
from boto3.resources.base import ServiceResource


def prepare_get_aws_client(service: str):
    client = None

    def get_aws_client() -> BaseClient:
        nonlocal client
        if client is None:
            client = boto3.client(service)
        return client
    return get_aws_client


def prepare_get_aws_resource(service: str):
    resource = None

    def get_aws_resource() -> ServiceResource:
        nonlocal resource
        if resource is None:
            resource = boto3.resource(service)
        return resource
    return get_aws_resource

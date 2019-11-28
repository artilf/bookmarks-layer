def can_access(event, ssm_client, is_header=False) -> bool:
    store = event["headers"] if is_header else event["queryStringParameters"]
    request_token = store.get("Authorization")
    if request_token is None:
        return False

    resp = ssm_client.get_parameter(Name="BookmarksPassword", WithDecryption=True)

    return request_token == resp["Parameter"]["Value"]

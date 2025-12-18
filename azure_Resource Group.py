from azure.mgmt.resource import ResourceManagementClient

client = ResourceManagementClient(credential, "SUBSCRIPTION_ID")

if client.resource_groups.check_existence("rg-dev"):
    print("RG exists")
else:
    raise SystemExit("RG not found")

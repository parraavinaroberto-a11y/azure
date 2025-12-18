from azure.mgmt.compute import ComputeManagementClient

compute = ComputeManagementClient(credential, "SUBSCRIPTION_ID")
compute.virtual_machines.begin_deallocate("rg", "vmname")

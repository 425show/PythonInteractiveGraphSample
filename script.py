# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from azure.identity import InteractiveBrowserCredential
from msgraph.core import GraphClient
import uuid
import json

broswer_credential = InteractiveBrowserCredential(client_id='7537790f-b619-4d30-a804-1c6b8b7f1523')
graph_client = GraphClient(credential=broswer_credential)
scopes = ['Application.ReadWrite.All', 'User.Read']


# %%


result = graph_client.get('/organization')
tenantJson = json.dumps(result.json())
tenant = json.loads(tenantJson)

print(f"Tenant Id: {tenant['id']}")



# %%

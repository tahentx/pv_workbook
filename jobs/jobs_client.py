
from google.cloud import talent_v4beta1
import six


def sample_create_tenant(project_id, external_id):
    """Create Tenant for scoping resources, e.g. companies and jobs"""

    client = talent_v4beta1.TenantServiceClient()

    # project_id = 'Your Google Cloud Project ID'
    # external_id = 'Your Unique Identifier for Tenant'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(external_id, six.binary_type):
        external_id = external_id.decode('utf-8')
    parent = client.project_path(project_id)
    tenant = {'external_id': external_id}

    response = client.create_tenant(parent, tenant)
    return response
    print('Created Tenant')
    print('Name: {}'.format(response.name))
    print('External ID: {}'.format(response.external_id))


def sample_list_companies(project_id, tenant_id):
    """List Companies"""

    client = talent_v4beta1.CompanyServiceClient()

    tenant_id = NULL
    if isinstance(tenant_id, six.binary_type):
        tenant_id = tenant_id.decode('utf-8')
    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')

    parent = client.tenant_path(project_id, tenant_id)

    # Iterate over all results
    for response_item in client.list_companies(parent):
        print('Company Name: {}'.format(response_item.name))
        print('Display Name: {}'.format(response_item.display_name))
        print('External ID: {}'.format(response_item.external_id))

project_id = '900448978521'
external_id = '6885'

sample_list_companies(project_id)

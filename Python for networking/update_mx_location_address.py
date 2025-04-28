
import meraki

API_KEY = 'your_api_key'
ORG_ID = 'your_org_id'
NEW_ADDRESS = 'your_new_address'

dashboard = meraki.DashboardAPI(API_KEY)
inventory = dashboard.organizations.getOrganizationInventory(ORG_ID)

for device in inventory:
    if 'MS' in device['model']:  # Check if the device is a switch
        dashboard.devices.updateDevice(
            device['serial'],
            address=NEW_ADDRESS
        )

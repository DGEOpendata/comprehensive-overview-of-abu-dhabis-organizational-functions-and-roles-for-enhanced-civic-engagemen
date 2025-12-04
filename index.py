python
import pandas as pd

# Load the dataset
file_path = 'Abu_Dhabi_Organizations_and_Their_Roles.csv'
data = pd.read_csv(file_path)

# Function to get organization details
def get_organization_details(org_name):
    try:
        org_details = data[data['Organization Name'] == org_name]
        if not org_details.empty:
            return org_details.iloc[0].to_dict()
        else:
            return 'Organization not found.'
    except Exception as e:
        return str(e)

# Example usage
organization_name = 'Abu Dhabi City Municipality'
print(get_organization_details(organization_name))

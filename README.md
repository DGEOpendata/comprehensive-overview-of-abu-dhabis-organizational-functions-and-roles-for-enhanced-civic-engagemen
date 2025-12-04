# Abu Dhabi Organizations and Their Roles Dataset

## Overview
This dataset provides comprehensive information about various organizations operating in Abu Dhabi, detailing their names and primary functions. It covers entities across sectors like heritage, finance, education, and conservation.

## Getting Started
To start using the dataset, you need to have a CSV file named `Abu_Dhabi_Organizations_and_Their_Roles.csv` containing the information about the organizations.

### Prerequisites
- Python 3.x
- Pandas library: You can install it using `pip install pandas`.

### Loading the Dataset
You can load the dataset using Pandas:
python
import pandas as pd

data = pd.read_csv('Abu_Dhabi_Organizations_and_Their_Roles.csv')


### Retrieving Organization Details
The script provides a function to retrieve details of an organization by its name:
python
def get_organization_details(org_name):
    try:
        org_details = data[data['Organization Name'] == org_name]
        if not org_details.empty:
            return org_details.iloc[0].to_dict()
        else:
            return 'Organization not found.'
    except Exception as e:
        return str(e)


### Example Usage
To get details of an organization, use the function `get_organization_details`:
python
organization_name = 'Abu Dhabi City Municipality'
print(get_organization_details(organization_name))

This will return a dictionary containing the details of the specified organization.

## Contributing
We welcome contributions to enhance the dataset and its usability. Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
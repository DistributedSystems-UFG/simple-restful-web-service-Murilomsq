import requests
import const

def serviceTester():
    api_base_url = 'http://' + const.IP_ADD + ':' + str(const.PORT) + '/empdb/employee'

    # Test get_all_employees endpoint
    api_url = api_base_url 
    response = requests.get(api_url)
    print (response.json())

    # Test get_an_employee endpoint
    api_url = api_base_url + '/201'
    response = requests.get(api_url)
    print (response.json())

    # Test update_employee endpoint
    api_url = api_base_url + '/101'
    update = {"title":"Programmer"}
    response = requests.put(api_url, json=update)
    print (response.json())

    # Test create_employee endpoint
    api_url = api_base_url
    employee = {"id":"301", "name":"J. Silva", "title":"Senior Programmer"}
    response = requests.post(api_url, json=employee)
    print (response.json())

    # Test delete_employee endpoint
    api_url = api_base_url + '/101'
    response = requests.delete(api_url)
    print (response.json())

if __name__ == '__main__':
    serviceTester()

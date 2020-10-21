from iTestBroadsoftAPI.api import ITestBroadworksAPI

HOST = '10.255.10.163'
USERNAME = 'itestautomation'
PASSWORD = 'iTest@123'

ITEST_BROADWORKS_API = ITestBroadworksAPI(host=HOST,
                                          username=USERNAME,
                                          password=PASSWORD)


def delete_user_schedules(phone_number):
    ITEST_BROADWORKS_API.delete_user_schedules(phone_number=phone_number)


if __name__ == '__main__':
    delete_user_schedules(phone_number='7025634890')

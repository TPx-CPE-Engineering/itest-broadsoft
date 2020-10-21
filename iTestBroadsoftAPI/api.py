from broadworks_ocip import BroadworksAPI


class ITestBroadworksAPI(BroadworksAPI):
    domain = '@lab-sv.telepacific.com'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete_user_schedules(self, phone_number):
        from broadworks_ocip.types import ScheduleKey

        user_id = phone_number + self.domain

        response = self.command('UserScheduleGetListRequest',
                                user_id=user_id)

        schedule_keys_to_del = []
        for schedule_name, schedule_type in zip(response.schedule_name, response.schedule_type):
            schedule_keys_to_del.append(ScheduleKey(schedule_name=schedule_name,
                                                    schedule_type=schedule_type))

        for key in schedule_keys_to_del:
            self.command('UserScheduleDeleteListRequest',
                         user_id=user_id,
                         schedule_key=key)

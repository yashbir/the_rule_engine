from datetime import datetime


class Operations:

    @classmethod
    async def greater_number_comparision(cls, event, rule):
        """
        Check if number is greater than given value
        :param event: dict
        :param rule: dict
        :return: boolean
        """
        return int(float(event['value'])) > rule['value']

    @classmethod
    async def lesser_number_comparision(cls, event, rule):
        """
        Check if number is greater than given value
        :param event: dict
        :param rule: dict
        :return: boolean
        """
        return int(float(event['value'])) < rule['value']

    @classmethod
    async def equal_number_comparision(cls, event, rule):
        """
        Check if number is greater than given value
        :param event: dict
        :param rule: dict
        :return: boolean
        """
        return int(float(event['value'])) == rule['value']

    @classmethod
    async def string_equality_comparision(cls, event, rule):
        """
        Check if string is equal to given value
        :param event: dict
        :param rule: dict
        :return: boolean
        """
        return event['value'] == rule['value']

    @classmethod
    async def string_partial_comparision(cls, event, rule):
        """
        Check if string partially equal given value
        :param event: dict
        :param rule: dict
        :return: boolean
        """
        return event['value'] in rule['value']

    @classmethod
    async def greater_datetime_comparision(cls, event, rule):
        """
        Check if datetime is greater than given value
        :param event: dict
        :param rule: dict
        :return: boolean
        """
        return (datetime.strptime(event['value'], '%Y-%m-%d %H:%M:%S')
                > datetime.strptime(rule['value'], '%Y-%m-%d %H:%M:%S'))

    @classmethod
    async def lesser_datetime_comparision(cls, event, rule):
        """
        Check if datetime is less than given value
        :param event: dict
        :param rule: dict
        :return: boolean
        """
        return (datetime.strptime(event['value'], '%Y-%m-%d %H:%M:%S')
                < datetime.strptime(rule['value'], '%Y-%m-%d %H:%M:%S'))

    @classmethod
    async def equal_datetime_comparision(cls, event, rule):
        """
        Check if datetime is equal to the given value
        :param event: dict
        :param rule: dict
        :return: boolean
        """
        return (datetime.strptime(event['value'], '%Y-%m-%d %H:%M:%S')
                == datetime.strptime(rule['value'], '%Y-%m-%d %H:%M:%S'))

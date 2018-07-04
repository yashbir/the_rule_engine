import os
import constants

from db_helper import DbHelper


class Ruler:

    @classmethod
    async def run(cls):
        """
        Create a rule
        """
        signal = input(constants.signal_prompt)
        value_type = None
        while value_type not in constants.value_type:
            value_type = input(constants.value_type_prompt)

        sub_ruler = getattr(cls, constants.value_type[value_type])
        await sub_ruler(signal)

    @classmethod
    async def create_rule_for_integer(cls, signal):
        """
        Create rule for integer data
        :param signal: string
        :return: None
        """
        rule = input(constants.integer_prompt)
        value = input(constants.value_prompt)

        # Insert the rule
        payload = {
            'signal': signal,
            'rule': rule,
            'value': int(value),
            'value_type': 'integer'
        }
        await DbHelper.insert(constants.rules_table, payload)

    @classmethod
    async def create_rule_for_string(cls, signal):
        """
        Create rule for string data
        :param signal: string
        :return: None
        """
        rule = input(constants.string_prompt)
        value = input(constants.value_prompt)

        # Insert the rule
        payload = {
            'signal': signal,
            'rule': rule,
            'value': str(value),
            'value_type': 'string'
        }
        await DbHelper.insert(constants.rules_table, payload)

    @classmethod
    async def create_rule_for_datetime(cls, signal):
        """
        Create rule for datetime data
        :param signal: string
        :return: None
        """
        rule = input(constants.datetime_prompt)
        value = input(constants.value_prompt)

        # Insert the rule
        payload = {
            'signal': signal,
            'rule': rule,
            'value': value,
            'value_type': 'datetime'
        }
        await DbHelper.insert(constants.rules_table, payload)

import os
import json
import constants

from db_helper import DbHelper
from operations import Operations


class EventProcessor:
    """
    Class for processing streaming events
    """

    @classmethod
    async def run(cls):
        """
        Run event processing
        """
        file_path = input(constants.file_prompt)
        if os.path.isfile(file_path):
            print('Reading file...')
            with open(file_path, 'r') as fd:
                data = json.load(fd)
            await cls.apply_rules(data)
        else:
            print('Please provide a correct file path')

    @classmethod
    async def apply_rules(cls, data):
        """
        Apply rules
        :param data: list
        :return: invalid data
        """
        invalid_events = []

        # Purging table
        await DbHelper.purge_table(constants.results_table)
        for event in data:
            event_rules = await DbHelper.get_rules(constants.rules_table,
                                                   'signal', event['signal'],
                                                   'value_type', event['value_type'].lower())
            if event_rules:
                event_test = await cls.if_violates(event, event_rules)
                if not event_test:
                    await DbHelper.insert(constants.results_table, event)
                    invalid_events.append(event)

        if invalid_events:
            print('Invalid Data')
            print(invalid_events)

    @classmethod
    async def if_violates(cls, event, event_rules):
        """
        Check if event violates the event rules
        :param event: dict
        :param event_rules: list
        :return: boolean
        """
        for rule in event_rules:
            comparator = getattr(Operations, constants.rules[rule['value_type']][rule['rule']])
            result = await comparator(event, rule)
            if not result:
                return False

        return True

import sys
import asyncio
import constants

from event_processor import EventProcessor
from ruler import Ruler


# Run event processing
async def run_event_processor():
    await EventProcessor.run()


# Run ruler
async def run_ruler():
    await Ruler.run()


# Get user input for the action to perform
async def run_the_engine():
    """
    Running the rules engine
    """
    action = None
    # Check if action is valid
    while action not in constants.actions:
        action = input(constants.action_prompt)

    # call the mapped action method
    try:
        method = getattr(sys.modules[__name__], constants.actions[action])
        await method()
    except KeyError:
        print('No Way! Please define a mapped action.')

asyncio.get_event_loop().run_until_complete(run_the_engine())


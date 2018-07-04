## The Rule Engine

### Dependency
- python3.6
- pip3(pip comes with python3.6)

### Installation
- Clone the repository.
- Run `pip3 install -r requirements.txt`.

### Running
- `python3 runner.py`


### Few things

#### Conceptual Approach
Event processing was the first term that came to my mind when I read the challenge. I chose to go with python dictionaries to keep the rules and save the rules in a file using tinyDb.
I am creating rules per signal as I am assuming that a signal means a sensor. So when I receive the streaming data I will get all the rules for the signal and value_type mapping. Then I would check if all those rules are satisfied or not, which will give us the invalid data.

Trade offs:
1. Iterating over all the rules to apply on the dataset. This is not a smart system which can predict which rule to apply when.
2. Cannot apply different signal's rule on another signal.

#### Runtime Performance
18400 Records - 2 Seconds
202400 Records - 89 Seconds

**Complexity** - O(ER) where E - number of events and R - number of rules.

**Bottlenecks** - Checking every rule associated with a signal with every event.

#### Improvements
- First I would learn about the complex event processing.
- To come up with a framework for these use cases.
- To implement RETE algorithm or modify it according to the use cases.
- Develop a UI where one can easily stream events and create rules at runtime.
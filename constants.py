actions = {
    '1': 'run_event_processor',
    '2': 'run_ruler'
}
action_prompt = 'Please select the action to perform:\n1.Stream Events. \n2.Create a rule.\n'
file_prompt = 'Enter the absolute file(Only JSON) path:\n'
signal_prompt = 'Please enter the signal:\n'
value_type_prompt = 'Please select the value type:\n1.Integer\n2.String\n3.Datetime\n'
integer_prompt = 'Please select the rule:\n1.Greater than\n2.Less than\n3.Equal\n'
string_prompt = 'Please select the rule:\n1.Equality\n2.Partial Equality\n'
datetime_prompt = 'Please select the rule:\n1.Greater than\n2.Less than\n3.Equal\n'
value_prompt = 'Please enter the value: '

value_type = {
    '1': 'create_rule_for_integer',
    '2': 'create_rule_for_string',
    '3': 'create_rule_for_datetime'
}

rules = {
    'integer': {
        '1': 'greater_number_comparision',
        '2': 'lesser_number_comparision',
        '3': 'equal_number_comparision'
    },
    'string': {
        '1': 'string_equality_comparision',
        '2': 'string_partial_comparision'
    },
    'datetime': {
        '1': 'greater_datetime_comparision',
        '2': 'lesser_datetime_comparision',
        '3': 'equal_datetime_comparision'
    }
}
rules_table = 'rules'
results_table = 'results'

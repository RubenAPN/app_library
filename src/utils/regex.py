import re


def to_snake_case(name: str) -> str:
    """
    Transforms a string to a snake-case-style string in lowercase. Splits it
    in based on the uppercase letters and words. For example, the following
    transformations will be made:

    'simplestring' -> 'simplestring'
    'ThisIsSimpleCamelCaseString' -> 'this_is_simple_camel_case_string'
    'thisIsSimpleCamelCaseString' -> 'this_is_simple_camel_case_string'
    'LangChainPGCollection' -> 'lang_chain_pg_collection'
    'HTTPResponseCode' -> 'http_response_code'
    'ALongTestCaseWithMultipleCaps' -> 'a_long_test_case_with_multiple_caps'
    """

    # Replace all non-word characters (excluding underscores) with underscores
    s = re.sub(r'[\W]+', '_', name)

    # Insert underscores between lowercase and uppercase characters
    s = re.sub(r'([a-z])([A-Z])', r'\1_\2', s)

    # Insert underscores between sequences of uppercase characters followed by lowercase characters
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', s)

    # Convert to lowercase
    return s.lower()

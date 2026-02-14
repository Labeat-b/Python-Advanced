from typing import Optional, Any, List, Union
def get_name(name: Optional[str] = None) -> str:    
    if name:
        return name
    return "Anonymous"

print(get_name())


def get_value(value: Union[int, str] = 18) -> int:    
    if isinstance(value, int):
        return F"Number: {value}"
    return F"String: {value}"

print(get_value(1))

def get_any_value(value: Any) -> str:
    return value
print(get_any_value("shpati is gay"))

def get_list_of_numbers(numbers: List[int]) -> int:
    return sum(numbers)
print(get_list_of_numbers([1, 2, 3, 4, 5]))
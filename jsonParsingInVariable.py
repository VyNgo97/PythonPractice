from typing import Any, Optional
from fastapi import FastAPI

app = FastAPI()

data = [
    {
        "id": "1",
        "model": "Lenovo Thinkpad",
        "disk_space": "512GB",
        "screen_size": "13in"
    },
    {
        "id": "2",
        "model": "Legion 5",
        "disk_space": "1TB",
        "screen_size": "17in"
    },
    {
        "id": "3",
        "model": "Macbook Pro",
        "disk_space": "1TB",
        "screen_size": "15in"
    },
    {
        "id": "4",
        "model": "Surface Pro 6",
        "disk_space": "256GB",
        "screen_size": "13in"
    }
]

@app.get('/computers')
def get_data(screen_size: Optional[str]=None) -> Any:
    sorted_computers = sort_by_computer_name(data)
    if not screen_size:
        return sorted_computers
    return filter_by_screen_size(sorted_computers, screen_size)

def sort_by_computer_name(computer_list: list) -> list:
    '''Sort list by model name'''
    return sorted(computer_list, key= lambda computer: computer["model"])

'''if query param screen_size is present, only return objects where screen size matches param'''
def filter_by_screen_size(computer_list: list, screen_size: str) -> list:
    return [computer for computer in computer_list if computer["screen_size"] == screen_size]
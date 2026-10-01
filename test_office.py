from collections.abc import Callable

import pytest
from hypothesis import given
from hypothesis.strategies import integers, composite, SearchStrategy

from office import generate_random_team, Employee, fire_random_employee


@composite
def teams(draw: Callable[[SearchStrategy[int]], int], min_value:int=1, max_value:int=20):
    random_value = draw(integers(min_value, max_value))
    return generate_random_team(random_value)



@given(integers(max_value=0))
def test_negative_team_size(team_size: int):
    with pytest.raises(ValueError):
        generate_random_team(team_size)

@given(integers(min_value=1, max_value=20))
def test_team_size(team_size: int):
    assert len(generate_random_team(team_size)) == team_size


@given(integers(min_value=1, max_value=20))
def test_team_has_ceo(team_size: int):
    team = generate_random_team(team_size)
    assert Employee.CEO in team

@given(teams())
def test_fire_employee(team: list[Employee]):
    # team = generate_random_team(team_size)
    team_copy = team.copy()
    fire_random_employee(team_copy)
    assert len(team_copy) == len(team) -1



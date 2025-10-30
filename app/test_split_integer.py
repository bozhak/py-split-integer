import pytest
from app.split_integer import split_integer


class TestSplit:
    @pytest.mark.parametrize(
        "value,number_of_parts,result",
        [
            pytest.param(
                8, 1, [8],
                id="sum of the parts "
                   "should be equal to value"
            ),

            pytest.param(
                17, 1, [17],
                id="should return part equals "
                   "to value when split into one part"
            ),

            pytest.param(
                20, 6, [3, 3, 3, 3, 4, 4],
                id="test parts should be "
                   "sorted when they are not equal"
            ),
            pytest.param(
                3, 5, [0, 0, 1, 1, 1],
                id="test should add zeros when "
                   "value is less than number of parts"
            )
        ]
    )
    def test_split_correctly(
            self,
            value: int,
            number_of_parts: int,
            result: list
    ) -> None:
        assert split_integer(value, number_of_parts) == result

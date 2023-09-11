from enum import StrEnum
from typing import TypeVar

import numpy as np
import static_frame as sf
from attrs import Attribute, field, frozen, validators
from static_frame.core.index_base import IndexBase

class TestEnum(StrEnum):
    Foo="Bar"

@frozen
class AttrsFrame:
    pass

def _check_series_type(series_or_index: sf.Series | IndexBase, data_type: type | np.dtype, field_name: str = ""):
    pass

IndexType = TypeVar("IndexType", bound=IndexBase)  # pylint: disable=invalid-name

def index_field_factory(
    index_class: type[IndexType] = sf.Index, index_type: type | np.dtype | None = None
) -> IndexType:
    validator = [validators.instance_of(index_class)]
    if index_type is not None:
        def _index_type_validator(instance: AttrsFrame, attribute: Attribute, value: IndexType):
            _check_series_type(value, index_type)
        validator.append(_index_type_validator)
    return field(validator=validator)

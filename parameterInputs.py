import datetime
from typing import Dict, List, Optional, Set, 
from enum import Enum

from prefect import flow
from pydantic import BaseModel, Field, Json

class FruitEnum(str, Enum):
    pear = 'pear'
    banana = 'banana'

class PydanticFieldsDefault(BaseModel): 

    bool_field_default: Optional[bool] = Field(
        title="Title bool_field_default", description="Description bool_field_default", default=True
    )
    int_field_default: Optional[int] = Field(
        title="Title int_field_default", description="Description int_field_default", default=42
    )
    float_field_default: Optional[float] = Field(
        title="Title float_field_default", description="Description float_field_default", default=1.23
    )
    str_field_default: Optional[str] = Field(
        title="Title str_field_default", description="Description str_field_default", default="default"
    )
    list_field_default: Optional[List[str]] = Field(
        title="Title list_field_default",
        description="Description list_field_default",
        default=["default", "default", "default"],
    )
    #tuples not currently supported in non json input
    # tuple_field_default: Optional[Tuple[str, str]] = Field(
    #     title="Title tuple_field_default",
    #     description="Description tuple_field_default",
    #     default=("default", "default"),
    # )
    dict_field_default: Optional[Dict[str, str]] = Field(
        title="Title dict_field_default", description="Description dict_field_default", default={"name": "default"}
    )
    set_field_default: Optional[Set[str]] = Field(
        title="Title set_field_default",
        description="Description set_field_default",
        default=("default_0", "default_1"),
    )
    date_field_default: Optional[datetime.date] = Field(
        title="Title date_field_default",
        description="Description date_field_default",
        default=datetime.date(2022, 1, 1),
    )
    time_field_default: Optional[datetime.time] = Field(
        title="Title time_field_default", description="Description time_field_default", default=datetime.time(12, 12)
    )
    datetime_field_default: Optional[datetime.datetime] = Field(
        title="Title datetime_field_default",
        description="Description datetime_field_default",
        default=datetime.datetime(2022, 1, 1, 12, 12),
    )
    #uuid objects are immutable
    # uuid_field_default: Optional[UUID4] = Field(
    #     title="Title uuid_field_default",
    #     description="Description uuid_field_default",
    #     default=UUID4("aa763817-0ba2-4771-bfc7-1550d1646874"),
    # )
    json_field_default: Optional[Json] = Field(
        title="Title json_field_default",
        description="Description json_field_default",
        default='{"name":"John", "age":30, "car":null}',
    )
    enum_field_default: Optional[FruitEnum] = Field(
        title="Title enum_field_default",
        description="Description enum_field_default",
        default=FruitEnum.pear,
    )

@flow(log_prints=True)
def parameterDisplays(
    pydantic_fields_default_defaults: PydanticFieldsDefault = PydanticFieldsDefault(),
) -> None:
    '''Flow to test display of Pydantic fields with default values
    
#Flow code

```python
import datetime
from typing import Dict, List, Optional, Set, Tuple

from prefect import flow, get_run_logger
from pydantic import UUID4, BaseModel, Field, Json


class PydanticFieldsDefault(BaseModel): 

    bool_field_default: Optional[bool] = Field(
        title="Title bool_field_default", description="Description bool_field_default", default=True
    )
    int_field_default: Optional[int] = Field(
        title="Title int_field_default", description="Description int_field_default", default=42
    )
    float_field_default: Optional[float] = Field(
        title="Title float_field_default", description="Description float_field_default", default=1.23
    )
    str_field_default: Optional[str] = Field(
        title="Title str_field_default", description="Description str_field_default", default="default"
    )
    list_field_default: Optional[List[str]] = Field(
        title="Title list_field_default",
        description="Description list_field_default",
        default=["default", "default", "default"],
    )
    #tuple inputs currently not supported - can be done via json
    # tuple_field_default: Optional[Tuple[str, str]] = Field(
    #     title="Title tuple_field_default",
    #     description="Description tuple_field_default",
    #     default=("default", "default"),
    # )
    dict_field_default: Optional[Dict[str, str]] = Field(
        title="Title dict_field_default", description="Description dict_field_default", default={"name": "default"}
    )
    set_field_default: Optional[Set[str]] = Field(
        title="Title set_field_default",
        description="Description set_field_default",
        default=("default_0", "default_1"),
    )
    date_field_default: Optional[datetime.date] = Field(
        title="Title date_field_default",
        description="Description date_field_default",
        default=datetime.date(2022, 1, 1),
    )
    time_field_default: Optional[datetime.time] = Field(
        title="Title time_field_default", description="Description time_field_default", default=datetime.time(12, 12)
    )
    datetime_field_default: Optional[datetime.datetime] = Field(
        title="Title datetime_field_default",
        description="Description datetime_field_default",
        default=datetime.datetime(2022, 1, 1, 12, 12),
    )
    #UUID objects are immutable
    # uuid_field_default: Optional[UUID4] = Field(
    #     title="Title uuid_field_default",
    #     description="Description uuid_field_default",
    #     default=UUID4("aa763817-0ba2-4771-bfc7-1550d1646874"),
    # )
    json_field_default: Optional[Json] = Field(
        title="Title json_field_default",
        description="Description json_field_default",
        default='{"name":"John", "age":30, "car":null}',
    )
    enum_field_default: Optional[FruitEnum] = Field(
        title="Title enum_field_default",
        description="Description enum_field_default",
        default=FruitEnum.pear,
    )


@flow(name="Pydantic Fields Default")
def mainPydantic(
    pydantic_fields_default_defaults: PydanticFieldsDefault = PydanticFieldsDefault(),
) -> None:
    logger = get_run_logger()
    logger.info(f"{pydantic_fields_default_defaults=}")

```
    '''
    
    print(f"{pydantic_fields_default_defaults=}")


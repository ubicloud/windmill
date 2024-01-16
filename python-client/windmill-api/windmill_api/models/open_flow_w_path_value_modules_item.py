from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast
from typing import Dict
from typing import cast, Union
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.open_flow_w_path_value_modules_item_sleep_type_1 import OpenFlowWPathValueModulesItemSleepType1
  from ..models.open_flow_w_path_value_modules_item_mock import OpenFlowWPathValueModulesItemMock
  from ..models.open_flow_w_path_value_modules_item_stop_after_if import OpenFlowWPathValueModulesItemStopAfterIf
  from ..models.open_flow_w_path_value_modules_item_suspend import OpenFlowWPathValueModulesItemSuspend
  from ..models.open_flow_w_path_value_modules_item_sleep_type_0 import OpenFlowWPathValueModulesItemSleepType0
  from ..models.open_flow_w_path_value_modules_item_retry import OpenFlowWPathValueModulesItemRetry





T = TypeVar("T", bound="OpenFlowWPathValueModulesItem")


@_attrs_define
class OpenFlowWPathValueModulesItem:
    """ 
        Attributes:
            id (str):
            value (Any):
            stop_after_if (Union[Unset, OpenFlowWPathValueModulesItemStopAfterIf]):
            sleep (Union['OpenFlowWPathValueModulesItemSleepType0', 'OpenFlowWPathValueModulesItemSleepType1', Unset]):
            cache_ttl (Union[Unset, float]):
            timeout (Union[Unset, float]):
            delete_after_use (Union[Unset, bool]):
            summary (Union[Unset, str]):
            mock (Union[Unset, OpenFlowWPathValueModulesItemMock]):
            suspend (Union[Unset, OpenFlowWPathValueModulesItemSuspend]):
            priority (Union[Unset, float]):
            retry (Union[Unset, OpenFlowWPathValueModulesItemRetry]):
     """

    id: str
    value: Any
    stop_after_if: Union[Unset, 'OpenFlowWPathValueModulesItemStopAfterIf'] = UNSET
    sleep: Union['OpenFlowWPathValueModulesItemSleepType0', 'OpenFlowWPathValueModulesItemSleepType1', Unset] = UNSET
    cache_ttl: Union[Unset, float] = UNSET
    timeout: Union[Unset, float] = UNSET
    delete_after_use: Union[Unset, bool] = UNSET
    summary: Union[Unset, str] = UNSET
    mock: Union[Unset, 'OpenFlowWPathValueModulesItemMock'] = UNSET
    suspend: Union[Unset, 'OpenFlowWPathValueModulesItemSuspend'] = UNSET
    priority: Union[Unset, float] = UNSET
    retry: Union[Unset, 'OpenFlowWPathValueModulesItemRetry'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.open_flow_w_path_value_modules_item_sleep_type_1 import OpenFlowWPathValueModulesItemSleepType1
        from ..models.open_flow_w_path_value_modules_item_mock import OpenFlowWPathValueModulesItemMock
        from ..models.open_flow_w_path_value_modules_item_stop_after_if import OpenFlowWPathValueModulesItemStopAfterIf
        from ..models.open_flow_w_path_value_modules_item_suspend import OpenFlowWPathValueModulesItemSuspend
        from ..models.open_flow_w_path_value_modules_item_sleep_type_0 import OpenFlowWPathValueModulesItemSleepType0
        from ..models.open_flow_w_path_value_modules_item_retry import OpenFlowWPathValueModulesItemRetry
        id = self.id
        value = self.value
        stop_after_if: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stop_after_if, Unset):
            stop_after_if = self.stop_after_if.to_dict()

        sleep: Union[Dict[str, Any], Unset]
        if isinstance(self.sleep, Unset):
            sleep = UNSET

        elif isinstance(self.sleep, OpenFlowWPathValueModulesItemSleepType0):
            sleep = UNSET
            if not isinstance(self.sleep, Unset):
                sleep = self.sleep.to_dict()

        else:
            sleep = UNSET
            if not isinstance(self.sleep, Unset):
                sleep = self.sleep.to_dict()



        cache_ttl = self.cache_ttl
        timeout = self.timeout
        delete_after_use = self.delete_after_use
        summary = self.summary
        mock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mock, Unset):
            mock = self.mock.to_dict()

        suspend: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.suspend, Unset):
            suspend = self.suspend.to_dict()

        priority = self.priority
        retry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retry, Unset):
            retry = self.retry.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "value": value,
        })
        if stop_after_if is not UNSET:
            field_dict["stop_after_if"] = stop_after_if
        if sleep is not UNSET:
            field_dict["sleep"] = sleep
        if cache_ttl is not UNSET:
            field_dict["cache_ttl"] = cache_ttl
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if delete_after_use is not UNSET:
            field_dict["delete_after_use"] = delete_after_use
        if summary is not UNSET:
            field_dict["summary"] = summary
        if mock is not UNSET:
            field_dict["mock"] = mock
        if suspend is not UNSET:
            field_dict["suspend"] = suspend
        if priority is not UNSET:
            field_dict["priority"] = priority
        if retry is not UNSET:
            field_dict["retry"] = retry

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_flow_w_path_value_modules_item_sleep_type_1 import OpenFlowWPathValueModulesItemSleepType1
        from ..models.open_flow_w_path_value_modules_item_mock import OpenFlowWPathValueModulesItemMock
        from ..models.open_flow_w_path_value_modules_item_stop_after_if import OpenFlowWPathValueModulesItemStopAfterIf
        from ..models.open_flow_w_path_value_modules_item_suspend import OpenFlowWPathValueModulesItemSuspend
        from ..models.open_flow_w_path_value_modules_item_sleep_type_0 import OpenFlowWPathValueModulesItemSleepType0
        from ..models.open_flow_w_path_value_modules_item_retry import OpenFlowWPathValueModulesItemRetry
        d = src_dict.copy()
        id = d.pop("id")

        value = d.pop("value")

        _stop_after_if = d.pop("stop_after_if", UNSET)
        stop_after_if: Union[Unset, OpenFlowWPathValueModulesItemStopAfterIf]
        if isinstance(_stop_after_if,  Unset):
            stop_after_if = UNSET
        else:
            stop_after_if = OpenFlowWPathValueModulesItemStopAfterIf.from_dict(_stop_after_if)




        def _parse_sleep(data: object) -> Union['OpenFlowWPathValueModulesItemSleepType0', 'OpenFlowWPathValueModulesItemSleepType1', Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _sleep_type_0 = data
                sleep_type_0: Union[Unset, OpenFlowWPathValueModulesItemSleepType0]
                if isinstance(_sleep_type_0,  Unset):
                    sleep_type_0 = UNSET
                else:
                    sleep_type_0 = OpenFlowWPathValueModulesItemSleepType0.from_dict(_sleep_type_0)



                return sleep_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _sleep_type_1 = data
            sleep_type_1: Union[Unset, OpenFlowWPathValueModulesItemSleepType1]
            if isinstance(_sleep_type_1,  Unset):
                sleep_type_1 = UNSET
            else:
                sleep_type_1 = OpenFlowWPathValueModulesItemSleepType1.from_dict(_sleep_type_1)



            return sleep_type_1

        sleep = _parse_sleep(d.pop("sleep", UNSET))


        cache_ttl = d.pop("cache_ttl", UNSET)

        timeout = d.pop("timeout", UNSET)

        delete_after_use = d.pop("delete_after_use", UNSET)

        summary = d.pop("summary", UNSET)

        _mock = d.pop("mock", UNSET)
        mock: Union[Unset, OpenFlowWPathValueModulesItemMock]
        if isinstance(_mock,  Unset):
            mock = UNSET
        else:
            mock = OpenFlowWPathValueModulesItemMock.from_dict(_mock)




        _suspend = d.pop("suspend", UNSET)
        suspend: Union[Unset, OpenFlowWPathValueModulesItemSuspend]
        if isinstance(_suspend,  Unset):
            suspend = UNSET
        else:
            suspend = OpenFlowWPathValueModulesItemSuspend.from_dict(_suspend)




        priority = d.pop("priority", UNSET)

        _retry = d.pop("retry", UNSET)
        retry: Union[Unset, OpenFlowWPathValueModulesItemRetry]
        if isinstance(_retry,  Unset):
            retry = UNSET
        else:
            retry = OpenFlowWPathValueModulesItemRetry.from_dict(_retry)




        open_flow_w_path_value_modules_item = cls(
            id=id,
            value=value,
            stop_after_if=stop_after_if,
            sleep=sleep,
            cache_ttl=cache_ttl,
            timeout=timeout,
            delete_after_use=delete_after_use,
            summary=summary,
            mock=mock,
            suspend=suspend,
            priority=priority,
            retry=retry,
        )

        open_flow_w_path_value_modules_item.additional_properties = d
        return open_flow_w_path_value_modules_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
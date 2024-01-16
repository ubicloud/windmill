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
  from ..models.queued_job_raw_flow_failure_module_suspend_user_groups_required_type_0 import QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType0
  from ..models.queued_job_raw_flow_failure_module_suspend_user_groups_required_type_1 import QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType1
  from ..models.queued_job_raw_flow_failure_module_suspend_resume_form import QueuedJobRawFlowFailureModuleSuspendResumeForm





T = TypeVar("T", bound="QueuedJobRawFlowFailureModuleSuspend")


@_attrs_define
class QueuedJobRawFlowFailureModuleSuspend:
    """ 
        Attributes:
            required_events (Union[Unset, int]):
            timeout (Union[Unset, int]):
            resume_form (Union[Unset, QueuedJobRawFlowFailureModuleSuspendResumeForm]):
            user_auth_required (Union[Unset, bool]):
            user_groups_required (Union['QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType0',
                'QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType1', Unset]):
     """

    required_events: Union[Unset, int] = UNSET
    timeout: Union[Unset, int] = UNSET
    resume_form: Union[Unset, 'QueuedJobRawFlowFailureModuleSuspendResumeForm'] = UNSET
    user_auth_required: Union[Unset, bool] = UNSET
    user_groups_required: Union['QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType0', 'QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType1', Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.queued_job_raw_flow_failure_module_suspend_user_groups_required_type_0 import QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType0
        from ..models.queued_job_raw_flow_failure_module_suspend_user_groups_required_type_1 import QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType1
        from ..models.queued_job_raw_flow_failure_module_suspend_resume_form import QueuedJobRawFlowFailureModuleSuspendResumeForm
        required_events = self.required_events
        timeout = self.timeout
        resume_form: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resume_form, Unset):
            resume_form = self.resume_form.to_dict()

        user_auth_required = self.user_auth_required
        user_groups_required: Union[Dict[str, Any], Unset]
        if isinstance(self.user_groups_required, Unset):
            user_groups_required = UNSET

        elif isinstance(self.user_groups_required, QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType0):
            user_groups_required = UNSET
            if not isinstance(self.user_groups_required, Unset):
                user_groups_required = self.user_groups_required.to_dict()

        else:
            user_groups_required = UNSET
            if not isinstance(self.user_groups_required, Unset):
                user_groups_required = self.user_groups_required.to_dict()




        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if required_events is not UNSET:
            field_dict["required_events"] = required_events
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if resume_form is not UNSET:
            field_dict["resume_form"] = resume_form
        if user_auth_required is not UNSET:
            field_dict["user_auth_required"] = user_auth_required
        if user_groups_required is not UNSET:
            field_dict["user_groups_required"] = user_groups_required

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.queued_job_raw_flow_failure_module_suspend_user_groups_required_type_0 import QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType0
        from ..models.queued_job_raw_flow_failure_module_suspend_user_groups_required_type_1 import QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType1
        from ..models.queued_job_raw_flow_failure_module_suspend_resume_form import QueuedJobRawFlowFailureModuleSuspendResumeForm
        d = src_dict.copy()
        required_events = d.pop("required_events", UNSET)

        timeout = d.pop("timeout", UNSET)

        _resume_form = d.pop("resume_form", UNSET)
        resume_form: Union[Unset, QueuedJobRawFlowFailureModuleSuspendResumeForm]
        if isinstance(_resume_form,  Unset):
            resume_form = UNSET
        else:
            resume_form = QueuedJobRawFlowFailureModuleSuspendResumeForm.from_dict(_resume_form)




        user_auth_required = d.pop("user_auth_required", UNSET)

        def _parse_user_groups_required(data: object) -> Union['QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType0', 'QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType1', Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _user_groups_required_type_0 = data
                user_groups_required_type_0: Union[Unset, QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType0]
                if isinstance(_user_groups_required_type_0,  Unset):
                    user_groups_required_type_0 = UNSET
                else:
                    user_groups_required_type_0 = QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType0.from_dict(_user_groups_required_type_0)



                return user_groups_required_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _user_groups_required_type_1 = data
            user_groups_required_type_1: Union[Unset, QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType1]
            if isinstance(_user_groups_required_type_1,  Unset):
                user_groups_required_type_1 = UNSET
            else:
                user_groups_required_type_1 = QueuedJobRawFlowFailureModuleSuspendUserGroupsRequiredType1.from_dict(_user_groups_required_type_1)



            return user_groups_required_type_1

        user_groups_required = _parse_user_groups_required(d.pop("user_groups_required", UNSET))


        queued_job_raw_flow_failure_module_suspend = cls(
            required_events=required_events,
            timeout=timeout,
            resume_form=resume_form,
            user_auth_required=user_auth_required,
            user_groups_required=user_groups_required,
        )

        queued_job_raw_flow_failure_module_suspend.additional_properties = d
        return queued_job_raw_flow_failure_module_suspend

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
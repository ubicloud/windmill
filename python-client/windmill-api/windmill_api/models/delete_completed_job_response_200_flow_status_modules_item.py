from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast
from typing import cast, List
from ..models.delete_completed_job_response_200_flow_status_modules_item_type import DeleteCompletedJobResponse200FlowStatusModulesItemType
from typing import Dict
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.delete_completed_job_response_200_flow_status_modules_item_branch_chosen import DeleteCompletedJobResponse200FlowStatusModulesItemBranchChosen
  from ..models.delete_completed_job_response_200_flow_status_modules_item_iterator import DeleteCompletedJobResponse200FlowStatusModulesItemIterator
  from ..models.delete_completed_job_response_200_flow_status_modules_item_branchall import DeleteCompletedJobResponse200FlowStatusModulesItemBranchall
  from ..models.delete_completed_job_response_200_flow_status_modules_item_approvers_item import DeleteCompletedJobResponse200FlowStatusModulesItemApproversItem





T = TypeVar("T", bound="DeleteCompletedJobResponse200FlowStatusModulesItem")


@_attrs_define
class DeleteCompletedJobResponse200FlowStatusModulesItem:
    """ 
        Attributes:
            type (DeleteCompletedJobResponse200FlowStatusModulesItemType):
            id (Union[Unset, str]):
            job (Union[Unset, str]):
            count (Union[Unset, int]):
            iterator (Union[Unset, DeleteCompletedJobResponse200FlowStatusModulesItemIterator]):
            flow_jobs (Union[Unset, List[str]]):
            branch_chosen (Union[Unset, DeleteCompletedJobResponse200FlowStatusModulesItemBranchChosen]):
            branchall (Union[Unset, DeleteCompletedJobResponse200FlowStatusModulesItemBranchall]):
            approvers (Union[Unset, List['DeleteCompletedJobResponse200FlowStatusModulesItemApproversItem']]):
     """

    type: DeleteCompletedJobResponse200FlowStatusModulesItemType
    id: Union[Unset, str] = UNSET
    job: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    iterator: Union[Unset, 'DeleteCompletedJobResponse200FlowStatusModulesItemIterator'] = UNSET
    flow_jobs: Union[Unset, List[str]] = UNSET
    branch_chosen: Union[Unset, 'DeleteCompletedJobResponse200FlowStatusModulesItemBranchChosen'] = UNSET
    branchall: Union[Unset, 'DeleteCompletedJobResponse200FlowStatusModulesItemBranchall'] = UNSET
    approvers: Union[Unset, List['DeleteCompletedJobResponse200FlowStatusModulesItemApproversItem']] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.delete_completed_job_response_200_flow_status_modules_item_branch_chosen import DeleteCompletedJobResponse200FlowStatusModulesItemBranchChosen
        from ..models.delete_completed_job_response_200_flow_status_modules_item_iterator import DeleteCompletedJobResponse200FlowStatusModulesItemIterator
        from ..models.delete_completed_job_response_200_flow_status_modules_item_branchall import DeleteCompletedJobResponse200FlowStatusModulesItemBranchall
        from ..models.delete_completed_job_response_200_flow_status_modules_item_approvers_item import DeleteCompletedJobResponse200FlowStatusModulesItemApproversItem
        type = self.type.value

        id = self.id
        job = self.job
        count = self.count
        iterator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.iterator, Unset):
            iterator = self.iterator.to_dict()

        flow_jobs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.flow_jobs, Unset):
            flow_jobs = self.flow_jobs




        branch_chosen: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branch_chosen, Unset):
            branch_chosen = self.branch_chosen.to_dict()

        branchall: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branchall, Unset):
            branchall = self.branchall.to_dict()

        approvers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.approvers, Unset):
            approvers = []
            for approvers_item_data in self.approvers:
                approvers_item = approvers_item_data.to_dict()

                approvers.append(approvers_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if job is not UNSET:
            field_dict["job"] = job
        if count is not UNSET:
            field_dict["count"] = count
        if iterator is not UNSET:
            field_dict["iterator"] = iterator
        if flow_jobs is not UNSET:
            field_dict["flow_jobs"] = flow_jobs
        if branch_chosen is not UNSET:
            field_dict["branch_chosen"] = branch_chosen
        if branchall is not UNSET:
            field_dict["branchall"] = branchall
        if approvers is not UNSET:
            field_dict["approvers"] = approvers

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delete_completed_job_response_200_flow_status_modules_item_branch_chosen import DeleteCompletedJobResponse200FlowStatusModulesItemBranchChosen
        from ..models.delete_completed_job_response_200_flow_status_modules_item_iterator import DeleteCompletedJobResponse200FlowStatusModulesItemIterator
        from ..models.delete_completed_job_response_200_flow_status_modules_item_branchall import DeleteCompletedJobResponse200FlowStatusModulesItemBranchall
        from ..models.delete_completed_job_response_200_flow_status_modules_item_approvers_item import DeleteCompletedJobResponse200FlowStatusModulesItemApproversItem
        d = src_dict.copy()
        type = DeleteCompletedJobResponse200FlowStatusModulesItemType(d.pop("type"))




        id = d.pop("id", UNSET)

        job = d.pop("job", UNSET)

        count = d.pop("count", UNSET)

        _iterator = d.pop("iterator", UNSET)
        iterator: Union[Unset, DeleteCompletedJobResponse200FlowStatusModulesItemIterator]
        if isinstance(_iterator,  Unset):
            iterator = UNSET
        else:
            iterator = DeleteCompletedJobResponse200FlowStatusModulesItemIterator.from_dict(_iterator)




        flow_jobs = cast(List[str], d.pop("flow_jobs", UNSET))


        _branch_chosen = d.pop("branch_chosen", UNSET)
        branch_chosen: Union[Unset, DeleteCompletedJobResponse200FlowStatusModulesItemBranchChosen]
        if isinstance(_branch_chosen,  Unset):
            branch_chosen = UNSET
        else:
            branch_chosen = DeleteCompletedJobResponse200FlowStatusModulesItemBranchChosen.from_dict(_branch_chosen)




        _branchall = d.pop("branchall", UNSET)
        branchall: Union[Unset, DeleteCompletedJobResponse200FlowStatusModulesItemBranchall]
        if isinstance(_branchall,  Unset):
            branchall = UNSET
        else:
            branchall = DeleteCompletedJobResponse200FlowStatusModulesItemBranchall.from_dict(_branchall)




        approvers = []
        _approvers = d.pop("approvers", UNSET)
        for approvers_item_data in (_approvers or []):
            approvers_item = DeleteCompletedJobResponse200FlowStatusModulesItemApproversItem.from_dict(approvers_item_data)



            approvers.append(approvers_item)


        delete_completed_job_response_200_flow_status_modules_item = cls(
            type=type,
            id=id,
            job=job,
            count=count,
            iterator=iterator,
            flow_jobs=flow_jobs,
            branch_chosen=branch_chosen,
            branchall=branchall,
            approvers=approvers,
        )

        delete_completed_job_response_200_flow_status_modules_item.additional_properties = d
        return delete_completed_job_response_200_flow_status_modules_item

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
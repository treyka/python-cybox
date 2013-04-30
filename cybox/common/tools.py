import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common.hash import HashList
from cybox.common.structured_text import StructuredText
from cybox.common.vocabs import VocabString


class ToolType(VocabString):
    _XSI_TYPE = 'cyboxVocabs:ToolTypeVocab-1.0'


class ToolInformation(cybox.Entity):

    def __init__(self):
        # TODO: Implement items commented out below.
        self.id_ = None
        self.idref = None
        self.name = None
        self.type_ = []
        self.description = None
        #self.references = None
        self.vendor = None
        self.version = None
        self.service_pack = None
        #self.tool_specific_data = None
        self.tool_hashes = None
        #self.tool_configuration = None
        #self.execution_environment = None
        #self.errors = None
        #self.metadata = []

    @property
    def tool_hashes(self):
        if self._tool_hashes is None:
            self._tool_hashes = HashList()
        return self._tool_hashes

    @tool_hashes.setter
    def tool_hashes(self, value):
        self._tool_hashes = value

    def to_obj(self):
        toolinfo_obj = common_binding.ToolInformationType()

        if self.id_ is not None:
            toolinfo_obj.set_id(self.id_)
        if self.idref is not None:
            toolinfo_obj.set_idref(self.idref)
        if self.name is not None:
            toolinfo_obj.set_Name(self.name)
        if self.type_:
            toolinfo_obj.set_Type([x.to_obj() for x in self.type_])
        if self.description is not None:
            toolinfo_obj.set_Description(self.description.to_obj())

        if self.vendor is not None:
            toolinfo_obj.set_Vendor(self.vendor)
        if self.version is not None:
            toolinfo_obj.set_Version(self.version)
        if self.service_pack is not None:
            toolinfo_obj.set_Service_Pack(self.service_pack)

        if self.tool_hashes:
            toolinfo_obj.set_Tool_Hashes(self.tool_hashes.to_obj())

        return toolinfo_obj

    def to_dict(self):
        toolinfo_dict = {}

        if self.id_ is not None:
            toolinfo_dict['id'] = self.id_
        if self.idref is not None:
            toolinfo_dict['idref'] = self.idref
        if self.name is not None:
            toolinfo_dict['name'] = self.name
        if self.type_:
            toolinfo_dict['type'] = [x.to_dict() for x in self.type_]
        if self.description is not None:
            toolinfo_dict['description'] = self.description.to_dict()

        if self.vendor is not None:
            toolinfo_dict['vendor'] = self.vendor
        if self.version is not None:
            toolinfo_dict['version'] = self.version
        if self.service_pack is not None:
            toolinfo_dict['service_pack'] = self.service_pack

        if self.tool_hashes:
            toolinfo_dict['tool_hashes'] = self.tool_hashes.to_list()

        return toolinfo_dict

    @staticmethod
    def from_obj(toolinfo_obj):
        if not toolinfo_obj:
            return None

        toolinfo = ToolInformation()

        toolinfo.id_ = toolinfo_obj.get_id()
        toolinfo.idref = toolinfo_obj.get_idref()
        toolinfo.name = toolinfo_obj.get_Name()
        toolinfo.type_ = [ToolType.from_obj(x) for x in toolinfo_obj.get_Type()]
        toolinfo.description = StructuredText.from_obj(toolinfo_obj.get_Description())

        toolinfo.vendor = toolinfo_obj.get_Vendor()
        toolinfo.version = toolinfo_obj.get_Version()
        toolinfo.service_pack = toolinfo_obj.get_Service_Pack()

        toolinfo.tool_hashes = HashList.from_obj(toolinfo_obj.get_Tool_Hashes())

        return toolinfo

    @staticmethod
    def from_dict(toolinfo_dict):
        if not toolinfo_dict:
            return None

        toolinfo = ToolInformation()

        toolinfo.id_ = toolinfo_dict.get('id')
        toolinfo.idref = toolinfo_dict.get('idref')
        toolinfo.name = toolinfo_dict.get('name')
        toolinfo.type_ = [ToolType.from_dict(x) for x in toolinfo_dict.get('type')]
        toolinfo.description = StructuredText.from_dict(toolinfo_dict.get('description'))

        toolinfo.vendor = toolinfo_dict.get('vendor')
        toolinfo.version = toolinfo_dict.get('version')
        toolinfo.service_pack = toolinfo_dict.get('service_pack')

        toolinfo.tool_hashes = HashList.from_list(toolinfo_dict.get('tool_hashes'))

        return toolinfo


class ToolInformationList(object):
    def __init__(self):
        self.tool_list = []

    def to_obj(self):
        tools_information_obj = common_binding.ToolsInformationType()
        for tool in self.tool_list:
            tools_information_obj.add_Tool(tool.to_obj())
        return tools_information_obj

    def to_dict(self):
        pass

    @staticmethod
    def from_list(tools_list):
        if not tools_list:
            return None
        tools_list_ = ToolInformationList()
        tools_list_.tool_list = [ToolInformation.from_dict(x) for x in tools_list]
        return tools_list_

    @staticmethod
    def from_obj(tools_obj):
        pass
from .base import BaseTool
from .get_issue import GetIssueTool
from .add_comment import AddCommentTool
from .add_comment_with_attachment import AddCommentWithAttachmentTool

_TOOLS = {
    'get_issue': GetIssueTool(),
    'add_comment': AddCommentTool(),
    'add_comment_with_attachment': AddCommentWithAttachmentTool(),
}

def get_all_tools():
    return [tool.get_tool_definition() for tool in _TOOLS.values()]

def get_tool(name: str) -> BaseTool:
    if name not in _TOOLS:
        raise ValueError(f"Unknown tool: {name}")
    return _TOOLS[name]
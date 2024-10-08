"""
Module: workspace_refactorer

This module provides the WorkspaceRefactorer class which is responsible for refactoring workspaces 
based on the project type. It delegates the actual refactoring logic to specific ProjectRefactorer 
classes, tailored to the unique requirements of each project type like Python, Java, or NodeJS.
"""

from autobyteus_server.workspaces.setting.project_types import ProjectType
from autobyteus_server.workspaces.workspace import Workspace
from autobyteus_server.workspaces.workspace_tools.base_workspace_tool import BaseWorkspaceTool
from autobyteus_server.workspaces.workspace_tools.workspace_refactorer.java_project_refactorer import JavaProjectRefactorer
from autobyteus_server.workspaces.workspace_tools.workspace_refactorer.nodejs_project_refactorer import NodeJSProjectRefactorer
from autobyteus_server.workspaces.workspace_tools.workspace_refactorer.python_project_refactorer import PythonProjectRefactorer


class WorkspaceRefactorer(BaseWorkspaceTool):
    """
    WorkspaceRefactorer is responsible for determining the appropriate project refactorer
    based on the workspace's project type.
    """
    
    # Mapping of project types to their respective refactorer classes
    REFACTORER_MAP = {
        ProjectType.PYTHON: PythonProjectRefactorer,
        ProjectType.JAVA: JavaProjectRefactorer,
        ProjectType.NODEJS: NodeJSProjectRefactorer
    }

    def __init__(self, workspace: Workspace):
        """
        Constructor for WorkspaceRefactorer.

        Args:
            workspace (Workspace): The workspace to be refactored.
        """
        super().__init__(workspace)

        # Find the appropriate refactorer class for the project type
        refactorer_class = self.REFACTORER_MAP.get(workspace.project_type)

        if not refactorer_class:
            raise ValueError(f"Invalid project type: {workspace.project_type}")

        self.project_refactorer = refactorer_class(workspace)
        
    @property
    def prompt_template(self) -> str:
        """
        Fetch the prompt template from the specific project refactorer.

        Returns:
            str: The prompt template for the specific project type.
        """
        return self.project_refactorer.prompt_template

    def execute(self):
        """
        Execute the refactoring process on the workspace.
        """
        self.project_refactorer.refactor()
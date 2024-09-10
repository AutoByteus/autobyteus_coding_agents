"""
config.py
The WORKFLOW_CONFIG dictionary defines the structure of the workflow, including steps and substeps.
Each step is defined as a key-value pair, where the key is the step name and the value is a dictionary containing:
    - 'step_class': The class representing the step.
    - 'steps': A dictionary of substeps, if any, following the same structure.

For example, the 'requirement_step' has a 'refine' substep with its own class.
"""

from autobyteus_server.workflow.steps.requirement_refine_step import RequirementRefineStep
from autobyteus_server.workflow.steps.requirement_step import RequirementStep
from autobyteus_server.workflow.steps.tests_generation_step import TestsGenerationStep
from autobyteus_server.workflow.steps.subtask_implementation_step import SubtaskImplementationStep
from autobyteus_server.workflow.steps.run_tests_step import RunTestsStep
from autobyteus_server.workflow.types.workflow_template_config import WorkflowTemplateStepsConfig

WORKFLOW_CONFIG: WorkflowTemplateStepsConfig = {
    'steps': {
        'requirement_step': {
            'step_class': RequirementStep,
            'steps': {
                'refine': {
                    'step_class': RequirementRefineStep
                }
            },
        },
        'test_generation_step': {
            'step_class': TestsGenerationStep,
        },
        'implementation_step': {
            'step_class': SubtaskImplementationStep,
        },
        'testing_step': {
            'step_class': RunTestsStep,
        },
    }
}

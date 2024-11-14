from behave import given, when, then
from services.powerbi_service import PowerBIService

@given('I have a connection to Power BI')
def step_impl(context):
    context.powerbi_service = PowerBIService()

@when('I retrieve the current model schema')
def step_impl(context):
    context.schema = context.powerbi_service.get_model_schema()

@then('it should match the expected schema structure')
def step_impl(context):
    assert "tables" in context.schema
    assert len(context.schema["tables"]) > 0 
from .get_files_info import *
from .get_file_content import *
from .write_file import *
from .run_python_file import *
from google.genai import types

def call_function(function_call_part=None, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    results = None
    function_call_part.args['working_directory'] = './calculator'
    match function_call_part.name:
        case 'get_files_info':
            results = get_files_info(**function_call_part.args)
        case 'get_file_content':
            results = get_file_content(**function_call_part.args)
        case 'write_file':
            results = write_file(**function_call_part.args)
        case 'run_python_file':
            results = run_python_file(**function_call_part.args)
        case _: 
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"Unknown function: {function_call_part.name}"},
                    )
                ],
            )

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": results},
            )
        ],
    )

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)
        
import os
import subprocess
import config
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_working_dir_path = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_file_path.startswith(abs_working_dir_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
    
        result = subprocess.run(
            ['python', abs_file_path , *args],
            timeout=config.EXECUTION_TIMEOUT,
            capture_output=True,
            cwd=abs_working_dir_path,
            text=True
        )

        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f'Error: executing Python file: {e}'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file given a file path and an arguments array, arguments are optional , constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to Python file to be executed, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items={"type": types.Type.STRING},
                description="The arguments to be passed into the Python file.",
            ),
        },
    ),
)
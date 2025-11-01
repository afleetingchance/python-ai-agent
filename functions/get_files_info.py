import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        abs_working_dir_path = os.path.abspath(working_directory)
        abs_dir_path = os.path.abspath(os.path.join(working_directory, directory))

        if not abs_dir_path.startswith(abs_working_dir_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(abs_dir_path):
            return f'Error: "{directory}" is not a directory'
        
        results = ''
        for content_name in os.listdir(abs_dir_path):
            filepath = os.path.join(abs_dir_path, content_name)
            results += f' - {content_name}: file_size={os.path.getsize(filepath)} bytes, is_dir={os.path.isdir(filepath)}\n'

        return results
    except Exception as e:
        return f'Error: {e}'
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
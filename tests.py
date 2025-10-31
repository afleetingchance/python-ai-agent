from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


def main():
    file_info_tests = [
        {
            'inputs': {
                'working_directory': 'calculator',
                'directory': '.'
            }
        },
        {
            'inputs': {
                'working_directory': 'calculator',
                'directory': 'pkg'
            }
        },
        {
            'inputs': {
                'working_directory': 'calculator',
                'directory': '/bin'
            }
        },
        {
            'inputs': {
                'working_directory': 'calculator',
                'directory': '../'
            }
        }
    ]

    file_content_tests = [
        {
            'inputs': {
                'working_directory': 'calculator',
                'file_path': 'main.py'
            }
        },
        {
            'inputs': {
                'working_directory': 'calculator',
                'file_path': 'pkg/calculator.py'
            }
        },
        {
            'inputs': {
                'working_directory': 'calculator',
                'file_path': '/bin/cat'
            }
        },
        {
            'inputs': {
                'working_directory': 'calculator',
                'file_path': 'pkg/does_not_exist.py'
            }
        }
    ]

    file_write_tests = [
        {
            'inputs': {
                'working_directory': 'calculator',
                'file_path': 'lorem.txt',
                'content': "wait, this isn't lorem ipsum"
            }
        },
        {
            'inputs': {
                'working_directory': 'calculator',
                'file_path': 'pkg/morelorem.txt',
                'content': 'lorem ipsum dolor sit amet'
            }
        },
        {
            'inputs': {
                'working_directory': 'calculator',
                'file_path': '/tmp/temp.txt',
                'content': 'this should not be allowed'
            }
        }
    ]

    # for test in file_info_tests:
    #     print(f"Result for '{test['inputs']['directory']}' directory:")
    #     print(get_files_info(test['inputs']['working_directory'], test['inputs']['directory']))

    # for test in file_content_tests:
    #     print(f"Result for '{test['inputs']['file_path']}' file:")
    #     print(get_file_content(test['inputs']['working_directory'], test['inputs']['file_path']))

    for test in file_write_tests:
        print(f"Result for '{test['inputs']['file_path']}' content:")
        print(write_file(**test['inputs']))
    



if __name__ == "__main__":
    main()
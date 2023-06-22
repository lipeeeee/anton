import win32con
import win32api

"""_summary_
    
"""

def xdd():
    import sys
    import ctypes.util
    
    # Resolving python.dll path in order to inject it in the target process
    python_library = 'python{}{}.dll'.format(sys.version_info.major, sys.version_info.minor)
    python_library = ctypes.util.find_library(python_library)
    
    from mayhem import utilities
    from mayhem.proc.windows import WindowsProcess
    from mayhem.windll import kernel32
    
    # Resolving Py_InitializeEx address in the remote process
    python_library_remote = process.load_library(python_library)
    python_library_local  = kernel32.GetModuleHandleW(python_library)
    
    initializer = python_library_remote + (
            kernel32.GetProcAddress(python_library_local, b'Py_InitializeEx') - python_library_local)
    
    # Calling Py_InitializeEx(0) in the remote process
    process.join_thread(process.start_thread(initializer, 0))
    
    

if __name__ == "__main__":
    xdd()
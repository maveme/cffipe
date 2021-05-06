from cffi import FFI

import os

ffi = FFI()
ffi.cdef("""
        int fooz(int a);
""")

# lib = ffi.dlopen("Dotnet_API.dylib")
# print(os.environ)
lib = ffi.dlopen("lang_protocol.dylib")
print("lib loaded")

print(lib.fooz(6))
from cffi import FFI

# import os

ffi = FFI()
ffi.cdef("""
int fooz(int a);
""")

# lib = ffi.dlopen("Dotnet_API.dylib")
# print(os.environ)
def call():
    # lib = ffi.dlopen("lang_protocol.dylib")
    # lib = ffi.dlopen("/Users/mauricio/Documents/ResearchProjects/Siemens/testing/lang_protocol.dylib")
    lib = ffi.dlopen("/lang_protocol.so")
    print("lib loaded")
    # num = ffi.new("int *", 6)
    print(lib.fooz(6))
    print("finished")
    ffi.dlclose(lib)


if __name__ == "__main__":
    call()
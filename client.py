from cffi import FFI

ffi = FFI()
ffi.cdef("""
        int fooz(int a);
""")

# lib = ffi.dlopen("Dotnet_API.dylib")
def call():
    lib = ffi.dlopen("/lang_protocol.so")
    print("lib loaded")
    print(lib.fooz(6))
    print("finished")
    ffi.dlclose(lib)


if __name__ == "__main__":
    call()

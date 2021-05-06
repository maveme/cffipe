from cffi import FFI

ffi = FFI()
ffi.cdef("""
        int fooz(int a);
""")

# lib = ffi.dlopen("Dotnet_API.dylib")
lib = ffi.dlopen("lang_protocol.dylib")
print("lib loaded")

print(lib.fooz(7))

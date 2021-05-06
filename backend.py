import cffi

ffibuilder = cffi.FFI()

with open('protocol.h') as f:
    data = ''.join([line for line in f if not line.startswith('#')])
    ffibuilder.embedding_api(data)

ffibuilder.set_source("lang_protocol", r'''
    #include "protocol.h"
''')

ffibuilder.embedding_init_code("""
    from lang_protocol import ffi

    @ffi.def_extern()
    def fooz(val):
        print("hello")
        return val
""")


ffibuilder.compile(verbose=True)

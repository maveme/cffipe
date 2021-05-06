import cffi

ffibuilder = cffi.FFI()

with open('protocol.h') as f:
    data = ''.join([line for line in f if not line.startswith('#')])
    ffibuilder.embedding_api(data)

ffibuilder.set_source("lang_protocol", 
r"""
    #include "protocol.h"
""")

ffibuilder.embedding_init_code("""
    from lang_protocol import ffi

    @ffi.def_extern()
    def fooz(c):
        print("hola")
        a = 1+1
        return 1
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

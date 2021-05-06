import cffi

ffibuilder = cffi.FFI()

with open('protocol.h') as f:
    data = ''.join([line for line in f if not line.startswith('#')])
    ffibuilder.embedding_api(data)

ffibuilder.set_source("lang_protocol", r'''
    #include "protocol.h"
''', libraries=[])

ffibuilder.cdef("""
int fooz(int val);
""")

ffibuilder.embedding_init_code("""
    from lang_protocol import ffi
    import weakref

     #include "interface.h"
    global_weakkeydict = weakref.WeakKeyDictionary()
    
    @ffi.def_extern()
    def fooz(val):
        print("hello")
        return val
""")


if __name__ == "__main__":
    # ffibuilder.compile(target="lang_protocol-1.0.*",verbose=True)
    ffibuilder.compile(verbose=True)

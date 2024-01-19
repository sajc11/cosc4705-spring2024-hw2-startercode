import py_compile

files = ['server.py','client.py']
does_pass = True

for f in files:
    print( f"running a super basic compilation check on {f}" )
    try:
        py_compile.compile(f, doraise=True)
        print( "\thurray! it passes a very basic check." )
    except py_compile.PyCompileError:
        print("\tcompilation failed!")
        does_pass = False
    except FileNotFoundError:
        print("\tcannot find that file")
        does_pass = False

if does_pass:
    exit(0)
else:
    exit(1)

from llvmlite import ir, binding

class GenCode():
    def __init__(self):
        self.binding = binding
        self.binding.initialize()
        self.binding.initialize_native_target()
        self.binding.initialize_native_asmprinter()
        self.configLLVM()
        self.createExecEng()
        self.printfFunc()

    def configLLVM(self):
        # Configuration of LLVM
        self.module = ir.Module(name=__file__)
        self.module.triple = self.binding.get_default_triple()
        fntype = ir.FunctionType(ir.VoidType(), [], False)
        basefun = ir.Function(self.module, fntype, name="main")
        blk = basefun.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(blk)

    def createExecEng(self):
        """
        Creating an ExecutionEngine which is suitable for generating JIT code  
        This engine can be reused for any no. of modules.
        """
        tgt = self.binding.Target.from_default_triple()
        tgt_mach = tgt.create_target_machine()
        backing_mod = binding.parse_assembly("")
        eng = binding.create_mcjit_compiler(backing_mod, tgt_mach)
        self.eng = eng

    def printfFunc(self):
        # Declaring functionality of printf 
        vptrty = ir.IntType(8).as_pointer()
        pfty = ir.FunctionType(ir.IntType(32), [vptrty], var_arg=True)
        pf = ir.Function(self.module, pfty, name="printf")
        self.printf = pf

    def CompIR(self):
        """
        Compiling the LLVM string with this engine.
        This will return the compiled module object
        """
        # Creating an LLVM module object
        self.builder.ret_void()
        llvmir = str(self.module)
        mod = self.binding.parse_assembly(llvmir)
        mod.verify()
        # adding the modules 
        self.engine.add_module(mod)
        self.engine.finalize_object()
        # make sure it is ready for execution
        self.engine.run_static_constructors()
        return mod

    def CreateIR(self):
        self.CompIR()

    def saveOpIR(self, filename):
        with open(filename, 'w') as opfile:
            opfile.write(str(self.module))

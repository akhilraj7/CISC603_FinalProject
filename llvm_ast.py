from llvmlite import ir


class Number():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        i = ir.Constant(ir.IntType(8), int(self.value))
        return i


class BinOper():
    def __init__(self, builder, module, left, right):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right


class Sum(BinOper):
    def eval(self):
        i = self.builder.add(self.left.eval(), self.right.eval())
        return i


class Sub(BinOper):
    def eval(self):
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i

class Mul(BinOper):
    def eval(self):
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i

class Div(BinOper):
    def eval(self):
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i

class Mod(BinOper):
    def eval(self):
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i


class Print():
    def __init__(self, builder, module, printf, value):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.value = value

    def eval(self):
        value = self.value.eval()

        # Declaring the list of arguments
        vpty = ir.IntType(8).as_pointer()
        ft = "%i \n\0"
        cft = ir.Constant(ir.ArrayType(ir.IntType(8), len(ft)),
                            bytearray(ft.encode("utf8")))
        globfmt = ir.GlobalVariable(self.module, cft.type, name="fstr")
        globfmt.linkage = 'internal'
        globfmt.global_constant = True
        globfmt.initializer = cft
        fmarg = self.builder.bitcast(globfmt, vpty)

        # Calling the Print Function
        self.builder.call(self.printf, [fmarg, value])

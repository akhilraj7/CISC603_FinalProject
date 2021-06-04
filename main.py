from rplyLexer import RPLYLexer
from llvmParser import LLVMParser
from genCode import CodeGen

fname = "input.tcom"
with open(fname) as inpfile:
    text_input = inpfile.read()

lxr = RPLYLexer().get_lexer()
tokens = lxr.lex(text_input)

cg = CodeGen()

module = cg.module
builder = cg.builder
printf = cg.printf

pg = LLVMParser(module, builder, printf)
pg.parse()
psr = pg.get_parser()
psr.parse(tokens).eval()

cg.create_ir()
cg.save_ir("output.ll")
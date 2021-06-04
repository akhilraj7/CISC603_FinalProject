target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-p:64:64:64-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-v64:64:64-v128:128:128-a0:0:64-s0:64:64-f80:128:128"
@.str = internal constant [14 x i8] c"Hello, world!\00"


define void @"main"() 
{
entry:
  %".2" = sub i8 5, 3
  %".3" = add i8 10, %".2"
  %".4" = bitcast [5 x i8]* @"fstr" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i8 %".3")
  %tmp2 = tail call i32 @puts( i8* getelementptr ([14 x i8], [14 x i8]* @.str, i32 0, i64 0) ) nounwind
  ret void
}
declare i32 @"printf"(i8* %".1", ...)
declare i32 @puts(i8*) 

@"fstr" = internal constant [5 x i8] c"%i \0a\00"

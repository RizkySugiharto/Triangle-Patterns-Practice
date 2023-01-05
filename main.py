start_message = """
------------------------------
     TRIANGLES PRINTER
------------------------------
Patterns:
1. * *           4. *
   *   *            * *
   *     *          * * *
   * * * * *        * * * *
   
2.     *         5. * * * * *
     * * *            * * *
   * * * * *            *
   
3. *             6.       *
   *  *                *  *
   *  *  *          *  *  *
   *  *                *  *
   *                      *
   
7.       *       8.       * * 
       * *              *   *
     * * *            *     *
   * * * *          * * * * *
------------------------------
"""
type_choices = {
  1: lambda size: "\n".join([f'* {"  "*i}*' for i in range(size-1)]) + f"\n* {'* '*(size-1)}* ",
  2: lambda size: "\n".join([f'{"  "*(size-i)}{"* "*((i-1)*2+1)}' for i in range(1, size+1)]),
  3: lambda size: "\n".join(["*  "*i for i in range(1, size+1)] + ["*  "*(size-i) for i in range(1, size)]),
  4: lambda size: "\n".join(["* "*i for i in range(1, size+1)]),
  5: lambda size: "\n".join([f"{'  '*i}{'* '*((size-(i+1))*2+1)}" for i in range(size)]),
  6: lambda size: "\n".join([f"{'  '*(size-i)}{'* '*i}" for i in range(1, size+1)] + [f"{'  '*i}{'* '*(size-i)}" for i in range(1, size)]),
  7: lambda size: "\n".join([f"{'  '*(size-i)}{'* '*i}" for i in range(1, size+1)]),
  8: lambda size: "\n".join([f"{'  '*(size-i)}* {'  '*(i-1)}* " for i in range(1, size)]) + f"\n{'* '*(size+1)}"
}

print(start_message)
type_input = int(input("Input one of the pattern choices (number): "))
size_input = int(input("Input the size (number): "))
print(f"------------------------------\nResult:\n{type_choices.get(type_input, lambda s: f'Invalid choice ({type_input})')(size_input)}\n------------------------------")


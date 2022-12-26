start_message = """
------------------------------
1. * *
   *   *
   *.    *
   * * * * *
   
2.     *
     * * *
   * * * * *
   
3. *
   *  *
   *  *  *
   *  *
   *
------------------------------
"""
type_choices = {
  1: lambda size: "\n".join([f'* {"  "*i}*' for i in range(size-1)]) + f"\n* {'* '*(size-1)}* ",
  2: lambda size: "\n".join([f'{"  "*(size-i)}{"* "*((i-1)*2+1)}' for i in range(1, size+1)]),
  3: lambda size: "\n".join(["*  "*i for i in range(1, size+1)] + ["*  "*(size-i) for i in range(1, size)])
}

print(start_message)
type_input = int(input("Input one choice of the pattern choices: "))
size_input = int(input("Input the size: "))
print(type_choices.get(type_input, lambda s: f"Invalid choice ({type_input})")(size_input))


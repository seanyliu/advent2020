class Console:

  def __init__(self, instructions):
    self.instructions = instructions
    self.reset()

  def reset(self):
    self.accumulator = 0
    self.pointer = 0
    self.pointers_seen = set()
    self.is_infinite_loop = False

  def get_instructions(self):
    return self.instructions

  def run(self):
    while True:
      #print("pointer="+str(self.pointer))

      # exit criteria
      if self.pointer in self.pointers_seen:
        self.is_infinite_loop = True
        break
      else:
        self.pointers_seen.add(self.pointer)
      if self.pointer >= len(self.instructions):
        break

      # process instructions
      instruction = self.instructions[self.pointer]
      operation = self.get_operation(instruction)
      argument = self.get_argument(instruction)
      if operation == "nop":
        self.pointer = self.run_nop()
      elif operation == "acc":
        self.pointer = self.run_acc(argument)
      elif operation == "jmp":
        self.pointer = self.run_jmp(argument)

    return self.accumulator

  def run_nop(self):
    return self.pointer + 1

  def run_acc(self, argument):
    self.accumulator += argument
    return self.pointer + 1

  def run_jmp(self, argument):
    return self.pointer + argument

  def get_operation(self, instruction):
    return instruction.split(" ")[0]

  def get_argument(self, instruction):
    return int(instruction.split(" ")[1])

  def get_is_infinite_loop(self):
    return self.is_infinite_loop
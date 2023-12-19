class Monkey:

    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.items = kwargs["items"]
        self.operation = kwargs["operation"]
        self.prime = kwargs["prime"]
        self.companions = (kwargs["true:"], kwargs["false:"])

    def __throw(self, item, monkey):
        monkey.items.append(item // 3)

    def set_companions(self, monkey_true, monkey_false):
        self.companions = (monkey_true, monkey_false)

    def catch(self, item):
        self.items.append(item)

    def inspect_item(self):
        item = self.items.pop(0)

        if self.operation[0] == "*": item *= self.operation[1]
        elif self.operation[0] == "**": item **= 2
        else: item += self.operation[1]

        self.__throw(item, self.companions[0] if item % self.prime == 0 else self.companions[1])


def monkey_god(lines):
    monkeys, monkey_data = [], {}
    for line in lines:
        words = line.split(" ")
        match words[0]:
            case "Monkey":
                monkey_data["id"] = words[1][0]
            case "Starting":
                monkey_data["items"] = [int(n.strip(",")) for n in words[2:]]
            case "Operation:":
                if (words[5] == "old"):  monkey_data["operation"] = ("**", 2)
                else: monkey_data["operation"] = (words[4], int(words[5]))
            case "Test:":
                monkey_data["prime"] = int(words[3])
            case "If":
                monkey_data[words[1]] = int(words[5])
                if (words[1] == "false:"):
                    monkeys.append(Monkey(**monkey_data))
                    monkey_data = {}
    return monkeys   

with open("adventOfCode/2022/11/monkey_bussines copy.txt") as file:
    lines = [line.strip() for line in file.readlines()]

monkeys = monkey_god(lines)
monkeys.sort(key=lambda x: x.id)

for monkey in monkeys:
    companions = monkey.companions
    monkey.set_companions(monkeys[companions[0]], monkeys[companions[1]])

monkey_items = {monkey.id:0 for monkey in monkeys}
for _ in range(20):
    for monkey in monkeys:
        for _ in range(len(monkey.items)):
            monkey_items[monkey.id] += 1
            monkey.inspect_item()
    for monkey in monkeys:
        print(f"{monkey.id} - {monkey.items}")

print(monkey_items)


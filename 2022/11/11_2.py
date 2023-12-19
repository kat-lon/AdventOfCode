class Monkey:

    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.items = kwargs["items"]
        self.operation = kwargs["operation"]
        self.prime = kwargs["prime"]
        self.companions = (kwargs["true:"], kwargs["false:"])

    def __throw__(self, item, monkey):
        monkey.items.append(item%9699690)

    def __reducer__(self, item):
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        reduced = 1
        for prime in primes:
            if item % prime == 0: reduced *= prime**(item//prime)
        return reduced


    def set_companions(self, monkey_true, monkey_false):
        self.companions = (monkey_true, monkey_false)

    def catch(self, item):
        self.items.append(item)

    def inspect_item(self):
        item = self.items.pop(0)

        if self.operation[0] == "*": item *= self.operation[1]
        elif self.operation[0] == "+": item += self.operation[1]
        else: item = item * item

        companion = self.companions[0] if item % self.prime == 0 else self.companions[1]

        self.__throw__(item, companion)


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

with open("adventOfCode/2022/11/monkey_bussines.txt") as file:
    lines = [line.strip() for line in file.readlines()]

monkeys = monkey_god(lines)
monkeys.sort(key=lambda x: x.id)

for monkey in monkeys:
    companions = monkey.companions
    monkey.set_companions(monkeys[companions[0]], monkeys[companions[1]])

monkey_items = {monkey.id:0 for monkey in monkeys}
for _ in range(10000):
    for monkey in monkeys:
        for _ in range(len(monkey.items)):
            monkey_items[monkey.id] += 1
            monkey.inspect_item()

print(monkey_items)
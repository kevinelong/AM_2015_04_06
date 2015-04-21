class Database():
    KEY = 0
    VALUE = 1
    OPERATOR = 2

    def __init__(self, node_list, relationships):
        self.node_list = node_list
        self.relationships = relationships
        self.criteria = []
        self.matches = {}
        self.node_dict = {}
        for n in self.node_list:
            self.node_dict[n["id"]] = n
        self.build_relationships()
        self.hops = 0
        self.max_hops = 0
        self.depth = 0

    def build_relationships(self):
        for r in self.relationships:
            n = self.node_dict[r[0]]
            n2 = self.node_dict[r[1]]
            self.add_related(n, n2)
            self.add_related(n2, n)

    @staticmethod
    def add_related(n, n2):
        if "related" not in n.keys():
            n["related"] = []
        n["related"].append(n2)

    def query(self, criteria, start_node, max_hops):
        self.hops = 0
        self.matches = {}
        self.criteria = criteria
        self.max_hops = max_hops
        self.query_node(start_node)

    def query_node(self, node):
        self.depth += 1
        match_count = 0

        for c in self.criteria:
            if self.evaluate_criterion(node, c):
                match_count += 1

        if match_count == len(self.criteria):
            self.matches[node["id"]] = node

        if self.depth < self.max_hops:
            for n in node["related"]:
                self.query_node(n)

        self.depth -= 1

    def evaluate_criterion(self, node, c):

        key = c[self.KEY]
        operator = c[self.OPERATOR]
        value = c[self.VALUE]

        if key not in node.keys():
            return False

        if operator is "=":
            return node[key] == value

        if operator is "<":
            return node[key] < value

        if operator is ">":
            return node[key] > value
        else:
            return node[key] == value


db = Database([
    {
        "id": 1,
        "name": "portland",
        "population": 111
    },
    {
        "id": 2,
        "name": "seattle",
        "population": 222
    },
    {
        "id": 3,
        "name": "san francisco",
        "population": 333
    },
    {
        "id": 4,
        "name": "moon"
    }

], [
    [1, 2],
    [1, 4],
    [3, 2],
    [3, 4],
])

db.query(
    [
        ["population", 100, ">"],
        ["population", 5900, "<"],
    ],
    db.node_list[0],
    2
)
for k, m in db.matches.items():
    print(m["name"])
# class Criterion():
# def __init__(self, key, value, relation):
# self.key = key
# self.value = value
# self.relation = relation if relation else "equals"

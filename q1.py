class Relevance:
    def __init__(self):
        with open("input.txt") as f:
            data = f.readlines()
        pages = [page for page in data if page.split(" ")[0] == 'P']
        queries = [query for query in data if query.split(" ")[0] == 'Q']
        self.pages = []
        for p in pages:
            page = [x.replace("\n", "") for x in p.split(" ")[1:]]
            self.pages.append(page)
        self.queries = []
        for q in queries:
            query = [x.replace("\n", "") for x in q.split(" ")[1:]]
            self.queries.append(query)

    def relation_query_page(self):
        self.relation = []
        for query in self.queries:
            n_page = []
            for page in self.pages:
                relation = 0
                for q in query:
                    for p in page:
                        if q == p:
                            relation = relation + (8-query.index(q)) * (8-page.index(p))

                n_page.append({
                    f"P{self.pages.index(page)+1}": relation
                })
            self.relation.append({
                f"Q{self.queries.index(query)+1}:": n_page
            })

    def outputData(self):
        print(self.relation)
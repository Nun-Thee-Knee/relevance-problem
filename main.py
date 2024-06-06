from q1 import Relevance

relevance = Relevance()
relevance.relation_query_page()

print(relevance.queries)
print(relevance.pages)

relevance.outputData()
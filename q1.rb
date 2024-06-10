class Relevance
  def initialize
    data = File.readlines("input.txt")
    pages = []
    queries = []
    for line in data
      if line.strip.split(" ")[0] == 'P'
        pages.push(line)
      else
        queries.push(line)
      end
    end
    @pages = pages
    @queries = queries
  end

  def relation_query_page
    @relation = []
    for query in @queries
      n_page = []
      for page in @pages
        relation = 0
        for q in query.split(" ")
          for p in page.split(" ")
            if q == p
              relation += (8 - query.split(" ")[1..-1].index(q)) * (8 - page.split(" ")[1..-1].index(p))
            end
          end
        end
        n_page.push({
          "P#{@pages.index(page)+1}" => relation
        })
      end
      @relation.push({"Q#{@queries.index(query)+1}" => n_page})
    end
  end

  def outputData
    print @relation
  end
end

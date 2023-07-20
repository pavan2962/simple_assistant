import wolframalpha
client=wolframalpha.Client('JGTY7P-2L5HG7XKTG')
while True:
    query=str(input('Query: '))
    res=client.query(query)
    output=next(res.results).text
    print(output) in test

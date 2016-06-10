from parser import Parser

parser = Parser()
dependency = parser.parseToStanfordDependencies("You raise me up to sing a song")
print dependency.dependencies[2]


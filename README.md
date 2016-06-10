 python interface to the Stanford Parser. It uses JPype to create a Java virtual machine, instantiate the parser, and call methods on it.
 Most of the code is focused on getting the Stanford Dependencies, but it's easy to add API to call any method on the parser
 You have to use rake to compile the 3rdparty library
 1. go to 3rdparty/jpype and type `rake setup`
 2. go to 3rdparty/stanfrod\_parser and type `rake download; rake setup`
 3. set STANFORD\_PARSER\_HOME to 3rdparty/stanford\_parser/parser directory to index the jar file

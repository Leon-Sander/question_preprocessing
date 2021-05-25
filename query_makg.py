from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

class mag_connection:

    def __init__(self):
        sparql_endpoint = 'https://makg.org/sparql'
        self.sparql = SPARQLWrapper(sparql_endpoint)
        self.sparql.setReturnFormat(JSON)

    def query_makg(self, author, keyword):
        paper_list = []
        if (author != None) and (keyword != None):
            # wenn man den author nicht exakt matcht sondern ein contains überprüft dauert der query ewig
            self.sparql.setQuery("""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                PREFIX dcterms: <http://purl.org/dc/terms/>
                PREFIX magc: <https://makg.org/class/>
                PREFIX prism: <http://prismstandard.org/namespaces/basic/2.0/>
                SELECT ?paper
                WHERE {
                    
                    ?author rdf:type <https://makg.org/class/Author> .
                    ?author foaf:name """ + '\"' + author + '\"' + """^^xsd:string .
                    ?paper dcterms:creator ?author .
                    ?paper rdf:type magc:Paper .
                    ?paper prism:keyword ?keyword .
                    filter contains(?keyword, """ + '\"' + keyword + '\"' + """^^xsd:string) 
                }
                """)
            


        elif (author == None) and (keyword != None):
            self.sparql.setQuery("""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX magc: <https://makg.org/class/>
                PREFIX prism: <http://prismstandard.org/namespaces/basic/2.0/>
                SELECT ?paper
                WHERE {
                    ?paper rdf:type magc:Paper .
                    ?paper prism:keyword ?keyword .
                    filter contains(?keyword, """ + '\"' + keyword + '\"' + """^^xsd:string) 
                }
                """)
                #?paper prism:keyword """ + '\"' + keyword + '\"' + """^^xsd:string .


        elif (author != None) and (keyword == None):
            self.sparql.setQuery("""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                PREFIX dcterms: <http://purl.org/dc/terms/>
                PREFIX magc: <https://makg.org/class/>
                SELECT ?paper
                WHERE {
                    
                    ?author rdf:type <https://makg.org/class/Author> .
                    ?author foaf:name """ + '\"' + author + '\"' + """^^xsd:string .
                    ?paper dcterms:creator ?author .
                }
                """)
        
        results = self.sparql.query().convert()
        results = results['results']['bindings']
        if results != []:
            for paper in results:
                paper_list.append(paper['paper']['value'])
            return paper_list

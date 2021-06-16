from nltk import pos_tag, word_tokenize
import re
import json
from query_makg import mag_connection
from templates import templates
class question_preprocessing:
    

    def __init__(self):
        self.qm = mag_connection()
        self.templates = templates()

    def question_classification(self,input_question):
        #### plural
        plural = self.check_plural(input_question)
        
        #### brackets
        brackets = self.check_brackets(input_question)
        if brackets != None:
            author , keyword = self.extract_author_and_keyword(input_question[brackets[0]+1:brackets[1]-1])
            if (author == None) and (keyword == None):
                print('Error, could not find an author or a keyword to query the mag')
                return None
    
            paper_id = self.query_makg(author, keyword)

        #### kg or ir
        kg = self.check_kg(input_question)


        if kg == True:
            output = json.dumps({'plural': plural, 
                                'MAG-IDs/MAKG-IDs' : paper_id,
                                'KG' : kg})
        else:
        #### annotations
            annotations = self.check_annotations(input_question)
        #### imrad
            imrad = self.check_imrad(input_question)
            
            output = json.dumps({'plural': plural, 
                                'MAG-IDs/MAKG-IDs' : paper_id,
                                'KG' : kg,
                                'annoations' : annotations,
                                'imrad' : imrad})
        return output
    
    def check_plural(self,input_question):
        """This Method checks if the first Noun is singular or plural


        :param input_question: input sentence to check on 
        """
        pos_tags = pos_tag(word_tokenize(input_question))
        for tag in pos_tags:
            if (tag[1] == 'NNS') or (tag[1] == 'NNPS'):
                
                return True
            else:
                if (tag[1] == 'NN') or (tag[1] == 'NNP'):
                    
                    return False
                
        print('No noun found.')
        return False

    def check_brackets(self, input_question):
        """This Method checks if there are brackets in the input_question
        and returns either the span of the brackts or None.

        :param input_question: input sentence to check on 
        """
        brackets = re.search(r"\[.*\]",input_question)
        if brackets != None:
            return brackets.span()
        else:
            return None

    def extract_author_and_keyword(self,input):
        keywords_for_authors = "written|authored" 
        result = re.search("(" + keywords_for_authors + ") by",input)
        if result != None:
            # gibt das erste Wort nach dem match aus, muss noch erweitert werden für längere Namen
            author = input[result.span()[1]:].strip().split(" ")[0]

        keywords_for_keyword = "about|on|regarding|with respect to"
        result = re.search("(paper|papers) .* (" + keywords_for_keyword + ") ",input)
        if result != None:
            # hier ebenso nur das erste Wort nach dem match
            keyword = input[result.span()[1]:].strip().split(" ")[0]


        return author , keyword

    def query_makg(self, author, keyword):
        # queried nach dem exakten author und dem exakten keyword
        return self.qm.query_makg(author, keyword)

    def check_kg(self, input_question):
        kg_single_pattern = self.templates.kg_single_pattern
        kg_global_pattern = self.templates.kg_global_pattern
        
        for template in kg_single_pattern:
            if re.match(template, input_question):
                return True

        for template in kg_global_pattern:
            if re.match(template, input_question):
                return True

        return False

    def check_annotations(self, input_question):
        annotation_templates = self.templates.annotation_templates
        for template in annotation_templates:
            if re.search(template, input_question) != None:
                return True
        
        return False


    def check_imrad(self, input_question):

        imrad_templates = self.templates.imrad_templates

        for template in imrad_templates:
            if re.match(template, input_question):
                return True

        return False

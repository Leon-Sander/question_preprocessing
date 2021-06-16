## Question Preprocessing

The Class **question_preprocessing** processes an input question in the following ways:

   1. Ckeck_plural: This Method checks if the first Noun is singular or plural
   2. Check_brackets: This method checks if the input question contains brackets, to further extract information from it.
   3. Extract_author_and_keyword: If there are brackets, then this method tries to extract an author and a keyword and then query the makg
      to retrieve paper_ids which are written by the author containing the respecting keywords 
   4. Check_kg: This method checks if the question is about meta data which can be extracted from a Knowledge Graph. This is done by regex matching.

   If kg == True -> 
   
                     Json return format: {'plural': True/False, 
                                 'MAG-IDs/MAKG-IDs' : [id/s],
                                 'KG' : True/False}
   If kg == False ->

   5. Check_annotations: This Method checks if the question contains the words dataset or method.
   6. Check_imrad: This method matches the sentence on regex pattern which indicate that the information can be
      retrieved from a specific section of the paper/s.

                    Json return format: {'plural': True/False, 
                                'MAG-IDs/MAKG-IDs' : [id/s],
                                'KG' : True/False,
                                'annoations' : True/False,
                                'imrad' : True/False} 

##### Templates.py

   This class contains all regex pattern/templates used in the methods check_kg, annotation_template, check_imrad and pattern to check if a 
   question is about information retrieval.

##### Templates used right now for check_kg

        kg_single_pattern = ["Which papers (is|does) the paper .* (cite|citing)\?",
                     "When (was|has) the paper .* published\?",
                     "Who authored paper .*",
                     "Who (was|were) the author(s)? of the paper .*"]

        kg_global_pattern = ["(Which|What) paper(s)? (were|are|is|has been|was) associated with .*",
                     "(Which|What) conference(s)? since ((^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)(19|20)[0-9][0-9]$)|\d+) (have been|were|are) most influential?",
                     "How many papers (have been|are|were) published .*",
                     "In (which|what) conference(s)? has .* published?"] 

##### Templates used right now for check_imrad

         imrad_templates = ["(Which|What) (data( )?set(s)?|.*method(s)?|metric(s)?) (are|is|were|have been) (used|proposed|employed|utilised|utilized|applied|provided|introduced) .*",
               "Does paper .* provide (a )?(data( )?set(s)?|.*method(s)?)\??",
               "Is paper .* (providing|using|proposing|utilising|utilizing) a data( )?set\??",
               "(Which|What) (data( )?set(s)?|.*method(s)?) does paper .* (compare|use|provide|employ)",
               "(Which|What) (data( )?set(s)?|.*method(s)?) (are|is|was|were) compared to, in the paper .*",
               "What (is|was|has been) proposed as future work .*"]


#### test.ipynb

   This notebook is to test the functionality of the question_preprocessing class.

#### programming.ipynb

   This notebook is for ongoing programming.

   *todo:*
   - *Extract_author_and_keyword erweitern um nicht nur das erste Wort zu extracten (evtl. mit einem NER)*
   - *Templates erweitern*

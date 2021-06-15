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

   5. Annotation_template: This Method checks if the question contains the words dataset or method.
   6. Check_imrad: This method matches the sentence on regex pattern which indicate that the information can be
      retrieved from a specific section of the paper/s.

                    Json return format: {'plural': True/False, 
                                'MAG-IDs/MAKG-IDs' : [id/s],
                                'KG' : True/False,
                                'annoations' : True/False,
                                'imrad' : True/False} 


#### test.ipynb

   This notebook is to test the functionality of the question_preprocessing class.

#### programming.ipynb

   This notebook is for ongoing programming.

   *todo:*
   - *Extract_author_and_keyword erweitern um nicht nur das erste Wort zu extracten (evtl. mit einem NER)*
   - *Templates erweitern*

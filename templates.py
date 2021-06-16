class templates:

    def __init__(self):
        # pattern to check if a question is about meta data which can be retrieved from a knowledge graph
        self.kg_single_pattern = ["Which papers (is|does) the paper .* (cite|citing)\?",
                     "When (was|has) the paper .* published\?",
                     "Who authored paper .*",
                     "Who (was|were) the author(s)? of the paper .*"]

        self.kg_global_pattern = ["(Which|What) paper(s)? (were|are|is|has been|was) associated with .*",
                     "(Which|What) conference(s)? since ((^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)(19|20)[0-9][0-9]$)|\d+) (have been|were|are) most influential?",
                     "How many papers (have been|are|were) published .*",
                     "In (which|what) conference(s)? has .* published?"] 


        # pattern to check if the information needed can be looked up in an imrad section of the paper
        self.imrad_templates = ["(Which|What) (data( )?set(s)?|.*method(s)?|metric(s)?) (are|is|were|have been) (used|proposed|employed|utilised|utilized|applied|provided|introduced) .*",
        "Does paper .* provide (a )?(data( )?set(s)?|.*method(s)?)\??",
        "Is paper .* (providing|using|proposing|utilising|utilizing) a data( )?set\??",
        "(Which|What) (data( )?set(s)?|.*method(s)?) does paper .* (compare|use|provide|employ)",
        "(Which|What) (data( )?set(s)?|.*method(s)?) (are|is|was|were) compared to, in the paper .*",
        "What (is|was|has been) proposed as future work .*"]



        self.annotation_templates = ["(data( )?set(s)?|.*method(s)?)"]



        # pattern to check if a question is about information retrieval
        self.ir_single_templates = ["What (are|is|were) the (main )?contribution(s)? of paper .*",
                     "Which .* (were|are|is) used in the paper .*",
                     "Does paper .* provide a .*",
                     "(What|Which) machine learning method(s)? does paper .* compare(\?)?",
                     "(Which|What) data( )?set(s)? (are|is) mentioned in the paper .*",
                     "(Which|What) data( )?set(s)? (are|is) compared to .* in the paper .*"]

        self.ir_global_templates = ["How .* are the .* models (in .* )?published since \d+\??",
                     "Which use cases exist for .*",
                     "Which (ML |.* )?methods have been used by author .*\??",
                     "Which data()?set(s)? (have been|were) introduced in (the )?papers .*( at conference .*\??)?",
                     "Which (ML |.* )?method(s)? (have been|were|are) used for .* data()?sets in papers?",
                     "What (is|was) proposed as future work regarding .*",
                     "Which metric(s)? (are|were|is) used for .*",
                     "(Which|What) data()?set(s)? (are|is|were) mentioned in the papers .*",
                     "(Which|What) data()?set(s)? (are|is|were) considered for (the )?use in the papers .*",
                     "(Which|What) evaluation data sets are mentioned/used in the context of citation recommendation?",
                     "(Which|What) method(s)? (were|are) proposed for .*",
                     "(Which|What) data( )?set(s)? (are|is|were) used in the papers .*",
                     "(Which|What) data( )?set(s)? (are|is|were) used in the evaluations regarding .*",
                     "(Which|What) data( )?set(s)? (do )?appear in the .*"
                     ]
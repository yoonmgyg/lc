class Solution:
    def interpret(command):
        list1 = []
        str1 = ""
        parser_table = {'G':'G',
                        '()':'o',
                        '(al)':'al'
                        }
        for each in command:
            str1 += each
            if str1 in parser_table:
            list1.append(parser_table[str1])
            str1 = ""
            
        return ''.join(list1)

import difflib
from collections import Counter

my_input = [
    'myhposlqgeauywfikztndcvrqr', 'mbhposlxfeauywoikztndcvjqi', 'mbhpoulxgeagywfikytndcvjqr',
    'jbhposlxgeauywdikztndcvjqk', 'mbhpsslxueauywfikzfndcvjqr', 'mbhposnxgeauzyfikztndcvjqr',
    'ibhposlxgetvywfikztndcvjqr', 'mbcposlxgeauywfikztxdcvjqv', 'mlhposltgeauywfikitndcvjqr',
    'mbhpostxgeauywfikztndjvjqy', 'mboboslxglauywfikztndcvjqr', 'mbhpoglxgeahywfikztndcvjqp',
    'mbhposlxgeapydpikztndcvjqr', 'mbhposlxseauywfikztnncljqr', 'mbhposlxgeauydfisztndcvjqj',
    'mbhposlxgeaugwwikzlndcvjqr', 'mbhpoklxgeauywfikztndvvmqr', 'mbhposlxgeauywfikdtndcmjqx',
    'mbhposlxaeauapfikztndcvjqr', 'mbwposgxgeauymfikztndcvjqr', 'mbhposlxgeauvwfirzcndcvjqr',
    'mbhpozlxgeaqywfykztndcvjqr', 'mahqoslxgeauywfikzgndcvjqr', 'mbhposlcgexbywfikztndcvjqr',
    'ykhposlxgeeuywfikztndcvjqr', 'mbhgoswxgeauywfikztndhvjqr', 'mbhposlxgeauywfikztnocmjqp',
    'mbvposfageauywfikztndcvjqr', 'mbhpnslxgeauywfikztndgejqr', 'mblposfxgeauypfikztndcvjqr',
    'mbhposlxyeauywfikzpndcvmqr', 'ibhposlbgeauywfikotndcvjqr', 'mbmposlxgeauywfiktwndcvjqr',
    'mbhposlxgeduywfikztndfvoqr', 'mbhpoklxdeauywfikztndcvuqr', 'mbhposlxgeauywfikltnlcvuqr',
    'mbhposlbgsauywfikztndsvjqr', 'mbhposlxgeauywfirzfndcbjqr', 'mphposlxgeauywfikztndcvjgg',
    'mohposlcgeauywfikzsndcvjqr', 'mbhpovlxgeauyqfikotndcvjqr', 'qbhpgslxgeauywqikztndcvjqr',
    'mbhposlxweauywfikztndtvjqm', 'pbhposlxgeauywfikztnncvjqm', 'mbbposlxpeauuwfikztndcvjqr',
    'mbhposlxgmauyrfikztndcvjir', 'pbhposlqgefuywfikztndcvjqr', 'mbhkoslxgeauywfikztndciwqr',
    'mbtpoflxgeauywfikztndrvjqr', 'mbhcoslxveguywfikztndcvjqr', 'mbhpovlxgeauywfhkdtndcvjqr',
    'mbhposlxgeauywftrztndcujqr', 'mbhposlxgeaoywfdkzpndcvjqr', 'mbnposlxgeyuywfikztldcvjqr',
    'mbaposlxweauywfikftndcvjqr', 'mbhposljgeauywfikztcdcvvqr', 'nbhpkslxgeauywfikzwndcvjqr',
    'mbhtoslxgeauywfikzkndcvjdr', 'mbhposxxgeaxywfikztndsvjqr', 'mbdpoflxgeauywfisztndcvjqr',
    'mbhposvxgeauywfikztnscvnqr', 'mbcposlxghauywfikztndcgjqr', 'mbhpovlxgeauywpckztndcvjqr',
    'mbhpfslxgeauywbikntndcvjqr', 'mbhpowyxgeauywfikztndcvjcr', 'mbhposlxoeatywfikztndcvoqr',
    'mchpfslxgeauywfikztidcvjqr', 'mbhposvxgearywfikztndcvjcr', 'mbhposlxgeauywfpcztnduvjqr',
    'mbhposlxgmauyyfiqztndcvjqr', 'mbhposlxteauuwfikwtndcvjqr', 'mbhpotlspeauywfikztndcvjqr',
    'mbhpoelxgeauywfikztndckjkr', 'mbhpnslxgeauywfikztndcvkqs', 'mbhpksfxgwauywfikztndcvjqr',
    'mxhwoglxgeauywfdkztndcvjqr', 'mbhphsbjgeauywfikztndcvjqr', 'mbhposlxgeauwifixztndcvjqr',
    'mbhposqxguauywfikztndcwjqr', 'mbhposlngeauywfikztedcvjor', 'nbhposlxgeauywiikztndcyjqr',
    'mbhposlxgeauawfykztndcvbqr', 'mbhplslxgeauywcikztndcvjrr', 'fshposlxgeagywfikztndcvjqr',
    'mbhposlxgeauymcikztndcxjqr', 'mbhponlxgeauyloikztndcvjqr', 'mbhposrxzeanywfikztndcvjqr',
    'mbhtoslxgeajyifikztndcvjqr', 'mbhposixkeauywfikhtndcvjqr', 'mahhoslxgeaufwfikztndcvjqr',
    'mbhpdslxteauywfikzvndcvjqr', 'mfhposlxgeauywfiqttndcvjqr', 'mbhplslxheauywfikztnscvjqr',
    'mbhpoylxgeauywbizztndcvjqr', 'mbhposlhgeawywfjkztndcvjqr', 'mbhkoslxgkauywfilztndcvjqr',
    'mbhposnxgeauywfikztkdcvlqr', 'mvhpxslxgevuywfikztndcvjqr', 'mbhpohlxgeauyrficztndcvjqr',
    'mbhsosuxgewuywfikztndcvjqr', 'mbhpoxlxgeauywuikztnhcvjqr', 'mbhposlxqeauyqfikztndcvrqr',
    'mbhpchlxgeauywfikztnhcvjqr', 'mbhposlxgeauywoikztndcfqqr', 'pbhposlxgeagmwfikztndcvjqr',
    'mxhwoglxgeauywfikztndcvjqr', 'mbhpospxgaauywfikstndcvjqr', 'mbhwoxlxgeauywfgkztndcvjqr',
    'mbhposlxgeauywfikvtndhvsqr', 'mbbposlxgesuywfikztnicvjqr', 'mhhjoslxgeauywfikztndccjqr',
    'mbhkoslxgeagywffkztndcvjqr', 'mbhposlxgesqywfukztndcvjqr', 'mbdposlxgeauywfilztndcvjqp',
    'mbhposlxgeakqwfikztedcvjqr', 'mbhposuxgeayywficztndcvjqr', 'mbhposlxgeauywfxkztndcloqr',
    'mchposlxgeauywoiiztndcvjqr', 'tbhporlxgeauywfikztndcvyqr', 'mbhposlxoevuywfikzindcvjqr',
    'qbhposlxfevuywfikztndcvjqr', 'mbhposlxfeauvwfikztndcvgqr', 'mbjposlxgsauywfikztnwcvjqr',
    'vbhposlxgeauvwfikztndcvjqk', 'pbhposlxguauyrfikztndcvjqr', 'mbhposlcgeauywfiketndcviqr',
    'mbsposlxgvauywfikztndcviqr', 'mbhposlxgeauynfxkztndcvjbr', 'mbhposlxtentywfikztndcvjqr',
    'mbhposlxgeavywfikztndhvjnr', 'mbhpsvlxgeauywfikztndcvzqr', 'mzhpotlxgeauywfiyztndcvjqr',
    'mbhposkqgeauywfiwztndcvjqr', 'mbhposlxoeakywfikztndcvjqt', 'mbhposlxghauywfikbdndcvjqr',
    'mbhpossxgeauywfikqxndcvjqr', 'mbhposlxgearywhikztydcvjqr', 'mbhposlxgeaiywfikztndfvjur',
    'mbhpxslxgoazywfikztndcvjqr', 'mbhposlxneauywfibqtndcvjqr', 'mnheoslxteauywfikztndcvjqr',
    'mbhposlxgeauywfmkztrdcvuqr', 'mbhzowlxgeauywfizztndcvjqr', 'mbhloslxgeauyofikztnucvjqr',
    'mbhposlxneagywfbkztndcvjqr', 'mbhposongeauywfikztnzcvjqr', 'mwyposlxgeauywfikztnqcvjqr',
    'mbhpnqaxgeauywfikztndcvjqr', 'mboposlxzeauywfioztndcvjqr', 'mbhposledeauywfikztndqvjqr',
    'mphpaslxgeauywfbkztndcvjqr', 'mbhposrxgeauywlikbtndcvjqr', 'ybhnoslxgeauywfihztndcvjqr',
    'mbhposlxgeauywfikntxccvjqr', 'mbhposlxgeauqwfikutndcfjqr', 'mbhposlxglabywfikztidcvjqr',
    'mbhpollxgeauywfikxtnscvjqr', 'mboposlggeaufwfikztndcvjqr', 'mbhposlxgeauywpikedndcvjqr',
    'mbhpoklxgeauywpikztndcvjlr', 'mbhposhxgeauywfifztndcvpqr', 'mbhposlxgwagywfikztndcvjwr',
    'mbhpokldgeauywfikztngcvjqr', 'nbhposlxgeauywfiketndcvjxr', 'mbhhoslxgexuywfikrtndcvjqr',
    'mbhposlxgefujwfikztkdcvjqr', 'mbhposlxggagywfikztndchjqr', 'mbhposlxgeauyvfilztnicvjqr',
    'mbhposlkgeauywfikzxndcvoqr', 'mbhposlxgeauvqfikztndcvuqr', 'zbhposlxgfauylfikztndcvjqr',
    'mbhyoshxgeauywfikztndcvjqa', 'sbhposlxgeauyxfikztndavjqr', 'mlhposlxgeauywfikzmndcqjqr',
    'mbhpaslxgekuywfikztnncvjqr', 'ibhhoslxteauywfikztndcvjqr', 'mbhposlxgeauyodibztndcvjqr',
    'mbhposlxgkaoywfikztndcvpqr', 'mbhonslxgearywfikztndcvjqr', 'mbdpoolxgealywfikztndcvjqr',
    'mbepfslxgvauywfikztndcvjqr', 'mbhposlygeauywfikztfdcvaqr', 'mthpoalxgeauywnikztndcvjqr',
    'mbhpesbogeauywfikztndcvjqr', 'mbhposlxgjauywfikztnmcvjqj', 'mbhnoslxgeauydfikgtndcvjqr',
    'mbhpxslxgeauywfikztndcvjcx', 'muhposlxgwauywfipztndcvjqr', 'mbhpcslxgeauywfiqztndcvjbr',
    'mbhpomlxgeauywfioftndcvjqr', 'mbhposlfgepuywfikzmndcvjqr', 'mbhsosliteauywfikztndcvjqr',
    'mbwposlxgeauywfikztnycveqr', 'mbhpfslxgeauywfqkztndcvjhr', 'mxhbvslxgeauywfikztndcvjqr',
    'fbhposlxgeauywfikzcnmcvjqr', 'mbhfosfxgeauywfikztnduvjqr', 'tbhporlxgeauywfikztndcvjqm',
    'mhhposlxgeauywfikctnecvjqr', 'mbhposlxgeqtywfikztnmcvjqr', 'qbhpjslxgeauywfikztndevjqr',
    'tbhpxslxgeaunwfikztndcvjqr', 'wbhposlxgeadywfikztndcujqr', 'mbhposlvgeauywfpkotndcvjqr',
    'mbhposlxgeagywfingtndcvjqr', 'mbnposlxgeauywfikztnvcjjqr', 'mohpoilxgeadywfikztndcvjqr',
    'mbhposlsgeauywfikztnxcvgqr', 'mbhposlogeauywfikqtndcvjor', 'mbhroslxgeauypfikztndcvjqg',
    'mblposuxgetuywfikztndcvjqr', 'mbhposlogeiuywfikztodcvjqr', 'mbhposlxgeauylfikztedcvrqr',
    'mbhfoslxgeautwxikztndcvjqr', 'mbhouslxgeauywfikztnycvjqr', 'mbhposlxgeauywfvkqtndlvjqr',
    'mbfposltgeauytfikztndcvjqr', 'mbhposlxgcapywfikztnddvjqr', 'hbhposlxgeasywfikztnxcvjqr',
    'mbhposntgeauywfikztcdcvjqr', 'mbhponlxgfauywfirztndcvjqr', 'mbhposlxgeatywlikztndcvrqr',
    'mohroslzgeauywfikztndcvjqr', 'mbhpojaxgeauywfifztndcvjqr', 'rbhposlxgwauywfikztndovjqr',
    'mbhpoclxgeaeywfikztndcvjqo', 'mbhposllgeauywfikzondcvmqr', 'mbhpxslxgeauywfikzymdcvjqr',
    'mbhposlxgeasywxikztndkvjqr', 'mbhposlxgeauywfivztndcmjqx', 'qbhposlxgpauywfikgtndcvjqr',
    'mbhposlxgeauyqdikztqdcvjqr', 'cbhposlxgeauywfikttjdcvjqr', 'mbhgoslxgeanywfihztndcvjqr',
    'mbhposlxgeajywfhkztndcvjvr', 'mbhpozlxgeauewfmkztndcvjqr', 'mbhposlxgeagywfbiztndcvjqr',
    'mbhmoslxgeauywfikztndrnjqr', 'ybhposmxgeauywfikztndcviqr', 'mrwposlxgeauywfikztndpvjqr',
    'mbhposlxneauywfikztndcbjqh', 'mbhpowlxheauywfikztndcojqr', 'mbeposlxgeauywfiwztnycvjqr',
    'mbhposixgeapywfikztndcvvqr', 'mbhposlxgeauywfikztnbcvjap', 'mzhposixgenuywfikztndcvjqr',
    'mbhposgxgeauywyikztndvvjqr', 'mbhposajgeauywfikztzdcvjqr', 'mbhyoslxgeauywfikzsndcvxqr',
    'mbhposlxgdauywfikmtndcljqr'
]


class Day2:
    @staticmethod
    def first(box_ids):
        twice_count = 0
        thrice_count = 0
        for box_id in box_ids:
            letter_counts = Counter(c for c in box_id)
            twice_count += 1 if len([k for k, v in letter_counts.items() if v == 2]) > 0 else 0
            thrice_count += 1 if len([k for k, v in letter_counts.items() if v == 3]) > 0 else 0

        return twice_count * thrice_count

    @staticmethod
    def second(box_ids):
        for box_id_1 in box_ids:
            for box_id_2 in box_ids:
                diff_between_ids = list(difflib.ndiff(box_id_1, box_id_2))
                additions = len([x for x in diff_between_ids if x.startswith('+')])
                subtractions = len([x for x in diff_between_ids if x.startswith('-')])
                if additions == subtractions == 1:
                    return ''.join([x.strip() for x in diff_between_ids if x.startswith(' ')])

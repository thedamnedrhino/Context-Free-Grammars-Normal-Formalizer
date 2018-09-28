from ContextFreeGrammars import ChomskyNF, CFG
import sys

if __name__ == '__main__':
    g = CFG.CFG()
    g.loadFromFile(sys.argv[1])
    choms = ChomskyNF.ChomskyNF()
    normalized = choms.convertToNF(g)
    print(g)
    print('++++++++++++++++')
    print(normalized.nlp_rep())
import tokenite as tok
import sys

b = tok.texts(sys.argv[1])
W = b.tread()
T = b.t_tok(W)

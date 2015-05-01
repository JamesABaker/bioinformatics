from Bio.SeqUtils.ProtParamData import kd
from Bio.SeqUtils import ProtParam
my_seq="MAEGEITTFTALTEKFNLPPGNYKKPKLLY"
pa = ProtParam.ProteinAnalysis(my_seq)
for value in pa.protein_scale(kd, window=19):
    print("%.3f" % value)

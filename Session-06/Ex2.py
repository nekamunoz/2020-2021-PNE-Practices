from Seq0 import Seq

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
for s in range(0, len(seq_list)):
    print(f"Sequence {s} (Length: {seq_list[s].len()}): {seq_list[s]}")




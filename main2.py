import pandas as pd
from src2.extractTransform2 import transacoes_pix
from src2.load2 import saveCsv, saveSQLite, saveMySQL

dadosPix2 = transacoes_pix("202501")
saveCsv(dadosPix2, "./src2/datasets2/transacoes_pix", ";", ".")

saveSQLite(dadosPix2, "src2/datasets2/dadosPix2.db", "transacoes_pix")

saveMySQL(dadosPix2, "root", "root", "localhost", "etlbcb", "transacoes_pix")

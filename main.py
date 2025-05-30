import pandas as pd
from src.extractTransform import transacoes_pix
from src.load import saveCsv, saveSQLite, saveMySQL

dadosPix = transacoes_pix("202501")
saveCsv(dadosPix, "./src/datasets/transacoes_pix", ";", ".")

saveSQLite(dadosPix, "src/datasets/dadosPix.db", "transacoes_pix")

#saveMySQL(dadosPix, "root", "root", "localhost", "etlbcb", "transacoes_pix")

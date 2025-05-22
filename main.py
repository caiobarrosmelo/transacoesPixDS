import pandas as pd
from src.extractTransform import transacoes_pix_ultimos_5_anos
from src.load import saveCsv, saveSQLite, saveMySQL

dadosPix = transacoes_pix_ultimos_5_anos()
saveCsv(dadosPix, "./src/datasets/transacoes_pix_ultimos_5_anos", ";", ".")

saveSQLite(dadosPix, "src/datasets/dadosPix.db", "transacoes_pix_ultimos_5_anos")

saveMySQL(
    dadosPix, "root", "root", "localhost", "etlbcb", "transacoes_pix_ultimos_5_anos")

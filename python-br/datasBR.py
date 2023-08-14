from datetime import datetime, timedelta

class DatasBR:

    def __init__(self):
        self.timestamp_cadastro = datetime.today()

    def __str__(self):
        return self.formatar_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro","fevereiro","março","abril","maio","junho",
            "julho","agosto","setembro","outubro","novembro","dezembro"
        ]
        mes_cadastro = self.timestamp_cadastro.month-1

        return meses_do_ano[mes_cadastro]
    
    def dia_semana(self):
        dias_da_semana = [
            "segunda","terça","quarta","quinta","sexta","sabado","domingo"
        ]
        dia_da_semana_cadastro = self.timestamp_cadastro.weekday()

        return dias_da_semana[dia_da_semana_cadastro]
    
    def formatar_data(self):
        data_formatada = self.timestamp_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.timestamp_cadastro
        return tempo_cadastro
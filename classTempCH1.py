from guardatCH1 import jsonFile

class temp_CH1(jsonFile):

    def __init__(self,name="",value="",sp='',lista=[]):
        super().__init__("temp_CH1.json")
        self.name = name
        self.value = value
        self.sp = sp
        self.namefile="temp_CH1.json"
        self.lista = lista

    def addCh1(self,temp):
        try:
            self.lista.append(temp)
            return "dato guardado"
        except:
            return "error al guardar"

    def deleteAllTemp(self):
        try:
            for i in self.lista:
                self.lista.remove(i)
            return "datos eliminados"
        except:
            return "no existen datos"

    def showData(self):
        try:
            return self.lista
        except:
            return "lista vacia"

    def guardarDatos(self):
        json_data={}
        json_data['Temp_CH1']=[]
        for x in self.lista:
            arreglo_Json={
                'name':f'{x.name}',
                'value':f'{x.value}',
                'sp':f'{x.sp}',
            }
            json_data['Temp_CH1'].append(arreglo_Json)
        self.toJson(json_data)

    def __str__(self):
        return f"name:{self.name},value:{self.value}"
    
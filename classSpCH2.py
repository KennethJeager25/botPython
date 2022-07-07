from guardarSpCH2 import jsonFile

class sp_CH2(jsonFile):

    def __init__(self,name="",value="",lista=[]):
        super().__init__("Sp_CH2.json")
        self.name = name
        self.sp = value
        self.namefile="Sp_CH2.json"
        self.lista = lista

    def addSp2(self,temp):
        try:
            self.lista.append(temp)
            return "dato guardado"
        except:
            return "error al guardar"

    def deleteAllSp(self):
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
        json_data['Sp_CH2']=[]
        for x in self.lista:
            arreglo_Json={
                'name':f'{x.name}',
                'sp':f'{x.sp}',
            }
            json_data['Sp_CH2'].append(arreglo_Json)
        self.toJson(json_data)

    def __str__(self):
        return f"name:{self.name},value:{self.sp}"
    